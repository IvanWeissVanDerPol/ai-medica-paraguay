# Lo que Paraguay puede hacer con el stack de IA — playbook completo

> **Qué es este archivo:** un único documento que consolida todas las acciones concretas que Paraguay podría tomar con el stack de IA open-source (Google + third-party). Cada acción tiene: objetivo, herramientas, actores locales, esfuerzo estimado, primer paso concreto.
>
> **Audiencia:** quien quiera ejecutar algo. Ya sea vos, un equipo en Paraguay, un socio académico, un financiador, un aliado técnico.
>
> **Última actualización:** septiembre 2026.

---

## Índice rápido

- §1 — Acciones Tier 1 (rápidas, alto impacto, costo bajo)
- §2 — Acciones Tier 2 (estratégicas, co-financiamiento externo)
- §3 — Acciones Tier 3 (largo plazo, institucionales)
- §4 — Acciones por institución paraguaya (mapa rápido)
- §5 — Acciones por enfermedad (Chagas / TB / dengue / cáncer / salud mental)
- §6 — Acciones por capacidad a construir (capacitación / datos / infraestructura / regulación)
- §7 — Matriz de priorización: esfuerzo × impacto
- §8 — Cómo arrancar (semana 1, semana 2, semana 3, semana 4)

---

## §1 — Tier 1: Acciones rápidas (1–3 meses, costo bajo)

Estas son las que recomiendo arrancar primero. Cada una resuelve un dolor inmediato y deja infraestructura reusable para las siguientes.

### 1.1 Taller Nextclade + nf-core en LCSP — vigilancia genómica reproducible

