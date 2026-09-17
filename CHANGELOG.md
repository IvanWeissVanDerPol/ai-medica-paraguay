# Changelog del repositorio

Historial de cambios significativos al repo `ai-medica-paraguay/`.

---

## 2026-09-16 — Sesión: top 10 explicado en profundidad

### Agregado

- **`research/top-10-explicado.md`** (~45 KB, 570 líneas) — explicación detallada de cada una de las 10 ideas top del master ranking. Para cada idea:
 - **Qué es exactamente** (definición técnica + stack)
 - **Por qué importa** (burden, gap, solución, first-mover)
 - **Evidencia que existe** (papers, validaciones previas, lo novel)
 - **Cómo se implementa paso a paso** (fases, outputs por fase)
 - **Qué necesitas** (GPU, storage, personas, partners, funding)
 - **Qué bloquea** (críticos + reales)
 - **Riesgos principales** (tabla con mitigaciones)
 - **Qué sale** (papers, modelos, programas, capacity)
 - **Por qué exactamente este score** (breakdown de las 7 dimensiones)
 - **Recomendación** (ejecutar ya, ejecutar este año, piloto primero, etc.)

### Top 10 (ordenados por score)

1. **TB cough screening HeAR** (92.5) — POC en 1 semana, $5-30k, 6 meses.
2. **Antiveneno sintético T. confluens** (89) — first-mover mundial, Baker Lab partnership, $400-1000k, 24-36 meses.
3. **Stack Chaco TB integrado** (88) — programa regional, $400-1000k, 12-18 meses.
4. **TxGemma+Boltz-2+OpenFold3+CEDIC** (86) — flagship drug discovery Paraguay, $200-500k, 12-24 meses.
5. **Chagas cardiomyopathy smart-monitoring** (84) — first-mover mundial smartwatch, $300k-1M, 24-36 meses.
6. **mRNA Leishmania vaccine design** (82) — first-mover mundial, $200-500k, 24-36 meses.
7. **tNGS directo desde esputo TB** (81) — MinION LCSP, $30-80k, 6-12 meses.
8. **CRISPR-Dx pipeline NTDs chaqueños** (80) — SHINE-TB + SHERLOCK, $50-100k, 6-12 meses.
9. **Nextclade + nf-core LCSP** (78) — quick win, $10-30k, 2-4 semanas.
10. **Biobanco FAIR + AlphaGenome** (76) — CEDIC × Galatea, $100-300k, 24-36 meses.

### Modificado

- **`INDEX.md`** — añadido `research/top-10-explicado.md` a navegación.

---

## 2026-09-16 — Sesión: master ranking de TODAS las ideas

### Agregado

- **`research/master-ranking.md`** (~30 KB) — consolidación definitiva de **130+ ideas** (100 POC + 10 first-mover + 9 áreas + Tier 1 + playbook) con scoring consistente en 7 dimensiones. Contiene:
 - **§1 Sistema de scoring**: 7 dimensiones (impacto salud PY 25%, viabilidad técnica 20%, costo 15%, tiempo a primer resultado 15%, riesgo 10%, first-mover 10%, replicabilidad 5%); escala 0-100; tier mapping S/A/B/C/D/E/F.
 - **§2 Top 30 ideas (score ≥70)** con análisis individual: score detallado, por qué alto, riesgos, dependencias, costo, timeline, recomendación.
 - **§3 Medias-altas (60-69)**: 30 ideas en 3 grupos (drug discovery, surveillance, clinical/imaging).
 - **§4 Medias (50-59)**: 30 ideas en 3 grupos (capacity, telemedicine, specialty).
 - **§5 Bajas (40-49)**: 30 ideas de replicación y capacidades futuras.
 - **§6 Más bajas (<40)**: 30 ideas archivadas.
 - **§7 Top-10 con análisis profundo** — 3 DEBE EJECUTARSE + 7 EJECUTAR ESTE AÑO.
 - **§8 Anti-recomendaciones** — 10 cosas que NO hacer y por qué.
 - **§9 Tesis final** — 5 ideas S-tier ejecutables en paralelo en 12 meses.

### Top 5 (S-tier, score ≥84)

1. **#1 TB cough screening HeAR** (92.5) — máximo impacto, mínimo costo, inmediato.
2. **#2 Antiveneno sintético T. confluens** (89) — first-mover mundial (Baker Lab partnership).
3. **#3 Stack Chaco integrado** (88) — programa regional unificado (TB + tNGS + CRISPR-Dx + D-Heart).
4. **#4 TxGemma+Boltz-2+OpenFold3+CEDIC pipeline Chagas** (86) — flagship drug discovery.
5. **#5 Chagas cardiomyopathy smart-monitoring** (84) — first-mover mundial (smartwatch + ECGFounder).

