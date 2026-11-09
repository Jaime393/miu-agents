# FAMILIA — miu-agents (Jaime393)

Fuente: lectura directa de los archivos del repo, 2026-11-09 ~07:08 -05.
Las relaciones se afirman solo donde el repo las nombra; el resto es NO SÉ.

## Relaciones nombradas dentro del repo

| El repo nombra | Dónde | Qué dice de la relación |
|---|---|---|
| Ecosistema MIU | `README.md`, `miu_agent.py`, `worker.js`, `polen_v133.html` | El repo se presenta como parte del ecosistema MIU ("Agentes autónomos del ecosistema MIU"). |
| 5 skills (sin nombrar) | docstring de `miu_agent.py` | Usaban Groq/DeepSeek junto a este agente. No se nombran cuáles son. |
| `miu-mesh` | `polen_v133.html` | La página consulta `https://Jaime393.github.io/miu-mesh/index.json` y enlaza `https://Jaime393.github.io/miu-mesh/`. |
| `Jaime393/infoflow-optimizer` | `config/WORKFLOW_CONFIG.yml` | Debe entrar en el inventario dinámico de 20 repos. |
| `Jaime393/MIU_V14` | `config/WORKFLOW_CONFIG.yml` | Debe entrar en el inventario dinámico de 20 repos. |
| `Jaime393/proyect1` | `config/WORKFLOW_CONFIG.yml` | Debe entrar en el inventario dinámico de 20 repos. |
| Deno / Cloudflare / Vercel | `polen_v133.html` | Destinos de copia del fragmento JS ("Copia esto en tu cuenta Deno/CF/Vercel - 1 click"). |
| Drive (carpeta, ID no reproducido) | `worker.js` | El JSON de `/miu/global` incluye el ID de carpeta. Es el mismo ID del racimo de agosto (huella `b3a56d7a…`). |
| Zenodo DOI 10.5281/zenodo.20547558 | `README.md` | El DOI de las publicaciones MIU. |

## Relaciones con familias ya minadas o censadas

- **Racimo de agosto (2026-08-23/25):** el commit `bf5954e3` (2026-08-23, "v27 expansion 16 repos") y el commit `be3f59b1` (2026-08-25, "polen v133") sitúan a este repo en el mismo vertido que `latido-sonoro`, `miu-colmena`, `miu-mesh`, `FranBot-Mural` y los `miu-auto-*`. Comparte con ellos el ID de Drive (huella `b3a56d7a…`) y el patrón del commit polen.
- **miu-mesh:** `polen_v133.html` depende de `miu-mesh/index.json` para mostrar el número de nodos. `miu-mesh` fue minado en la tanda 2 (muerto 2026-08-24; su heartbeat escribe `"vive": true` sin medir nada).
- **miu-portable-skills:** el docstring de `miu_agent.py` habla de "5 skills más" que usaban Groq/DeepSeek; `miu-portable-skills` es el módulo de skills del ecosistema, pero el repo no lo nombra y la relación es inferencia, no SÉ.
- **Familia miu-auto:** el commit polen v133 es el mismo mensaje que aparece en los 22 repos `miu-auto-*` de 2 commits ("polen v133 - suelo que sostiene a otros"). Este repo es el origen visible de esa frase en el ecosistema.
- **Familia v150 / PVA:** sin relación nombrada en este repo. NO SÉ si existe alguna.

## NO SÉ

- Cuáles son las "5 skills" del docstring (no se nombran).
- Si `worker.js` se desplegó en Cloudflare o en otro sitio (no hay URL en el repo).
- Si `miu-mesh/index.json` seguía respondiendo cuando se escribió `polen_v133.html` (no verificado).
- Qué son "24 Pages + 40 CF" en concreto (la afirmación es del HTML; no se contrastó con ningún inventario).
- Si `MIU_V14`, `infoflow-optimizer` o `proyect1` usan este agente (la config solo los cita para el inventario).
