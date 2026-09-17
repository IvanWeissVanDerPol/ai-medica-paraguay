# Análisis profundo de los Tier 1 POC — riesgos, dependencias, recursos, reproducibilidad

> **Qué es este archivo:** el análisis que viene ANTES de hacer trabajo. Mapea riesgos, dependencias, recursos computacionales, datasets específicos, y criterios de éxito para los 10 proyectos Tier 1. Sin outreach, sin código, sin contactos externos. Solo investigación y planificación profunda.
>
> **Audiencia:** quien ejecuta. Para cada proyecto, este doc te dice: qué puede fallar, qué necesitas, cuánto cuesta realmente (compute + tiempo + dinero), y cómo sabes que funciona.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — Mapa de riesgos por proyecto
- §2 — Dependencias y bloqueos
- §3 — Requisitos computacionales detallados (GPU, RAM, storage)
- §4 — Datasets específicos (públicos) por proyecto
- §5 — Champion profiles (qué buscar en cada institución)
- §6 — Funding map: $ → milestones
- §7 — Reproducibilidad: checklist por proyecto
- §8 — Timeline realista con paralelización
- §9 — Decisión final: qué construir primero

---

## §1 — Mapa de riesgos por proyecto Tier 1

Cada proyecto tiene riesgos específicos. Los categorizo en: **técnicos** (algo no funciona), **datos** (no hay datos paraguayos o son malos), **personas** (no hay champion), **regulatorios** (Ley 7593 bloquea), **éticos** (CARE Principles), **financieros** (se acaba el dinero), **técnicos-dependientes** (otra cosa no funciona primero).

### #1 — TB cough screening HeAR

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| HeAR no funciona bien para TB (solo validado para COVID/asma en papers) | Media | Alto | Linear probe primero sobre datasets públicos antes de comprometer |
| No hay toses TB paraguayas etiquetadas | Alta | Alto | Empezar con COUGHVID + SPRSound; datos locales solo en fase 2 |
| Conectividad Chaco es pobre | Alta | Medio | App offline-first (modelo on-device via TFLite) |
| Resistencia del MSPBS/SENEPA | Baja | Alto | Resolución 367/2020 ya endosa; pre-acuerdo antes de field pilot |
| Dispositivos smartphones no son uniformes en Chaco | Media | Medio | Validar con subset antes; documentar device heterogeneity |
| CARE compliance con pueblos indígenas | Media | Alto | Consentimiento colectivo; consulta previa; governance de datos |
| Champion MSPBS/SENEPA cambia de puesto | Media | Medio | Identificar 2+ champions; documentar procesos |

**Riesgo neto: MEDIO.** Mitigable con POC previo (linear probe en datasets públicos) que cuesta ~$0.

### #2 — TxGemma + Boltz-2 + OpenFold3 Chagas pipeline

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Dianas *T. cruzi* validadas son pocas/bajas calidad | Media | Alto | CEDIC confirma primero las 3-5 dianas prioritarias |
| Boltz-2 afinidad no es tan buena como paper sugiere | Baja | Alto | Validar contra datos experimentales existentes en CEDIC antes de paper |
| TxGemma alucina en queries ADMET (Spanish) | Media | Medio | Cross-validar con ChemBERTa-3; usar consensus entre modelos |
| Tesabio no comparte acceso a su microARN expertise | Baja | Medio | Empezar con colaboración BioProsNat + CEDIC (no requiere Tesabio) |
| BioProsNat no tiene suficientes compuestos caracterizados | Media | Medio | Empezar con compounds públicos (PubChem, CO-ADD) si necesario |
| GPU insuficiente para OpenFold3 + Boltz-2 | Baja | Bajo | HIVE BUZZ + X8 Cloud; AlphaFold Server para tests iniciales |
| Sin paper-ready targets en TrypanoDB | Baja | Bajo | AlphaFold Database + OpenFold3 generan nuevos |

**Riesgo neto: BAJO.** El stack está bien validado. Lo único no validado es la combinación con BioProsNat específicamente.

