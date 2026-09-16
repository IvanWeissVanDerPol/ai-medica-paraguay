# Área 5 — Resistencia antimicrobiana

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§2-química-y-descubrimiento-de-fármacos) · [research findings](../docs/research-findings.md)

---

## Problema

Paraguay no tiene un sistema nacional automatizado de vigilancia genómica de resistencia antimicrobiana. IICS opera una red desde 2007 para caracterización molecular de resistencia, con 17 años de datos acumulados pero sin capa de aprendizaje automático. La convocatoria 2026 FAPESP-CONACYT-CONICET está explícitamente dirigida a resistencia antimicrobiana en producción animal — Paraguay es exportador importante de carne.

## Capacidades locales

- **IICS-UNA** opera la Red Nacional de Resistencia Antibiótica desde 2007 con IPS + Hospital de Clínicas.
- **Hospital General de Barrio Obrero** — datos activos de TB IGRA (estudio 2025 publicado).
- **BioProsNat** — screening antimicrobiano experimental.
- **SENACSA** — Servicio Nacional de Calidad y Salud Animal, regula uso veterinario.
- **2025 estudio TB IGRA-TB vs QFT-Plus** (Front Public Health, Barrio Obrero) — precedentes en evaluación diagnóstica.

## Herramientas de código abierto

| Herramienta | Función | Patógeno |
|---|---|---|
| [Mykrobe](https://github.com/Mykrobe-tools/mykrobe) | Predicción de resistencia desde WGS | *M. tuberculosis*, *S. aureus* |
| [TBProfiler](https://github.com/jodyphelan/TBProfiler) | Genotipado + resistencia TB | *M. tuberculosis* |
| [AMRFinderPlus (NCBI)](https://github.com/ncbi/amr) | Genes de resistencia desde genomas bacterianos | General |
| [Staramr](https://github.com/phac-nml/staramr) | Predicción AMR desde WGS | General |
| [ResFinder](https://genomicepidemiology.org/services/) | Base de datos genes de resistencia | General |
| [ARIBA](https://github.com/sanger-pathogens/ariba) | Genes de resistencia desde reads | General |

## Primer proyecto concreto

> Aplicar Mykrobe + AMRFinderPlus sobre el archivo histórico de aislamientos del IICS. Entrenar un clasificador XGBoost sobre los 17 años de datos de la red. Construir un dashboard de vigilancia nacional. Aplicar a la convocatoria 2026 FAPESP-CONACYT-CONICET.

Entregables:
- Paper con perfil genómico de resistencia histórica del Paraguay.
- Pipeline reproducible abierto.
- Dashboard web de vigilancia.
- Propuesta formal a la convocatoria 2026 FAPESP-CONACYT-CONICET (fecha de cierre abril 2026 — verificar).

## Vacíos de información

- ¿Los datos están en WHONET o en un sistema propio?
- ¿Hay aislados secuenciados (WGS) disponibles?
- ¿Cuál es la capacidad de cómputo del IICS?
- ¿Cuál es la política del SENACSA sobre datos de uso veterinario?
- ¿Hay coinvestigadores brasileños o argentinos con trabajo previo en AMR animal con los que aliarnos?

## Próximo paso inmediato

Contactar a **Dra. Rosa Guillén Fretes** (IICS Microbiología, PRONII II) — es la persona que lidera la red desde 2007. Una conversación inicial responde la mitad de las preguntas.

## Notas regulatorias

- Si los datos son a nivel paciente (no aislado): aplica Ley 7593/2025.
- Si son aislados con metadata epidemiológica: caso por caso.
- SENACSA regula el lado animal; requiere acuerdo específico.
- La convocatoria 2026 FAPESP-CONACYT-CONICET tiene requisitos administrativos — verificar elegibilidad institucional con CONACYT.