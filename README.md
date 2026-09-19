# AI Médica Paraguay

> **Investigación y prototipos abiertos para integrar inteligencia artificial de código abierto en la investigación médica y atención clínica del Paraguay.**
>
> Estado: **fase de exploración y mapeo** (septiembre 2026). Este repositorio documenta áreas de investigación prioritarias, personas e instituciones, oportunidades concretas de proyectos y vacíos de información que necesitamos cerrar antes de iniciar trabajo real.
>
> **Documento ejecutable:** si vas a actuar, abre [`docs/playbook-acciones.md`](docs/playbook-acciones.md) o [`MEJORES-COSAS-PARAGUAY.md`](MEJORES-COSAS-PARAGUAY.md). **Si vas a investigar:** [`INDEX.md`](INDEX.md) es el mapa completo.

---

## ¿Por qué Paraguay?

Paraguay tiene capacidades biomédicas reales y concentradas (**IICS-UNA, LCSP, CEDIC, INCAN, Hospital de Clínicas, BioProsNat/CEMIT-UNA**) que podrían multiplicarse con herramientas de IA de código abierto bien adaptadas. La ventana regulatoria está abierta: la **Ley 7593/2025 de protección de datos personales** entra en vigencia en noviembre de 2027 y no existe todavía un marco de aprobación para IA clínica. Hay enfermedades desatendidas (**Chagas, dengue, tuberculosis**) donde Paraguay ya es referente regional y donde la IA puede acelerar diagnósticos, vigilancia genómica y descubrimiento de fármacos.

## Tres recomendaciones principales de IA open-source para Paraguay

1. **MedGemma 4B** (HAI-DEF, Apache wrapper) — clinical NLP. Best entry point para Hospital de Clínicas. Español-capaz, fine-tuneable en una sola GPU, corre en HIVE BUZZ.
2. **TxGemma 27B-Chat** (Gemma terms) — drug discovery. Sleeper hit para CEDIC × BioProsNat × Tesabio. Queries terapéuticas en español, ADMET, binding affinity.
3. **HeAR** (HAI-DEF) — health acoustics. **Sleeper hit social**: TB cough screening en smartphone para el Chaco, deployable hoy.

**Honorable mentions:** Boltz-2 + OpenFold3 (estructura AF3-class con licencia comercial), NVIDIA BioNeMo Agent Toolkit (orquestación), AlphaGenome (variant interpretation para CEDIC × Galatea), Path/CXR/Derm Foundation (image embeddings para INCAN/Hospital de Clínicas).

---

## Cómo navegar (por tiempo disponible)

| Si tienes… | Lee… |
|---|---|
| **5 minutos** | Este README. |
| **30 minutos** | README + [`docs/research-areas.md`](docs/research-areas.md). |
| **2 horas** | README + research-areas + [`docs/research-findings.md`](docs/research-findings.md) + [`docs/ai-stack-reference.md`](docs/ai-stack-reference.md). |
| **Vas a actuar** | [`docs/playbook-acciones.md`](docs/playbook-acciones.md) o [`MEJORES-COSAS-PARAGUAY.md`](MEJORES-COSAS-PARAGUAY.md). |
| **Vas a decidir** | research-findings + [`docs/plan-preparacion.md`](docs/plan-preparacion.md). |
| **Vas a hablar con alguien en PY** | [`docs/mapa-actor-instituciones.md`](docs/mapa-actor-instituciones.md) + [`docs/marco-regulatorio.md`](docs/marco-regulatorio.md). |
| **Vas a elegir herramientas** | [`docs/ai-stack-reference.md`](docs/ai-stack-reference.md) + [`docs/google-deepmind-paraguay.md`](docs/google-deepmind-paraguay.md). |
| **Vas a elegir QUÉ construir** (de las 100 opciones) | [`research/100-ideas-poc.md`](research/100-ideas-poc.md) o [`research/master-ranking.md`](research/master-ranking.md). |
| **Vas a ejecutar** (protocolo nivel proyecto) | [`research/top-5-detalle-completo.md`](research/top-5-detalle-completo.md). |
| **Vas a verificar fuentes** | [`docs/research-sources.md`](docs/research-sources.md). |

---

## Áreas de investigación prioritarias

