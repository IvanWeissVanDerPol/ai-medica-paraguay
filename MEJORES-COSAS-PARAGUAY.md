# Mejores cosas que podemos hacer por Paraguay — guía definitiva

> **Qué es este archivo:** la síntesis final. Después de investigar todo el landscape, las 100 ideas rankeadas, lo que otros hacen, y los gaps reales — esta es la respuesta corta a "¿qué deberíamos hacer?".
>
> **Audiencia:** quien toma decisiones. Fundador, director, inversionista, aliado institucional.
>
> **Última actualización:** septiembre 2026.

---

## TL;DR — si solo lees 30 segundos

**Tres cosas, en orden de prioridad:**

1. **TB cough screening con HeAR en smartphone para el Chaco** — Paraguay hiperendémico para TB, HeAR deployable en smartphone HOY, éticamente alineado con CARE Principles. Único proyecto con cero dependencias regulatorias externas y máximo impacto social.

2. **Pipeline TxGemma + Boltz-2 + OpenFold3 + CEDIC para Chagas drug discovery** — el único país del mundo que tiene simultáneamente: CEDIC (wet-lab validation), BioProsNat (natural products), Tesabio (commercial biotech), FIUNA (AI), IICS (in vivo models). Paraguay puede ser el primer país en cerrar el loop end-to-end de drug discovery para Chagas.

3. **Hospital Italiano de Buenos Aires partnership técnico** — el modelo regional más cercano, mismo idioma, 27 años de trayectoria en informática en salud. Adopción directa de Argot (NLP clínico español), TANA (chatbot clínico), TRx (CXR AI) como blueprints para Hospital de Clínicas.

**Si pudiera hacer solo UNA:** TB cough screening con HeAR. La respuesta corta está en `research/100-ideas-poc.md` idea #1 con fit_score 10/10.

---

## §1 — Por qué Paraguay es especial para este momento

Paraguay tiene una combinación única de factores que convergen HOY:

### §1.1 Capacidades reales, no promesas

- **IICS-UNA**: 44 años, 10 departamentos, produce kits diagnósticos in vitro, infraestructura wet-lab completa, Red Nacional de Resistencia Antibiótica desde 2007
- **CEDIC**: tamizaje in vitro explícito sobre *T. cruzi*, screening *in silico*, alianza con Galatea Bio (Stanford), 5+ dianas terapéuticas validadas para Chagas
- **BioProsNat (CEMIT-UNA)**: biblioteca de productos naturales paraguayos con screening antimicrobiano, vínculos con UFPB/UFG/FIOCRUZ
- **Tesabio.ai**: startup paraguaya con SAB de Harvard/Broad/Cornell, pre-seed de GRIDX, equipo de 3 fundadores, foco en microARN
- **FIUNA**: Diego Galeano (PhD Royal Holloway, Tesabio CTO), Diego Stalder (deep learning), Benjamin Barán (ex presidente CONACYT, PRONII III)
- **LCSP**: BSL-3, Illumina MiSeq + MinION, opera Red Nacional de Vigilancia Genómica, 99 genomas dengue + 30 MPXV publicados
- **Hospital de Clínicas**: 45+ especialidades, 1.150 visitas/día, IRB institucional, residencia activa
- **INCAN**: perfil molecular de cáncer colorrectal, City Cancer Challenge partner, programa RACAM
- **HIVE BUZZ AI Cloud**: cluster GPU live desde marzo 2026
- **X8 Cloud**: MOU $8B firmado con ANDE (50→500 MW)

### §1.2 Vacíos únicos que Paraguay puede llenar

De `research/peer-landscape.md` §4 — **cinco gaps donde Paraguay puede ser first mover:**

1. **No Paraguayan Spanish clinical corpus** para fine-tuning de LLMs médicos
2. **No Paraguayan cough TB dataset** etiquetado
3. **No FAIR-aligned Paraguayan biobank** open
4. **No clinical AI regulatory framework** en Paraguay (ni en LatAm) — ventana antes de Nov 2027
5. **No scorpion envenoming AI POC** (1,383 casos Paraguay mid-2022 a mid-2023, 4 muertes pediátricas, *Tityus confluens* endémico en Chaco)

