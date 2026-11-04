import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("routes", ROOT / "route_resources.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def discovery():
    return {"schema": "miu.discovery-result/v1", "repositories": [],
            "auto_apply": False, "runtime_verified": False}


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)
        (self.path / "scripts").mkdir()
        self.source = self.path / "scripts/discover.py"
        self.source.write_text("# bounded mock\n")
        self.digest = hashlib.sha256(self.source.read_bytes()).hexdigest()

    def invoke(self, task="", front=None, result=None, returncode=0):
        def runner(args, **kwargs):
            self.assertIn("-I", args)
            self.assertEqual(args[5], self.source.read_text())
            self.assertNotIn("MIU_API_KEY", kwargs["env"])
            self.assertNotIn("shell", kwargs)
            return SimpleNamespace(returncode=returncode, stdout=json.dumps(result or discovery()))
        return MODULE.route_resources(task, front, self.path, 10, self.digest, runner)

    def test_accented_hint(self):
        self.assertEqual(MODULE.front_hint("Necesito validación PVA"), "validation-pva")
        self.assertEqual(self.invoke("validación")["selection"], "keyword_hint")

    def test_explicit_front_overrides_hint(self):
        r = self.invoke("pva", "agents-routing")
        self.assertEqual(r["front"], "agents-routing")
        self.assertEqual(r["selection"], "explicit")

    def test_literal_query_is_not_execution(self):
        r = self.invoke("; curl example.invalid")
        self.assertEqual(r["selection"], "literal_query")
        for field in ("model_called", "capability_executed", "auto_apply"):
            self.assertFalse(r[field])

    def test_digest_divergence_blocks(self):
        with self.assertRaisesRegex(ValueError, "diverged"):
            MODULE.route_resources(registry=self.path)

    def test_registry_failure_blocks(self):
        with self.assertRaisesRegex(ValueError, "blocked"):
            self.invoke(returncode=2)

    def test_scope_escalation_blocks(self):
        r = discovery()
        r["runtime_verified"] = True
        with self.assertRaisesRegex(ValueError, "runtime"):
            self.invoke(result=r)

    def test_limit_bounds(self):
        for limit in (0, 101, True):
            with self.assertRaisesRegex(ValueError, "limit"):
                MODULE.route_resources(registry=self.path, limit=limit)

    def test_real_cross_repo_cli_without_model(self):
        registry = ROOT.parent / "miu-portable-registry"
        source = registry / "scripts/discover.py"
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != MODULE.READER_SHA256:
            self.skipTest("Pinned sibling registry required for integration")
        p = subprocess.run([sys.executable, str(ROOT / "miu_agent.py"),
                            "--discover", "validación PVA"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stderr)
        r = json.loads(p.stdout)
        self.assertGreater(r["discovery"]["matched"], 0)
        self.assertEqual(r["front"], "validation-pva")
        self.assertFalse(r["model_called"])


if __name__ == "__main__":
    unittest.main()
