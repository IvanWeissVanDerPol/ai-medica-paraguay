# Google DeepMind + HAI-DEF para Paraguay — análisis dedicado

Documento de referencia específico sobre el portafolio de Google aplicado a Paraguay. Complementa `docs/ai-stack-reference.md` §14–16 con contexto local, mapeo institucional, y proyectos concretos.

> Última actualización: septiembre 2026.

---

## §1. Por qué Google es prioritario para Paraguay

Google tiene el portafolio abierto más completo del mundo en IA biomédica. Para Paraguay específicamente:

1. **Dominio match**: enfermedades desatendidas (Chagas), salud pública (TB, dengue), cáncer — todos modelados por HAI-DEF o DeepMind.
2. **Idioma base**: Gemma 3 es multilingual; MedGemma hereda eso. Fine-tuneable en español paraguayo.
3. **Sin restricción comercial abierta**: la mayoría de HAI-DEF + Gemma 3 permite uso comercial (excepto AlphaFold3 weights, AlphaGenome API).
4. **No requiere GPU pesada**: MedGemma 4B corre en una sola GPU; HeAR cabe en un smartphone.
5. **Pre-positioning regulatorio**: HAI-DEF *prohíbe* uso como dispositivo médico regulado. Paraguay no tiene regulación aún — oportunidad para diseñar el framework que otros no han hecho.

---

## §2. Mapeo: Google tools × Paraguay

### §2.1 Tabla de fit

| Google tool | Necesidad Paraguay | Fit | Barrera principal |
|---|---|---|---|
| **MedGemma 4B/27B** | Clinical NLP en Hospital de Clínicas | ⭐⭐⭐ | Fine-tune español paraguayo |
| **TxGemma 27B-Chat** | Drug discovery (Chagas, Leishmania) | ⭐⭐⭐ | Necesita fine-tune con datos paraguayos |
| **HeAR** | TB screening rural | ⭐⭐⭐ | Audio data local (puede bootstrapping con datasets públicos) |
| **OpenFold3** | Estructura de proteínas (AF3-class, open) | ⭐⭐⭐ | Ninguna significativa |
| **Boltz-2** | Drug discovery con afinidad | ⭐⭐⭐ | GPU para correr localmente |
| **AlphaGenome API** | Variant interpretation (CEDIC × Galatea) | ⭐⭐ | API cap, no comercial |
| **CXR Foundation** | TB screening, cardiomegaly | ⭐⭐ | Necesita chest X-rays digitalizados |
| **Path Foundation** | INCAN pathology | ⭐⭐ | Necesita slide scanner |
| **Derm Foundation** | Teledermatología rural | ⭐⭐ | Distribución rural + smartphones |
| **MedSigLIP** | Image embeddings general | ⭐⭐ | Mixto |
| **AlphaFold Server** | Estructura ad-hoc académica | ⭐ | 10–20 jobs/día por usuario |
| **MedASR** | Template para Spanish medical dictation | ⭐ | English-only |
| **Gemini 2.5 Pro** | Research assistant | ⭐ | Pagado, closed source |
| **AI Co-Scientist** | Drug repurposing para Chagas | ⏸ | No acceso público aún |
| **PaliGemma 2** | Backup VLM | ⭐ | No médico-tuned |

### §2.2 Fits detallados por área del repo

| Área del repo | Google tools recomendados |
|---|---|
| **Vigilancia genómica (LCSP)** | AlphaGenome (variant calls), AlphaFold Server (protein structures para patógenos) |
| **Drug discovery (CEDIC, BioProsNat, Tesabio)** | TxGemma (ADMET, queries), OpenFold3 (estructura), Boltz-2 (afinidad, MIT — complement) |
| **LLMs clínicos (Hospital de Clínicas)** | MedGemma 4B + MedSigLIP |
| **Patología digital (INCAN)** | Path Foundation, CONCH (third-party), UNI |
| **Resistencia antimicrobiana** | HeAR (TB cough screening), CXR Foundation, AlphaFold Server (estructura M. tuberculosis targets) |
| **Salud mental (Cátedra Psiquiatría)** | MedGemma 4B fine-tune, Gemini 2.5 Pro como research assistant |
| **Telemedicina (Chaco)** | Derm Foundation (teledermatología), HeAR (TB), MedGemma 4B (triage LLM) |
| **Capacitación investigación** | Notebook HAI-DEF, Gemini 2.5 Pro como research assistant |
| **Health acoustics TB screening (nueva área)** | HeAR (heart of the project) |