| # | Área | Carpeta | Estado |
|---|---|---|---|
| 1 | **Vigilancia genómica** — pipelines reproducibles (Nextclade, Augur, nf-core) sobre datos que LCSP ya genera para dengue, SARS-CoV-2, monkeypox y Chagas | [`areas/genomic-surveillance/`](areas/genomic-surveillance/README.md) | baseline |
| 2 | **Descubrimiento de fármacos para enfermedades desatendidas** — Boltz-2, AlphaFold 3, DiffDock y herramientas generativas sobre dianas de *T. cruzi* y *Leishmania*, en alianza con BioProsNat (CEMIT-UNA), CEDIC y Tesabio.ai | [`areas/drug-discovery/`](areas/drug-discovery/README.md) | patched con Boltz-2 |
| 3 | **Modelos de lenguaje clínico en español paraguayo** — fine-tuning de MedGemma 4B/27B sobre notas clínicas locales, despliegue en HIVE BUZZ | [`areas/clinical-llms/`](areas/clinical-llms/README.md) | patched con MedGemma + OpenMedLM |
| 4 | **Patología digital e imágenes médicas** — modelos fundacionales (CONCH, UNI, Virchow2, MedSAM) sobre la primera cohorte digital del INCAN | [`areas/pathology-imaging/`](areas/pathology-imaging/README.md) | baseline |
| 5 | **Resistencia antimicrobiana** — predicción de resistencia a partir de genómica (Mykrobe, TBProfiler) sobre la red del IICS, convocatoria 2026 FAPESP-CONACYT-CONICET | [`areas/antimicrobial-resistance/`](areas/antimicrobial-resistance/README.md) | baseline |
| 6 | **Salud mental y triaje** — LLM clínicos para tamizaje de depresión e ideación suicida (28% pediatras PY con conocimiento alto) | [`areas/mental-health/`](areas/mental-health/README.md) | baseline |
| 7 | **Telemedicina y atención primaria** — modelos para telesalud rural (Ley 5482/2015 + Resolución 367/2020) | [`areas/telemedicine/`](areas/telemedicine/README.md) | baseline |
| 8 | **Capacitación en investigación clínica** — cerrar la brecha de bioestadística en residencias (78% sin metodología posgrado) | [`areas/medical-research-training/`](areas/medical-research-training/README.md) | baseline |
| 9 | **Health acoustics & TB cough screening** *(nueva sept 2026)* — HeAR + clasificador lineal + smartphone para screening de TB en comunidades rurales chaqueñas | [`areas/health-acoustics-tb-screening/`](areas/health-acoustics-tb-screening/README.md) | nuevo |

Cada `areas/*/README.md` describe: problema concreto en Paraguay, herramientas open-source relevantes, contactos paraguayos, posibles proyectos y vacíos de información.

---

## Estructura del repositorio