### §1.3 Marco regulatorio en apertura

- **Ley 7593/2025** (protección de datos) entra en vigencia noviembre 2027
- **Política Nacional de Ética en Investigación en Salud** (agosto 2024)
- **Resolución 367/2020** ya endosa IA/ML en telesalud
- **No hay framework regulatorio para IA clínica** — Paraguay puede diseñar el primero

### §1.4 Stack de IA disponible ahora

- Google HAI-DEF: MedGemma 4B/27B, TxGemma 2B/9B/27B, HeAR, Path/CXR/Derm Foundation, MedSigLIP, MedASR
- DeepMind: AlphaFold 3 (académico), AlphaGenome (API no comercial), AI Co-Scientist (futuro)
- Third-party open: Boltz-2 (MIT), OpenFold3 (Apache 2.0), LigandMPNN, Whisper guaraní baseline
- Infrastructure: NVIDIA BioNeMo NIMs (free for prototyping), HIVE BUZZ GPU, X8 Cloud

---

## §2 — Las 10 mejores cosas (concretas, ejecutables, rankeadas)

### #1 — TB cough screening con HeAR en smartphone para el Chaco

**Qué:** App móvil que graba tos → embedding HeAR (HAI-DEF) → clasificador → triage TB.
**Por qué #1:**
- Paraguay hiperendémico para TB en Chaco
- HeAR deployable en smartphone HOY (300M+ audio clips entrenados)
- Linear probe sobre datasets públicos (COUGHVID/SPRSound) en 1 semana
- Éticamente alineado con CARE Principles (comunidades chaqueñas)
- Replicable para COVID/asma/COPD después
- Cero dependencias regulatorias externas
**Actores:** SENEPA, Hospital General de Barrio Obrero, Hospital de Clínicas (Neumología), CEDIC (campo).
**Costo:** $10–30k USD. **Tiempo:** 2 personas 6 meses.
**Entregable:** paper de field validation + app funcional.
**Aplica a:** cualquier convocatoria de salud pública global.

### #2 — Pipeline TxGemma + Boltz-2 + OpenFold3 para Chagas drug discovery

**Qué:** Pipeline cerrado de AI para Chagas — dianas *T. cruzi* (cruzipaína, trans-sialidasa, TcGAPDH) → screening virtual BioProsNat → ADMET TxGemma-Chat → afinidad Boltz-2 → validación experimental CEDIC.
**Por qué #2:**
- Único país con la cadena completa cerrada (CEDIC + BioProsNat + Tesabio + FIUNA + IICS)
- Tesabio puede usar Boltz-2/OpenFold3 comercialmente (MIT/Apache 2.0)
- TxGemma queries en español para ADMET
- Aplica a convocatoria 2026 FAPESP-CONACYT-CONICET AMR
**Actores:** CEDIC, BioProsNat, Tesabio.ai, FIUNA, IICS Producción.
**Costo:** $5–15k USD + co-financiamiento FAPESP.
**Tiempo:** 1 persona 2 meses (paper técnico) + 6 meses (pipeline completo).
**Entregable:** paper con hit list + pipeline open-source.

### #3 — Hospital Italiano de Buenos Aires partnership técnico

**Qué:** Adopción de Argot (NLP clínico español maduro desde 2019), TANA (chatbot clínico desde 2023), TRx (CXR AI) como blueprints para Hospital de Clínicas.
**Por qué #3:**
- HIBA es el modelo regional más cercano (mismo idioma, mismo perfil de paciente)
- 27 años de trayectoria en informática en salud
- Programa pIASHIBA maduro (desde 2020)
- Productos open-source adaptables directamente
- Misiones técnicas cortas (2–4 semanas cada una)
**Actores:** DIS-HIBA, Argentina.
**Costo:** $5–10k (viaje + tiempo técnico).
**Tiempo:** 1–2 misiones técnicas en 6 meses.
**Entregable:** 3 blueprints adaptados al español paraguayo + paper conjunto.

