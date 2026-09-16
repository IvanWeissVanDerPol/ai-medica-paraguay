# AI Médica Paraguay

Investigación y prototipos abiertos para integrar inteligencia artificial de código abierto en la investigación médica y atención clínica del Paraguay.

> Estado: **fase de exploración y mapeo**. Este repositorio documenta áreas de investigación prioritarias, personas e instituciones, oportunidades concretas de proyectos, y vacíos de información que necesitamos cerrar antes de iniciar trabajo real.

---

## ¿Por qué Paraguay?

Paraguay tiene capacidades biomédicas reales y concentradas (IICS-UNA, LCSP, CEDIC, INCAN, Hospital de Clínicas) que podrían multiplicarse con herramientas de IA de código abierto bien adaptadas. La ventana regulatoria está abierta: la Ley 7593/2025 de protección de datos personales entra en vigencia en noviembre de 2027, y no existe todavía un marco de aprobación para IA clínica. Hay enfermedades desatendidas (Chagas, dengue, tuberculosis) donde Paraguay ya es referente regional, y donde la IA puede acelerar diagnósticos, vigilancia genómica y descubrimiento de fármacos.

## Documentos principales

### Estrategia y contexto

- [`docs/research-areas.md`](docs/research-areas.md) — descripción de las **8 áreas de investigación** con problemas, herramientas, proyectos concretos y vacíos. Priorización.
- [`docs/research-findings.md`](docs/research-findings.md) — **hallazgos consolidados de investigación** sobre Paraguay: carga de enfermedad, capacidades locales, datos cuantitativos, comparaciones regionales.
- [`docs/research-session-log.md`](docs/research-session-log.md) — log cronológico de las sesiones de investigación que construyeron este repo.
- [`docs/research-sources.md`](docs/research-sources.md) — bibliografía consolidada, todas las fuentes citadas con URLs y verificación.

### Mapas operativos

- [`docs/mapa-actor-instituciones.md`](docs/mapa-actor-instituciones.md) — personas, instituciones y financiamiento.
- [`docs/marco-regulatorio.md`](docs/marco-regulatorio.md) — Ley 7593/2025, Política Ética 2024, Resolución 367/2020, CARE Principles.
- [`docs/ai-stack-reference.md`](docs/ai-stack-reference.md) — **referencia completa del stack de IA open source**: AlphaFold 3, Boltz-2, MedGemma, ESM3, pathology FMs, BioNeMo, etc. Con licencias y casos de uso.

### Plan de trabajo

- [`docs/plan-preparacion.md`](docs/plan-preparacion.md) — fases 1–6 de investigación previa antes de iniciar cualquier proyecto real.

## Áreas de investigación prioritarias (resumen)

1. **Vigilancia genómica** — pipelines reproducibles (Nextclade, Augur, nf-core) sobre datos que LCSP ya genera para dengue, SARS-CoV-2, monkeypox y Chagas.
2. **Descubrimiento de fármacos para enfermedades desatendidas** — uso de **Boltz-2**, AlphaFold 3, DiffDock y herramientas generativas sobre dianas de *T. cruzi* y *Leishmania*, en alianza con BioProsNat (CEMIT-UNA), CEDIC y Tesabio.ai.
3. **Modelos de lenguaje clínico en español paraguayo** — fine-tuning de **MedGemma 4B/27B** sobre notas clínicas locales, despliegue en HIVE BUZZ.
4. **Patología digital e imágenes médicas** — modelos fundacionales (**CONCH, UNI, Virchow2, MedSAM**) aplicados a la primera cohorte digital del INCAN.
5. **Resistencia antimicrobiana** — predicción de resistencia a partir de genómica (Mykrobe, TBProfiler) sobre la red del IICS, aprovechando la convocatoria 2026 FAPESP-CONACYT-CONICET.
6. **Salud mental y triaje** — LLM clínicos para tamizaje de depresión e ideación suicida, donde solo el 28 % de los pediatras paraguayos tiene conocimiento alto.
7. **Telemedicina y atención primaria** — modelos para telesalud rural en alianza con la Ley 5482/2015 y Resolución 367/2020.
8. **Capacitación en investigación clínica** — cerrar la brecha de bioestadística e investigación en residencias (78% sin metodología posgrado), mediante herramientas y plantillas abiertas.

