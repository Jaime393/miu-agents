#!/usr/bin/env python3
"""Route discovery through a pinned local registry reader, without model calls."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import unicodedata

READER_SHA256 = "f66762190c91475b4577a26c13b015a028df848472540078ebe5e7eb076bcebb"
DEFAULT_REGISTRY = Path(__file__).resolve().parent.parent / "miu-portable-registry"
SAFE_ENV = {"PATH": os.defpath, "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1"}
HINTS = (
    ("validation-pva", {"pva", "validacion", "validation", "lint"}),
    ("agents-routing", {"agente", "agentes", "agent", "agents"}),
    ("skills-methodology", {"skill", "skills", "metodologia", "methodology"}),
    ("tools-evidence", {"acta", "actas", "auditoria", "audit"}),
    ("grimorio-knowledge", {"grimorio"}),
    ("portability-network", {"portabilidad", "portable", "mesh"}),
)


def front_hint(task):
    normalized = unicodedata.normalize("NFKD", task).encode("ascii", "ignore").decode().lower()
    words = set(re.findall(r"[a-z0-9]+", normalized))
    return next((front for front, terms in HINTS if words & terms), None)


def route_resources(task="", front=None, registry=DEFAULT_REGISTRY, limit=10,
                    expected_reader_sha256=READER_SHA256, runner=subprocess.run):
    if type(limit) is not int or not 1 <= limit <= 100:
        raise ValueError("limit must be between 1 and 100")
    registry = Path(registry).resolve(strict=True)
    source = registry / "scripts" / "discover.py"
    if source.is_symlink() or not source.is_file() or source.stat().st_size > 65536:
        raise ValueError("bounded regular registry reader required")
    code = source.read_bytes()
    digest = hashlib.sha256(code).hexdigest()
    if digest != expected_reader_sha256:
        raise ValueError("registry reader diverged; inspect it before changing the pin")
    selected = front if front is not None else front_hint(task)
    # -I prevents local import shadowing. Run pinned bytes with an explicit catalog path.
    bootstrap = "import sys;__file__=sys.argv.pop(1);exec(compile(sys.argv.pop(1),__file__,'exec'))"
    args = [sys.executable, "-I", "-c", bootstrap, str(source), code.decode("utf-8"),
            "--catalog", str(registry / "catalog/capabilities.json"), "--limit", str(limit)]
    if selected is not None:
        args += ["--front", selected]
    elif task:
        args += ["--query", task]
    proc = runner(args, capture_output=True, text=True, timeout=15,
                  env=SAFE_ENV.copy(), check=False)
    if proc.returncode != 0 or len(proc.stdout.encode("utf-8")) > 2 * 1024 * 1024:
        raise ValueError("registry query blocked or exceeded output limit")
    result = json.loads(proc.stdout)
    if result.get("schema") != "miu.discovery-result/v1" or result.get("auto_apply") is not False:
        raise ValueError("registry schema or execution scope changed")
    if result.get("runtime_verified") is not False:
        raise ValueError("discovery must not claim runtime validation")
    return {
        "schema": "miu.agent-discovery-route/v1",
        "front": selected,
        "selection": "explicit" if front is not None else "keyword_hint" if selected else "literal_query",
        "reader_sha256": digest,
        "discovery": result,
        "model_called": False,
        "capability_executed": False,
        "auto_apply": False,
        "next_step": "Read the selected source and workflow triggers, validate current permissions, test one bounded capability, then save and read back its remote checkpoint.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", nargs="?", default="")
    parser.add_argument("--front")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args(argv)
    try:
        result = route_resources(args.task, args.front, args.registry, args.limit)
    except (OSError, ValueError, TypeError, AttributeError, subprocess.SubprocessError):
        print("Blocked: local registry, reader integrity or evidence scope could not be verified.", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
