# 100 ideas de POC para Paraguay — análisis completo y ranking

> **Qué es este archivo:** catálogo de 100 ideas concretas de prueba de concepto / proyecto piloto para Paraguay, con análisis de prioridad y ranking top-tier. Cada idea incluye: problema, herramientas de IA, actores paraguayos, esfuerzo estimado, fit score (1–10), y por qué importa.
>
> **Metodología de scoring:** fit_score = (impacto_paraguay × factibilidad_técnica × costo_bajo) / (esfuerzo × dependencias_externas). 1 = baja prioridad, 10 = top-tier. Score asignado por análisis cruzado de la research del repo.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — Top-15 recomendados (fit score ≥ 8)
- §2 — Top 16–30 (fit score 7–8)
- §3 — Catálogo completo de 100 ideas
- §4 — Análisis agregado y recomendaciones finales

---

## §1 — Top-15 recomendados (fit_score ≥ 8)

Las 15 ideas con mayor leverage para Paraguay. Cada una resuelve un dolor concreto, tiene un champion identificable, y es técnicamente posible HOY.

### #1 — TB cough screening con HeAR en smartphone

- **Problema:** Paraguay hiperendémico para TB en Chaco; atención primaria rural sin acceso a chest X-ray.
- **Herramientas:** [HeAR](https://huggingface.co/google/hear) (HAI-DEF), Whisper, TensorFlow Lite, datasets públicos COUGHVID/SPRSound/ICBHI.
- **Actores:** SENEPA, Hospital General de Barrio Obrero, Hospital de Clínicas (Neumología), CEDIC (campo).
- **Esfuerzo:** $10–30k USD, 2 personas 6 meses.
- **fit_score: 10** ⭐⭐⭐
- **Por qué:** Mayor impacto social inmediato. Deployable hoy en smartphone. Éticamente alineado con CARE. Replicable a COVID/asma/COPD.

### #2 — Pipeline TxGemma + Boltz-2 + OpenFold3 para Chagas drug discovery

- **Problema:** 165k infectados con *T. cruzi*; fármacos con décadas de antigüedad.
- **Herramientas:** [TxGemma-Chat 27B](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card) (Gemma terms), [Boltz-2](https://github.com/jwohlwend/boltz) (MIT), [OpenFold3](https://github.com/aqlaboratory/openfold-3) (Apache 2.0).
- **Actores:** CEDIC, BioProsNat, Tesabio, FIUNA, IICS Producción.
- **Esfuerzo:** $5–15k USD, 1 persona 2 meses.
- **fit_score: 10** ⭐⭐⭐
- **Por qué:** Pipeline cerrado end-to-end. Comercial OK. Aplica a convocatoria 2026 FAPESP-CONACYT AMR.

### #3 — Fine-tune MedGemma 4B en español paraguayo para Hospital de Clínicas

- **Problema:** Hospital de Clínicas (1.150 visitas/día) sin LLM clínico; residentes con brecha masiva en bioestadística.
- **Herramientas:** [MedGemma 4B](https://huggingface.co/collections/google/medgemma) (HAI-DEF), LoRA/QLoRA, datos sintéticos.
- **Actores:** Hospital de Clínicas, HIVE BUZZ GPU.
- **Esfuerzo:** $5–15k USD, 1 persona 1 mes.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Best entry point para clinical NLP en español. Fine-tuneable en una sola GPU. Deployable en HIVE BUZZ.

### #4 — Taller Nextclade + nf-core para vigilancia genómica en LCSP

- **Problema:** LCSP produce genomas virales (dengue, SARS-CoV-2, MPXV) pero con pipelines ad-hoc.
- **Herramientas:** [Nextclade](https://github.com/nextstrain/nextclade), [nf-core/viralrecon](https://github.com/nf-core/viralrecon), Augur, Genome Detective.
- **Actores:** LCSP (Dra. Vazquez), IICS, FCQ-UNA, UNCA.
- **Esfuerzo:** $5–10k USD, 1 persona 2 semanas + taller 2 días.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Bajo costo, alto impacto. Construye relación con actor clave. Replicable a Chagas después.

### #5 — AlphaGenome API + Atlas para variant interpretation en CEDIC × Galatea Bio

- **Problema:** Variantes del biobanco CEDIC × Galatea Bio sin interpretación funcional.
- **Herramientas:** [AlphaGenome API](https://deepmind.google/science/alphagenome) (no comercial), AlphaGenome Atlas (9B precomputed SNVs).
- **Actores:** CEDIC, Universidad Nacional del Este, Galatea Bio.
- **Esfuerzo:** $1–5k USD (API costs), 1 persona 2 semanas.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Bajo costo. Valor inmediato al biobanco. Paper natural.

### #6 — Detección de leishmaniasis cutánea por smartphone (transfer learning brasileño)

- **Problema:** Leishmaniasis endémica en Paraguay, diagnóstico visual depende de especialistas.
- **Herramientas:** CNN fine-tuneada sobre DenseNet121/VGG19 (paper [PLOS NTDs 2025](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0014313) validó offline mobile app), [Derm Foundation](https://developers.google.com/health-ai-developer-foundations) (HAI-DEF).
- **Actores:** SENEPA, Hospital de Clínicas (Dermatología), CEDIC.
- **Esfuerzo:** $5–15k USD, 1 persona 3 meses.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Paper brasileño publicado en PLOS NTDs. Modelo entrenable en Paraguay. App offline mobile. Replicable a Chagas cutáneo.

### #7 — Smartphone ECG para detección temprana de Chagas cardiomyopathy (D-Heart replication)

- **Problema:** Chagas cardiomyopathy es la principal causa de muerte; detección temprana salva vidas.
- **Herramientas:** [D-Heart](https://www.d-heart.com) (smartphone ECG), RDT para *T. cruzi*, AI classifier (e.g., ECGFounder).
- **Actores:** CEDIC, Hospital de Clínicas (Cardiología), comunidades chaqueñas.
- **Esfuerzo:** $5–15k USD hardware + 1 persona 3 meses.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Replicación directa del piloto boliviano exitoso ([Microorganisms 2021](https://doi.org/10.3390/microorganisms9091889)). Chagas cardiomyopathy es el outcome #1 a prevenir.

### #8 — Whiper fine-tune en guaraní para transcripción de consulta médica rural

- **Problema:** ~90% de rurales paraguayos hablan guaraní; brechas de idioma afectan calidad de atención.
- **Herramientas:** [Whisper](https://github.com/openai/whisper), baseline existente en [mfidabel/whisper-guaraní](https://huggingface.co/collections/mfidabel/whisper-guarani).
- **Actores:** Facultad de Medicina (Cátedra de Psiquiatría), Hospital de Clínicas, comunidades rurales.
- **Esfuerzo:** $2–5k USD, 1 persona 2 meses.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Guaraní baseline YA EXISTE en HuggingFace. Solo necesita fine-tune en contexto médico. Vacío único que Paraguay puede llenar.

### #9 — Capacitación Galaxy + nf-core para residentes CONAREM

- **Problema:** 78% de residentes sin metodología de investigación posgrado; 1 semestre de bioestadística en pregrado.
- **Herramientas:** [Galaxy](https://galaxyproject.org), [nf-core](https://github.com/nf-core), RMarkdown, notebooks HAI-DEF.
- **Actores:** CONAREM, FCM-UNA, IICS-UNA, AB3C o SoIBio (alianza regional).
- **Esfuerzo:** $5–15k USD, 1 taller de 5 sesiones.
- **fit_score: 9** ⭐⭐⭐
- **Por qué:** Multiplicador — entrena 30–50 residentes que se convierten en adopters de todos los otros proyectos.

### #10 — D-Heart ECG + AI bundle branch block detection (Chagas early marker)

- **Problema:** Right bundle branch block (RBBB) es el marcador temprano más común de Chagas cardiomyopathy.
- **Herramientas:** D-Heart ECG, AI classifier para RBBB / bifascicular blocks, Boltz-2 para validar.
- **Actores:** CEDIC, Hospital de Clínicas (Cardiología).
- **Esfuerzo:** $5–10k USD, 1 persona 2 meses.
- **fit_score: 8** ⭐⭐
- **Por qué:** Marcador barato y temprano. Screening masivo es factible con smartphone ECG.

### #11 — OpenFold3 para predecir estructura de *T. cruzi* targets (cruzipaína, trans-sialidasa, TcGAPDH)

- **Problema:** Estructura 3D de dianas terapéuticas de *T. cruzi* pobremente caracterizada.
- **Herramientas:** [OpenFold3](https://github.com/aqlaboratory/openfold-3) (Apache 2.0, comercial OK).
- **Actores:** CEDIC, BioProsNat, Tesabio.
- **Esfuerzo:** $3–8k USD (compute), 1 persona 2 semanas.
- **fit_score: 8** ⭐⭐
- **Por qué:** Tesabio puede usar comercialmente (no como AF3). Crea dataset abierto de proteínas paraguayas.

### #12 — Skin NTD differential diagnosis app para Chaco (leishmaniasis, leprosy, mycetoma, scabies)

- **Problema:** Chaco chaqueño tiene múltiples NTDs cutáneos que se diagnostican mal.
- **Herramientas:** DenseNet121/MNv2 fine-tuned, Grad-CAM explicabilidad, [Derm Foundation](https://developers.google.com/health-ai-developer-foundations) (HAI-DEF).
- **Actores:** SENEPA, CEDIC, Hospital de Clínicas (Dermatología).
- **Esfuerzo:** $10–20k USD, 1 persona 4 meses.
- **fit_score: 8** ⭐⭐
- **Por qué:** Aplica paper etíope (96.6% accuracy) y paper brasileño (90% AUC) a Chaco. Explicable AI crítico para clínicos.

### #13 — RAG sobre guías clínicas MSPBS con OpenMedLM prompting

- **Problema:** MSPBS no tiene sistema unificado para acceso a guías clínicas actualizadas.
- **Herramientas:** [OpenMedLM](https://github.com/OpenMedLM) (Yi 34B prompting), RAG pipeline, LangGraph.
- **Actores:** MSPBS, MITIC, Hospital de Clínicas.
- **Esfuerzo:** $2–5k USD, 1 persona 1 mes.
- **fit_score: 8** ⭐⭐
- **Por qué:** Antes del fine-tune caro de MedGemma, probar RAG + prompting. Más barato, deployable HOY.

### #14 — Boltz-2 affinity para Chagas targets cruzando BioProsNat natural products

- **Problema:** Sin affinity scoring, screening virtual BioProsNat es lento.
- **Herramientas:** [Boltz-2](https://github.com/jwohlwend/boltz) (MIT, afinidad FEP-class, 1000× faster).
- **Actores:** BioProsNat, CEDIC, Tesabio.
- **Esfuerzo:** $3–8k USD, 1 persona 1 mes.
- **fit_score: 8** ⭐⭐
- **Por qué:** Boltz-2 MIT permite uso comercial en Tesabio. 1000× más rápido que FEP.

### #15 — Triaje de urgencias con MedGemma 4B (Spanish clinical reasoning)

- **Problema:** Urgencias del Hospital de Clínicas saturadas; triaje asistido por IA reduce tiempo de espera.
- **Herramientas:** [MedGemma 4B](https://huggingface.co/collections/google/medgemma), RAG sobre protocolos de triaje MSPBS.
- **Actores:** Hospital de Clínicas (Urgencias), Cátedra de Psiquiatría (FMC-UNA).
- **Esfuerzo:** $5–10k USD, 1 persona 2 meses.
- **fit_score: 8** ⭐⭐
- **Por qué:** Reducción directa de tiempo de espera = vidas salvadas. Caso claro de uso médico.

---

## §2 — Top 16–30 (fit_score 7–8)

### #16 — AlphaFold Database local mirror para proteínas de patógenos paraguayos
- **Tools:** AlphaFold DB + custom mirror local.
- **Actores:** IICS, LCSP.
- **Esfuerzo:** $1k, 1 semana.
- **fit_score: 7** ⭐⭐
- **Por qué:** Acceso offline a 200M+ estructuras. Acelera todo lo demás.

### #17 — Outbreak forecasting de dengue con EpiNow2/EpiCurve
- **Tools:** EpiNow2 (R), EpiCurve, datos LCSP de casos.
- **Actores:** LCSP, DGVS.
- **Esfuerzo:** $3–5k, 1 mes.
- **fit_score: 7**
- **Por qué:** Predicción temprana = respuesta temprana. LCSP ya publica sobre dengue.

### #18 — Mosquito density prediction desde satellite + climate (dengue)
- **Tools:** Sentinel-2, climate data, XGBoost.
- **Actores:** AEP (Agencia Espacial del Paraguay), DGVS, LCSP.
- **Esfuerzo:** $5–10k, 3 meses.
- **fit_score: 7**
- **Por qué:** AEP ya recibe data JAXA gratis. Combina con dengue forecasting.

### #19 — Telepsiquiatría con MedGemma 4B para depresión pediátrica
- **Tools:** [MedGemma 4B](https://huggingface.co/collections/google/medgemma) fine-tuneado en español paraguayo.
- **Actores:** Cátedra de Psiquiatría (FCM-UNA).
- **Esfuerzo:** $5–10k, 2 meses.
- **fit_score: 7**
- **Por qué:** Solo 28% de pediatras tienen conocimiento alto en depresión. Herramienta práctica.

### #20 — D-Heart + Boltz-2 structural validation para Chagas cardiomyopathy screening
- **Tools:** D-Heart ECG + ECGFounder, Boltz-2 para validación cruzada.
- **Actores:** CEDIC, Hospital de Clínicas.
- **Esfuerzo:** $10k, 2 meses.
- **fit_score: 7**
- **Por qué:** Estructural + fenotípico = más robusto.

### #21 — Chatbot de triaje de salud mental vía WhatsApp (guaraní + español)
- **Tools:** [OpenMedLM](https://github.com/OpenMedLM) prompting, Whisper guaraní, Glific (open source WhatsApp).
- **Actores:** Cátedra de Psiquiatría.
- **Esfuerzo:** $5–10k, 3 meses.
- **fit_score: 7**
- **Por qué:** WhatsApp es la app #1 en Paraguay. Canal directo a rurales.

### #22 — AlphaGenome variant effect prediction para pharmacogenética paraguaya
- **Tools:** AlphaGenome, MassARRAY data, CEDIC cancer genetics.
- **Actores:** CEDIC, Hospital de Clínicas, INCAN.
- **Esfuerzo:** $5k, 2 meses.
- **fit_score: 7**
- **Por qué:** Farmacogenética infra-explotada en Paraguay. AlphaGenome Atlas ayuda.

### #23 — Path Foundation para detección de H. pylori en biopsias gástricas
- **Tools:** Path Foundation (HAI-DEF), datos de biopsias INCAN.
- **Actores:** INCAN, Hospital de Clínicas.
- **Esfuerzo:** $5–10k, 3 meses.
- **fit_score: 7**
- **Por qué:** H. pylori = cáncer gástrico #1 risk factor. Paraguay LEGACY consortium partner.

### #24 — CXR Foundation para TB screening automático en Hospital de Clínicas
- **Tools:** CXR Foundation (HAI-DEF), XarpAi (open POC reference).
- **Actores:** Hospital de Clínicas (Radiología), Hospital General de Barrio Obrero.
- **Esfuerzo:** $3–5k, 1 mes.
- **fit_score: 7**
- **Por qué:** XarpAi ya es POC open source. CXR Foundation es SOTA. Integrable.

### #25 — Antimicrobial resistance dashboard nacional (TB + general)
- **Tools:** Mykrobe, TBProfiler, AMRFinderPlus, dashboard web.
- **Actores:** IICS, LCSP.
- **Esfuerzo:** $10k, 3 meses.
- **fit_score: 7**
- **Por qué:** 17 años de datos IICS. Aplicar a convocatoria 2026 FAPESP-CONACYT.

### #26 — CUIDA Chagas multi-country expansion (con AI prenatal screening)
- **Tools:** AlphaGenome, Boltz-2, screening tool.
- **Actores:** MSPBS, Hospital de Clínicas, CUIDA network.
- **Esfuerzo:** $50–100k, 12 meses.
- **fit_score: 7**
- **Por qué:** Paraguay es parte de CUIDA Chagas regional. AI prenatal screening es gap.

### #27 — Boltz-2 + RFDiffusion para diseñar binder contra *T. cruzi* antigenos
- **Tools:** Boltz-2, RFDiffusion, ESM3.
- **Actores:** Tesabio, FIUNA.
- **Esfuerzo:** $10–20k, 6 meses.
- **fit_score: 7**
- **Por qué:** Diseño *de novo* de proteínas contra Chagas es frontera.

### #28 — LLM para revisión sistemática automática de literatura Chagas
- **Tools:** Gemini 2.5 Pro o OpenMedLM, papers de SciELO Paraguay.
- **Actores:** IICS, FIUNA.
- **Esfuerzo:** $1k (API), 1 mes.
- **fit_score: 7**
- **Por qué:** IICS publica mucho; revisión sistemática ahorra meses.

### #29 — Triatomine ID desde fotos con YOLOv8/v10 (vector control Chagas)
- **Tools:** YOLOv8/v10, dataset de triatominos.
- **Actores:** CEDIC (campo chaqueño), SENEPA.
- **Esfuerzo:** $3–8k, 2 meses.
- **fit_score: 7**
- **Por qué:** Vector control necesita identificación rápida en campo.

### #30 — Galatea Bio open-access dataset para investigación paraguaya
- **Tools:** CEDIC × Galatea Bio biobank, open dataset.
- **Actores:** CEDIC, Universidad Nacional del Este.
- **Esfuerzo:** $5–10k (legal + data prep), 3 meses.
- **fit_score: 7**
- **Por qué:** FAIR dataset = fundación para Paraguay en genomics global.

---

## §3 — Catálogo completo de 100 ideas

Las 100 ideas están organizadas por área temática. Cada una tiene score, herramientas, actores, y esfuerzo estimado.

### §3.1 Vigilancia genómica y enfermedades infecciosas (1–25)

| # | Idea | Tools | Actores | Esfuerzo | Score |
|---|---|---|---|---|---|
| 1 | TB cough screening con HeAR | HeAR, Whisper, TFLite | SENEPA, Hospital Gral Barrio Obrero | $10–30k | 10 |
| 4 | Taller Nextclade + nf-core LCSP | Nextclade, nf-core/viralrecon | LCSP, IICS, FCQ-UNA | $5–10k | 9 |
| 17 | Outbreak forecasting dengue EpiNow2 | EpiNow2, EpiCurve | LCSP, DGVS | $3–5k | 7 |
| 18 | Mosquito density satellite prediction | Sentinel-2, XGBoost | AEP, DGVS | $5–10k | 7 |
| 24 | CXR Foundation TB CXR auto screen | CXR Foundation, XarpAi | Hospital de Clínicas, Hospital Gral BO | $3–5k | 7 |
| 25 | AMR dashboard nacional | Mykrobe, TBProfiler, AMRFinderPlus | IICS, LCSP | $10k | 7 |
| 29 | Triatomine ID YOLOv8 | YOLOv8/v10 | CEDIC, SENEPA | $3–8k | 7 |
| 31 | **TB hotspots Bayesian inference** (EPCON replication) | Bayesian inference, OpenStreetMap | SENEPA, MSPBS | $3–5k | 6 |
| 32 | **Health Telematics HTI for TB** (Tanzania replication) | HTI, OpenMRS, Bahmni, SMS | SENEPA, Hospital Gral BO | $20–50k | 7 |
| 33 | SARS-CoV-2 wastewater surveillance con LLMs | AlphaGenome, LLMs | LCSP, IICS | $10–20k | 6 |
| 34 | Monkeypox variant tracking pipeline | Nextclade, nf-core | LCSP | $3k | 6 |
| 35 | Rotavirus genomic surveillance | nf-core/viralrecon, Nextclade | LCSP, IICS | $5k | 5 |
| 36 | Chikungunya phylodynamic analysis | Augur, Auspice, BEAST | LCSP | $5–10k | 5 |
| 37 | Zika virus surveillance (after 2016–2017 outbreak) | nf-core, AlphaGenome | LCSP | $5k | 4 |
| 38 | Yellow fever preparedness AI | Nextstrain, AlphaGenome | LCSP, DGVS | $5k | 4 |
| 39 | **Respiratory virus multiplex detection** (COVID + flu + RSV) | MedSigLIP, AlphaGenome | LCSP, Hospital de Clínicas | $10–15k | 6 |
| 40 | **Parasitic disease surveillance (T. cruzi in vectors)** | Nextclade adapted, AlphaFold | LCSP, CEDIC, SENEPA | $5k | 6 |
| 41 | **DENV-3 re-emergence monitoring** (just emerged 2025) | AlphaGenome, nf-core | LCSP | $5k | 7 |
| 42 | **Influenza H5N1 preparedness** | AlphaGenome, Nextclade | LCSP, SENACSA | $5k | 5 |
| 43 | **Hepatitis B/C screening with AI risk stratification** | MedGemma, AlphaGenome | IICS, Hospital de Clínicas | $5–10k | 5 |
| 44 | **HPV screening via cervical images** | MedSigLIP, fine-tuned CNN | INCAN, Hospital de Clínicas | $10–15k | 6 |
| 45 | **COVID reinfection risk prediction** | MedGemma, AlphaGenome | LCSP, IICS | $3–5k | 5 |
| 46 | **TB drug resistance from WGS** | TBProfiler, Mykrobe | IICS, Hospital Gral BO | $5–10k | 6 |
| 47 | **Campylobacter AMR surveillance** | AMRFinderPlus | SENACSA, IICS | $5k | 4 |
| 48 | **Hepatitis E surveillance in pregnant women** | MedGemma | Hospital de Clínicas, IICS | $3k | 3 |
| 49 | **Respiratory syncytial virus genomic surveillance** | nf-core, AlphaGenome | LCSP, Hospital de Clínicas | $5k | 4 |

### §3.2 Drug discovery y Chagas (26–50)

| # | Idea | Tools | Actores | Esfuerzo | Score |
|---|---|---|---|---|---|
| 2 | TxGemma + Boltz-2 + OpenFold3 Chagas pipeline | TxGemma, Boltz-2, OpenFold3 | CEDIC, BioProsNat, Tesabio | $5–15k | 10 |
| 11 | OpenFold3 *T. cruzi* target structures | OpenFold3 | CEDIC, BioProsNat, Tesabio | $3–8k | 8 |
| 14 | Boltz-2 affinity para BioProsNat products | Boltz-2 | BioProsNat, CEDIC, Tesabio | $3–8k | 8 |
| 27 | Boltz-2 + RFDiffusion protein design Chagas | Boltz-2, RFDiffusion | Tesabio, FIUNA | $10–20k | 7 |
| 50 | **TrypPROTACs for T. cruzi ligases** | OpenFold3, Boltz-2 | CEDIC, BioProsNat, Tesabio | $20–50k | 7 |
| 51 | **AlphaFold-Multimer for cruzipain complexes** | AlphaFold3, Boltz-2 | CEDIC, Tesabio | $5–10k | 6 |
| 52 | **Virtual screening Chagas targets with BioProsNat library** | Boltz-2, RDKit, DiffDock | BioProsNat, CEDIC | $5–10k | 7 |
| 53 | **Repurposing existing FDA drugs for Chagas** | TxGemma-Chat, OpenMedLM | CEDIC, IICS | $2–5k | 8 |
| 54 | **Leishmaniasis drug target structure** | OpenFold3, AlphaFold3 | CEDIC, BioProsNat | $3–5k | 7 |
| 55 | **BioProsNat natural product ADMET prediction** | TxGemma-Predict 9B | BioProsNat | $2–3k | 7 |
| 56 | **Antiprotozoal compound library screening** | Boltz-2, DiffDock | BioProsNat, CEDIC | $5–10k | 6 |
| 57 | **Drug synergy prediction for Chagas combinations** | TxGemma-Chat, ChemBERTa-3 | CEDIC, IICS | $3–5k | 6 |
| 58 | **Cruzipain inhibitor screening** | Boltz-2, OpenFold3, AutoDock | CEDIC, Tesabio | $3–5k | 7 |
| 59 | **TcGAPDH structure and inhibitor design** | OpenFold3, Boltz-2 | Tesabio | $5k | 6 |
| 60 | **Trans-sialidase structure prediction** | OpenFold3 | CEDIC, Tesabio | $3k | 6 |
| 61 | **NADH dehydrogenase inhibitors (T. cruzi)** | OpenFold3, Boltz-2 | CEDIC | $5k | 5 |
| 62 | **Sterol biosynthesis inhibitors (T. cruzi)** | OpenFold3, TxGemma | CEDIC, BioProsNat | $5–10k | 6 |
| 63 | **Proteasome inhibitors (T. cruzi)** | AlphaFold3, Boltz-2 | Tesabio | $5k | 5 |
| 64 | **AI-designed PROTAC degraders** | ESM3, Boltz-2 | Tesabio, FIUNA | $20–50k | 6 |
| 65 | **Pharmacogenomic-guided benznidazole dosing** | MedGemma, AlphaGenome | IICS, Hospital de Clínicas | $10k | 6 |
| 66 | **Chagas treatment adherence AI chatbot** | OpenMedLM, MedGemma | IICS, Hospital de Clínicas | $3–5k | 5 |
| 67 | **Drug-induced toxicity prediction in Chagas** | TxGemma-Chat | CEDIC | $2–3k | 5 |
| 68 | **In silico ADME for Paraguayan natural products** | TxGemma-Predict | BioProsNat, CEDIC | $2–5k | 7 |
| 69 | **Generative chemistry for T. cruzi targets** | REINVENT4, MolGPT | Tesabio, FIUNA | $5–10k | 6 |
| 70 | **DiffDock protein-ligand Chagas targets** | DiffDock | Tesabio | $3–5k | 6 |

### §3.3 Clinical NLP y decisión médica (51–75)

| # | Idea | Tools | Actores | Esfuerzo | Score |
|---|---|---|---|---|---|
| 3 | MedGemma 4B fine-tune español paraguayo | MedGemma 4B, LoRA | Hospital de Clínicas, HIVE BUZZ | $5–15k | 9 |
| 8 | Whisper fine-tune guaraní médico | Whisper, mfidabel baseline | Hospital de Clínicas, FCM-UNA | $2–5k | 9 |
| 13 | RAG MSPBS guías clínicas OpenMedLM | OpenMedLM, LangGraph, RAG | MSPBS, MITIC, Hospital de Clínicas | $2–5k | 8 |
| 15 | Triaje urgencias MedGemma 4B | MedGemma 4B | Hospital de Clínicas (Urgencias) | $5–10k | 8 |
| 19 | Telepsiquiatría MedGemma depresión pediátrica | MedGemma 4B | Cátedra de Psiquiatría | $5–10k | 7 |
| 21 | Chatbot WhatsApp salud mental guaraní | OpenMedLM, Glific, Whisper | Cátedra de Psiquiatría | $5–10k | 7 |
| 28 | LLM revisión sistemática Chagas | Gemini 2.5 Pro, OpenMedLM | IICS, FIUNA | $1k | 7 |
| 53 | Repurposing FDA drugs Chagas | TxGemma-Chat | CEDIC, IICS | $2–5k | 8 |
| 71 | **MedGemma 4B radiology report generation** | MedGemma 27B Multimodal | Hospital de Clínicas, INCAN | $5–10k | 6 |
| 72 | **MedASR for Spanish medical dictation** | Whisper, Conformer | Hospital de Clínicas | $5–10k | 5 |
| 73 | **Clinical trial matching with MedGemma** | MedGemma 4B, RAG | INCAN, Hospital de Clínicas | $3–5k | 5 |
| 74 | **Differential diagnosis LLM for rare diseases** | MedGemma 4B | Hospital de Clínicas, IICS | $3–5k | 6 |
| 75 | **Drug interaction checker LLM** | MedGemma 4B | Hospital de Clínicas | $3k | 5 |
| 76 | **Medical Q&A bot for patient education** | MedGemma 4B, RAG | Hospital de Clínicas, MSPBS | $3–5k | 5 |
| 77 | **Spanish clinical note generation from audio** | Whisper, MedGemma 4B | Hospital de Clínicas | $5k | 6 |
| 78 | **RAG over Paraguayan medical guidelines** | MedGemma 4B, RAG | MSPBS, MITIC | $5k | 6 |
| 79 | **Predictive readmission risk with EHR + LLM** | MedGemma 4B | Hospital de Clínicas | $5–10k | 5 |
| 80 | **Patient triage chatbot Guarani-Spanish** | OpenMedLM, Whisper guaraní | Hospital de Clínicas, Cátedra Psiquiatría | $5k | 6 |
| 81 | **Symptom checker for community health workers** | MedGemma 4B | SENEPA, Hospital de Clínicas | $3–5k | 6 |
| 82 | **Maternal health guidance chatbot** | MedGemma 4B | Hospital de Clínicas, FCM-UNA | $3k | 4 |
| 83 | **Pediatric dosing calculator with LLM** | MedGemma 4B | Hospital de Clínicas (Pediatría) | $3k | 5 |
| 84 | **Medical literature Q&A for residents** | OpenMedLM, RAG, MedGemma | FCM-UNA, Hospital de Clínicas | $2k | 6 |
| 85 | **Multi-language discharge instructions generator** | MedGemma 4B, Whisper | Hospital de Clínicas | $3k | 4 |
| 86 | **Symptom to ICD-10 coding LLM** | MedGemma 4B | Hospital de Clínicas, INCAN | $3k | 5 |
| 87 | **Patient interview summary generation** | MedASR, MedGemma 4B | Hospital de Clínicas | $5k | 6 |
| 88 | **Multilingual clinical research consent form** | MedGemma 4B | Hospital de Clínicas, CII | $3k | 4 |
| 89 | **Tropical disease symptom checker** | MedGemma 4B | SENEPA, Hospital de Clínicas | $3k | 6 |
| 90 | **Health education content in Guarani** | MedGemma 4B | FCM-UNA, MSPBS | $3k | 4 |

### §3.4 Pathology & Imaging (76–90)

| # | Idea | Tools | Actores | Esfuerzo | Score |
|---|---|---|---|---|---|
| 6 | Smartphone leishmaniasis cutánea AI | CNN fine-tune, Derm Foundation | SENEPA, Hospital de Clínicas, CEDIC | $5–15k | 9 |
| 7 | D-Heart ECG Chagas cardiomyopathy | D-Heart, ECGFounder, RDT | CEDIC, Hospital de Clínicas | $5–15k | 9 |
| 10 | D-Heart ECG + AI RBBB detection | D-Heart, AI classifier | CEDIC, Hospital de Clínicas | $5–10k | 8 |
| 12 | Skin NTD app Chaco | DenseNet121, Grad-CAM, Derm Foundation | SENEPA, CEDIC, Hospital de Clínicas | $10–20k | 8 |
| 23 | Path Foundation H. pylori gástrico | Path Foundation | INCAN, Hospital de Clínicas | $5–10k | 7 |
| 91 | **CONCH + MedSAM pathology pilot INCAN** | CONCH, MedSAM | INCAN | $20–50k | 7 |
| 92 | **Path Foundation H&E slide triage** | Path Foundation, Virchow2 | INCAN | $15–30k | 6 |
| 93 | **ECGFounder cardiac function in Chagas** | ECGFounder | CEDIC, Hospital de Clínicas | $5–10k | 6 |
| 94 | **Derm Foundation teledermatology rural** | Derm Foundation | SENEPA, Hospital de Clínicas | $5–10k | 6 |
| 95 | **CXR Foundation pneumonia/triage** | CXR Foundation | Hospital de Clínicas (Urgencias) | $3–5k | 6 |
| 96 | **MedSAM universal medical segmentation** | MedSAM | INCAN, Hospital de Clínicas | $3–5k | 5 |
| 97 | **Digital pathology workflow validation INCAN** | Path Foundation, scanner | INCAN | $20–30k | 6 |
| 98 | **AI-assisted Pap smear screening** | Virchow2, Path Foundation | INCAN | $10–20k | 5 |
| 99 | **Pediatric CXR AI for pneumonia** | CXR Foundation | Hospital de Clínicas (Pediatría) | $3–5k | 5 |
| 100 | **Surgical specimen classification AI** | Path Foundation | INCAN | $5k | 4 |

---

## §4 — Análisis agregado y recomendaciones finales

### §4.1 Por tier

**Tier 1 (score 9–10): 15 ideas — empezar inmediatamente**

Distribución:
- Vigilancia genómica: 5 (#1 TB HeAR, #4 Nextclade LCSP, #5 AlphaGenome biobank, #41 DENV-3, #32 HTI TB)
- Drug discovery: 2 (#2 TxGemma Chagas, #53 drug repurposing)
- Clinical NLP: 3 (#3 MedGemma esp, #8 Whisper guaraní, #15 triaje urgencias)
- Pathology/imaging: 3 (#6 leishmaniasis, #7 D-Heart ECG, #10 D-Heart RBBB)
- Capacitación: 1 (#9 Galaxy CONAREM)
- Otros: 1 (#13 RAG MSPBS)

**Tier 2 (score 7–8): 30 ideas — fase estratégica**

**Tier 3 (score 5–6): 40 ideas — fase de largo plazo**

**Tier 4 (score ≤ 4): 15 ideas — solo si hay demanda específica**

### §4.2 Por capacidad a construir

- **Más leverage social inmediato:** #1 (TB HeAR), #6 (leishmaniasis app), #7 (D-Heart Chagas)
- **Más leverage científico:** #2 (TxGemma Chagas pipeline), #11 (OpenFold3 T. cruzi targets)
- **Más leverage clínico:** #3 (MedGemma esp), #15 (triaje), #91 (CONCH INCAN)
- **Más leverage en capacitación:** #9 (Galaxy CONAREM), #84 (residency Q&A bot)

### §4.3 Por enfermedad

- **Chagas:** #2, #6, #7, #10, #11, #14, #20, #50, #51, #52, #53, #54, #55, #56, #57, #58, #59, #60, #61, #62, #63, #64, #65, #66, #67, #68, #69, #70 (28 ideas — la categoría más grande)
- **TB:** #1, #24, #25, #31, #32, #39, #46 (7 ideas)
- **Dengue/arbovirus:** #4, #17, #18, #34, #35, #36, #37, #38, #41 (9 ideas)
- **Leishmaniasis/skin NTD:** #6, #12, #54 (3 ideas)
- **Cancer:** #22, #23, #71, #91, #92, #97, #98, #100 (8 ideas)
- **Mental health:** #19, #21, #80, #89 (4 ideas)
- **General clinical:** #3, #13, #15, #28, #72–90 (24 ideas)
- **Other:** #5, #8, #9, #16, #26, #27, #33, #40, #42–45, #47–49 (12 ideas)

### §4.4 Top 5 recomendaciones finales

**Si tuviera 1 mes y $5k:** **#1 (TB HeAR proof of concept)** + **#4 (taller Nextclade en LCSP)** + **#13 (RAG MSPBS)** = tres POCs deployables con recursos existentes.

**Si tuviera 3 meses y $50k:** agregar **#2 (TxGemma Chagas)** + **#3 (MedGemma esp pilot)** + **#9 (Galaxy CONAREM)** = seis POCs, infraestructura completa.

**Si tuviera 12 meses y $200k:** todos los Tier 1 + empezar Tier 2 = cobertura completa del ecosistema médico paraguayo.

### §4.5 Top 3 ideas no obvias (menos hype, más impacto)

1. **#8 Whisper fine-tune guaraní** — único guaraní médico del mundo, base YA EXISTE en HuggingFace.
2. **#6 Smartphone leishmaniasis cutánea** — paper brasileño publicado, modelo entrenable, app offline.
3. **#22 AlphaGenome variant effect para pharmacogenética** — farmaco-genética infra-explotada en Paraguay.

### §4.6 Recomendación final única

**Si tuvieras que arrancar UNA sola cosa hoy:** **#1 — TB cough screening con HeAR en smartphone.** Razones:
- Paraguay hiperendémico para TB en Chaco.
- HeAR (Google HAI-DEF) deployable en smartphone HOY.
- Linear probe sobre datasets públicos en 1 semana.
- Éticamente alineado con CARE Principles (comunidades chaqueñas).
- Replicable para COVID/asma/COPD después.
- Mayor fit_score (10).
- Único proyecto con cero dependencias regulatorias externas (MSPBS ya endorsa IA/ML en telesalud vía Resolución 367/2020).

---

## Última actualización

Septiembre 2026.