### #4 — Nextclade + nf-core + Augur pipeline para vigilancia genómica LCSP

**Qué:** Estandarizar el pipeline bioinformático de LCSP para dengue, SARS-CoV-2, MPXV, Chagas. Hoy ad-hoc.
**Por qué #4:**
- Bajo costo ($5–10k)
- Alto impacto inmediato (ya producen genomas)
- Construye relación con actor clave
- Replicable a Chagas después
- Paper de métodos natural
**Actores:** LCSP (Dra. Cynthia Vazquez), IICS, FCQ-UNA, UNCA.
**Costo:** $5–10k USD. **Tiempo:** 1 persona 2 semanas + taller 2 días.
**Entregable:** SOPs en español, dashboard Nextstrain público, paper de métodos.

### #5 — MedGemma 4B piloto en Hospital de Clínicas

**Qué:** Fine-tune MedGemma 4B en español paraguayo para triaje y resumen de notas clínicas.
**Por qué #5:**
- Best entry point para clinical NLP en español
- Single-GPU fine-tuneable
- Deployable en HIVE BUZZ
- Sirve como infraestructura para todos los proyectos clínicos futuros
**Actores:** Hospital de Clínicas, HIVE BUZZ.
**Costo:** $5–15k USD. **Tiempo:** 1 persona 1 mes.
**Entregable:** modelo open-weight + paper de evaluación + piloto clínico.

### #6 — AlphaGenome + Atlas para variant interpretation en CEDIC × Galatea Bio

**Qué:** Cada nueva variante del biobanco CEDIC × Galatea Bio → AlphaGenome API → score de impacto regulatorio.
**Por qué #6:**
- Bajo costo (API costs)
- Valor inmediato al biobanco
- Paper natural
- Sin GPU requerido
**Actores:** CEDIC, Universidad Nacional del Este, Galatea Bio.
**Costo:** $1–5k USD. **Tiempo:** 1 persona 2 semanas.
**Entregable:** paper de valor agregado del biobanco + metodología.

### #7 — Smartphone ECG (D-Heart) + AI para Chagas cardiomyopathy en Chaco

**Qué:** Replicar el piloto boliviano exitoso. D-Heart smartphone ECG + ECGFounder (NEJM AI Nov 2025) + RDT para *T. cruzi*.
**Por qué #7:**
- Chagas cardiomyopathy es la #1 causa de muerte en Chagas crónico
- D-Heart probado en Bolivia Chaco (2021)
- ECGFounder (NEJM AI) es SOTA ECG FM
- Detección temprana salva vidas
**Actores:** CEDIC, Hospital de Clínicas (Cardiología), comunidades chaqueñas.
**Costo:** $5–15k USD (hardware + viaje). **Tiempo:** 1 persona 3 meses.
**Entregable:** paper de field validation.

### #8 — Capacitación CONAREM en Galaxy + nf-core

**Qué:** Taller de 5 sesiones para residentes sobre bioinformática práctica con Galaxy + nf-core + notebooks HAI-DEF.
**Por qué #8:**
- Multiplicador — entrena 30–50 residentes que se convierten en adopters
- Cierra la brecha de 78% sin metodología posgrado
- Crea infraestructura humana para todos los otros proyectos
**Actores:** CONAREM, FCM-UNA, IICS-UNA, alianza CABANA.
**Costo:** $5–15k USD. **Tiempo:** 1 taller.
**Entregable:** materiales del curso en español, certificados EMC, paper sobre la experiencia.

### #9 — Whisper fine-tune en guaraní médico

**Qué:** Fine-tune Whisper sobre el baseline existente de mfidabel/whisper-guarani para contexto médico.
**Por qué #9:**
- Baseline guaraní YA EXISTE en HuggingFace (mfidabel)
- Solo necesita contexto médico
- ~90% de rurales paraguayos hablan guaraní
- Vacío único que Paraguay puede llenar
**Actores:** Facultad de Medicina (Cátedra de Psiquiatría), Hospital de Clínicas.
**Costo:** $2–5k USD. **Tiempo:** 1 persona 2 meses.
**Entregable:** modelo Whisper fine-tuneado en guaraní + paper.