---

## §3. Tres recomendaciones principales (orden de prioridad)

### 🥇 #1: MedGemma 4B — clinical LLM

**Por qué**: Hospital de Clínicas tiene 1.150 visitas/día, registro en papel, sin LLM clínico desplegado. MedGemma 4B es el LLM clínico open más capaz que cabe en una sola GPU, con licencia que permite deploy local. Fine-tuneable en español paraguayo.

**Primer proyecto concreto (Tier 1, 1–3 meses)**:

1. Descargar MedGemma 4B (gated) desde HuggingFace.
2. Evaluar zero-shot con un eval set de preguntas médicas en español paraguayo.
3. Construir un mini-corpus de notas clínicas sintéticas (generadas con LLM + revisadas por médico local).
4. Fine-tune LoRA en el corpus sintético.
5. Evaluar performance antes/después.
6. **Entregable**: notebook + paper + open-weight model.

**Recursos para arrancar:**

- Notebook quick start: [colab.research.google.com/github/google-health/medgemma](https://colab.research.google.com/github/google-health/medgemma/blob/main/notebooks/quick_start_with_hugging_face.ipynb)
- HF: [huggingface.co/collections/google/medgemma](https://huggingface.co/collections/google/medgemma)
- Fine-tuning notebook: en [github.com/google-health/medgemma](https://github.com/google-health/medgemma) (carpeta `notebooks/`)

### 🥈 #2: TxGemma 27B-Chat — drug discovery

**Por qué**: Paraguay tiene CEDIC + BioProsNat + Tesabio — la cadena exacta para drug discovery local. TxGemma puede predecir ADMET (toxicidad, BBB penetration, CYP) y afinidad de unión proteína-ligando desde SMILES. Combinado con Boltz-2 (MIT, comercial OK) para estructura, da el loop cerrado que ningún lab paraguayo tiene hoy.

**Primer proyecto concreto (Tier 1, 1–3 meses)**:

1. Descargar TxGemma-Chat 27B.
2. Query en español sobre la biblioteca de productos naturales de BioProsNat.
3. Comparar predicciones con datos in vitro existentes en CEDIC.
4. **Entregable**: paper de priorización con los mejores hits.

**Recursos:**

- Model card: [developers.google.com/health-ai-developer-foundations/txgemma/model-card](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card)
- Blog: [developers.googleblog.com/introducing-txgemma](https://developers.googleblog.com/introducing-txgemma-open-models-improving-therapeutics-development/)
- Therapeutics Data Commons: [tdcommons.ai](https://tdcommons.ai/)

### 🥉 #3: HeAR — TB cough screening (sleeper hit)

**Por qué**: Paraguay es hiperendémico para TB. Atención primaria rural no tiene chest X-ray. HeAR convierte un smartphone en un sensor de screening. Es la aplicación con mayor impacto social inmediato.

**Primer proyecto concreto (Tier 1, 3–6 meses)**:

1. Cargar HeAR (HuggingFace).
2. Construir o usar dataset público de toses (COUGHVID, SPRSound).
3. Entrenar clasificador lineal (logistic regression) para TB.
4. Evaluar performance.
5. **Si funciona**: piloto en Chaco con community health workers usando smartphones.

**Recursos:**

- HF: [huggingface.co/google/hear](https://huggingface.co/google/hear)
- Paper: [arxiv.org/abs/2403.02522](https://arxiv.org/abs/2403.02522)
- Linear classifier notebook: en la [página oficial](https://developers.google.com/health-ai-developer-foundations/hear)

---

## §4. Recomendaciones secundarias (orden de prioridad)

### #4: OpenFold3 — estructura AF3-class open

- **Por qué**: Tesabio no puede usar AF3 weights comercialmente. OpenFold3 da misma performance, Apache 2.0.
- **Primer proyecto**: CEDIC + Tesabio predicen estructuras de dianas de *T. cruzi* con OpenFold3; comparan con AF3 (académico) cuando ambos disponibles.
- Repo: [github.com/aqlaboratory/openfold-3](https://github.com/aqlaboratory/openfold-3)

### #5: AlphaGenome API + Atlas

- **Por qué**: CEDIC × Galatea Bio biobank necesita variant interpretation. AlphaGenome Atlas tiene 9B precomputed scores.
- **Primer proyecto**: cada nueva variante secuenciada en Paraguay → AlphaGenome API → score de impacto regulatorio → paper.
- Sitio: [deepmind.google/science/alphagenome](https://deepmind.google/science/alphagenome)

### #6: Path Foundation + CXR Foundation + Derm Foundation

- **Por qué**: INCAN necesita patología digital; Hospital de Clínicas tiene CXRs digitalizados esporádicos; Chaco necesita teledermatología.
- **Primer proyecto**: cuando INCAN digitalice 1.000 slides, aplicar Path Foundation zero-shot. Documentar performance vs patólogos.
- Sitio: [developers.google.com/health-ai-developer-foundations](https://developers.google.com/health-ai-developer-foundations)

### #7: MedASR como template para Spanish medical ASR

- **Por qué**: Hospital de Clínicas tiene dictado de residentes; transcripción ahorra tiempo.
- **Primer proyecto**: usar MedASR como reference architecture para entrenar Whisper o un Conformer español/guaraní.
- HF: [huggingface.co/google/medasr](https://huggingface.co/google/medasr)

### #8: AI Co-Scientist (futuro)

- **Por qué**: drug repurposing para Chagas es la aplicación exacta del playbook AML.
- **Status**: no producto público. Si Google abre Trusted Tester, aplicar.
- Sitio: [research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)

---

## §5. Compliance + regulatory para Paraguay

### §5.1 Lo que HAI-DEF prohíbe explícitamente

- **Cualquier uso que haga a Google ser considerado "manufacturer" de dispositivo médico**.
- **Usos restringidos** según Prohibited Use Policy (incluye generar contenido dañino, ilegal, etc.).
- **Violación de leyes/regulaciones aplicables**.

### §5.2 Implicación práctica para Paraguay

Si Paraguay quiere usar MedGemma en un hospital clínico (no solo investigación), hay dos opciones:

1. **No usar como dispositivo médico regulado** — solo asistir al clínico (decision support, no autonomous diagnosis). Esto es lo que HAI-DEF permite.
2. **Validar independientemente** y obtener clearance regulatorio paraguayo (cuando exista). Esto es responsabilidad del deployer, no de Google.

### §5.3 Ventana regulatoria abierta

- Ley 7593/2025 de protección de datos entra en vigencia noviembre 2027.
- No hay pathway regulatorio para IA clínica en Paraguay.
- **Oportunidad**: Paraguay puede diseñar el primer framework de "Health Regulatory Authorization" para IA clínica en LatAm, alineado con HAI-DEF terms.

### §5.4 Soberanía de datos + CARE Principles

Cualquier deploy de modelos Google en Paraguay con datos de comunidades indígenas chaqueñas requiere:
- Consentimiento colectivo además del individual.
- Gobernanza de datos con comunidades.
- Devolución de resultados a la comunidad.
- CARE Principles (Collective benefit, Authority to control, Responsibility, Ethics).

---

## §6. Próximos pasos operativos

### Semana 1 (preparación)
- [ ] Confirmar champions en Hospital de Clínicas, CEDIC, IICS, Tesabio (ver `docs/plan-preparacion.md`).
- [ ] Leer National Health Research Ethics Policy 2024 (pendiente crítico).
- [ ] Identificar datasets paraguayos disponibles (de-identified TB coughs, notas clínicas, variantes).

### Semana 2 (preparación técnica)
- [ ] Descargar MedGemma 4B + TxGemma-Chat 9B (gated via HF).
- [ ] Evaluar MedGemma zero-shot con preguntas médicas en español.
- [ ] Construir mini-corpus de notas clínicas sintéticas en español paraguayo.
- [ ] Fine-tune MedGemma 4B con LoRA.

### Semana 3 (alcance externo)
- [ ] Cold outreach a Dr. Diego Galeano (FIUNA + Tesabio CTO) — colaboración TxGemma + Tesabio.
- [ ] Cold outreach a Dr. Cynthia Vazquez (LCSP) — AlphaGenome API.
- [ ] Cold outreach a Dra. Rosa Guillén Fretes (IICS, AMR) — HeAR TB screening.

### Semana 4 (proyecto piloto)
- [ ] Si hay champion: arrancar el Tier 1 proyecto MedGemma + Hospital de Clínicas.
- [ ] Si no: ajustar outreach y reintentar.

---

## §7. Recursos consolidados para implementación

### Documentación oficial HAI-DEF

- [Health AI Developer Foundations home](https://developers.google.com/health-ai-developer-foundations)
- [Terms](https://developers.google.com/health-ai-developer-foundations/terms)
- [Prohibited Use Policy](https://developers.google.com/health-ai-developer-foundations/prohibited-use-policy)
- [Overview](https://developers.google.com/health-ai-developer-foundations/overview)
- [FAQ](https://developers.google.com/health-ai-developer-foundations/faqs)

### Models — quick links

- MedGemma: [developers.google.com/health-ai-developer-foundations/medgemma](https://developers.google.com/health-ai-developer-foundations/medgemma/model-card) · [HF](https://huggingface.co/collections/google/medgemma) · [GitHub](https://github.com/google-health/medgemma)
- TxGemma: [developers.google.com/health-ai-developer-foundations/txgemma/model-card](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card) · [DeepMind blog](https://deepmind.google/models/gemma/txgemma/)
- HeAR: [developers.google.com/health-ai-developer-foundations/hear](https://developers.google.com/health-ai-developer-foundations/hear) · [HF](https://huggingface.co/google/hear) · [paper](https://arxiv.org/abs/2403.02522)
- MedSigLIP: [developers.google.com/health-ai-developer-foundations/medsiglip/model-card](https://developers.google.com/health-ai-developer-foundations/medsiglip/model-card)
- Path Foundation: [developers.google.com/health-ai-developer-foundations](https://developers.google.com/health-ai-developer-foundations)
- CXR Foundation: [developers.google.com/health-ai-developer-foundations/cxr-foundation](https://developers.google.com/health-ai-developer-foundations/cxr-foundation)
- MedASR: [medasr.org](https://medasr.org) · [HF](https://huggingface.co/google/medasr) · [paper](https://arxiv.org/pdf/2605.16555)

### DeepMind models

- AlphaFold 3: [github.com/google-deepmind/alphafold3](https://github.com/google-deepmind/alphafold3) · [AlphaFold Server](https://alphafoldserver.com)
- AlphaGenome: [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome) · [API](https://deepmind.google/science/alphagenome) · [Atlas](https://deepmind.google/science/alphagenome/atlas)
- AI Co-Scientist: [research.google/blog](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) · [Nature paper](https://doi.org/10.1038/s41586-026-10644-y)
- Gemini 2.5: [ai.google.dev/gemini-2.5](https://ai.google.dev/gemini-api/docs/models)
- OpenFold3 (third-party): [github.com/aqlaboratory/openfold-3](https://github.com/aqlaboratory/openfold-3)

### Notebooks para arrancar

- MedGemma quick start: [colab.research.google.com/github/google-health/medgemma](https://colab.research.google.com/github/google-health/medgemma/blob/main/notebooks/quick_start_with_hugging_face.ipynb)
- MedGemma fine-tuning: en [github.com/google-health/medgemma](https://github.com/google-health/medgemma) carpeta `notebooks/`
- HeAR linear classifier: en [developers.google.com/health-ai-developer-foundations/hear](https://developers.google.com/health-ai-developer-foundations/hear)

---

## Última actualización

Septiembre 2026.