### #3 — HIBA Argentina partnership

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| HIBA no responde a outreach | Media | Medio | Bajar de jerarquía "oficial" a "técnico"; contactos personales |
| Tiempo de aprobación institucional largo | Alta | Medio | Empezar con visita exploratoria corta (1 semana) |
| Costos de adopción de Argot más altos de lo esperado | Baja | Medio | Empezar con POC de evaluación, no adopción full |
| Diferencias regulatorias Paraguay-Argentina | Baja | Bajo | Paraguay no tiene regulación de IA clínica — es ventaja |
| Idioma distinto (español argentino vs paraguayo) | Baja | Bajo | Argot ya soporta español; ajustamos a paraguayo después |

**Riesgo neto: BAJO.** Partnership técnico, no regulatorio.

### #4 — Nextclade + nf-core en LCSP

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| LCSP ya tiene pipeline ad-hoc que funciona | Media | Bajo | Empezar con reunión para entender estado actual antes de proponer |
| No hay presupuesto LCSP para taller | Baja | Alto | CABANA workshops son gratis; co-financiamiento con IICS |
| Resistencia del personal a nuevo pipeline | Media | Medio | Incluir 2-3 personas LCSP en el taller; champion interno |
| Datos de dengue/MPXV no están bien curados | Media | Medio | Empezar con SARS-CoV-2 (mejor curado) |
| nf-core/viralrecon no funciona para dengue específicamente | Baja | Bajo | Usar Augur directo o adaptar pipeline manualmente |

**Riesgo neto: BAJO.** LCSP ya tiene infraestructura; el cambio es incremental.

### #5 — MedGemma 4B en Hospital de Clínicas

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| No hay champion clínico en Hospital de Clínicas | Alta | Alto | Identificar 2-3 residentes motivados; outreach amplio |
| IRB tarda más de lo esperado | Alta | Alto | Preparar protocolo IRB ANTES de empezar; pre-reunión con comité |
| Datos sintéticos no son suficiente para fine-tune útil | Media | Medio | Empezar con RAG + prompting (OpenMedLM) sin fine-tune |
| HIVE BUZZ no da acceso a investigación médica | Media | Alto | Confirmar ANTES de comprometer; backup X8 Cloud |
| Médicos no adoptan la herramienta | Alta | Alto | Diseño centrado en el clínico; feedback continuo; no forzar adoption |
| Performance en español paraguayo < inglés esperado | Media | Medio | Validar en eval set realista antes de deployment |

**Riesgo neto: MEDIO-ALTO.** Es el proyecto con mayor dependencia humana.

### #6 — AlphaGenome + CEDIC biobank

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Biobanco CEDIC × Galatea no tiene datos utilizables aún | Alta | Alto | Confirmar estado actual del biobanco antes de empezar |
| Variantes paraguayas son pocas (insufficient sample size) | Alta | Alto | Combinar con datos públicos; meta-análisis |
| API rate limits de AlphaGenome | Baja | Bajo | Cachear resultados; procesar offline |
| CEDIC no tiene investigador dedicado a esto | Alta | Alto | Outreach a Tesabio + Galatea para identificar champion |

**Riesgo neto: MEDIO-ALTO.** Depende completamente de la existencia del biobanco.

### #7 — D-Heart ECG Chagas cardiomyopathy

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Adquisición de D-Heart units lenta | Baja | Bajo | Comprar 5-10 unidades online; llega en 2-3 semanas |
| Personal de campo no sabe usar D-Heart | Media | Medio | Training de 1-2 días; manual ilustrado |
| No hay gold-standard (RBBB/bifascicular block) para validar | Media | Medio | Cardiologist remoto vía D-Heart Telecardiology Platform |
| Distribución de ECG units en Chaco es difícil | Alta | Medio | Visitas periódicas; no pretender cobertura universal |
| Batería del smartphone en Chaco | Alta | Medio | Power banks; solar chargers |

**Riesgo neto: BAJO-MEDIO.** Ya hay piloto exitoso en Bolivia.

### #8 — Capacitación CONAREM en Galaxy

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| No hay instructor local de Galaxy/nf-core | Alta | Medio | Facilitador externo (CABANA, SoIBio) |
| Los residentes no pueden dedicar tiempo | Alta | Medio | Acreditar como EMC (educación médica continua) |
| No hay laptops adecuadas | Media | Medio | Proporcionar acceso a Galaxy.eu (cloud) |
| Material en español no existe | Alta | Bajo | Crear materiales nuevos (output del taller) |

**Riesgo neto: BAJO.** Es multiplicador; bajo costo.

