# Lo que otros hacen — investigación de pares, proyectos abiertos, y modelos a considerar

> **Qué es este archivo:** una investigación de los proyectos open-source, repos, instituciones y peer efforts más relevantes del mundo que Paraguay debería mirar y considerar借鉴. Por área, por necesidad, por nivel de madurez.
>
> **Audiencia:** quien planifica partnerships, fundraising, o simplemente quiere entender qué ya existe y qué gaps quedan.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — El ecosistema de "awesome lists" (mapas del terreno)
- §2 — Hospital Italiano de Buenos Aires — el modelo regional más cercano
- §3 — Proyectos open-source por categoría, con fit para Paraguay
- §4 — Gaps observados: lo que nadie está haciendo bien
- §5 — Partnerships recomendados
- §6 — Lo que Paraguay puede construir sobre hombros de gigantes

---

## §1 — El ecosistema de "awesome lists" — mapas del terreno

Antes de construir, vale mirar qué ya existe. Los siguientes repos son mapas vivos de todo el espacio de IA médica open-source.

### §1.1 Awesome lists principales

| Repo | Stars (aprox) | Contenido | URL |
|---|---|---|---|
| [awesome-medical-ai](https://github.com/JuneYaooo/awesome-medical-ai) | ~3k+ | Curated list: medical LLMs, imaging, multi-agent, clinical software. Calificado A–C. | github.com/JuneYaooo/awesome-medical-ai |
| [awesome-medical-rag](https://github.com/justin-marian/awesome-medical-rag) | ~2k+ | **250+ papers, datasets, benchmarks** sobre Medical RAG + Knowledge Graphs + Clinical LLMs + Multilingual Reasoning. | github.com/justin-marian/awesome-medical-rag |
| [Awesome-AI4Med](https://github.com/FreedomIntelligence/Awesome-AI4Med) | alto | Medical LLMs, multimodal, datasets, benchmarks. | github.com/FreedomIntelligence/Awesome-AI4Med |
| [Awesome-AI-Agents-for-Healthcare](https://github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare) | medio | Survey-style de agentes IA en salud. | github.com/AgenticHealthAI/Awesome-AI-Agents-for-Healthcare |
| [Awesome-AI4DigitalPathology](https://github.com/lingxitong/Awesome-AI4DigitalPathology) | medio | Pathology AI curated. | github.com/lingxitong/Awesome-AI4DigitalPathology |
| [awesome-medical-rag](https://github.com/justin-marian/awesome-medical-rag) | ~2k+ | Medical RAG + KG | (ya listado) |
| [georg-wolflein/pathology-foundation-models](https://github.com/georg-wolflein/pathology-foundation-models) | ~1k+ | Lista curada con licencias y parámetros de TODOS los pathology FMs. | github.com/georg-wolflein/pathology-foundation-models |
| [dibalokechanda/PFMs](https://github.com/dibalokechanda/PFMs) | medio | Catálogo curado de pathology FMs. | github.com/dibalokechanda/PFMs |

### §1.2 Lo que estos repos confirman (vs mi análisis previo del repo)

- **Mi catálogo AI stack** ya cubre el ~80% de lo importante. Lo que **falta** en mi repo y estos awesome lists sí incluyen:
 - **AI-MARRVEL** (NEJM AI 2024) — variant interpretation + AI
 - **MDAgents** (NeurIPS 2024) — adaptive collaboration of LLMs para medical decision-making
 - **DrugAgent** — explainable drug repurposing agent con LLM
 - **BioRAG** — biological question reasoning RAG
 - **DrugAgent** — específicamente para Chagas-relevant drug repurposing
 - **PathAsst** — 207K pathology image-text pairs
 - **MAMMOTH** (Mahmood Lab) — mixture-of-mini-experts for pathology
 - **PMC-VQA** — 227K medical VQA pairs

---

## §2 — Hospital Italiano de Buenos Aires — el modelo regional más cercano

### §2.1 Por qué es el modelo más relevante para Paraguay

**Misma región, mismo idioma base (español), mismo nivel regulatorio, mismo perfil de paciente, mismo contexto cultural.** Si Paraguay quiere hacer algo similar a escala de un hospital universitario, Hospital Italiano es el referente directo.

### §2.2 Lo que han construido (cronología verificada)

| Año | Hito |
|---|---|
| 1998 | Plan maestro de gobernanza informática (Hospital decide informatizarse) |
| 2001 | Creación del **Departamento de Informática en Salud (DIS)** |
| 2018 | Bases para IA en salud (colaboración DxI-HIBA + Dermatología) |
| 2019 | Lanzamiento de **Argot** — NLP para codificación automática de términos médicos |
| 2020 | Fundación de **pIASHIBA** — Programa de IA en Salud HIBA |
| 2020+ | **Artemisia** — mamografías; **TRx** — radiografías de tórax |
| 2023 | **TANA** — chatbot clínico (hoy copiloto asistencial con IA integrado en HCE) |
| 2026 | Retrospectiva publicada en Int J Med Inform |

### §2.3 Productos activos hoy

- **Argot** (2019, NLP clínico maduro) → Paraguay puede借鉴 para procesar notas en español
- **Artemisia** (mamografía AI) → Paraguay tiene INCAN con programa de cáncer de mama, podría adaptar
- **TRx** (radiografía de tórax AI) → Paraguay necesita TB screening + CXR — exactamente este caso de uso
- **TANA** (chatbot clínico) → Paraguay tiene Hospital de Clínicas + Cátedra de Psiquiatría

### §2.4 Lecciones aprendidas del paper 2026

Del paper "Evolution of artificial intelligence at Hospital Italiano de Buenos Aires" (Int J Med Inform 2026), las lecciones son:
1. **Programa institucional translacional** (>5 años para madurar)
2. **Equipo transdisciplinario** (ingeniería biomédica + medicina + software)
3. **Comenzar con CDSS + NLP + visión** — no saltarse a "AI mágica"
4. **Iteración clínica** constante
5. **Adaptar tecnologías globales a problemáticas locales**
6. **Acompañar a los profesionales en el cambio de rol**

### §2.5 Recomendación

**Paraguay debería contactar Hospital Italiano para:**
- Partnership técnico (no solo参观): adopción de Argot para procesar notas en español paraguayo
- **TANA como blueprint** para chatbot clínico del Hospital de Clínicas
- **TRx como blueprint** para CXR AI
- **Programa de intercambio** IICS-HIBA para entrenamiento de residentes en IA clínica

**Contacto**: a través del Departamento de Informática en Salud (DIS-HIBA), Buenos Aires. Bajar de jerarquía "oficial" a "técnico" — funciona mejor.

---

## §3 — Proyectos open-source por categoría, con fit para Paraguay

### §3.1 LLMs médicos (fit Paraguay: ⭐⭐⭐)

| Proyecto | Stars | License | Fit Paraguay | Notas |
|---|---|---|---|---|
| [MedGemma 4B/27B](https://github.com/google-health/medgemma) | 1.5k+ | HAI-DEF | ⭐⭐⭐⭐⭐ | **Default**. Ya en repo. |
| [TxGemma](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card) | nuevo | Gemma terms | ⭐⭐⭐⭐⭐ | **Default** para drug discovery. Ya en repo. |
| [OpenMedLM](https://github.com/OpenMedLM) | 1k+ | Apache 2.0 | ⭐⭐⭐⭐ | Yi 34B prompting; baseline barato |
| [Meditron](https://huggingface.co/collections/OpenMedLM/meditron) | alto | Llama community | ⭐⭐⭐ | Llama 2 70B fine-tune |
| [BioMistral](https://huggingface.co/BioMistral) | medio | Apache 2.0 | ⭐⭐⭐ | Mistral biomedical 7B |
| [Baichuan-M1](https://arxiv.org/abs/...) | — | — | ⭐⭐⭐ | 14B medical-specific. SOTA en MedR-Bench efficiency. |
| [BianQue-2](https://github.com/) | medio | — | ⭐⭐ | Chinese medical, no priority |
| [Qwen-QwQ](https://huggingface.co/Qwen/QwQ-32B-Preview) | muy alto | Apache 2.0 | ⭐⭐⭐ | Reasoning model; 32B |
| [DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | muy alto | MIT | ⭐⭐⭐ | Reasoning model; 671B. SOTA efficiency en MedR-Bench. |
| [ChatMed](https://github.com/michael-wzhu/ChatMed) | alto | — | ⭐⭐ | Chinese, no priority |
| [AlpaCare](https://github.com/XZhang97666/AlpaCare) | medio | Apache 2.0 | ⭐⭐ | 7B/13B medical instruction |
| [medAlpaca](https://github.com/kbressem/medAlpaca) | alto | — | ⭐ | Alpaca-based medical |

### §3.2 Imaging / Radiology / Pathology (fit Paraguay: ⭐⭐⭐)

| Proyecto | Stars | License | Fit | Notas |
|---|---|---|---|---|
| [MedSAM](https://github.com/bowang-lab/MedSAM) | 5k+ | MIT | ⭐⭐⭐⭐ | Ya en repo. **Default** para segmentación. |
| [MedSAM2](https://github.com/bowang-lab/MedSAM2) | alto | MIT | ⭐⭐⭐⭐ | 3D + video. Más reciente. |
| [RadFM](https://github.com/chaoyi-wu/RadFM) | 1k+ | (paper-specific) | ⭐⭐⭐ | Radiology 2D/3D. Ya en repo. |
| [MedRAX](https://github.com/bowang-lab/MedRAX) | alto | (paper-specific) | ⭐⭐⭐⭐⭐ | **ICML 2025**. Chest X-ray AI agent. Combina CheXagent + LLaVA-Med + MedSAM + Maira-2 + DenseNet-121. ChestAgentBench (2,500 queries). LangChain-based. **Directamente relevante para TB screening.** |
| [LLaVA-Med](https://github.com/microsoft/LLaVA-Med) | 2k+ | Apache 2.0 | ⭐⭐⭐ | Microsoft. Biomedical VLM. Ya mencionado. |
| [CheXagent](https://github.com/Stanford-AIMI/CheXagent) | 800+ | Apache 2.0 | ⭐⭐⭐⭐ | Stanford AIMI. Chest X-ray. |
| [XRayGPT](https://github.com/mbzuai-oryx/XRayGPT) | 600+ | Apache 2.0 | ⭐⭐⭐ | MBZUAI. Chest X-ray. |
| [BiomedCLIP](https://github.com/microsoft/BiomedCLIP) | 1k+ | Apache 2.0 | ⭐⭐⭐ | Microsoft. Image-text retrieval. |
| [RadFM](https://github.com/chaoyi-wu/RadFM) | 1k+ | (paper-specific) | ⭐⭐⭐ | Generalist radiology |
| [PathAsst](https://github.com/superjamessyx/Pathology) | alto | — | ⭐⭐⭐ | 207K image-text pairs pathology |
| [MAMMOTH](https://github.com/mahmoodlab/MAMMOTH) | medio | — | ⭐⭐⭐ | Mahmood Lab. Mixture-of-experts for pathology |
| [PathFLIP](https://github.com/cyclexfy/PathFLIP) | medio | — | ⭐⭐⭐ | AAAI 2026 pathology VLM |
| [TorchIO](https://github.com/TorchIO-project/torchio) | 2k+ | Apache 2.0 | ⭐⭐⭐ | PyTorch toolkit medical image preprocessing |
| [TIA Toolbox](https://github.com/TissueImageAnalytics/tiatoolbox) | 1k+ | BSD-3 | ⭐⭐⭐ | Computational pathology toolbox, WHOLE-SLIDE IO |
| [MONAI](https://github.com/Project-MONAI/MONAI) | 6k+ | Apache 2.0 | ⭐⭐⭐⭐ | **Medical imaging framework**, NVIDIA + academia. Industry standard. |

### §3.3 Multi-agent / LLM agents (fit Paraguay: ⭐⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [MedRAX](https://github.com/bowang-lab/MedRAX) | alto | ⭐⭐⭐⭐⭐ | Chest X-ray AI agent. Combina 4-5 modelos. **Relevante directamente.** |
| [MedSci Agent](https://github.com/omar-A-hassan/medsci-agent) | alto | ⭐⭐⭐⭐ | **Soporta MedGemma y TxGemma locales vía Ollama.** 28 MCP tools. **Directamente desplegable en Paraguay.** |
| [ChemCrow](https://github.com/) | 894 | ⭐⭐⭐⭐ | LLM + chemistry tools. **Dormant desde dic 2024.** |
| [RxLM-Med-Agent](https://github.com/tokisaka23/RxLM-Med-Agent) | medio | ⭐⭐⭐ | Multimodal clinical diagnostic agent. Qwen-VL + RAG. |
| [MedAgents](https://github.com/gersteinlab/MedAgents) | alto | ⭐⭐⭐ | ACL 2024 multi-disciplinary LLM collaboration |
| [MAM](https://github.com/yczhou001/MAM) | medio | ⭐⭐⭐ | ACL 2025 modular multi-agent |
| [MMedAgent](https://github.com/Wangyixinxin/MMedAgent) | medio | ⭐⭐⭐ | Multi-modal medical tool-use |
| [MDAgents](https://github.com/) | alto | ⭐⭐⭐ | Adaptive collaboration of LLMs |
| [clin-evidence](https://github.com/Hilary-Henshaw/clin-evidence) | medio | ⭐⭐⭐ | LangGraph ICU evidence + RAG + PubMed |
| [MedGraph-AI](https://github.com/chencyan21/MedGraphAI) | medio | ⭐⭐⭐ | LangGraph multi-agent + RAG + image |
| [CLARA-Care](https://github.com/Project-CLARA-HBT/CLARA-Care) | medio | ⭐⭐⭐ | Safety-first medical assistant |
| [HERA](https://github.com/Nerdboss-stm/hera-healthcare-ai) | medio | ⭐⭐⭐ | Triage/diagnostic/treatment agents + FHIR |
| [MedgeClaw](https://github.com/xjtulyc/MedgeClaw) | medio | ⭐⭐⭐ | XJTU. Integrates 140+ K-Dense scientific skills via Claude Code |
| [HealthFlow](https://github.com/yhzhu99/HealthFlow) | medio | ⭐⭐⭐ | Self-evolving healthcare research agent |
| [Multi-Agent-Medical-Assistant](https://github.com/souvikmajumder26/Multi-Agent-Medical-Assistant) | medio | ⭐⭐ | Diagnostics + research chatbot |
| [SepsisAgent](https://github.com/FreedomIntelligence/SepsisAgent) | medio | ⭐⭐ | HuatuoGPT team. Clinical workflow agent. |
| [DrugAgent](https://github.com/) | — | ⭐⭐⭐⭐ | **Explainable drug repurposing agent**. Relevante para Chagas. |
| [BioAgentics](https://github.com/Agentomics/BioAgentics) | bajo | ⭐⭐ | Multi-agent biomedical research |

### §3.4 Genomics & Drug Discovery (fit Paraguay: ⭐⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [Boltz-1/Boltz-2](https://github.com/jwohlwend/boltz) | alto | ⭐⭐⭐⭐⭐ | **MIT**, comercial OK. **Default** para drug discovery Paraguay. |
| [OpenFold3](https://github.com/aqlaboratory/openfold-3) | alto | ⭐⭐⭐⭐⭐ | Apache 2.0. Único AF3-class open. **Para Tesabio.** |
| [AlphaFold 3](https://github.com/google-deepmind/alphafold3) | alto | ⭐⭐⭐ | Código Apache 2.0, pesos non-commercial. |
| [AlphaGenome](https://github.com/google-deepmind/alphagenome) | alto | ⭐⭐⭐⭐ | API no commercial. **Variant interpretation para CEDIC.** |
| [Chai-1](https://github.com/chaidiscovery/chai-lab) | alto | ⭐⭐⭐ | Apache 2.0 |
| [ESM-3](https://github.com/evolutionaryscale/esm) | alto | ⭐⭐⭐ | Cambrian Non-Commercial (1.4B), API para mayor |
| [LigandMPNN](https://github.com/dauparas/LigandMPNN) | alto | ⭐⭐⭐⭐ | Open. **Compañero perfecto de Boltz-2.** |
| [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) | alto | ⭐⭐⭐ | Diseño backbone |
| [ChemBERTa-3](https://github.com/deepchem/deepchem) | alto | ⭐⭐⭐ | DeepChem. Fine-tunable chemical FMs. |
| [REINVENT4](https://github.com/MolecularAI/REINVENT) | medio | ⭐⭐⭐ | Generative chemistry |
| [DiffDock](https://github.com/gcorso/diffdock) | alto | ⭐⭐⭐ | Docking SOTA |
| [TDC](https://tdcommons.ai/) | alto | ⭐⭐⭐⭐ | Therapeutics Data Commons. **Benchmarks para validar todo.** |
| [scFoundry](https://github.com/Svvord/scFoundry) | bajo | ⭐⭐ | Single-cell. Menos prioritario para Paraguay inmediato. |
| [scGPT](https://github.com/bowang-lab/scGPT) | alto | ⭐⭐ | Single-cell foundation model |

### §3.5 EHR / Clinical Software (fit Paraguay: ⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [OpenMRS](https://github.com/openmrs/openmrs) | muy alto | ⭐⭐⭐⭐ | **EHR open source #1 en LMIC**. EMR4All variant funciona offline-first en Raspberry Pi. |
| [Bahmni](https://github.com/Bahmni) | alto | ⭐⭐⭐⭐ | OpenMRS-based + imaging + lab + billing. |
| [EMR4All](https://openmrs.org/the-emr4all-journey/) | bajo | ⭐⭐⭐⭐⭐ | **EMR offline-first en Raspberry Pi + OpenMRS**. Nigeria + DRC production. **Directamente relevante para Paraguay rural.** |
| [HealthChain](https://github.com/healthchainai/HealthChain) | bajo | ⭐⭐⭐ | FHIR tools para agents |
| [HasteHealth](https://github.com/HasteHealth/HasteHealth) | bajo | ⭐⭐⭐ | Headless EHR, FHIR R4 |
| [openmed](https://github.com/maziyarpanahi/openmed) | bajo | ⭐⭐⭐ | Local-first NER + PII deidentification. 2,200+ medical models. |
| [odyssey](https://github.com/VectorInstitute/odyssey) | bajo | ⭐⭐⭐ | Interpretable foundation model of patient clinical timeline |
| [Clinical Quality Language](https://github.com/cqframework/clinical_quality_language) | medio | ⭐⭐ | HL7 CQL para CDSS |

### §3.6 ECG / Wearables / Signals (fit Paraguay: ⭐⭐⭐⭐ para D-Heart Chagas)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [ECGFounder](https://github.com/) | — | ⭐⭐⭐⭐⭐ | NEJM AI Nov 2025. **10M+ recordings. Cardiac + coronary function.** |
| [CardioHelp](https://github.com/) | — | ⭐⭐⭐⭐ | Smartphone ECG + AI classifier. LSTM. |
| [D-Heart](https://www.d-heart.com) | — | ⭐⭐⭐⭐ | **Smartphone ECG usado en Bolivia Chaco para Chagas cardiomyopathy**. **Replicable para Paraguay.** |

### §3.7 Dermatology / NTD skin (fit Paraguay: ⭐⭐⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [Derm Foundation](https://developers.google.com/health-ai-developer-foundations) | nuevo | ⭐⭐⭐⭐ | HAI-DEF. Dermatology embeddings. |
| [SkinGPT-4](https://github.com/JoshuaChou2018/SkinGPT-4) | alto | ⭐⭐⭐ | Nature Communications. Dermatology multimodal LLM. |
| [PLOS NTD 2025 leishmaniasis app](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0014313) | — | ⭐⭐⭐⭐⭐ | **POC brasileiro publicado. App offline mobile para leishmaniasis cutánea.** Replicable para Paraguay. |
| [DenseNet121 skin NTD pilot](https://derma.jmir.org/2026/1/e91544) | — | ⭐⭐⭐⭐ | Ethiopian skin NTD pilot, 96.6% accuracy. Replicable. |
| [Yale skin NTD pilot](https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0011230) | — | ⭐⭐⭐⭐ | Côte d'Ivoire + Ghana. Buruli ulcer, leprosy, mycetoma, scabies, yaws. |
| [CBM-NET / Derm Foundation](https://developers.google.com/health-ai-developer-foundations) | — | ⭐⭐⭐⭐ | Ya mencionado. |
| [Derm Foundation](https://developers.google.com/health-ai-developer-foundations) | — | ⭐⭐⭐⭐ | Ya mencionado. |

### §3.8 ASR / Speech / NLP clínico (fit Paraguay: ⭐⭐⭐⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [Whisper](https://github.com/openai/whisper) | muy alto | ⭐⭐⭐⭐⭐ | Ya en repo. **Base para guaraní.** |
| [mfidabel/whisper-guaraní](https://huggingface.co/collections/mfidabel/whisper-guarani) | bajo | ⭐⭐⭐⭐⭐ | **Ya existe baseline guaraní en HF.** Listo para fine-tune médico. |
| [BuzzASR](https://arxiv.org/html/2609.09554) | — | ⭐⭐⭐⭐ | 102 language-specialized Whisper fine-tunes |
| [MedASR](https://huggingface.co/google/medasr) | — | ⭐⭐⭐ | English-only medical. Template para Spanish ASR. |
| [Argot (HIBA)](https://) | — | ⭐⭐⭐⭐ | **NLP clínico en español maduro.** Adopción directa posible. |
| [openmed](https://github.com/maziyarpanahi/openmed) | bajo | ⭐⭐⭐ | Clinical NER + PII deidentification local-first |

### §3.9 Health Acoustics / Cough (fit Paraguay: ⭐⭐⭐⭐⭐)

| Proyecto | Stars | Fit | Notas |
|---|---|---|---|
| [HeAR](https://huggingface.co/google/hear) | — | ⭐⭐⭐⭐⭐ | **HAI-DEF. 300M audio clips. SOTA health acoustics.** Ya en repo. |
| [XarpAi Lung Opacity Detector](https://github.com/vbookshelf/XarpAi-Lung-Opacity-Detector) | bajo | ⭐⭐⭐⭐ | **MIT-licensed CXR opacity detector for TB + pneumonia.** Runs on CPU. POC open. |

### §3.10 Tuberculosis-specific (fit Paraguay: ⭐⭐⭐⭐⭐)

| Proyecto | URL | Fit | Notas |
|---|---|---|---|
| **XarpAi** | [github.com/vbookshelf/XarpAi-Lung-Opacity-Detector](https://github.com/vbookshelf/XarpAi-Lung-Opacity-Detector) | ⭐⭐⭐⭐⭐ | **MIT-licensed CXR opacity detector for TB + pneumonia.** Runs on CPU. POC open. Directamente replicable. |
| **EPCON TB Hotspots** | [epcon.ai/post/using-ai-for-low-data-areas-finding-tb-hotspots-in-bangui](https://www.epcon.ai/post/using-ai-for-low-data-areas-finding-tb-hotspots-in-bangui) | ⭐⭐⭐⭐ | Bayesian inference para TB hotspots en CAR. Paper presentado en Union World Conference. |
| **Health Telematics HTI** | [infpneumologie.impfstudien.org](https://infpneumologie.impfstudien.org/research-groups/zoller-lab/health-telematics-infrastructure/) | ⭐⭐⭐⭐ | Open source TB/HIV telematics Tanzania. Bajo ancho de banda, SMS. Replicable para Paraguay. |

### §3.11 Snake/scorpion envenoming + rural emergency (fit Paraguay: ⭐⭐⭐⭐)

**Hallazgo crítico:** Paraguay tiene 1,383 casos de envenenamiento por escorpión reportados (mid-2022 a mid-2023), 41 moderados/severos, 4 muertes pediátricas. La región del Chaco es endémica para *Tityus confluens*. NO hay POC específico pero sí herramientas adyacentes:

- [BMJ Snakebite review](https://www.bmj.com/content/376/bmj-2020-057926) — guidelines clínicos
- [Panregional antivenom paper (PMC11619490)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11619490/) — contexto regional
- **Gap identificado:** no existe POC de IA open-source para envenenamiento por escorpión/serpiente. **Oportunidad para Paraguay ser primero.**

### §3.12 Genomic data equity (fit Paraguay: ⭐⭐⭐⭐)

- [Annual Reviews — Inequalities and Inclusion in Genomics Applied to Healthcare: A Latin American Perspective](https://www.annualreviews.org/content/journals/10.1146/annurev-genom-111224-100329) — diagnóstico del gap LatAm
- [BIPMed](https://bipmed.org/) — Brazilian Initiative on Precision Medicine
- [ClinGen JEDI Action Plan v2.1](https://clinicalgenome.org/site/assets/files/7569/clingen_jedi_action_plan_v2_1.pdf) — Diversity, Equity, Inclusion plan
- [Genomics England Diverse Data](https://www.genomicsengland.co.uk/initiatives/diverse-data) — modelo a借鉴
- **Gap:** no existe biobanco open paraguayo. CEDIC × Galatea Bio es la oportunidad.

---

## §4 — Gaps observados: lo que nadie está haciendo bien

De toda la research, estos son los vacíos que Paraguay podría llenar como **first mover**:

### §4.1 Gaps de datos

- ❌ **No existe corpus clínico en español paraguayo** para fine-tuning de LLMs médicos.
- ❌ **No existe dataset abierto de toses paraguayas** etiquetadas con TB status.
- ❌ **No existe biobanco genómico abierto FAIR-aligned** con datos paraguayos.
- ❌ **No existe dataset abierto de radiografías de tórax** paraguayas.

### §4.2 Gaps de modelo

- ❌ **No existe LLM médico fine-tuneado en español paraguayo**.
- ❌ **No existe Whisper fine-tuneado en guaraní médico**.
- ❌ **No existe foundation model ECG** específicamente entrenado en Chagas cardiomyopathy.
- ❌ **No existe modelo AI específico para envenenamiento escorpión** (gap regional).

### §4.3 Gaps regulatorios

- ❌ **No existe framework regulatorio** de IA clínica en Paraguay (ni en LatAm en general). Oportunidad para ser primero.
- ❌ **No existe pathway de prequalificación** de IA médica en Paraguay (PAHO tiene uno nuevo para TB CAD).

### §4.4 Gaps de implementación

- ❌ **No existe red multi-hospital de IA** en Paraguay (Hospital de Clínicas + INCAN + Hospital General de Barrio Obero).
- ❌ **No existe programa de Telemedicina con IA** en zonas rurales chaqueñas (Resolución 367/2020 lo endosa pero no hay deployment).
- ❌ **No existe EHR con AI assistant** en Paraguay (Bahmni + EMR4All podrían ser el blueprint).

### §4.5 Gaps de comunidad

- ❌ **No existe SoIBio / AB3C chapter paraguayo** (sí hay en Brasil y Argentina).
- ❌ **No existe red regional LatAm de AI en salud** (aunque CUIDA Chagas existe, no incluye AI).
- ❌ **No existe programa de intercambio IICS-HIBA** (Argentina-Paraguay en IA clínica).

---

## §5 — Partnerships recomendados

Basado en el análisis, estos son los partnerships con mayor leverage:

### §5.1 Tier 1 — Partnerships estratégicos

| Partner | Razón | Contacto | Acción |
|---|---|---|---|
| **Hospital Italiano de Buenos Aires (HIBA)** | Modelo regional más cercano. 27 años en informática en salud. Programa pIASHIBA maduro. Mismo idioma. | DIS-HIBA, Argentina | Partnership técnico sobre Argot + TANA + TRx. Visita técnica. |
| **CABANA** (capacity building LatAm bioinformatics) | Ofrece workshops 2-week gratis. Entrena residentes en nf-core, Galaxy. | [cabanaproject.org](https://www.cabana.online) | Solicitar workshop Paraguay. |
| **SoIBio / AB3C** | Redes regionales de bioinformática. Argentina y Brasil tienen capítulos activos. Paraguay no. | SoIBio.org | Crear capítulo Paraguay. |
| **AI4Med / MedGemma team (Google)** | Mantenedores de MedGemma, TxGemma, HeAR. | developers.google.com/health-ai-developer-foundations | Aplicar a HAI-DEF partner program. |
| **NVIDIA BioNeMo team** | Mantenedores de NIM microservices. Free tier para prototyping. | build.nvidia.com | Solicitar research access. |

### §5.2 Tier 2 — Partnerships regionales

| Partner | Razón | Acción |
|---|---|---|
| **Stanford / Galatea Bio** | Ya trabaja con CEDIC. Biobanco abierto potencial. | Continuar conversación CEDIC × Galatea. |
| **Fiocruz (Brasil)** | Galatea Bio es spinout Stanford; Fiocruz trabaja con Brasil/Caribe. | Explorar conexión Paraguay-Brasil. |
| **NIH Fogarty** | LMIC research training grants. | Aplicar a convocatoria LMIC. |
| **Chan Zuckerberg Initiative EOSS** | Open-source science tooling grants. | Aplicar ($100k). |
| **Wellcome Trust** | LMIC-led research. | Aplicar a Discovery Awards. |

### §5.3 Tier 3 — Partnerships de capacity building

| Partner | Razón |
|---|---|
| **CABANA** | Workshops bioinformatics para CONAREM |
| **OpenMRS community** | EMR4All setup Paraguay rural |
| **Galaxy Training Network** | Galaxy instance para IICS + Hospital de Clínicas |
| **OHIF community** | Pathology + radiology viewer setup para INCAN |
| **MIT Jameel Clinic (Boltz team)** | Boltz-2 training para Tesabio + CEDIC |

---

## §6 — Lo que Paraguay puede construir sobre hombros de gigantes

### §6.1 El plan "build on giants"

En lugar de inventar desde cero, Paraguay puede **adaptar proyectos validados**:

**Drug discovery pipeline:**
- Adaptar Boltz-2 + TxGemma-Chat workflow para Chagas (modelo: cualquier paper reciente con Boltz)
- Usar TDC para benchmarks (ya validados)
- Aplicar a convocatoria 2026 FAPESP-CONACYT AMR

**TB screening:**
- Replicar [EPCON TB Hotspots](https://www.epcon.ai/post/using-ai-for-low-data-areas-finding-tb-hotspots-in-bangui) en Paraguay (Bayesian inference para hotspots)
- Replicar [XarpAi](https://github.com/vbookshelf/XarpAi-Lung-Opacity-Detector) para CXR TB (MIT license, runs on CPU)
- Adaptar [Health Telematics HTI](https://infpneumologie.impfstudien.org/research-groups/zoller-lab/health-telematics-infrastructure/) para SMS-based TB/HIV en Chaco

**Clinical NLP:**
- Fine-tunear MedGemma 4B sobre corpus español paraguayo (HAI-DEF license)
- Usar OpenMedLM prompting como baseline barato antes de fine-tune caro
- Adaptar TANA de Hospital Italiano como blueprint para chatbot clínico del Hospital de Clínicas

**Pathology:**
- Replicar INCAN con MedRAX + Path Foundation + CONCH pipeline
- Usar [TIA Toolbox](https://github.com/TissueImageAnalytics/tiatoolbox) para whole-slide processing
- MONAI para pre-processing de imágenes médicas

**EHR + Hospital AI:**
- EMR4All (OpenMRS en Raspberry Pi offline) para Hospital General de Barrio Obero + SENEPA
- Argot de HIBA para procesamiento de notas clínicas
- TANA de HIBA como blueprint para Hospital de Clínicas

**Dermatology / NTD:**
- Replicar paper brasileño PLOS NTD 2025 para leishmaniasis cutánea
- Replicar paper etíope para skin NTD app en Chaco
- Adaptar Derm Foundation (HAI-DEF) para teledermatología rural

**ASR / Speech:**
- Whisper fine-tune guaraní médico (base ya existe)
- Adaptar Argot de HIBA para procesamiento de notas

**Snake/scorpion envenoming (gap único):**
- **Ser PRIMERO** en crear POC open-source de IA para envenenamiento escorpión/serpiente en LatAm
- Usar snake ID model (snake-specific, no LatAm-specific)
- Conectar con SENEPA + Hospital de Clínicas Toxicología

### §6.2 El "stack Paraguay" — combinación óptima

Para Paraguay, el stack ideal es:

```
Layer A: Genómica + Drug discovery
   ├─ Boltz-2 (MIT, comercial) — estructura + afinidad
   ├─ OpenFold3 (Apache 2.0) — estructura comercial
   ├─ AlphaFold 3 (académico) — pesos no comerciales
   ├─ TxGemma-Chat 9B (Gemma terms) — queries terapéuticas
   ├─ TDC (open) — benchmarks
   └─ LigandMPNN (open) — inverse folding

Layer B: Clinical NLP
   ├─ MedGemma 4B (HAI-DEF) — base
   ├─ MedSigLIP (HAI-DEF) — visión
   ├─ OpenMedLM Yi 34B (Apache 2.0) — baseline prompting
   └─ Argot de HIBA — NLP clínico español (modelo a借鉴)

Layer C: Imaging / Pathology
   ├─ Path Foundation (HAI-DEF) — embeddings
   ├─ CONCH (research use) — vision-language
   ├─ MedSAM2 (MIT) — segmentación
   ├─ MONAI (Apache 2.0) — framework
   ├─ TIA Toolbox (BSD-3) — whole-slide
   └─ CXR Foundation / Derm Foundation (HAI-DEF) — radiology/dermatology

Layer D: Audio / Speech
   ├─ HeAR (HAI-DEF) — health acoustics
   ├─ Whisper guaraní (mfidabel base, MIT) — ASR guaraní
   └─ BuzzASR — 102 language Whisper fine-tunes

Layer E: ECG / Wearables
   ├─ ECGFounder (NEJM AI) — universal ECG FM
   └─ D-Heart (commercial, Bolivia Chagas pilot) — smartphone ECG

Layer F: Infrastructure
   ├─ HIVE BUZZ GPU cluster (Asunción)
   ├─ X8 Cloud (when live)
   ├─ NVIDIA BioNeMo NIMs (free for prototyping)
   ├─ LangGraph (Apache 2.0) — agentic orchestration
   └─ MedSci Agent (MIT) — multi-agent biomedical

Layer G: EHR + Hospital IT
   ├─ EMR4All / OpenMRS + Bahmni (offline-first)
   ├─ Argot de HIBA — NLP clínico
   └─ FHIR R4 + HealthChain SDK

Layer H: Genomics Data Equity
   ├─ CEDIC × Galatea Bio biobank
   ├─ AlphaGenome API (variant interpretation)
   └─ BIPMed-style data sharing
```

### §6.3 Tres "firsts" que Paraguay podría reclamar

1. **First Paraguayan Spanish medical LLM fine-tuneado** — nadie lo ha hecho todavía
2. **First scorpion envenoming AI POC** en LatAm (gap regional)
3. **First TB cough screening app en Paraguay** (basado en HeAR + COUGHVID)

---

## §7 — Resumen ejecutivo

### §7.1 Lo que ya existe (no reinventar)

- **Boltz-2 + TxGemma + OpenFold3 + LigandMPNN** = pipeline completo para Chagas drug discovery, ya validado en otras enfermedades
- **HeAR + Whisper guaraní + EMR4All** = stack completo para TB screening rural
- **MedGemma + MedSigLIP + OpenMedLM** = stack para clinical NLP en español paraguayo
- **Path Foundation + CONCH + MedSAM** = stack para patología digital
- **ECGFounder + D-Heart** = stack para Chagas cardiomyopathy screening
- **OpenMRS + EMR4All + Argot** = stack para EHR + IA clínica

### §7.2 Lo que Paraguay debe construir

1. **Dataset local de toses TB** + validación HeAR (gap en Paraguay)
2. **Corpus de notas clínicas en español paraguayo** + fine-tune MedGemma (gap LatAm)
3. **POC de envenenamiento escorpión** (gap regional único)
4. **Framework regulatorio IA clínica** (oportunidad LatAm-wide)
5. **Biobanco FAIR paraguayo** (CEDIC × Galatea Bio lead)
6. **Programa de capacitación CONAREM** (multiplicador)
7. **Capítulo Paraguay de SoIBio/AB3C** (network effect)

### §7.3 Tres partnerships críticos

1. **Hospital Italiano (HIBA/Argentina)** — modelo regional más cercano, mismo idioma
2. **Google Health AI Dev Foundations team** — soporte oficial para MedGemma + TxGemma + HeAR
3. **NVIDIA BioNeMo team** — compute y NIM microservices

### §7.4 El principio guía

**"Stand on the shoulders of giants"** — Paraguay no necesita inventar modelos nuevos. Necesita **adaptar modelos open-source validados** a su contexto único (español paraguayo, guaraní, Chagas, TB, dengue, leishmaniasis) y **crear los datasets locales** que faltan. La infraestructura técnica ya existe. Lo que falta es: datos paraguayos, capacidad local, partnerships, y un marco regulatorio.

---

## Última actualización

Septiembre 2026.