- **Objetivo:** estandarizar el pipeline bioinformático de LCSP para dengue, SARS-CoV-2, MPXV, Chagas. Hoy es ad-hoc.
- **Herramientas:** [Nextclade](https://github.com/nextstrain/nextclade), [Augur + Auspice](https://github.com/nextstrain/augur), [nf-core/viralrecon](https://github.com/nf-core/viralrecon), [Genome Detective](https://www.genomedetective.com) (ya usado por LCSP).
- **Actores paraguayos:** LCSP (Dra. Cynthia Vazquez), IICS-UNA, FCQ-UNA, UNCA.
- **Esfuerzo:** $5–10k USD (viajes + honorarios facilitador externo, p.ej. CABANA). 1 persona 2 semanas para instalación + 2 días para taller.
- **Entregables:** SOPs en español, dashboard Nextstrain público, GitHub repo con pipeline reproducible, paper de métodos en revista regional.
- **Primer paso:** email a Dra. Cynthia Vazquez con la nota: *"vi su paper sobre MPXV, acá va cómo automatizaríamos este flujo con Nextclade + nf-core, ¿tenemos 30 min?"*

### 1.2 MedGemma 4B piloto en Hospital de Clínicas — clinical LLM en español paraguayo

- **Objetivo:** probar y fine-tunear MedGemma 4B (HAI-DEF) para tareas de triaje + resumen sobre notas clínicas en español paraguayo.
- **Herramientas:** [MedGemma 4B](https://huggingface.co/collections/google/medgemma) (HAI-DEF, fine-tuneable en una sola GPU), [OpenMedLM](https://github.com/OpenMedLM) (Yi 34B prompting como baseline), [RAG sobre guías MSPBS](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card), Whisper fine-tune para ASR guaraní si hay audio.
- **Actores paraguayos:** Hospital de Clínicas (UNAchampion clínico), FCM-UNA (Cátedra de Psiquiatría), HIVE BUZZ GPU cluster.
- **Esfuerzo:** $5–15k USD (annotation + GPU). 1 persona 1 mes.
- **Entregables:** notebook ejecutable, paper de evaluación, open-weight model fine-tuneado, ruta para piloto clínico.
- **Primer paso:** construir demo mínimo viable (notebook que toma notas clínicas sintéticas y produce resumen estructurado).

### 1.3 TxGemma 27B-Chat + Boltz-2 sobre BioProsNat — drug discovery queries en español

- **Objetivo:** usar TxGemma para queries ADMET (toxicidad, BBB penetration, CYP inhibition) sobre la biblioteca de productos naturales paraguayos de BioProsNat. Priorizar hits para validación experimental en CEDIC.
- **Herramientas:** [TxGemma 27B-Chat](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card) (Gemma terms, comercial OK), [Boltz-2](https://github.com/jwohlwend/boltz) (MIT, comercial OK), [OpenFold3](https://github.com/aqlaboratory/openfold-3) (Apache 2.0, comercial OK), [TrypanoDB](https://tritrypdb.org), [TDC](https://tdcommons.ai/).
- **Actores paraguayos:** BioProsNat (CEMIT-UNA), CEDIC, Tesabio.ai, FIUNA (Diego Galeano).
- **Esfuerzo:** $5–15k USD (GPU + API). 1 persona 2 meses.
- **Entregables:** paper con hit list priorizada para Chagas, pipeline reproducible open-source, aplicación a convocatoria 2026 FAPESP-CONACYT-CONICET AMR.
- **Primer paso:** email a Diego Galeano (Tesabio CTO): *"armamos un pipeline end-to-end con TxGemma + Boltz-2 + CEDIC para Chagas — ¿tenemos 30 min?"*

### 1.4 HeAR para TB cough screening — proyecto social de mayor impacto

- **Objetivo:** deployar un sistema smartphone-based que use HeAR (Google HAI-DEF) para detectar TB por análisis de tos en comunidades rurales chaqueñas donde no hay acceso a chest X-ray.
- **Herramientas:** [HeAR](https://huggingface.co/google/hear) (HAI-DEF, embeddings 512-d, 300M+ clips entrenados), [Whisper](https://github.com/openai/whisper), [TensorFlow Lite](https://www.tensorflow.org/lite) o [ONNX Runtime Mobile](https://onnxruntime.ai) para deploy, [React Native](https://reactnative.dev) o [Flutter](https://flutter.dev) para app.
- **Datasets para bootstrap:** COUGHVID, SPRSound, ICBHI 2017, FluSense, FSD50K (todos públicos).
- **Actores paraguayos:** SENEPA, Hospital General de Barrio Obrero, Hospital de Clínicas (Cátedra de Neumología), CEDIC (campo chaqueño).
- **Esfuerzo:** $10–30k USD (dataset local + app + field pilot). 2 personas 6 meses.
- **Entregables:** paper de viabilidad técnica, dataset local etiquetado (con CARE Principles si hay comunidades indígenas), app móvil funcional, paper de field validation.
- **Primer paso:** linear probe sobre COUGHVID + SPRSound con HeAR público; validar la premisa técnica antes de capturar datos locales.
- **Por qué esto es el sleeper hit social:** Paraguay hiperendémico para TB en Chaco; HeAR deployable en smartphone HOY; éticamente alineado con CARE; replicable para COVID/asma/COPD después.

### 1.5 AlphaGenome para CEDIC × Galatea Bio biobank — variant interpretation

- **Objetivo:** cada nueva variante secuenciada en el biobanco paraguayo → AlphaGenome API → score de impacto regulatorio. Combinar con AlphaGenome Atlas (9B precomputed).
- **Herramientas:** [AlphaGenome API](https://deepmind.google/science/alphagenome) (no comercial, gratis), [AlphaGenome Atlas](https://deepmind.google/science/alphagenome/atlas) (browser para 9B SNVs), [Genomic Variant Calling pipelines](https://github.com/google-deepmind/alphagenome).
- **Actores paraguayos:** CEDIC, Universidad Nacional del Este, Galatea Bio.
- **Esfuerzo:** $1–5k USD (solo API costs). 1 persona 2 semanas para setup.
- **Entregables:** paper de valor agregado del biobanco, dashboard interno, metodología replicable.
- **Primer paso:** confirmar estado actual del biobanco con CEDIC y Galatea Bio.

### 1.6 Capacitación: Bioinformática + Galaxy para residentes

- **Objetivo:** cerrar la brecha de conocimiento de los 500 residentes de CONAREM (78% sin metodología posgrado) en bioinformática.
- **Herramientas:** [Galaxy](https://galaxyproject.org), [nf-core](https://github.com/nf-core), [RMarkdown](https://rmarkdown.rstudio.com), [Bioconductor](https://bioconductor.org), notebooks HAI-DEF oficiales.
- **Actores paraguayos:** CONAREM, FCM-UNA, Hospital de Clínicas, IICS-UNA, AB3C o SoIBio (alianza regional), CABANA (workshop partner).
- **Esfuerzo:** $5–15k USD (facilitador + materiales). 1 taller de 5 sesiones.
- **Entregables:** materiales del curso en español, certificado como EMC (educación médica continua), 30+ residentes entrenados, paper sobre la experiencia.
- **Primer paso:** confirmar champion en CONAREM o FCM-UNA.

---

## §2 — Tier 2: Acciones estratégicas (3–9 meses, co-financiamiento externo)

Estas son las que requieren partnerships externos, financiamiento, o tiempo significativo. Son las que **definen el posicionamiento regional de Paraguay en IA médica**.

### 2.1 Pipeline TxGemma + Boltz-2 + OpenFold3 + CEDIC wet-lab (drug discovery end-to-end)

- **Objetivo:** cerrar el loop completo de drug discovery para Chagas: estructura 3D de dianas (*T. cruzi*) → screening virtual con productos naturales paraguayos → predicción de ADMET con TxGemma → validación experimental in vitro en CEDIC.
- **Herramientas:** TxGemma, Boltz-2, OpenFold3, TDC, TrypanoDB.
- **Actores paraguayos:** CEDIC, BioProsNat, Tesabio.ai, FIUNA, IICS Producción.
- **Financiamiento:** convocatoria 2026 FAPESP-CONACYT-CONICET AMR (R$300k), CZI EOSS ($100k), IDB Lab (~$100k).
- **Esfuerzo:** 3 investigadores 6 meses. ~$50k USD total.
- **Entregables:** paper con hit list validada experimentalmente, pipeline open-source, modelo predictivo entrenado con datos paraguayos.
- **Por qué importa:** Paraguay se convierte en referente regional de drug discovery con IA para enfermedades desatendidas. Tesabio escala. BioProsNat se internacionaliza.

### 2.2 MedGemma 4B fine-tuneado en español paraguayo (clinical NLP production-ready)

- **Objetivo:** construir un corpus de notas clínicas en español paraguayo (synthetic + IRB-approved) y fine-tunear MedGemma 4B o 27B para tareas específicas del Hospital de Clínicas.
- **Herramientas:** MedGemma 4B/27B, LoRA/QLoRA, datasets sintéticos generados por LLM + revisados por médicos locales.
- **Actores paraguayos:** Hospital de Clínicas, FCM-UNA, HIVE BUZZ, Tesabio.
- **Financiamiento:** PROCIENCIA II (Gs. 90M ≈ $12k), CZI EOSS ($100k), Wellcome Trust.
- **Esfuerzo:** 4 personas 6 meses. ~$50–150k USD.
- **Entregables:** modelo open-weight fine-tuneado, paper de evaluación, piloto de despliegue.
- **Por qué importa:** Paraguay se convierte en el referente regional de medical AI en español. Es el "first mover" advantage.

### 2.3 INCAN patología digital pilot — first national digital pathology network

- **Objetivo:** escanear 1.000 slides de H&E retrospectivos de INCAN, aplicar Path Foundation / CONCH / MedSAM para detección de tumor, validar contra patólogos.
- **Herramientas:** slide scanner (~$15–50k), Path Foundation (HAI-DEF), CONCH (research use), MedSAM (MIT).
- **Actores paraguayos:** INCAN, Sociedad Paraguaya de Anatomía Patológica, Hospital de Clínicas, City Cancer Challenge.
- **Financiamiento:** IDB Lab, PROCIENCIA II + co-financing, CZI EOSS.
- **Esfuerzo:** 6–12 meses. ~$100k USD (incluye scanner).
- **Entregables:** paper de validación, dataset abierto, white paper regulatorio para MSPBS.
- **Por qué importa:** Paraguay entra al grupo de países con patología digital sistemática. Es infraestructura para futuras investigaciones de cáncer.

### 2.4 Biobank genómico nacional (extensión CEDIC × Galatea Bio)

- **Objetivo:** expandir el biobanco CEDIC × Galatea Bio para incluir no solo COVID sino todas las enfermedades relevantes paraguayas (Chagas, cáncer hereditario, TB, dengue), con análisis integrado de AlphaGenome.
- **Herramientas:** AlphaGenome API, OpenFold3, TrypanoDB, GISAID para viral.
- **Actores paraguayos:** CEDIC, Universidad Nacional del Este, Galatea Bio, IICS, Hospital de Clínicas, LCSP.
- **Financiamiento:** Stanford (vía Galatea), CZI EOSS, IDB Lab, NIH Fogarty.
- **Esfuerzo:** 12+ meses, multi-institucional. ~$200k USD.
- **Entregables:** biobanco nacional FAIR-aligned, paper multi-institucional, infraestructura para futuras investigaciones.

### 2.5 TB cough screening field validation en Chaco (extensión de 1.4)

- **Objetivo:** después de validar la técnica con datos públicos (1.4), capturar datos locales en Chaco con SENEPA + CEDIC. Validar con gold-standard TB (microbiología, GeneXpert).
- **Herramientas:** HeAR, datasets públicos + dataset local, app móvil en producción.
- **Actores paraguayos:** SENEPA, CEDIC (campo chaqueño), Hospital General de Barrio Obrero (TB), comunidades chaqueñas.
- **Financiamiento:** IDB Lab, JICA (vía Nagasaki), CZI EOSS.
- **Esfuerzo:** 12 meses. ~$100k USD.
- **Entregables:** app en producción, paper de field validation, política pública MSPBS.
- **Por qué importa:** es el primer deployment clínico real de IA médica en Paraguay. Marca precedente regulatorio.

---

## §3 — Tier 3: Acciones institucionales de largo plazo (12+ meses)

Estas son las que cambian la posición de Paraguay en el mapa regional. Requieren tiempo y voluntad política.

### 3.1 National AI Strategy for Healthcare (MSPBS + MITIC)

- **Objetivo:** ayudar a Paraguay a diseñar su primera estrategia nacional de IA en salud, alineada con Ley 7593/2025 y con el vacío regulatorio que se puede convertir en oportunidad.
- **Actores:** MSPBS, MITIC, IICS, INCAN, CONACYT, PAHO/WHO.
- **Esfuerzo:** white paper + workshops. ~6 meses.
- **Entregables:** documento estratégico, framework regulatorio para IA clínica (primer país LatAm), white paper público.
- **Por qué importa:** Paraguay sería el primer país LatAm con framework explícito para IA clínica. Es un precedente.

### 3.2 Paraguay Biobank FAIR-aligned nacional

- **Objetivo:** infraestructura de datos genómicos paraguayos alineada con FAIR, conectada con Galatea Bio y otros biobancos internacionales.
- **Actores:** CEDIC, IICS, Universidad Nacional del Este, Hospital de Clínicas, Galatea Bio, CZI.
- **Financiamiento:** CZI EOSS ($1M+), IDB, Wellcome Trust, NIH Fogarty.
- **Esfuerzo:** 24+ meses. ~$1M USD.
- **Entregables:** biobanco nacional FAIR, papers, infraestructura para generaciones futuras.

### 3.3 Centro de IA Médica en Asunción (AECID-style partnership)

- **Objetivo:** establecer un centro dedicado de IA médica en Paraguay, similar a AECID partnerships o al Centro de IA del Hospital Italiano de Buenos Aires.
- **Actores:** UNA, FIUNA, Tesabio, INCAN, Hospital de Clínicas, aliados internacionales (Stanford, MIT, Imperial).
- **Financiamiento:** mixed (PROCIENCIA, CZI, IDB, aliados privados).
- **Esfuerzo:** 24+ meses. ~$5M USD.
- **Entregables:** centro físico + digital, 50+ investigadores, paper anual, spin-offs.

### 3.4 Tesabio commercialization + expansion LatAm

- **Objetivo:** apoyar a Tesabio a escalar su pipeline de drug discovery para Chagas y expandir a otros mercados LatAm.
- **Actores:** Tesabio, FIUNA, GRIDX, aliados en Brasil (USP, Fiocruz), aliados en Argentina (CONICET).
- **Esfuerzo:** continuous.
- **Entregables:** Tesabio Series A, pipeline de drug discovery comercial, partnerships.

### 3.5 AI Co-Scientist para Chagas drug repurposing (cuando Google abra acceso)

- **Objetivo:** aplicar AI Co-Scientist para drug repurposing en Chagas, siguiendo el playbook AML validado por Google en Nature 2026.
- **Actores:** IICS, CEDIC, Tesabio, FIUNA, aliados académicos.
- **Esfuerzo:** cuando Google abra Trusted Tester, aplicar.
- **Entregables:** hit list validada experimentalmente.

---

## §4 — Acciones por institución paraguaya

### IICS-UNA (Instituto de Investigaciones en Ciencias de la Salud)

1. **Taller Nextclade + nf-core** para vigilancia genómica viral — ver §1.1.
2. **Fine-tune MedGemma 4B** con notas clínicas paraguayas — ver §2.2.
3. **Aplicar AlphaGenome** a variantes del biobanco CEDIC × Galatea — ver §1.5.
4. **Capacitación en bioinformática para residentes** — ver §1.6.
5. **Aplicar Boltz-2 + OpenFold3 a dianas de *T. cruzi*** — ver §1.3.

### LCSP (Laboratorio Central de Salud Pública)

1. **Taller Nextclade + nf-core** — ver §1.1.
2. **Pipeline AlphaGenome** para variante interpretation — ver §1.5.
3. **Coordinación con IICS** para integración TB screening con HeAR — ver §1.4.

### CEDIC (Centro para el Desarrollo de la Investigación Científica)

1. **Validar pipeline TxGemma + Boltz-2 con su biblioteca experimental** — ver §1.3, §2.1.
2. **Biobank extension** con Galatea Bio + AlphaGenome integration — ver §2.4.
3. **Field work TB screening con SENEPA** — ver §1.4, §2.5.

### BioProsNat (CEMIT-UNA)

1. **Submit biblioteca de productos naturales a TxGemma + Boltz-2** — ver §1.3, §2.1.
2. **Validation cruzada** con datos experimentales in vitro de CEDIC.

### Tesabio.ai

1. **Partnership académico con FIUNA + CEDIC + BioProsNat** para Chagas drug discovery — ver §1.3, §2.1.
2. **Integration de OpenFold3** para estructura comercialmente usable — ver §1.3.
3. **Pipeline TxGemma** para queries terapéuticas en español — ver §1.3.

### FIUNA (Facultad de Ingeniería, UNA)

1. **Diego Galeano** es el bridge natural para todos los proyectos IA en Paraguay. Outreach inmediato.
2. **Diego Stalder** para time-series, Bayesian, bioengineering applications.
3. **Integration con Tesabio** para Chagas pipeline.
4. **Cómputo:** cluster HIVE BUZZ + X8 Cloud para proyectos pesados.

### INCAN (Instituto Nacional del Cáncer)

1. **Pathology digitalization pilot** — ver §2.3.
2. **Path Foundation / CONCH / MedSAM** para detección zero-shot — ver §2.3.
3. **City Cancer Challenge + LEGACY** partnerships para ampliar.

### Hospital de Clínicas (UNA)

1. **MedGemma 4B pilot** — ver §1.2, §2.2.
2. **Champions clínicos** para cada proyecto IA clínica.
3. **IRB processes** para todos los proyectos clínicos.
4. **Telemedicina con IA** (Resolución 367/2020) — ver §1.6.

### Hospital General de Barrio Obrero

1. **TB research active** — partner para HeAR TB screening.
2. **Datos de TB** accesibles para validación.

### Cátedra de Psiquiatría (FCM-UNA)

1. **Mental health LLM pilot** con MedGemma 4B fine-tuneado — ver §2.2.
2. **Telepsychiatry integration** con IA para ampliar alcance.

### SENEPA

1. **Field data collection** para TB cough screening — ver §1.4, §2.5.

### Universidad Nacional del Este

1. **Partner con CEDIC × Galatea Bio** para biobank.
2. **Crecimiento de research profile** vía proyectos IA.

---

## §5 — Acciones por enfermedad

### Chagas (*Trypanosoma cruzi*)

- **Pipeline completo:** TxGemma + Boltz-2 + OpenFold3 + CEDIC wet-lab (ver §2.1).
- **Vector ID:** YOLOv8/v10 para triatomine ID desde fotos (campo).
- **Phylodynamic surveillance:** Nextclade + Augur para *T. cruzi* DTUs.
- **Drug discovery:** BioProsNat products → TxGemma ADMET → Boltz-2 affinity → CEDIC validation.
- **CARE compliance** obligatorio para cualquier dato del Chaco.

### TB (tuberculosis)

- **Screening por tos:** HeAR + linear classifier + smartphone (ver §1.4, §2.5).
- **Resistance prediction:** Mykrobe + TBProfiler sobre WGS del IICS (ver §5 AMR).
- **CXR analysis:** CXR Foundation + fine-tune con datos paraguayos.

### Dengue / arbovirus

- **Genomic surveillance:** Nextclade + Augur + nf-core/viralrecon (ver §1.1).
- **Outbreak forecasting:** EpiNow2 + EpiCurve sobre datos LCSP.
- **Variant tracking:** AlphaGenome Atlas + API.

### Cáncer

- **Pathology digital:** Path Foundation / CONCH / MedSAM en INCAN (ver §2.3).
- **Molecular profiling:** MassARRAY data + AlphaGenome variant interpretation.
- **EHR summarization:** MedGemma 4B + RAG sobre historias clínicas.

### Salud mental (pediátrica)

- **Depression screening LLM:** MedGemma 4B fine-tuneado en español paraguayo (ver §2.2).
- **Triage conversational:** MedGemma 4B para atención primaria.
- **Suicide detection:** investigación cuidadosa, no es primer proyecto.

### AMR (resistencia antimicrobiana)

- **WGS resistance prediction:** Mykrobe + TBProfiler + AMRFinderPlus (ver §1.4 AMR).
- **17 años de datos IICS:** ML sobre archivo histórico (ver AMR existente).
- **Convocatoria 2026 FAPESP-CONACYT-CONICET AMR** ya identificada.

---

## §6 — Acciones por capacidad a construir

### Capacitación (training + literacy)

- **Talleres Galaxy/nf-core** para residentes (§1.6).
- **CABANA workshop** en Paraguay (training partner).
- **AI literacy** para investigadores senior (Gemini 2.5 Pro + prompting).
- **Capacitación en español paraguayo** para MedGemma 4B fine-tuning.

### Datos (datasets + biobanks)

- **Biobank nacional FAIR-aligned** (ver §3.2).
- **Dataset local de toses TB** (ver §2.5).
- **Corpus de notas clínicas en español paraguayo** (ver §2.2).
- **Dataset de productos naturales paraguayos** (ver §1.3).

### Infraestructura (compute + deployment)

- **HIVE BUZZ GPU cluster** como primary (ver §1.2, §2.2).
- **X8 Cloud** para proyectos pesados.
- **NVIDIA BioNeMo NIMs** para prototyping gratis (ver §1.3, §2.1).
- **Smartphones en el Chaco** para TB screening (ver §1.4).
- **On-prem servers** en IICS/CEDIC para datos sensibles.

### Regulación (compliance + frameworks)

- **National AI Strategy for Healthcare** (ver §3.1).
- **Compliance Ley 7593/2025** (DPIA template en `docs/marco-regulatorio.md`).
- **IRB approval processes** en cada piloto.
- **CARE Principles** para datos chaqueños.
- **HAI-DEF Prohibited Use compliance** — solo decision support, no autonomous diagnosis.

---

## §7 — Matriz de priorización: esfuerzo × impacto

```
                    Impacto bajo     Impacto medio      Impacto alto
Esfuerzo bajo       (ninguno)        Capacitación (1.6)  AlphaGenome (1.5)
                                                     Taller Nextclade (1.1)
                                                     TB HeAR (1.4)

Esfuerzo medio      (ninguno)        MedGemma (1.2)     TxGemma pipeline (1.3)

Esfuerzo alto       (ninguno)        (ninguno)           Pathology pilot (2.3)
                                                      MedGemma fine-tune (2.2)
                                                      Biobank nacional (2.4)
                                                      TB field validation (2.5)
```

**Recomendado arrancar**: esquina inferior derecha (esfuerzo bajo + impacto alto).

---

## §8 — Cómo arrancar (plan de 4 semanas)

### Semana 1 — Reconocimiento final

- [ ] Confirmar champions en Hospital de Clínicas, CEDIC, IICS, Tesabio, SENEPA (ver `docs/plan-preparacion.md`).
- [ ] Leer National Health Research Ethics Policy 2024 (crítico pendiente).
- [ ] Identificar datasets paraguayos disponibles (TB coughs, notas clínicas, variantes).
- [ ] Confirmar disponibilidad real de HIVE BUZZ para investigación médica.

### Semana 2 — Primer alcance externo

- [ ] Cold outreach a **Diego Galeano** (FIUNA + Tesabio CTO) — colaboración TxGemma + Tesabio.
- [ ] Cold outreach a **Cynthia Vazquez** (LCSP) — Nextclade + AlphaGenome.
- [ ] Cold outreach a **Rosa Guillén Fretes** (IICS, AMR) — Mykrobe + TBProfiler + HeAR.
- [ ] Cold outreach a champion en **Hospital de Clínicas** para MedGemma.
- [ ] Cold outreach a **SENEPA** para TB screening field work.

### Semana 3 — Primer artefacto

- [ ] Construir **demo MedGemma 4B** en notebook público con notas clínicas sintéticas en español paraguayo.
- [ ] Construir **pipeline Nextclade + nf-core** funcional para dengue (usando datos públicos, no locales todavía).
- [ ] Linear probe **HeAR** sobre COUGHVID (validación técnica, no local todavía).
- [ ] Construir **queries TxGemma** sobre 50 productos naturales públicos paraguayos.

### Semana 4 — Go/No-Go decision

- [ ] Evaluar respuestas de outreach. Si ≥3 champions confirmados → continuar.
- [ ] Evaluar demos. Si ≥1 funciona técnicamente → ir a propuesta formal.
- [ ] Aplicar a primera convocatoria externa (CZI EOSS, Google.org, o FAPESP-CONACYT 2026).
- [ ] Si Go: arrancar proyecto Tier 1 elegido. Si No-Go: ajustar outreach, reintentar.

---

## Resumen ejecutivo

**Las 5 acciones de mayor leverage inmediato** (esfuerzo bajo, impacto alto, técnicamente posibles hoy):

1. **TB cough screening con HeAR** (§1.4) — mayor impacto social, deployable en smartphone, éticamente alineado con CARE.
2. **Taller Nextclade + nf-core en LCSP** (§1.1) — abre la puerta a toda vigilancia genómica.
3. **MedGemma 4B pilot** (§1.2) — clinical NLP, infraestructura para todo lo clínico.
4. **TxGemma + Boltz-2 sobre BioProsNat** (§1.3) — drug discovery queries en español, pipeline cerrado con CEDIC.
5. **AlphaGenome + CEDIC biobank** (§1.5) — variant interpretation sobre datos paraguayos.

**Si solo pudiera hacer una**: TB cough screening con HeAR. Paraguay hiperendémico para TB, HeAR deployable HOY, éticamente perfecto, replicable para otras enfermedades respiratorias.

**Si pudiera hacer tres**: TB HeAR + Nextclade en LCSP + MedGemma 4B. Cubre vigilancia genómica + clinical NLP + screening rural.

**Si pudiera hacer todas las Tier 1**: cubriríamos vigilancia genómica + clinical NLP + drug discovery + screening rural + variant interpretation + capacitación en 6 meses con $50–80k USD total.

---

## Última actualización

Septiembre 2026.