### #9 — Whisper fine-tune en guaraní médico

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Baseline mfidabel no es suficiente para fine-tune médico | Baja | Bajo | Evaluar primero; si no, entrenar desde cero con datos médicos |
| No hay datos médicos en guaraní etiquetados | Alta | Alto | Empezar con adaptación de dominio general a médico; crowdsourcing con comunidad chaqueña |
| Speakers guaraní tienen acentos muy diversos | Media | Medio | Fine-tune con datos de múltiples regiones |
| Speakers nativos de guaraní no están disponibles para evaluación | Media | Alto | Partnership con Cátedra de Guaraní (UNA) |

**Riesgo neto: MEDIO.** Depende de datos.

### #10 — Smartphone leishmaniasis app

| Riesgo | Probabilidad | Impacto | Mitigación |
|---|---|---|---|
| Modelo del paper brasileño no generaliza a Paraguay | Media | Alto | Re-entrenar con datos paraguayos antes de pilot |
| Variabilidad de calidad de imágenes | Media | Medio | Pre-procesamiento con blur detection (paper usa esto) |
| Acceptance por agentes de salud comunitaria | Media | Alto | Diseño centrado en el usuario; training; feedback |

**Riesgo neto: BAJO-MEDIO.** Paper brasileño es base sólida.

---

## §2 — Dependencias y bloqueos

Mapa de qué bloquea qué. Proyectos en paralelo si no hay dependencias entre ellos.

```
DEPENDENCY MAP
═══════════════════════════════════════════════════════

#5 MedGemma Hospital    ← necesita champion clínico (Riesgo: alto)
   ↑
   │  (mismo champion puede ser para #5 y para #21 chatbot)
   │
#21 WhatsApp salud mental  ← depende de #5 (LLM fine-tuneado) + #9 (Whisper guaraní)

#9 Whisper guaraní       ← NO bloqueado por nadie; solo necesita datos
   ↓
#21 WhatsApp salud mental (usa guaraní ASR)

#1 TB cough screening    ← NO bloqueado por nadie; linear probe solo
   ↑                              necesita HeAR + COUGHVID público
   │
#32 Health Telematics HTI ← puede seguir a #1 si HTI SMS es exitoso

#4 Nextclade LCSP        ← NO bloqueado por nadie; nf-core listo

#2 TxGemma Chagas        ← NO bloqueado por nadie; tools open + CEDIC datos

#6 AlphaGenome biobank    ← BLOQUEADO por existencia de biobanco CEDIC × Galatea
                            (verificar ANTES de comprometer)

#7 D-Heart ECG Chagas    ← NO bloqueado por nadie; piloto boliviano ya hecho

#8 CONAREM capacitación   ← NO bloqueado por nadie; facilitador externo

#10 Leishmaniasis app    ← NO bloqueado por nadie; paper brasileño como base
```

### §2.1 Análisis de paralelización

**Proyectos independientes (pueden correr en paralelo):**
- #1 TB HeAR
- #2 TxGemma Chagas
- #4 Nextclade LCSP
- #7 D-Heart ECG
- #8 CONAREM capacitación
- #10 Leishmaniasis app
- #9 Whisper guaraní

**Proyectos con dependencias:**
- #5 MedGemma → #21 WhatsApp salud mental
- #6 AlphaGenome → depende de biobanco CEDIC × Galatea (verificación previa)

**Recomendación:** empezar 3-4 proyectos en paralelo. Priorizar #1, #2, #4 por impacto + bajo riesgo.

---

## §3 — Requisitos computacionales detallados