### #10 — Smartphone leishmaniasis cutánea app (replicación paper brasileño)

**Qué:** Replicar el paper brasileño PLOS NTDs 2025 (DenseNet121 + offline mobile) para leishmaniasis cutánea.
**Por qué #10:**
- Paper ya publicado, modelo entrenable
- Leishmaniasis endémica en Paraguay
- App offline mobile, deployable en Chaco
- Tiempo a paper: 3 meses
**Actores:** SENEPA, Hospital de Clínicas (Dermatología), CEDIC.
**Costo:** $5–15k USD. **Tiempo:** 1 persona 3 meses.
**Entregable:** app funcional + paper.

---

## §3 — Por orden de tiempo (4-week execution plan)

### Semana 1 — Reconocimiento
- [ ] Confirmar champions en Hospital de Clínicas, CEDIC, IICS, Tesabio
- [ ] Leer National Health Research Ethics Policy 2024 (crítico pendiente)
- [ ] Identificar datasets paraguayos disponibles

### Semana 2 — Primer alcance
- [ ] Cold outreach a Diego Galeano (FIUNA + Tesabio) — TxGemma + Tesabio (#2)
- [ ] Cold outreach a Cynthia Vazquez (LCSP) — Nextclade (#4)
- [ ] Cold outreach a Rosa Guillén Fretes (IICS, AMR) — AMR dashboard
- [ ] Cold outreach a Hospital de Clínicas champion — MedGemma (#5)
- [ ] Cold outreach a HIBA Argentina partnership (#3)

### Semana 3 — Primer artefacto
- [ ] Construir demo MedGemma 4B en notebook público
- [ ] Construir pipeline Nextclade para dengue
- [ ] Linear probe HeAR sobre COUGHVID
- [ ] Queries TxGemma sobre 50 productos naturales públicos

### Semana 4 — Go/No-Go decision
- [ ] Evaluar respuestas de outreach
- [ ] Evaluar demos
- [ ] Aplicar a primera convocatoria externa (CZI EOSS, Google.org, o FAPESP-CONACYT 2026)
- [ ] Si Go: arrancar proyecto Tier 1 elegido

---

## §4 — Por nivel de inversión

### $0 (solo tiempo)
- Construir 3-4 notebooks demo públicos (MedGemma, TxGemma, HeAR, Nextclade)
- Contribuir a awesome-medical-ai list
- Aplicar a fellowships / grants

### $5–10k (Tier 1 MVP)
- TB cough screening HeAR proof-of-concept (#1)
- Nextclade + nf-core en LCSP (#4)
- Capacitación CONAREM Galaxy (#8)
- HIBA partnership técnico inicial (#3)
- MedGemma 4B fine-tune MVP (#5)

### $10–50k (Tier 1 + Tier 2)
- TB HeAR field validation
- TxGemma + Boltz-2 + OpenFold3 Chagas pipeline (#2)
- Smartphone ECG Chagas cardiomyopathy (#7)
- Whisper guaraní fine-tune (#9)
- Leishmaniasis app (#10)
- AlphaGenome biobank integration (#6)

### $50–200k (Tier 2 + Tier 3)
- Field validation TB HeAR en Chaco
- Aplicación a convocatorias externas (FAPESP-CONACYT 2026, CZI EOSS, Wellcome)
- Biobank FAIR nacional
- Programa de IA clínica Hospital de Clínicas

### $200k+ (Tier 3 institucional)
- Centro de IA Médica en Asunción
- Tesabio commercialization
- National AI Strategy for Healthcare
- AI Co-Scientist para Chagas (cuando abra acceso)

---

## §5 — Por enfermedad

### Chagas (28 ideas en `research/100-ideas-poc.md`)
**Top-3:**
- #2 — TxGemma + Boltz-2 + OpenFold3 pipeline
- #7 — Smartphone ECG Chagas cardiomyopathy
- #11 — OpenFold3 *T. cruzi* target structures

### TB (7 ideas)
**Top-3:**
- #1 — TB cough screening con HeAR (recomendado #1 global)
- #24 — CXR Foundation TB CXR auto screen
- #25 — AMR dashboard nacional

### Dengue / arbovirus (9 ideas)
**Top-3:**
- #4 — Nextclade + nf-core en LCSP (recomendado #4 global)
- #17 — Outbreak forecasting con EpiNow2
- #41 — DENV-3 re-emergence monitoring

### Leishmaniasis / skin NTD (3 ideas)
**Top-3:**
- #6 — Smartphone leishmaniasis cutánea AI (recomendado #10 global)
- #12 — Skin NTD app Chaco
- #54 — Leishmaniasis drug target structure

### Cancer (8 ideas)
**Top-3:**
- #91 — CONCH + MedSAM pathology pilot INCAN
- #92 — Path Foundation H&E slide triage
- #23 — Path Foundation H. pylori gástrico

### Mental health (4 ideas)
**Top-3:**
- #19 — Telepsiquiatría MedGemma depresión pediátrica
- #21 — Chatbot WhatsApp salud mental guaraní
- #8 — Whisper fine-tune guaraní médico (recomendado #9 global)

### General clinical (24 ideas)
**Top-3:**
- #3 — MedGemma 4B fine-tune español paraguayo (recomendado #5 global)
- #13 — RAG MSPBS guías clínicas OpenMedLM
- #15 — Triaje urgencias MedGemma 4B

### Other (12 ideas)
**Top-3:**
- #22 — AlphaGenome variant effect pharmacogenética
- #31 — TB hotspots Bayesian inference (EPCON replication)
- #32 — Health Telematics HTI for TB (Tanzania replication)

---

## §6 — Por capacidad a construir

### Datos (datasets)
1. Corpus de notas clínicas en español paraguayo
2. Dataset de toses TB paraguayas etiquetadas
3. Slides H&E paraguayos INCAN digitalizados
4. Biobanco genómico FAIR-aligned CEDIC × Galatea
5. ECG dataset Chagas cardiomyopathy

### Capacitación (training)
1. Taller CONAREM Galaxy + nf-core (#8)
2. Fine-tune Whisper guaraní médico (#9)
3. Programa de intercambio IICS-HIBA
4. Capítulo Paraguay SoIBio/AB3C

### Infraestructura (compute)
1. HIVE BUZZ cluster (ya operativo)
2. X8 Cloud (when live, 50–500 MW)
3. NVIDIA BioNeMo NIMs (free for prototyping)
4. EMR4All OpenMRS en Raspberry Pi para rural

### Regulación (compliance)
1. White paper sobre IA clínica en Paraguay
2. DPIA template Ley 7593/2025 (ya existe en `docs/marco-regulatorio.md`)
3. CARE Principles compliance para datos chaqueños
4. HAI-DEF Prohibited Use compliance template

---

## §7 — Por partnership

### Tier 1 — Estratégicos
1. **Hospital Italiano (HIBA)** — Argot + TANA + TRx (#3)
2. **CABANA** — workshops bioinformatics Paraguay
3. **SoIBio / AB3C** — regional bioinformatics networks
4. **Google HAI-DEF team** — official support

### Tier 2 — Académicos
5. **NVIDIA BioNeMo team** — compute
6. **Stanford / Galatea Bio** — biobanco
7. **Fiocruz (Brasil)** — Galatea network
8. **NIH Fogarty** — LMIC training grants

### Tier 3 — Financiamiento
9. **CZI EOSS** — open-source tooling grants ($100k)
10. **Wellcome Trust** — LMIC-led research
11. **Google.org AI for Social Good** — workshop + compute
12. **IDB Lab** — innovation ($200k+)

---

## §8 — Top-5 cosas NO hacer

1. **No usar AlphaFold 3 pesos comercialmente** — son non-commercial. Usar OpenFold3 o Boltz-2.
2. **No hacer clinical AI deployment sin DPIA + DPO** — Ley 7593/2025 lo requiere.
3. **No deployar LLM clínico como dispositivo médico regulado** — HAI-DEF Prohibited Use lo prohíbe.
4. **No deployar AI sin consentimento explícito** en comunidades indígenas chaqueñas — CARE Principles.
5. **No construir desde cero lo que ya existe** — el stack Paraguay completo está mapeado en `research/peer-landscape.md`.

---

## §9 — Métricas de éxito (cómo saber si está funcionando)

### Corto plazo (3 meses)
- # de champions identificados en Paraguay (meta: 5+)
- # de demos construidos (meta: 3+)
- # de cold outreach enviados (meta: 5+)
- # de respuestas positivas (meta: 3+)

### Mediano plazo (6–12 meses)
- # de papers publicados con co-autoría paraguaya (meta: 1+)
- # de datasets paraguayos publicados (meta: 1+)
- # de modelos open-weight en español paraguayo (meta: 1+)
- # de partnerships activos firmados (meta: 1+)

### Largo plazo (12–24 meses)
- # de tesis de residentes CONAREM usando stack Paraguay (meta: 5+)
- # de pacientes chaqueños beneficiados por TB screening (meta: 100+)
- # de hit list Chagas validados experimentalmente (meta: 3+)
- # de centros médicos paraguayos usando IA clínica (meta: 2+)

---

## §10 — Lo que el repo provee

El repo `ai-medica-paraguay` ya contiene todo lo necesario para ejecutar:

| Documento | Qué provee |
|---|---|
| [README.md](../README.md) | Landing, visión, principios |
| [INDEX.md](../INDEX.md) | Navegación con tiempos de lectura |
| [docs/research-areas.md](../docs/research-areas.md) | 8 áreas de investigación, estrategia |
| [docs/research-findings.md](../docs/research-findings.md) | Hallazgos consolidados sobre Paraguay |
| [docs/research-session-log.md](../docs/research-session-log.md) | Cómo se construyó el repo |
| [docs/research-sources.md](../docs/research-sources.md) | Bibliografía verificada |
| [docs/ai-stack-reference.md](../docs/ai-stack-reference.md) | Catálogo del stack IA open source |
| [docs/google-deepmind-paraguay.md](../docs/google-deepmind-paraguay.md) | Análisis Google/HAI-DEF para Paraguay |
| [docs/playbook-acciones.md](../docs/playbook-acciones.md) | Playbook ejecutable por tier |
| [docs/mapa-actor-instituciones.md](../docs/mapa-actor-instituciones.md) | Personas e instituciones |
| [docs/marco-regulatorio.md](../docs/marco-regulatorio.md) | Ley 7593/2025 + marco regulatorio |
| [docs/plan-preparacion.md](../docs/plan-preparacion.md) | Plan de 6 fases antes de proyecto real |
| [areas/](../areas/) | 9 áreas con planes detallados |
| [research/100-ideas-poc.md](../research/100-ideas-poc.md) | 100 POC ideas rankeadas |
| [research/peer-landscape.md](../research/peer-landscape.md) | Lo que otros hacen |
| **ESTE DOC** | Las mejores cosas para hacer |

---

## §11 — Una sola pregunta para responder

**¿Qué es lo que Paraguay tiene que el mundo necesita?**

- Chagas: 165k infectados, transmisión congénita dominante, vector controlado en región oriental, **hiperendémico en Chaco indígena**
- TB: hiperendémico, infraestructura rural débil, **smartphone es la única opción viable**
- Guaraní: 90% rural, sin NLP médico, **gap global**
- Scorpion envenoming: endémico en Chaco, **4 muertes pediátricas/año, sin POC AI**
- Biobanco genómico: subrepresentado globalmente, **oportunidad de ser el primer dataset abierto FAIR-aligned de LatAm**
- Healthcare regulation: ventana abierta hasta Nov 2027, **oportunidad de ser primer framework de IA clínica en LatAm**

**La respuesta a esta pregunta es la tesis del repo entero.**

---

## Última actualización

Septiembre 2026.