### Modificado

- **`INDEX.md`** — añadido `research/master-ranking.md` a navegación.

---

## 2026-09-16 — Sesión: avances médicos 2024-2026 + first-mover opportunities

### Agregado

- **`research/avances-medicina-posibilidades-paraguay.md`** (~29 KB) — análisis de las 7 fronteras médico-tecnológicas más transformadoras 2024-2026 con foco en Paraguay. Contiene:
 - **§1 7 fronteras médico-tecnológicas**: AlphaFold 3 + AlphaGenome + RFdiffusion3, Casgevy + base/prime editing, mRNA platforms, mHealth + wearables, MinION + tNGS, CRISPR-Dx (SHERLOCK/DETECTR), AI-designed therapeutics.
 - **§2 10 oportunidades first-mover para Paraguay**: antiveneno sintético T. confluens, Chagas smart-monitoring, CRISPR-Dx NTDs chaqueños, tNGS directo desde esputo, mRNA vaccine Leishmania, biobanco FAIR, organoid platform, binders para Bothrops, smartwatch pregnancy monitoring, digital twin nacional de salud.
 - **§3 Análisis por enfermedad**: Chagas, TB, leishmaniasis, dengue, chikungunya, escorpión envenoming, cáncer cervical/mama/próstata, diabetes/hipertensión, mental health.
 - **§4 Análisis por institución**: CEDIC, IICS, LCSP, Tesabio, BioProsNat, FIUNA, Hospital de Clínicas, Hospital Nacional de Itauguá, INCAN, CONAREM.
 - **§5 Cronograma realista 12 meses**.
 - **§6 Recomendaciones estratégicas finales**: 3 opciones de first-mover según prioridad (impacto salud pública vs. impacto científico vs. bajo riesgo).

### Hallazgos nuevos clave

- **AI-designed synthetic antivenoms** (Baker Lab, Nature 2024) — oportunidad first-mover para Paraguay en **T. confluens** (1,383 casos/año, 4 muertes infantiles) + **Bothrops chaqueña**. Partnership con Susana Vázquez Torres (lead author Baker Lab) + Tesabio + CEDIC.
- **tNGS directo desde esputo para TB** (ICMR-NIRT India, 2025) — 95% sensibilidad RIF sin BSL3. Replicable en LCSP.
- **SHINE-TB CRISPR-Dx** (Broad Institute, 2025) — 100% sensibilidad vs. culture, suitcase-sized POC. Aplicación directa al Chaco.
- **ECGFounder** (NEJM AI Nov 2025) — universal ECG foundation model. Combinable con smartwatches para Chagas monitoring.
- **AlphaGenome** (Nature 2026) — API para non-commercial research. Aplicación a biobanco CEDIC × Galatea.
- **Casgevy + prime editing** (Prime Medicine mayo 2025) — CRISPR curativo ya en clínica. No aplicable directamente a Paraguay, pero CRISPR-Dx sí.
- **GSK mRNA influenza** fase 3 (set 2024) + **mRNA-4157 melanoma** fase 3 — platform validada. Aplicación a Leishmania vaccine design con Tesabio.

### Modificado

- **`INDEX.md`** — añadido `research/avances-medicina-posibilidades-paraguay.md` a navegación.

---

## 2026-09-16 — Sesión: análisis profundo Tier 1

### Agregado

- **`research/analisis-tier1-profund.md`** (~30 KB) — análisis pre-ejecución detallado de los 10 proyectos Tier 1. Contiene:
 - **§1 Mapa de riesgos por proyecto** — 7 categorías de riesgo por proyecto, probabilidad, impacto, mitigación.
 - **§2 Mapa de dependencias** — qué bloquea qué; qué corre en paralelo.
 - **§3 Requisitos computacionales** — GPU/RAM/storage/costo compute exacto por proyecto.
 - **§4 Datasets específicos por proyecto** — URLs, tamaños, datasets locales necesarios.
 - **§5 Champion profiles** — perfil ideal de persona para cada proyecto, cómo identificarla.
 - **§6 Funding map** — $ → milestones; fuentes de financiamiento mapeadas.
 - **§7 Reproducibilidad** — universal checklist + por proyecto.
 - **§8 Timeline realista** — 12 meses con paralelización.
 - **§9 Decisión final** — uno, tres, seis, doce proyectos según recursos.
 - **§10 Tesis** — ventana de 12–18 meses que se cierra.

