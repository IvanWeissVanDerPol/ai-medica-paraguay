# Área 1 — Vigilancia genómica

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§1-genómica-y-estructura-de-proteínas) · [research findings](../docs/research-findings.md)

---

## Problema

Paraguay tiene vigilancia genómica activa en LCSP (Illumina MiSeq + nanopore) y produce publicaciones en filodinámica de dengue, SARS-CoV-2 y MPXV. Pero cada análisis depende de pipelines ad-hoc no estandarizados, no reproducibles. Cuando llega un nuevo outbreak, hay que reconstruir el flujo bioinformático desde cero.

## Capacidades locales

- **LCSP (Ministerio de Salud)** — opera la Red Nacional de Vigilancia Genómica (Resolución Ministerial 875). BSL-3. Illumina MiSeq. MinION desde 2020 (vía CONACYT COVID express call).
- **IICS-UNA** — experiencia publicada en filodinámica de dengue, SARS-CoV-2, MPXV.
- **CEDIC, FCQ-UNA, UNCA, Cyrlab** — nodos de la red con capacidad de PCR y secuenciación.
- **Genome Detective** — usado por LCSP en publicaciones previas.

## Herramientas de código abierto

| Herramienta | Función |
|---|---|
| [Nextclade](https://github.com/nextstrain/nextclade) | Asignación de clado, mutaciones, calidad |
| [Augur + Auspice](https://github.com/nextstrain/augur) | Filogenia + visualización Nextstrain |
| [nf-core/viralrecon](https://github.com/nf-core/viralrecon) | Pipeline automatizado virus respiratorios |
| [nf-core/ampliseq](https://github.com/nf-core/ampliseq) | Pipeline para datos amplicón |
| [Pangolin](https://github.com/cov-lineages/pangolin) | Linaje SARS-CoV-2 |
| [ViralFlow](https://github.com/viralflow) / [V-pipe](https://github.com/cbg-ethz/v-pipe) | Workflows virales integrados |
| [Galaxy](https://galaxyproject.org) | UI web sin instalación |

## Primer proyecto concreto

> Instalar Nextclade + Augur + nf-core/viralrecon en un servidor de LCSP, escribir SOPs en español, correr un taller de 2 días para bioinformáticos del LCSP/IICS.

Entregables:
- Dashboard Nextstrain público, actualizado cuando llegue un nuevo genoma.
- SOPs bilingües (español + guaraní si aplica).
- Materiales del taller en repo abierto.
- Paper de métodos en revista regional (Revista Memorias del IICS o equivalente).

Costo estimado: bajo (~$3–5k viajes + honorarios facilitador externo, p.ej. CABANA).

## Vacíos de información

- ¿Cuántas secuencias crudas tiene LCSP sin publicar?
- ¿Qué pipeline usan actualmente?
- ¿Hay capacidad local para mantener un servidor Nextstrain?
- ¿Cuál es el ancho de banda real de LCSP?
- ¿Cuál es la postura de CONACYT/PROCIENCIA para financiar herramientas de software (vs. hardware/wet-lab)?

## Próximo paso inmediato

Contactar a **Dra. Cynthia Vazquez** (LCSP) con una nota de 1 página que diga: "vi su publicación sobre MPXV, acá va cómo automatizaríamos este flujo con Nextclade + nf-core, ¿tenemos 30 min?"