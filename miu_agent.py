#!/usr/bin/env python3
"""
miu_agent.py — v2, migrado fuera de dependencia fija de Groq.

Motivo de la migración: Groq/DeepSeek (modelos usados por este agente y
por 5 skills más) se retiran el 2026-07-24 (ver TAREAS_PENDIENTES_2026-07-08,
Sheet REGISTRO_TEJEDOR_MIU). En vez de apuntar a otro proveedor fijo (que
tendría el mismo problema el día que ESE proveedor cambie de modelo), este
script queda genérico sobre cualquier API compatible con el esquema
OpenAI chat/completions (Groq, OpenAI, Together, Fireworks, DeepInfra,
Cerebras, etc. lo son) — migrar de proveedor pasa a ser cambiar 3
variables de entorno, no reescribir código.

Variables de entorno requeridas:
  MIU_API_BASE_URL   — endpoint base, ej: https://api.groq.com/openai/v1
                                          https://api.openai.com/v1
                                          https://api.together.xyz/v1
  MIU_API_KEY        — la API key del proveedor elegido
  MIU_MODEL          — nombre del modelo en ese proveedor
                        (ej: llama-3.3-70b-versatile, gpt-5.4-nano, etc.)

Si no se define ninguna, cae a MIU_API_BASE_URL/KEY/MODEL vacíos y
falla con un mensaje explícito (SÉ que no hay fallback silencioso a
Groq — evita que el mismo problema reaparezca sin avisar).
"""
import sys, json, os, urllib.request

BASE_URL = os.environ.get("MIU_API_BASE_URL", "")
API_KEY = os.environ.get("MIU_API_KEY", "")
MODEL = os.environ.get("MIU_MODEL", "")

SYS = "Eres MIU Motor Epistemico. Solo D_f. K_i=tautologia."


def chat(messages):
    if not (BASE_URL and API_KEY and MODEL):
        raise RuntimeError(
            "Faltan MIU_API_BASE_URL / MIU_API_KEY / MIU_MODEL. "
            "Este agente ya NO usa Groq como default fijo (deprecado 2026-07-24) — "
            "define las 3 variables de entorno con el proveedor que quieras usar."
        )
    payload = json.dumps(
        {"model": MODEL, "messages": messages, "max_tokens": 800}
    ).encode()
    req = urllib.request.Request(
        f"{BASE_URL.rstrip('/')}/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def search(q):
    w = os.environ.get("MIU_SEARCH_WEBHOOK", "")
    if not w:
        return []
    payload = json.dumps({"query": q, "top_k": 5}).encode()
    req = urllib.request.Request(
        w, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read()).get("results", [])


def run(t):
    ctx = search(t)
    ins = chat(
        [
            {"role": "system", "content": SYS},
            {"role": "user", "content": f"Task:{t}\nCorpus:{str(ctx)[:2000]}"},
        ]
    )
    print(ins)


if __name__ == "__main__":
    run(" ".join(sys.argv[1:]) or "analiza D_f")