### Modificado

- **`INDEX.md`** — añadido `research/analisis-tier1-profund.md` a navegación.

---

## 2026-09-16 — Sesión final: MEJORES-COSAS-PARAGUAY.md

### Agregado

- **`MEJORES-COSAS-PARAGUAY.md`** (~20 KB, raíz del repo) — **la guía definitiva**. La síntesis final que responde "¿qué deberíamos hacer?". Contiene:
 - TL;DR de 30 segundos con 3 recomendaciones top
 - Top-10 cosas concretas ejecutables con costo/tiempo/actores
 - Plan de 4 semanas
 - Roadmap por nivel de inversión ($0 → $200k+)
 - Roadmap por enfermedad, capacidad, partnership
 - 5 cosas NO hacer
 - Métricas de éxito
 - Tesis final del repo

### Modificado

- **`INDEX.md`** — añadido `MEJORES-COSAS-PARAGUAY.md` a navegación.

---

## 2026-09-16 — Sesión de peer landscape

### Agregado

- **`research/peer-landscape.md`** (~31 KB) — investigación de lo que otros hacen relevante para Paraguay. Cubre:
 - Awesome lists del espacio (medical-AI, medical-RAG, AI4Med, pathology FMs).
 - **Hospital Italiano de Buenos Aires** (pIASHIBA) — el modelo regional más cercano, 27 años de trayectoria, productos activos (Argot NLP, Artemisia mamografía, TRx CXR, TANA chatbot).
 - Tabla de proyectos open-source por categoría con fit score para Paraguay (LLMs médicos, imaging, multi-agent, genomics, EHR, ECG, dermatology, ASR, TB-specific).
 - **5 gaps identificados** donde Paraguay puede ser first mover: datos locales, modelos en español paraguayo, framework regulatorio, envenenamiento escorpión, biobanco FAIR.
 - **7 partnerships recomendados** (HIBA, CABANA, SoIBio/AB3C, Google HAI-DEF, NVIDIA BioNeMo, Galatea Bio, Wellcome).
 - **Stack Paraguay completo** en 8 capas (genómica + drug, clinical NLP, imaging, audio, ECG, infra, EHR, genomics data equity).
 - **7 "firsts"** que Paraguay podría reclamar.

### Hallazgo clave

**Hospital Italiano de Buenos Aires (HIBA/Argentina)** es el modelo regional más relevante para Paraguay. Mismo idioma, mismo perfil de paciente, 27 años de trayectoria en informática en salud. Programa pIASHIBA (2020) con productos maduros (Argot NLP clínico desde 2019, Artemisia mamografía, TRx CXR, TANA chatbot clínico desde 2023). **Partnership técnico directo recomendado** — adopción de Argot, TANA, TRx como blueprints.

### Modificado

- **`INDEX.md`** — añadido `research/peer-landscape.md` a navegación.

---

## 2026-09-16 — Sesión de 100 ideas de POC

### Agregado

- **`research/100-ideas-poc.md`** (~29 KB) — **catálogo de 100 ideas concretas de POC/proyecto piloto para Paraguay**, con fit_score 1–10, herramientas de IA, actores paraguayos, esfuerzo estimado. Organizado por enfermedad (Chagas: 28 ideas, TB: 7, dengue: 9, leishmaniasis: 3, cáncer: 8, salud mental: 4, clínico general: 24) y por capacidad. Top-15 con score ≥9 priorizados. Top-3 no obvios: Whisper guaraní, leishmaniasis app, AlphaGenome pharmacogenética.

### Recomendación #1 del análisis