```
ai-medica-paraguay/                                  44 archivos · 39 .md · ~830 KB
├── README.md                                        ← este archivo (landing page)
├── INDEX.md                                         mapa completo (tabla con líneas y tamaños de cada doc)
├── MEJORES-COSAS-PARAGUAY.md                        la síntesis final: qué hacer, en qué orden, por qué
├── CHANGELOG.md                                     bitácora de sesiones (formato Keep-a-Changelog)
├── docs/                                            10 documentos de estrategia/contexto
│   ├── research-areas.md                            las 8 (→9) áreas — estrategia, qué hacer primero
│   ├── research-findings.md                         hallazgos consolidados sobre Paraguay (carga, capacidades, datos cuantitativos)
│   ├── ai-stack-reference.md                        catálogo IA open-source (AlphaFold 3, Boltz-2, MedGemma, ESM3, …)
│   ├── google-deepmind-paraguay.md                  análisis dedicado del portafolio Google/HAI-DEF para PY
│   ├── playbook-acciones.md                         playbook ejecutable: acciones Tier 1/2/3 por institución y enfermedad
│   ├── mapa-actor-instituciones.md                  personas, instituciones y financiamiento
│   ├── marco-regulatorio.md                         Ley 7593/2025 + Política Ética 2024 + Resolución 367/2020 + CARE
│   ├── plan-preparacion.md                          6 fases de investigación previa antes de iniciar proyecto real
│   ├── research-session-log.md                      log cronológico de las sesiones que construyeron este repo
│   └── research-sources.md                          bibliografía consolidada, URLs verificadas
├── areas/                                           9 carpetas (una por área de investigación)
│   ├── genomic-surveillance/
│   ├── drug-discovery/                              (patches con Boltz-2 prioritario)
│   ├── clinical-llms/                               (patches con MedGemma + OpenMedLM)
│   ├── pathology-imaging/
│   ├── antimicrobial-resistance/
│   ├── mental-health/
│   ├── telemedicine/
│   ├── medical-research-training/
│   └── health-acoustics-tb-screening/               (nuevo sept 2026)
└── research/                                        16 documentos de trabajo avanzado (rankings, protocolos, sinergias)
    ├── 100-ideas-poc.md                             100 ideas de POC rankeadas con scores
    ├── master-ranking.md                            master ranking 130+ ideas con scoring consistente
    ├── top-10-explicado.md                          top 10 explicadas en profundidad (paso a paso)
    ├── top-5-detalle-completo.md                    top 5 a nivel protocolo de ejecución (epidemiología, arquitectura, gates, presupuesto)
    ├── analisis-tier1-profund.md                    análisis profundo Tier 1 (riesgos, compute, datasets, champions, funding)
    ├── peer-landscape.md                            qué hacen otros (Hospital Italiano, awesome lists, peer projects, gaps)
    ├── avances-medicina-posibilidades-paraguay.md   avances médicos 2024-2026 + 10 oportunidades first-mover
    ├── LA-IDEA-COMPLETA.md                          capstone v1 (superado por EL-PLAN-MAESTRO)
    ├── LA-IDEA-COMPLETA-v2.md                       capstone v2 (corrección de roles + inventario AIW)
    ├── EL-PLAN-MAESTRO.md                           EL PLAN MAESTRO actual — 2 tracks (Ometz/foso), 16 meses
    ├── SISTEMA-OMETZ-TOP10.md                       top 10 ideas + arquitectura del sistema
    ├── sinergias-top5-extensiones.md                mapa de sinergias (motor/volante/salidas, 12 emergentes)
    ├── cancer-oral-smartphone-protocolo.md          protocolo: tamizaje de cáncer oral con smartphone
    ├── odontologia-40-ideas.md                      40 ideas de IA en odontología y salud bucal (ranking)
    ├── red-privada-odontologia-top5-gabi.md         re-estrategia red privada (top 5 para Gaby + secuencia 90 días)
    └── _gaby100/                                    corpus + 100 ideas para Gaby con evidencia académica (5 APIs)
        ├── harness.py                               motor reutilizable (PubMed, OpenAlex, Europe PMC, CORE, Unpaywall)
        ├── queries.json                             queries de las 2 pasadas (amplia + fina)
        ├── corpus_dental.json                       56 papers dentales relevantes (gitignored)
        ├── corpus_pass1.json                        131 papers brutos pasada 1 (gitignored por tamaño)
        ├── research_corpus.json                     corpus pasada fina
        └── 100-ideas-gaby.md                        100 ideas con evidencia + top-12 priorizada
```

---

## Documentos principales — qué hay en cada uno

### Estrategia y contexto (en `docs/`)
- [`docs/research-areas.md`](docs/research-areas.md) — descripción de las **8 (→9) áreas** con problemas, herramientas, proyectos concretos y vacíos. Priorización.
- [`docs/research-findings.md`](docs/research-findings.md) — hallazgos consolidados sobre Paraguay: carga de enfermedad, capacidades locales, datos cuantitativos, comparaciones regionales.
- [`docs/research-session-log.md`](docs/research-session-log.md) — log cronológico de las sesiones que construyeron este repo.
- [`docs/research-sources.md`](docs/research-sources.md) — bibliografía consolidada, todas las fuentes citadas con URLs y verificación.

### Mapas operativos (en `docs/`)
- [`docs/mapa-actor-instituciones.md`](docs/mapa-actor-instituciones.md) — personas, instituciones y financiamiento.
- [`docs/marco-regulatorio.md`](docs/marco-regulatorio.md) — Ley 7593/2025, Política Ética 2024, Resolución 367/2020, CARE Principles.
- [`docs/ai-stack-reference.md`](docs/ai-stack-reference.md) — catálogo completo del stack IA open source con licencias y casos de uso.
- [`docs/google-deepmind-paraguay.md`](docs/google-deepmind-paraguay.md) — análisis dedicado del portafolio Google/HAI-DEF.

### Plan y playbook ejecutable
- [`docs/plan-preparacion.md`](docs/plan-preparacion.md) — 6 fases de investigación previa antes de iniciar cualquier proyecto real.
- [`docs/playbook-acciones.md`](docs/playbook-acciones.md) — **el playbook ejecutable**: acciones Tier 1/2/3 por institución, enfermedad y capacidad. Por dónde arrancar la semana 1.
- [`MEJORES-COSAS-PARAGUAY.md`](MEJORES-COSAS-PARAGUAY.md) — **la guía definitiva**: la respuesta corta a "¿qué deberíamos hacer?".

