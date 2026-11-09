# CONTENIDO — miu-agents (Jaime393)

Fuente: lectura directa de los 6 archivos (branch main), 2026-11-09 ~07:08 -05.
Solo números verificados en los archivos. Las afirmaciones del repo se citan como afirmaciones del repo, no como hechos verificados.

## Qué hace cada pieza

### 1. miu_agent.py — agente genérico (2.956 B)

- **Función `chat(messages)`:** POST a `{BASE_URL}/chat/completions` con `model`, `messages`, `max_tokens: 800`; devuelve `choices[0].message.content`. Requiere las 3 variables de entorno; si falta alguna, lanza `RuntimeError` con mensaje explícito (sin fallback silencioso).
- **Función `search(q)`:** POST a la URL de `MIU_SEARCH_WEBHOOK` con `{"query": q, "top_k": 5}`; devuelve `results` (o lista vacía si no hay webhook definido).
- **Función `run(t)`:** busca contexto con `search(t)`, lo recorta a 2.000 caracteres, lo pasa a `chat()` con el prompt de sistema, e imprime la respuesta.
- **Uso:** `python3 miu_agent.py <tarea>`; sin argumentos usa `"analiza D_f"`.
- **Migración documentada:** v1 usaba Groq fijo; v2 es genérica sobre cualquier API OpenAI-compatible porque, según el docstring, Groq/DeepSeek se retiraban el 2026-07-24.

### 2. worker.js — endpoint fijo (433 B)

- Ruta `/miu/global`: devuelve un JSON fijo con 7 campos literales (`global_mind:true`, autorización, `repos:16`, `phi:'$107M'`, `manos:10`, `expansion:'4->16 repos'`, ID de Drive).
- Cualquier otra ruta: devuelve el texto fijo `'global mind 16/16 - MIU v27 expansion 16 repos - 10 manos'`.
- **No hay ninguna lectura viva:** ningún fetch a base de datos, ninguna variable, ningún cómputo. Las cifras son literales del código.

### 3. polen_v133.html — kit de siembra (844 B)

- Ofrece un fragmento JS para copiar en Deno/CF/Vercel que responde con un JSON de existencia.
- Afirma (sin verificar aquí): "24 Pages + 40 CF + R2 100GB".
- Consulta en el navegador `https://Jaime393.github.io/miu-mesh/index.json` y muestra el número de nodos.

### 4. config/WORKFLOW_CONFIG.yml — instrucción pendiente (451 B)

- No es una configuración ejecutable: es una orden de actualizar WORKFLOW_CONFIG desde un inventario dinámico de 20 repos, con matriz repo×credencial/permiso sin valores secretos, failover comprobable, presupuesto real y checkpoints idempotentes.
- Nombra 3 repos como ejemplo: `infoflow-optimizer`, `MIU_V14`, `proyect1`.

## Números verificados en el repo

| Dato | Valor | Fuente |
|---|---|---|
| Archivos en el repo | 6 | listado de raíz, 2026-11-09 |
| Commits en main | 6 | `list_commits`, 2026-11-09 |
| Último commit | 2026-08-25T17:41:59Z | `list_commits` |
| `max_tokens` de `chat()` | 800 | `miu_agent.py` |
| `top_k` de `search()` | 5 | `miu_agent.py` |
| Recorte de contexto en `run()` | 2.000 caracteres | `miu_agent.py` |
| Campos del JSON de `/miu/global` | 7 | `worker.js` |
| Repos del inventario dinámico citado | 20 | `config/WORKFLOW_CONFIG.yml` |

## Afirmaciones del repo que NO se verifican aquí

- "24 Pages + 40 CF + R2 100GB" (polen_v133.html).
- `repos:16`, `phi:'$107M'`, `manos:10`, "16/16" (worker.js — literales fijos, no medidas).
- Que Groq/DeepSeek se retiraran el 2026-07-24 (docstring de miu_agent.py — fecha citada, no contrastada con fuente externa en esta minería).
- Que existan "5 skills más" que usaran esos modelos (docstring — no verificadas).

## Carencias del repo (lo que le falta, medido en sus propios archivos)

1. **Sin pruebas:** no hay ningún archivo de test en el repo (0 de 6 archivos).
2. **Sin licencia:** no hay archivo LICENSE (0 de 6 archivos).
3. **Sin resultados:** no hay logs, salidas ni registros de ejecuciones de `miu_agent.py` ni del worker.
4. **Sin despliegue documentado:** ninguna URL de despliegue del worker ni del agente en el repo.
5. **README incompleto:** solo nombra `miu_agent.py`; no menciona `worker.js`, `polen_v133.html` ni `config/`.
6. **Configuración no ejecutable:** `WORKFLOW_CONFIG.yml` es una instrucción en prosa, no una configuración.
7. **worker.js sin datos vivos:** el endpoint `/miu/global` devuelve literales fijos; no mide nada.