## Tres recomendaciones principales de IA open-source para Paraguay

1. **Boltz-2** (MIT, full open) — drug discovery. Único modelo AF3-clase con licencia comercial OK. Hace estructura + afinidad. **Mayor gap-closer único para CEDIC × BioProsNat × Tesabio.**
2. **MedGemma 4B** (Apache wrapper + Health AI Dev Foundations License) — clinical NLP. Best entry point para Hospital de Clínicas. Español-capaz, fine-tuneable en una sola GPU, corre en HIVE BUZZ.
3. **NVIDIA BioNeMo Agent Toolkit** (CC BY 4.0) — único framework de agentes bio activamente mantenido, agent-agnostic, gratis para prototyping.

Honorable mentions: AlphaGenome (variant interpretation), scFoundry + Geneformer (single-cell), Midnight/OpenMidnight (pathology FM entrenable desde datos públicos).

## Estructura del repositorio

```
ai-medica-paraguay/
├── README.md                       Este archivo
├── docs/                           Documentos principales
│   ├── research-areas.md           8 áreas — estrategia
│   ├── research-findings.md        Hallazgos consolidados sobre Paraguay
│   ├── research-session-log.md     Log cronológico de sesiones
│   ├── research-sources.md         Bibliografía verificada
│   ├── mapa-actor-instituciones.md Personas, instituciones, financiamiento
│   ├── marco-regulatorio.md        Ley 7593/2025, Política Ética 2024
│   ├── ai-stack-reference.md       Catálogo del stack IA open source
│   └── plan-preparacion.md         Fases 1–6 antes de proyecto real
├── areas/                          Una carpeta por área de investigación
│   ├── genomic-surveillance/
│   ├── drug-discovery/             (patches con Boltz-2 prioritario)
│   ├── clinical-llms/              (patches con MedGemma + OpenMedLM)
│   ├── pathology-imaging/
│   ├── antimicrobial-resistance/
│   ├── mental-health/
│   ├── telemedicine/
│   └── medical-research-training/
├── assets/                         Logos, figuras, plantillas
└── references/                     PDFs, papers clave, resoluciones
```

Cada carpeta `areas/*` contiene un `README.md` con descripción del área, herramientas de código abierto relevantes, contactos paraguayos y posibles proyectos concretos.

## Principios

- **Código abierto por defecto.** Usar y contribuir a herramientas abiertas (Nextstrain, nf-core, MedGemma, Boltz, etc.). Nada propietario en el flujo principal.
- **Construir con, no para.** Toda investigación se hace con coinvestigadores paraguayos; los papers y los modelos llevan coautoría local.
- **Cumplimiento regulatorio temprano.** DPIA y protocolos de consentimiento antes de tocar datos de pacientes.
- **Soberanía de datos.** Los datos paraguayos quedan en Paraguay. Cualquier modelo entrenado es abierto y reproducible localmente.
- **Lengua.** El español paraguayo y el guaraní son primeras clases; los modelos deben reconocerlos.

## Próximos pasos

Antes de iniciar cualquier proyecto concreto, falta cerrar varias líneas de investigación previa (ver `docs/plan-preparacion.md`):

- Mapear investigadores en formación (postdocs y residentes) que serían usuarios reales.
- Leer a fondo la Política Nacional de Ética en Investigación en Salud (PAHO, agosto 2024) y la Ley 7593/2025.
- Confirmar el estado actual del biobanco CEDIC × Galatea Bio.
- Identificar convocatorias abiertas (PROCIENCIA II 2026, FAPESP-CONACYT AMR 2026, CZI EOSS, Google.org).
- Construir un demo mínimo viable (MedGemma 4B + notas clínicas sintéticas en español paraguayo).

## Licencia

Documentación bajo CC BY 4.0. Código bajo Apache 2.0 (cuando se agregue).