### Trabajo avanzado (en `research/`)
- [`research/100-ideas-poc.md`](research/100-ideas-poc.md) — 100 ideas de POC rankeadas con análisis por enfermedad y capacidad.
- [`research/master-ranking.md`](research/master-ranking.md) — master ranking 130+ ideas con scoring consistente y anti-recomendaciones.
- [`research/top-10-explicado.md`](research/top-10-explicado.md) — top 10 explicadas en profundidad, paso a paso.
- [`research/top-5-detalle-completo.md`](research/top-5-detalle-completo.md) — top 5 a nivel protocolo de ejecución: epidemiología, arquitectura técnica, fases con gates, presupuesto línea por línea, equipo, ética, kill criteria.
- [`research/analisis-tier1-profund.md`](research/analisis-tier1-profund.md) — análisis profundo Tier 1 (riesgos, compute, datasets, champions, funding, reproducibilidad, timeline).
- [`research/peer-landscape.md`](research/peer-landscape.md) — qué hacen otros: Hospital Italiano, awesome lists, peer projects, gaps, partnerships.
- [`research/avances-medicina-posibilidades-paraguay.md`](research/avances-medicina-posibilidades-paraguay.md) — avances médicos 2024-2026 + 10 oportunidades first-mover específicas para Paraguay.
- [`research/EL-PLAN-MAESTRO.md`](research/EL-PLAN-MAESTRO.md) — el plan maestro internalizado: 2 tracks (Ometz/foso), secuencia 16 meses, números honestos, próxima acción.
- [`research/cancer-oral-smartphone-protocolo.md`](research/cancer-oral-smartphone-protocolo.md) — protocolo: tamizaje de cáncer oral con smartphone.
- [`research/odontologia-40-ideas.md`](research/odontologia-40-ideas.md) — 40 ideas de IA en odontología y salud bucal (ranking).
- [`research/red-privada-odontologia-top5-gabi.md`](research/red-privada-odontologia-top5-gabi.md) — re-estrategia red privada, top 5 para Gaby + secuencia 90 días.
- [`research/sinergias-top5-extensiones.md`](research/sinergias-top5-extensiones.md) — mapa de sinergias del sistema (motor/volante/salidas), 12 proyectos emergentes, orden de construcción.
- [`research/SISTEMA-OMETZ-TOP10.md`](research/SISTEMA-OMETZ-TOP10.md) — top 10 ideas + arquitectura completa del sistema.
- `research/LA-IDEA-COMPLETA.md` y `research/LA-IDEA-COMPLETA-v2.md` — versiones previas del capstone (superadas por `EL-PLAN-MAESTRO.md`).
- [`research/_gaby100/100-ideas-gaby.md`](research/_gaby100/100-ideas-gaby.md) — 100 ideas para Gaby con evidencia académica real (131 papers, 5 APIs).

---

## Principios

- **Código abierto por defecto.** Usar y contribuir a herramientas abiertas (Nextstrain, nf-core, MedGemma, Boltz, etc.). Nada propietario en el flujo principal.
- **Construir con, no para.** Toda investigación se hace con coinvestigadores paraguayos; los papers y los modelos llevan coautoría local.
- **Cumplimiento regulatorio temprano.** DPIA y protocolos de consentimiento antes de tocar datos de pacientes.
- **Soberanía de datos.** Los datos paraguayos quedan en Paraguay. Cualquier modelo entrenado es abierto y reproducible localmente.
- **Lengua.** El español paraguayo y el guaraní son primeras clases; los modelos deben reconocerlos.

## Próximos pasos

Antes de iniciar cualquier proyecto concreto, falta cerrar varias líneas de investigación previa (ver [`docs/plan-preparacion.md`](docs/plan-preparacion.md)):

- Mapear investigadores en formación (postdocs y residentes) que serían usuarios reales.
- Leer a fondo la Política Nacional de Ética en Investigación en Salud (PAHO, agosto 2024) y la Ley 7593/2025.
- Confirmar el estado actual del biobanco CEDIC × Galatea Bio.
- Identificar convocatorias abiertas (PROCIENCIA II 2026, FAPESP-CONACYT AMR 2026, CZI EOSS, Google.org).
- Construir un demo mínimo viable (MedGemma 4B + notas clínicas sintéticas en español paraguayo).

## Licencia

Documentación bajo CC BY 4.0. Código bajo Apache 2.0 (cuando se agregue).

## Repos relacionados

- [`IvanWeissVanDerPol/gonzalez-vs-odontologia3`](https://github.com/IvanWeissVanDerPol/gonzalez-vs-odontologia3) — caso laboral Dra. González Pane c/ Odontología 3 (sister repo, privado/público)
- [`Ai-Whisperers/gaby-client-engine`](https://github.com/Ai-Whisperers/gaby-client-engine) — operaciones de acquisition para Ometz Dental
- [`Ai-Whisperers/dentist`](https://github.com/Ai-Whisperers/dentist) — enciclopedia estratégica dental (400+ archivos)