| Proyecto | GPU mínimo | GPU óptimo | VRAM | Storage | Tiempo GPU | Costo compute |
|---|---|---|---|---|---|---|
| #1 TB HeAR POC | T4 (16GB) | A100 (40GB) | 16GB+ | ~5GB COUGHVID + ~500MB SPRSound | 2-4 horas | $0-5 con Colab |
| #1 TB HeAR field pilot | Edge TPU / smartphone | — | — | 100MB modelo en dispositivo | — | $0 (offline) |
| #2 TxGemma Chagas POC | A100 (40GB) | A100 (80GB) | 40-80GB | ~30GB TxGemma + Boltz-2 | 8-24 horas | $20-100 con HIVE BUZZ |
| #2 TxGemma full pipeline | H100 | multi-H100 | 80GB+ | ~100GB (compound library + protein structures) | 1-2 semanas | $500-2000 con X8 Cloud |
| #4 Nextclade LCSP | T4 (16GB) | A100 (40GB) | 16-40GB | ~50GB viral genomes | 1 semana setup | $50-200 |
| #5 MedGemma 4B fine-tune | A100 (40GB) | A100 (80GB) | 40-80GB con LoRA | ~30GB modelo + datasets | 1-2 semanas | $100-500 |
| #5 MedGemma 27B fine-tune | H100 | multi-H100 | 80GB+ | ~80GB modelo | 2-4 semanas | $500-2000 |
| #6 AlphaGenome | CPU suficiente | — | 8GB RAM | API solo, no storage local | — | $1-5 API costs |
| #7 D-Heart ECG | CPU | — | 8GB | ~10GB ECG recordings | 1 semana training | $0 (open data) |
| #8 CONAREM Galaxy | Browser-only | — | — | — | — | $0 (usando usegalaxy.eu) |
| #9 Whisper guaraní | T4 (16GB) | A100 (40GB) | 16-40GB | ~5-10GB audio data | 1-2 semanas | $50-300 |
| #10 Leishmaniasis app | T4 (16GB) | A100 (40GB) | 16-40GB | ~2GB model + images | 1 semana | $20-100 |

### §3.1 Total compute budget estimado

**Si se ejecutan todos los Tier 1 en paralelo durante 3 meses:**
- **GPU-hours totales:** ~5,000-15,000 horas
- **Costo total compute:** ~$3,000-10,000 USD (con HIVE BUZZ gratis + Colab free tier)
- **Storage total:** ~300GB

**Recomendación:** ejecutar todo en HIVE BUZZ cuando esté disponible para research médica; backup X8 Cloud.

---

## §4 — Datasets específicos por proyecto (todos públicos)

Esta es la lista exacta de datasets que cada proyecto necesita. Sin datasets paraguayos locales todavía (los crearemos en fase 2).

### #1 — TB cough screening HeAR

**Datasets públicos para POC inicial:**

