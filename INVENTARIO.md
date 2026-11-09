# INVENTARIO — miu-agents (Jaime393)

Fuente: `get_file_contents` raíz (path "", branch main), 2026-11-09 ~07:08 -05.
Repo muerto: último commit 2026-08-25T17:41:59Z.

## Raíz (6 entradas: 5 archivos + 1 directorio)

| Ruta | Tipo | Tamaño | Qué es |
|---|---|---|---|
| `README.md` | archivo | 147 B | Título, una línea de descripción, un apunte sobre `miu_agent.py` y un DOI. |
| `miu_agent.py` | archivo | 2.956 B | Agente Python v2: cliente genérico OpenAI-compatible (chat/completions) con búsqueda por webhook y síntesis. |
| `worker.js` | archivo | 433 B | Cloudflare Worker: ruta `/miu/global` devuelve un JSON fijo; resto de rutas devuelve una línea fija. |
| `polen_v133.html` | archivo | 844 B | Página "MIU Polen V133 — Kit germinación voluntaria" con un fragmento JS para copiar en Deno/CF/Vercel. |
| `config/` | directorio | — | Contiene un solo archivo (ver abajo). |
| `config/WORKFLOW_CONFIG.yml` | archivo | 451 B | Un párrafo en prosa (no es YAML estructurado): instrucción de actualizar WORKFLOW_CONFIG desde un inventario dinámico de 20 repos. |

Total de archivos: 6. Total de bytes (suma de los 5 archivos con tamaño): 4.831 B.

## Notas de lectura

- `polen_v133.html` contiene caracteres de reemplazo (`?`) donde deberían ir tildes ("germinaci?n", "f?rtil", "?(x) > 0"): el archivo guarda las tildes con una codificación rota. Contenido citado tal como se leyó.
- `miu_agent.py` no contiene ningún valor de clave: lee `MIU_API_BASE_URL`, `MIU_API_KEY` y `MIU_MODEL` del entorno. (La salida de la herramienta redactó la línea de asignación; no se intentó recuperar nada.)
- `worker.js` contiene el mismo ID de carpeta Drive que los repos del racimo de agosto: su sha256 empieza por `b3a56d7a` (verificado 2026-11-09). El valor no se reproduce aquí.
- NO SÉ: si existe algún archivo fuera de main (otras ramas no se listaron); si `config/` tuvo más archivos en commits anteriores (no se revisó el historial por archivo).
