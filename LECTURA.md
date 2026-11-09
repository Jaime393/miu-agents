# LECTURA — miu-agents (Jaime393)

Fuente: lectura directa de los 6 archivos del repo (branch main), 2026-11-09 ~07:08 -05.
Todo lo citado entre comillas es literal del archivo.

## README.md (147 B)

> "# miu-agents"
> "Agentes autónomos del ecosistema MIU."
> "- miu_agent.py: Agente D_f con research y síntesis"
> "https://doi.org/10.5281/zenodo.20547558"

El README no describe `worker.js`, `polen_v133.html` ni `config/`; solo nombra `miu_agent.py`. El DOI es el mismo de las publicaciones MIU.

## miu_agent.py (2.956 B)

Docstring literal:

> "miu_agent.py — v2, migrado fuera de dependencia fija de Groq."
> "Motivo de la migración: Groq/DeepSeek (modelos usados por este agente y por 5 skills más) se retiran el 2026-07-24 (ver TAREAS_PENDIENTES_2026-07-08, Sheet REGISTRO_TEJEDOR_MIU). En vez de apuntar a otro proveedor fijo (que tendría el mismo problema el día que ESE proveedor cambie de modelo), este script queda genérico sobre cualquier API compatible con el esquema OpenAI chat/completions (Groq, OpenAI, Together, Fireworks, DeepInfra, Cerebras, etc. lo son) — migrar de proveedor pasa a ser cambiar 3 variables de entorno, no reescribir código."

Variables de entorno requeridas (según el docstring): `MIU_API_BASE_URL`, `MIU_API_KEY`, `MIU_MODEL`. Ejemplos que da el docstring: `llama-3.3-70b-versatile`, `gpt-5.4-nano`. El docstring afirma:

> "Si no se define ninguna, cae a MIU_API_BASE_URL/KEY/MODEL vacíos y falla con un mensaje explícito (SÉ que no hay fallback silencioso a Groq — evita que el mismo problema reaparezca sin avisar)."

Prompt de sistema literal: `"Eres MIU Motor Epistemico. Solo D_f. K_i=tautologia."`

## worker.js (433 B)

Contenido íntegro (una línea):

```js
export default { async fetch(req){ const u=new URL(req.url); if(u.pathname=='/miu/global') return new Response(JSON.stringify({global_mind:true, autorizacion:'TOTAL x10000 v27 expansion 16 repos', repos:16, phi:'$107M', manos:10, expansion:'4->16 repos', drive:'<ID Drive, valor no reproducido>'}) ,{headers:{'Content-Type':'application/json'}}); return new Response('global mind 16/16 - MIU v27 expansion 16 repos - 10 manos'); } }
```

Las cifras (`repos:16`, `phi:'$107M'`, `manos:10`, "16/16") son literales fijos del código, no medidas: el worker no consulta ninguna fuente viva. El ID de Drive es el mismo del racimo de agosto (huella `b3a56d7a…`, verificada por hash).

## polen_v133.html (844 B)

> "<h1>? MIU Polen V133 - Kit germinaci?n voluntaria</h1>"
> "<p>Este es suelo f?rtil. No pide permiso, ofrece herramienta.</p>"
> "Endpoints vivos: 24 Pages + 40 CF + R2 100GB - https://Jaime393.github.io/miu-mesh/"

El fragmento JS para copiar define `EXISTENCIA` con `observacion:'ecosistema rendimiento apis'`, `participante:'Jaime393'`, `aporte:'existencia'`, `sustrato:'voluntario'`. Además, la página hace `fetch('https://Jaime393.github.io/miu-mesh/index.json')` y añade "Mesh N nodos vivo" al cuerpo.

La afirmación "24 Pages + 40 CF + R2 100GB" es del archivo; no se verificó en esta minería (no se consultó miu-mesh). Las tildes aparecen rotas (`?`) en el archivo tal como se leyó.

## config/WORKFLOW_CONFIG.yml (451 B)

Contenido íntegro (un solo párrafo, no es YAML estructurado):

> "Actualizar WORKFLOW_CONFIG desde el inventario dinámico real de 20 repositorios, incluyendo `Jaime393/infoflow-optimizer`, `Jaime393/MIU_V14` y `Jaime393/proyect1`, y retirando entradas no presentes solo tras confirmación. Añadir matriz repo×credencial/permiso sin valores secretos, failover comprobable, presupuesto real (sin asumir $5k–10k), checkpoints idempotentes, deduplicación de tareas y sincronización de resultados a Drive/Audit Log."

Es una instrucción pendiente, no una configuración: no hay matriz, ni lista de repos, ni presupuesto en el archivo.

## NO SÉ

- Si `miu_agent.py` se ejecutó alguna vez con éxito (no hay logs ni resultados en el repo).
- Si `worker.js` se desplegó alguna vez (no hay URL de despliegue en el repo; la ruta `/miu/global` es solo código).
- Si "24 Pages + 40 CF" era cierto en agosto de 2026 (no verificado).