| Dataset | URL/Access | Tamaño | Uso |
|---|---|---|---|
| **COUGHVID** | [coughvid](https://coughvid.epfl.ch/) | ~25,000 clips | Cough COVID/healthy baseline |
| **SPRSound** | [sprsound](https://github.com/SJTU-YONGFU/SPRSound) | ~9,000 clips | Pediatric respiratory sounds |
| **ICBHI 2017** | [kaggle icbhi](https://www.kaggle.com/datasets/...) | ~5,000 clips | Respiratory cycle classification |
| **FluSense** | [flusense](https://github.com/FluSense/FluSense) | ~50,000 clips | Cough/sneeze classification |
| **FSD50K** | [fsd50k](https://github.com/...fsd50k) | ~50,000 clips | General audio incl. respiratory |
| **Coswara** | [coswara.iisc.ac.in](https://coswara.iisc.ac.in/) | ~1,500+ COVID/healthy | Cough/breathing/speech |

**Datasets locales necesarios (fase 2):**
- Toses paraguayas con TB status confirmado (microbiología o GeneXpert)
- 200-500 muestras etiquetadas

### #2 — TxGemma + Boltz-2 Chagas

**Datasets públicos:**

| Dataset | URL | Uso |
|---|---|---|
| **Therapeutics Data Commons** | [tdcommons.ai](https://tdcommons.ai/) | Benchmarks para TxGemma |
| **PubChem** | [pubchem.ncbi.nlm.nih.gov](https://pubchem.ncbi.nlm.nih.gov/) | BioProsNat compounds + SMILES |
| **ChEMBL** | [ebi.ac.uk/chembl](https://www.ebi.ac.uk/chembl/) | Drug-target activity data |
| **TrypanoDB** | [tritrypdb.org](https://tritrypdb.org/) | *T. cruzi* / *Leishmania* specific |
| **AlphaFold DB** | [alphafold.ebi.ac.uk](https://alphafold.ebi.ac.uk) | Structures para cruzain, trans-sialidasa |
| **BindingDB** | [bindingdb.org](https://www.bindingdb.org/) | Protein-ligand binding affinity |

### #3 — HIBA partnership

No requiere datasets propios. Adopta los de HIBA.

### #4 — Nextclade + nf-core LCSP

| Dataset | URL | Uso |
|---|---|---|
| **GenBank dengue** | [ncbi.nlm.nih.gov](https://www.ncbi.nlm.nih.gov/genbank/) | Dengue reference sequences |
| **GISAID** | [gisaid.org](https://gisaid.org/) | SARS-CoV-2 + influenza |
| **Nextstrain** | [nextstrain.org](https://nextstrain.org/) | Pre-computed datasets |
| **MPXV sequences** | NCBI GenBank | Monkeypox reference |

### #5 — MedGemma Hospital de Clínicas

| Dataset | URL | Uso |
|---|---|---|
| **PubMedQA** | [pubmedqa](https://github.com/pubmedqa) | Medical QA baseline |
| **MedQA** | [github.com/jond3k/MedQA](https://github.com/jond3k/MedQA) | USMLE-style questions |
| **MedMCQA** | [medmcqa.github.io](https://medmcqa.github.io/) | Medical MCQ |
| **Spanish biomedical models** | [github.com/PlanTL/San-Bernard](https://github.com/PlanTL/San-Bernard) | Spanish biomedical BERT |

**Datasets locales necesarios:**
- Notas clínicas paraguayas anonimizadas (con IRB)
- Preguntas médicas en español paraguayo (synthetic + reales)

### #6 — AlphaGenome biobank

Solo API. No requiere dataset local previo.

### #7 — D-Heart ECG

| Dataset | URL | Uso |
|---|---|---|
| **PTB-XL** | [physionet.org/content/ptbxl](https://physionet.org/content/ptbxl/) | 21,837 12-lead ECGs |
| **Chapman** | [physionet.org/content/chapman](https://physionet.org/content/chapman/) | 10,646 12-lead ECGs |
| **CPSC2018** | [physionet.org/content/chapman](https://physionet.org/content/chapman/) | 6,877 12-lead ECGs |

### #8 — CONAREM Galaxy

| Recurso | URL |
|---|---|
| **usegalaxy.eu** | [usegalaxy.org](https://usegalaxy.org) |
| **Galaxy Training Material** | [training.galaxyproject.org](https://training.galaxyproject.org/) |

### #9 — Whisper guaraní

| Recurso | URL |
|---|---|
| **mfidabel/whisper-guaraní** | [huggingface.co/mfidabel](https://huggingface.co/mfidabel) (baseline existe) |
| **Common Voice Guaraní** (si existe) | [commonvoice.mozilla.org](https://commonvoice.mozilla.org/) |
| **FLEURS Guaraní** | [huggingface.co/google/fleurs](https://huggingface.co/google/fleurs) |

### #10 — Leishmaniasis app

| Dataset | URL | Uso |
|---|---|---|
| **ISIC Archive** | [isic-archive.com](https://www.isic-archive.com/) | Dermatoscopic images baseline |
| **HAM10000** | [dataverse.harvard.edu](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW79T) | Skin lesion classification |
| **Brazilian leishmaniasis dataset** | [paper PLOS NTD 2025](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0014313) | Leishmaniasis-specific images |

---

## §5 — Champion profiles (qué buscar en cada institución)

No basta saber los nombres de los directores. Necesitamos los champions reales: mid-career researchers motivados, con tiempo, con disposición al cambio. Perfiles ideales:

### Champion para #1 (TB HeAR) — en SENEPA o Hospital de Clínicas

**Perfil ideal:**
- Epidemiólogo o médico internista, 30-45 años
- Con experiencia en salud pública rural
- Interesado en tecnología pero no técnico
- Con tiempo protegido para proyecto (al menos 20% del tiempo)
- Con red de contactos en comunidades chaqueñas

**Cómo identificar:** LinkedIn search "SENEPA Paraguay" + "salud pública" + "Chaco" + filtro por actividad reciente. O: reuniones de la Sociedad Paraguaya de Neumología.

### Champion para #2 (TxGemma Chagas) — en CEDIC + BioProsNat

**Perfil ideal:**
- Bioquímico/farmacéutico, 30-50 años
- Con publicaciones en Chagas o leishmaniasis
- Con experiencia en screening experimental
- Con disposición a aprender herramientas computacionales
- Con tiempo protegido

**Cómo identificar:** revisión de publicaciones CEDIC 2023-2026, autores no senior, contacto via email.

### Champion para #3 (HIBA partnership) — bilingüe Paraguay-Argentina

**Perfil ideal:**
- Médico/informático, 35-50 años
- Con experiencia en implementación de IA en salud
- Con red de contactos en HIBA
- Con tiempo para misiones técnicas

**Cómo identificar:** revisar publicaciones del DIS-HIBA, encontrar investigadores junior o medio que trabajen en Argot o TANA.

### Champion para #4 (Nextclade LCSP) — LCSP

**Perfil ideal:**
- Bioinformático o virólogo molecular, 30-45 años
- Ya trabaja con secuencias genómicas virales
- Con disposición a estandarizar pipeline
- En LCSP específicamente

**Cómo identificar:** Dra. Cynthia Vazquez es la investigadora senior más visible. Pero el champion operativo probablemente sea un técnico o bioinformático junior que ella supervise.

### Champion para #5 (MedGemma Hospital de Clínicas) — Hospital de Clínicas

**Perfil ideal:**
- Residente avanzado (R3-R5) o médico joven con interés en tecnología
- Con disposición a usar herramientas IA en su práctica
- Con tiempo para participar en diseño y evaluación
- Con credibilidad ante colegas

**Cómo identificar:** revisión de residentes de Medicina Familiar o Medicina Interna con publicaciones, LinkedIn search "Hospital de Clínicas UNA" + "tecnología".

### Champion para #6 (AlphaGenome CEDIC) — CEDIC × Galatea

**Perfil ideal:**
- Investigador con experiencia en genómica
- Con acceso al biobanco CEDIC × Galatea
- Con disposición a análisis computacional
- Con tiempo protegido

**Cómo identificar:** revisión de autores CEDIC 2024-2026 en genomics, contacto con Dr. Adolfo Borges (Director CEDIC).

### Champion para #7 (D-Heart ECG) — Cardiología Hospital de Clínicas

**Perfil ideal:**
- Cardiólogo con interés en screening
- Con experiencia en comunidades rurales
- Con disposición a ECG básico en campo
- Con red de contactos en el Chaco

**Cómo identificar:** revisión de cardiólogos Hospital de Clínicas, contacto con Cátedra de Cardiología.

### Champion para #8 (CONAREM capacitación) — CONAREM o FCM-UNA

**Perfil ideal:**
- Director o coordinador académico de CONAREM
- Con disposición a incluir nuevas metodologías
- Con autoridad para acreditar EMC
- Con red de contactos con todos los residentes

**Cómo identificar:** LinkedIn, sitio web CONAREM.

### Champion para #9 (Whisper guaraní) — FCM-UNA + Cátedra Guaraní

**Perfil ideal:**
- Académico con experiencia en lingüística guaraní
- Con acceso a comunidad de hablantes nativos
- Con tiempo para participar en evaluación
- Con disposición a tecnología

**Cómo identificar:** Cátedra de Guaraní (UNA), Instituto de Lengua Guaraní.

### Champion para #10 (Leishmaniasis app) — Dermatología Hospital de Clínicas

**Perfil ideal:**
- Dermatólogo con experiencia tropical
- Con contacto con SENEPA
- Con disposición a teledermatología
- Con red de contactos en comunidades afectadas

**Cómo identificar:** revisión de dermatólogos con publicaciones sobre leishmaniasis.

---

## §6 — Funding map: $ → milestones

### $0 (solo tiempo)
- Construir 4 notebooks demo públicos (MedGemma, TxGemma, HeAR, Nextclade)
- Contribuir a awesome-medical-ai list
- Aplicar a fellowships / grants (CZI EOSS, Wellcome)
- **Milestone:** 4 demos públicos + 2 grants aplicados

### $2–5k (Tier 1 MVP)
- TB HeAR proof-of-concept notebook
- Nextclade nf-core setup en LCSP
- Whisper guaraní fine-tune MVP
- **Milestone:** 3 POCs validados técnicamente

### $10–30k (Tier 1 + Tier 2)
- TB HeAR field pilot
- TxGemma Chagas pipeline
- Smartphone ECG Chagas pilot
- D-Heart ECG Chagas
- Leishmaniasis app
- **Milestone:** 4-5 papers publicados

### $50–200k (Tier 2 + Tier 3)
- Field validation de TB HeAR en Chaco
- Biobanco FAIR nacional
- Programa de IA clínica Hospital de Clínicas
- Aplicación a convocatorias externas (FAPESP-CONACYT 2026, CZI EOSS, Wellcome)
- **Milestone:** programa institucional + co-financiamiento asegurado

### $200k+ (Tier 3 institucional)
- Centro de IA Médica en Asunción
- Tesabio commercialization
- National AI Strategy for Healthcare
- **Milestone:** centro autosostenible

### §6.1 Fuentes de financiamiento mapeadas

| Fuente | Ticket | Elegibilidad Paraguay | Fit |
|---|---|---|---|
| **PROCIENCIA II** (CONACYT) | ~$12k USD | Sí | Proyectos pequeños |
| **CZI EOSS** | ~$100k | Sí | Open-source tooling |
| **Google.org AI for Social Good** | Variable | Sí | Workshops + compute |
| **FAPESP-CONACYT-CONICET 2026 AMR** | ~$60k USD | Sí (vía coinvestigador) | Drug discovery AMR |
| **Wellcome Trust** | Variable | Sí | LMIC-led research |
| **NIH Fogarty** | $100-500k | Sí (vía socio US) | Research training |
| **IDB Lab** | $100-200k | Sí | Innovation, healthcare |
| **JICA (Japan)** | Variable | Sí (Paraguay priorizado) | Equipment + training |

---

## §7 — Reproducibilidad: checklist por proyecto

Para que cada POC sea **publicable y defendible**, debe cumplir:

### Universal checklist
- [ ] Dataset versionado y documentado
- [ ] Random seeds fijos en código
- [ ] Hyperparameters documentados
- [ ] Train/val/test split documentado
- [ ] Métricas estándar (AUROC, sensitivity, specificity, F1)
- [ ] Baseline comparison (vs modelo simple o estado del arte)
- [ ] Statistical testing (bootstrap CI, McNemar test, etc.)
- [ ] Error analysis (cuáles falla y por qué)
- [ ] Code open-source (GitHub, license)
- [ ] Model open-weight (cuando posible)
- [ ] Docker container (reproducibilidad de environment)
- [ ] README exhaustivo
- [ ] Limitations section explícita
- [ ] Ethics section (consentimiento, IRB, CARE Principles)
- [ ] Author contributions (CRediT)

### Por proyecto

**#1 TB HeAR:**
- [ ] Eval set estratificado por edad/sexo/región
- [ ] Validación cross-dataset (entrenar en COUGHVID, test en SPRSound)
- [ ] Test con datos TB-específicos cuando estén disponibles
- [ ] Comparar con WHO-recommended TB screening tools

**#2 TxGemma Chagas:**
- [ ] Validación con datos experimentales de CEDIC
- [ ] Comparar con virtual screening tradicional (AutoDock Vina)
- [ ] Test con compuestos no-BioProsNat
- [ ] Análisis de failure modes

**#4 Nextclade LCSP:**
- [ ] Validación contra genomas ya publicados
- [ ] Reproducibilidad del pipeline (Nextflow + nf-core)
- [ ] Comparación con pipeline anterior de LCSP

**#5 MedGemma Hospital de Clínicas:**
- [ ] Eval set con gold-standard (médicos senior)
- [ ] Comparación con general GPT/Gemini
- [ ] Evaluación clínica prospectiva
- [ ] Análisis de failure modes por subgrupo (pediátrico, geriátrico)

**#7 D-Heart ECG:**
- [ ] Gold-standard por cardiólogo certificado
- [ ] Validación contra ECG hospitalario (12-lead)
- [ ] Comparación con algoritmo de RBBB estándar

---

## §8 — Timeline realista con paralelización

### Mes 1 — POC técnicos
- Semana 1-2: Demos individuales (#1 POC notebook, #4 Nextclade setup, #9 Whisper MVP, #10 leishmaniasis notebook)
- Semana 3-4: Validación técnica, identificación de champions

**Output:** 4 notebooks demo + 2 champions identificados

### Mes 2 — Validación inicial
- Semana 1-2: Outreach a champions (#2 TxGemma + CEDIC, #5 MedGemma + Hospital de Clínicas, #7 D-Heart + cardiología)
- Semana 3-4: Primer paper (probablemente #1 TB HeAR POC o #4 Nextclade paper)

**Output:** 3 outreach + 1 paper submitted

### Mes 3 — Field pilots
- Semana 1-2: Setup de field pilots (#1 TB HeAR, #7 D-Heart)
- Semana 3-4: Aplicación a convocatorias externas (FAPESP-CONACYT 2026, CZI EOSS)

**Output:** 2 field pilots + 1 grant submitted

### Mes 4–6 — Scaling
- Field validation de TB HeAR
- Pipeline TxGemma + Boltz-2 + OpenFold3 completo
- Capacitación CONAREM
- Paper #5 MedGemma Hospital de Clínicas

**Output:** 3-4 papers + 1 grant funded

### Mes 7–12 — Strategic
- National AI Strategy for Healthcare white paper
- Biobanco FAIR nacional
- Partnership HIBA formalizado
- Tesabio commercialization

**Output:** 5+ papers + 1-2 grants funded + strategic document

### Diagrama de paralelización

```
Mes 1     Mes 2     Mes 3     Mes 4-6    Mes 7-12
─────────────────────────────────────────────────
#1 HeAR   →  POC →  Pilot → Field →  Paper
#2 Chagas →  POC →  Pipeline → Paper →  Grant
#4 LCSP   →  POC →  Paper  →  Adopt
#5 MedGem →  Setup → Fine-tune → Pilot → Paper
#7 DHeart →  Setup →  Pilot  →  Paper
#8 CONAR  →  Plan  →  Workshop → Adopt
#9 Whisper →  Setup → Fine-tune → Paper
#10 Leish →  POC  →  Adapt    → Paper
#6 Alpha →  Verify biobank → Paper
#3 HIBA  →  Contact →  Visit  → Partner
─────────────────────────────────────────────────
```

---

## §9 — Decisión final: qué construir primero

Basado en todos los análisis previos:

### Si solo pudiera hacer UNO hoy
**#1 — TB cough screening con HeAR.** El único proyecto con:
- Máximo impacto social (TB hiperendémico)
- Cero dependencias regulatorias externas
- Stack 100% open y deployable HOY
- Éticamente alineado con CARE Principles
- Replicable a otras enfermedades

### Si pudiera hacer TRES en paralelo
**#1 + #2 + #4:**
- **#1 TB HeAR** (impacto social, rápido)
- **#2 TxGemma Chagas** (impacto científico, mediano plazo)
- **#4 Nextclade LCSP** (impacto inmediato, bajo costo)

Cubre: vigilancia genómica + drug discovery + screening rural. Tres dimensiones del sistema de salud paraguayo.

### Si tuviera $50k y 6 meses
Los 6 proyectos con fit_score 8-10:
1. #1 TB HeAR
2. #2 TxGemma Chagas
3. #4 Nextclade LCSP
4. #5 MedGemma Hospital de Clínicas
5. #7 D-Heart ECG
6. #10 Leishmaniasis app

Cubre: screening rural + drug discovery + vigilancia genómica + clinical NLP + Chagas cardiomyopathy + skin NTD.

### Si tuviera $200k y 12 meses
Todos los Tier 1 + el partnership HIBA + biobanco FAIR.

### El principio

**Empezar con #1 (TB HeAR), validar la metodología con datos públicos, luego expandir.** Si el POC funciona técnicamente, tiene alta probabilidad de conseguir financiamiento. Si no, es una pérdida barata que aún produce un paper publicable.

---

## §10 — Tesis del análisis

Después de este análisis profundo, la tesis es:

**Paraguay está en una posición única para aprovechar IA médica open-source en 2026. La convergencia de:**

1. Stack de IA maduro (Boltz-2, MedGemma, HeAR, TxGemma, OpenFold3)
2. Marco regulatorio en apertura (Ley 7593/2025 vigente en Nov 2027)
3. Partnerships disponibles (HIBA, Stanford, Google, NVIDIA)
4. Capacidad institucional real (IICS, CEDIC, LCSP, Tesabio, FIUNA, Hospital de Clínicas)
5. Burden de enfermedad que el mundo necesita resolver (Chagas, TB, leishmaniasis)

**Es una ventana de 12–18 meses.** Después:
- Otros países latinoamericanos harán lo mismo
- Ley 7593/2025 entrará en vigencia
- El talento humano paraguayo se habrá ido a otros lados
- Los datasets paraguayos no estarán disponibles para Paraguay

**La pregunta no es si Paraguay debe hacer esto. Es si Paraguay lo hace antes de que la ventana se cierre.**

---

## Última actualización

Septiembre 2026.