**Si tuvieras que arrancar UNA sola cosa hoy:** TB cough screening con HeAR (idea #1 del catálogo, fit_score 10). Paraguay hiperendémico, HeAR deployable hoy, ético, replicable.

### Modificado

- **`INDEX.md`** — añadido `research/100-ideas-poc.md` a navegación.

---

## 2026-09-16 — Sesión de playbook ejecutable

### Agregado

- **`docs/playbook-acciones.md`** (~24 KB) — **el documento ejecutable**. Un único archivo que consolida TODAS las acciones concretas que Paraguay podría tomar con el stack de IA, organizado en 3 tiers, con mapeo por institución, por enfermedad, y por capacidad. Incluye plan de 4 semanas y matriz de priorización esfuerzo × impacto.

### Modificado

- **`INDEX.md`** — añadido playbook a navegación + tabla de áreas.

### Recomendación clave

Si solo pudiera hacer una acción: **TB cough screening con HeAR** (§1.4 del playbook). Paraguay hiperendémico para TB, HeAR deployable HOY, éticamente alineado con CARE.

Si pudiera hacer tres: **TB HeAR + Nextclade en LCSP + MedGemma 4B**. Cubre vigilancia genómica + clinical NLP + screening rural.

---

## 2026-09-16 — Sesión de actualización Google/HAI-DEF

### Agregado

- **`docs/google-deepmind-paraguay.md`** (~15 KB) — análisis dedicado del portafolio Google DeepMind + HAI-DEF específicamente para Paraguay. Mapeo fit × institución, top-3 recomendaciones (MedGemma 4B, TxGemma 27B-Chat, HeAR), próximos pasos operativos.
- **`areas/health-acoustics-tb-screening/README.md`** — **Área 9 nueva**. HeAR (Google HAI-DEF) + clasificador lineal + smartphone para screening de TB en Chaco. Es el "sleeper hit" social — máximo impacto inmediato en Paraguay.
- **`docs/ai-stack-reference.md` §14-§16** — catálogo detallado de todos los Google/HAI-DEF tools con licencias verificadas, tabla maestra de licencias actualizada, top-5 recomendaciones actualizadas para Paraguay. Se añadieron: AlphaFold 3, AlphaFold Server, AlphaFold Database, AlphaGenome, AI Co-Scientist, Gemini 2.5 Pro/Flash, MedGemma, MedSigLIP, TxGemma, Path/CXR/Derm Foundation, HeAR, MedASR, PaliGemma 2, y **OpenFold3** (Apache 2.0, AF3-class con pesos comerciales).

### Modificado

- **`docs/research-areas.md`** — actualizada priorización. Ahora se recomiendan tres proyectos iniciales: Nextclade+nf-core, MedGemma 4B, y TB cough screening con HeAR.
- **`docs/research-findings.md`** §10 — actualizado "Próximo paso" con 4 candidatos (incluye HeAR); añadido §10.1 con stack tecnológico consolidado.
- **`areas/drug-discovery/README.md`** — reescrito. Ahora recomienda **TxGemma 27B-Chat** + Boltz-2 + OpenFold3 como pipeline end-to-end para Chagas. Subraya que AF3 weights no son comercialmente usables — usar OpenFold3 o Boltz-2 para Tesabio.
- **`areas/clinical-llms/README.md`** — actualizado. MedGemma 4B ahora es el default con licencia HAI-DEF verificada. Incluye nota regulatoria sobre HAI-DEF Prohibited Use.
- **`areas/antimicrobial-resistance/README.md`** — renombrado conceptualmente a "AMR + screening TB respiratorio". Añade Opción B: HeAR TB cough screening.
- **`areas/pathology-imaging/README.md`** — añadidos Path Foundation, CXR Foundation, Derm Foundation (HAI-DEF) como alternativas/complemento a CONCH/UNI/Virchow2.
- **`README.md`** — añadido área 9, actualizada la lista de tres recomendaciones principales (MedGemma + TxGemma + HeAR).
- **`INDEX.md`** — añadido el nuevo documento `google-deepmind-paraguay.md` y el área 9 a las tablas de navegación.

### Hallazgos clave nuevos (verificados)

1. **AlphaFold 3 weights son non-commercial** pero el **código es Apache 2.0**. Use the AlphaFold Server para academia; usa **OpenFold3** (Apache 2.0) para comercial.
2. **OpenFold3** (octubre 2025, AlQuraishi Lab + OpenFold Consortium) es la **única alternativa open a AF3** con pesos comercialmente usables y rendimiento comparable.
3. **HAI-DEF Prohibited Use** prohíbe explícitamente uso clínico regulado. Paraguay necesita su propio framework regulatorio.
4. **MedGemma 4B/27B** (HAI-DEF) es el LLM clínico open más capaz del mundo para el caso paraguayo.
5. **TxGemma 27B-Chat** (Gemma terms) es el sleeper hit para drug discovery: queries terapéuticas en español, ADMET, binding affinity. Combina perfectamente con Boltz-2.
6. **HeAR** (HAI-DEF, 300M+ audio clips) hace deployable el TB cough screening en smartphone hoy.
7. **MedASR** (HAI-DEF, 4.6% WER en radiology) es English-only — sirve como template para construir Spanish medical ASR.
8. **AI Co-Scientist** (Gemini 2.0 multi-agent) está validado en AML drug repurposing, liver fibrosis targets, AMR mechanism — caso natural para Paraguay es drug repurposing para Chagas. No público aún (Trusted Tester only).
9. **PaliGemma 2** es backup general VLM, no médico-tuned.
10. **Tres recomendaciones actualizadas** para Paraguay: MedGemma 4B, TxGemma 27B-Chat, HeAR (no más Boltz-2 como #1 — Boltz-2 es complementario, no el lead).

---

## 2026-09-16 — Sesión de consolidación

### Agregado

- **`docs/ai-stack-reference.md`** — Catálogo completo del stack IA open source (sección §1 a §13). Cubre AlphaFold 3, Boltz-2, ESM3, AlphaGenome, MedGemma, pathology FMs, BioNeMo, single-cell FMs, agentic frameworks, infrastructure layer. Tabla maestra de licencias, gaps honestos, top-3 recomendaciones.
- **`docs/research-findings.md`** — Hallazgos consolidados de investigación sobre Paraguay. Datos cuantitativos (165k Chagas, 1.7M en riesgo, 1.150 visitas/día Hospital de Clínicas, etc.), carga de enfermedad, capacidades locales, conectores internacionales, comparaciones regionales.
- **`docs/research-session-log.md`** — Log cronológico de las sesiones de conversación que construyeron el repo. Por qué existe cada decisión.
- **`docs/research-sources.md`** — Bibliografía verificada con URLs, fechas de verificación, y qué claim sustenta cada fuente.
- **`INDEX.md`** — Tabla de navegación rápida con tiempos estimados de lectura.
- **`CHANGELOG.md`** — Este archivo.

### Modificado

- **`README.md`** — Reorganizado para referenciar los nuevos docs. Tres recomendaciones principales ahora en el landing.
- **`docs/mapa-actor-instituciones.md`** — Tesabio ampliado con SAB completo + indicadores de credibilidad. PROCIENCIA II cap ahora explícito en USD.
- **`areas/drug-discovery/README.md`** — Reescrito para destacar **Boltz-2 como default** (no AF3) por licencia. Incluida nota sobre por qué AF3 no es comercialmente usable.
- **`areas/clinical-llms/README.md`** — Reescrito con **MedGemma 4B como default** + variante de menor costo con **OpenMedLM prompting + RAG** antes de hacer fine-tune.

### Decisiones de diseño tomadas

- **AI stack** y **research findings** son documentos separados porque el primero es perenne (herramientas), el segundo es específico del contexto paraguayo.
- **Session log** separado de findings porque es histórico (cómo llegamos aquí), no el estado actual.
- **Top-3 recomendaciones** puestas en el landing page directamente — el lector que llega debe saber cuál es la apuesta del repo en 30 segundos.

### Verificaciones de licencias hechas

- AlphaFold 3 v3.0.3: código Apache 2.0, **pesos non-commercial only** (corregido vs respuesta previa que sugería open weights).
- Boltz-2: MIT (modelo + pesos + training code + data). Comercial OK.
- MedGemma: wrapper Apache 2.0, pesos Health AI Dev Foundations License (research + comercial).
- ESM3 1.4B: Cambrian Non-Commercial License. 7B/98B API only.
- AlphaGenome: API no commercial only. Pesos no públicos.

---

## 2026-09-15 — Creación inicial del repo

### Agregado

- **`README.md`** — Landing page inicial.
- **`docs/research-areas.md`** — 8 áreas de investigación con descripción, herramientas, proyectos, vacíos.
- **`docs/mapa-actor-instituciones.md`** — Personas e instituciones.
- **`docs/marco-regulatorio.md`** — Marco regulatorio.
- **`docs/plan-preparacion.md`** — Plan de investigación previa.
- **`areas/{8 carpetas}/README.md`** — Descripción por área.

### Notas

- Versión inicial con 13 archivos, ~1,360 líneas.
- Enfoque en 8 áreas de investigación médica con justificación específica para Paraguay.
- Stack IA identificado pero no exhaustivo.

---

## Próxima entrada esperada

Cuando se complete cualquiera de:

- Lectura de la Política Nacional de Ética en Investigación en Salud (2024).
- Confirmación de contactos (Galeano, Vazquez, Granada, Hospital de Clínicas champion).
- Construcción del demo MedGemma 4B en español paraguayo.
- Confirmación del estado del biobanco CEDIC × Galatea Bio.
- Aplicación a una convocatoria externa.
- Primer paper del repo publicado.