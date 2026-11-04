# miu-agents

Cliente de síntesis y rutas de descubrimiento del ecosistema MIU. La presencia del cliente no demuestra autonomía, disponibilidad de un modelo ni permisos vigentes.

- miu_agent.py: Agente D_f con research y síntesis

## Descubrir antes de ejecutar

```bash
python3 miu_agent.py --discover "validación PVA"
python3 miu_agent.py --discover --front skills-methodology
python3 route_resources.py --registry ../miu-portable-registry --front agents-routing
python3 -m unittest discover -s tests -v
```

El modo `--discover` no usa el cliente de modelos, claves ni webhooks. Consulta el lector del repositorio vecino `miu-portable-registry`, comprobado por SHA-256, con entorno mínimo y Python aislado; bloquea divergencias en lugar de descargar o ejecutar capacidades nuevas.

Requiere el lector y catálogo incorporados en el [PR de registry](https://github.com/Jaime393/miu-portable-registry/pull/1), no disponibles por asumir una copia antigua de main. Los hints por palabras son pistas de navegación, no comprensión certificada de la tarea.

El resultado mantiene `model_called=false`, `capability_executed=false` y `auto_apply=false`. La ruta de validación conduce a PVA, pero no transforma un catálogo en evidencia de que Docker, Lean, ledger o swarm se hayan ejecutado.

La ruta histórica de síntesis sin `--discover` conserva sus requisitos `MIU_API_BASE_URL`, `MIU_API_KEY` y `MIU_MODEL`. No se probó contra un proveedor ni se incurrió en llamadas de modelo en esta incorporación.

https://doi.org/10.5281/zenodo.20547558
