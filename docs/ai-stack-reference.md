# Stack de IA de código abierto para investigación médica — referencia consolidada

Documento de referencia principal. Cubre toda la pila abierta de IA aplicable a las 8 áreas de investigación del repositorio. Última actualización: septiembre 2026.

> Esta no es una recomendación única. Es un catálogo con licencias verificadas, usos prácticos para Paraguay, y notas honestas sobre brechas. Cada proyecto del repo debería poder leer este documento y elegir su stack.

---

## Cómo leer este documento

Por **problema que resuelve** (no por herramienta):

- §1 — Genómica y estructura de proteínas
- §2 — Química y descubrimiento de fármacos
- §3 — LLMs clínicos y médicos
- §4 — Modelos fundacionales de patología
- §5 — Radiología e imágenes médicas
- §6 — Biología unicelular
- §7 — Agentes de IA para ciencia
- §8 — Capa de infraestructura (NVIDIA BioNeMo)
- §9 — Cómo encaja todo en Paraguay (stacks recomendados por área)
- §10 — Tabla maestra de licencias
- §11 — Brechas honestas
- §12 — Tres recomendaciones principales

---

## §1. Genómica y estructura de proteínas

### AlphaFold 3 (DeepMind)

- **Versión actual:** v3.0.4 (julio 2025).
- **Código:** Apache 2.0 desde v3.0.3 (junio 2025).
- **Pesos:** uso **no comercial** únicamente. Solo universidades, ONGs, institutos de investigación, gobierno, periodismo. No se puede usar para investigación en nombre de organizaciones comerciales.
- **Qué hace:** predice estructuras de complejos biomoleculares — proteínas, ADN, ARN, ligandos, iones. Naturaleza 2024 (Abramson et al.).
- **Apto para Paraguay:** sí, para uso académico/oficial (IICS, CEDIC, universidades). Útil para predecir estructuras de enzimas de *T. cruzi*, dianas de *Leishmania*, NS1 de dengue.
- **Limitación clave:** si Tesabio o cualquier empresa local quiere comercialización, **no puede usar AF3 directamente** — debe usar Boltz-2 o Chai-1.
- **Repo:** [github.com/google-deepmind/alphafold3](https://github.com/google-deepmind/alphafold3)
- **Servidor:** [alphafoldserver.com](https://alphafoldserver.com) (uso no comercial, set limitado de ligandos)
- **Releases:** v3.0.0 (nov 2024), v3.0.1 (ene 2025), v3.0.2 (abr 2025), v3.0.3 (jun 2025), v3.0.4 (jul 2025). v3.0.4 corre en CPU-only y Apple Silicon.

### Boltz-1 y Boltz-2 (MIT Jameel Clinic)

- **Licencia:** **MIT**. Modelo + pesos + código de entrenamiento + datos. **Comercial OK.**
- **Boltz-1** (noviembre 2024): estructura AF3-clase, totalmente abierto. Usado por miles de laboratorios académicos, biotechs y las20 mayores farmacéuticas.
- **Boltz-2** (9 junio 2025): primer modelo DL en acercarse a la precisión FEP (free-energy perturbation) para afinidad de unión, **1000× más rápido**. Pearson r=0.62 en FEP+ benchmark vs OpenFE; superó todos los métodos CASP16 affinity en140 complejos; duplicó average precision en MF-PCBA.
- **Nuevo en Boltz-2:**
  - Módulo de afinidad (predice fuerza de unión proteína-ligando).
  - Condicionamiento por método experimental.
  - Restricciones de distancia.
  - Integración de plantillas multi-cadena.
  - Optimizaciones GPU + datos sintéticos + MD.
  - **Boltz-Steering** — cues físicas para refinar estructuras.
- **Apto para Paraguay:** **modelo por defecto para drug discovery.** CEDIC + BioProsNat + Tesabio deberían estandarizar en este. Único AF3-clase con licencia verdaderamente abierta para downstream comercial.
- **Co-autores destacados:** Saro Passaro, Gabriele Corso, Jeremy Wohlwend (MIT CSAIL + MIT Jameel Clinic); en colaboración con Recursion; co-autores adicionales Regina Barzilay, Tommi Jaakkola.
- **Recursos GPU:** NERSC GenAI@NERSC.
- **Repos:** [github.com/jwohlwend/boltz](https://github.com/jwohlwend/boltz), [boltz.bio/boltz2](https://boltz.bio/boltz2)

### Chai-1 y Chai-2 (Chai Discovery)

- **Licencia:** Apache 2.0, comercial OK.
- **Chai-1:** predictor de estructura AF3-clase.
- **Chai-2:** pivotando hacia diseño de anticuerpos. Reportadamente competitivo con Boltz en binders.
- **Apto para Paraguay:** buen respaldo si Boltz tiene issues de inferencia. Validación cruzada con Boltz-2 para dianas críticas.
- **Repo:** [github.com/chaidiscovery/chai-lab](https://github.com/chaidiscovery/chai-lab)

### ESM-3 (EvolutionaryScale → Chan Zuckerberg Biohub)

- **Adquirido por CZ Biohub en noviembre 2025.**
- **Arquitectura:** LM generativo multimodal sobre **secuencia + estructura 3D + función** en un solo modelo. Entrenado en 2.78B proteínas.
- **Tres tamaños:**
  - **1.4B** (esm3_sm_open_v1) — pesos abiertos en HuggingFace + GitHub.
  - **7B** — API only (BioNeMo).
  - **98B** (esm3-large-2024-03) — API only (BioNeMo + AWS SageMaker).
- **Licencia:** **Cambrian Non-Commercial License** para el open 1.4B. Biosecurity mitigations: secuencias virales removidas, USDA Select Agents excluidas, function decoder keyword-filtered. Atribución "Built with ESM" requerida.
- **Resultado destacado (Science, enero 2025):** **esmGFP** — proteína fluorescente verde *de novo* a ~58% identidad de secuencia con GFPs naturales, descrito como "simulación de ~500M años de evolución."
- **Familia relacionada:** ESM C (Cambrian) — modelos de representación (no generativos) en300M/600M/6B. 300M/600M pesos abiertos.
- **Apto para Paraguay:** ideal para **diseño de novo de proteínas** (e.g., diseñar binders para antígenos de *T. cruzi*). El 1.4B corre en una sola GPU.
- **Repos:** [github.com/evolutionaryscale/esm](https://github.com/evolutionaryscale/esm)

### AlphaGenome (DeepMind)

- **Released:** 25 junio 2025. **Naturaleza:** enero 2026 (Avsec et al.).
- **Qué hace:** toma **1 Mb de ADN**, predice miles de propiedades regulatorias a resolución de pares de bases: expresión génica, splicing, accesibilidad de cromatina, modificaciones de histonas, unión de factores de transcripción, mapas de contacto de cromatina.
- **Rendimiento:** 22/24 en predicciones de secuencia, 24/26 en efectos de variantes vs SOTA externos. Único modelo que predice todas las modalidades conjuntamente.
- **API:** gratis para uso **no comercial** vía [deepmind.google/science/alphagenome](https://deepmind.google/science/alphagenome). Tasa variable según demanda, adecuada para ≤1M predicciones.
- **Companion: AlphaGenome Atlas** — predicciones precomputadas para **9 mil millones de variantes de nucleótido único** posibles en el genoma humano. Accesible vía navegador o agente de IA.
- **Sin pesos públicos:** API only, código en [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome).
- **Apto para Paraguay:** enorme para el trabajo CEDIC × Galatea Bio. Permite priorizar variantes funcionales en cohortes paraguayos. Caso de uso: identificar variantes regulatorias que afecten respuesta a *T. cruzi*, predisposición a cáncer hereditario, o susceptibilidad a Chagas.

### Nucleotide Transformer (InstaDeep)

- **Licencia:** Apache 2.0. Cuatro variantes (decenas de millones a multi-mil millones de parámetros).
- **Qué hace:** preentrenado en miles de genomas multi-especie; representaciones de secuencia igualan o superan métodos especializados en 12/18 tareas downstream.
- **Repo:** [github.com/instadeepai/nucleotide-transformer](https://github.com/instadeepai/nucleotide-transformer)

### HyenaDNA, Caduceus, Evo (modelos de lenguaje genómicos)

- **HyenaDNA** (NeurIPS 2023): modelado de secuencia genómica de largo alcance, contexto hasta 1M tokens, **160× más rápido que transformers** a esa longitud.
- **Caduceus:** FM de ADN bidireccional usando modelos de espacio de estado.
- **Evo** (Arc Institute / Stanford, Science 2024): **7B parámetros FM genómico**, contexto131k tokens, arquitectura híbrida. Genera ADN a escala de genoma completo.
- **Evo 2:** sucesor, aún más grande.
- **Apto para Paraguay:** herramientas de investigación; relevantes si LCSP quiere caracterizar genomas de patógenos más allá del variant calling (e.g., elementos regulatorios en genoma de dengue).
- **Otros relevantes:**
  - **GENA-LM** — LM especializado en ADN
  - **DNABERT-2** — BERT para ADN
  - **JanusDNA** (2025) — bi-directional hybrid DNA FM
  - **NTv3** (2025) — extensión de Nucleotide Transformer

### LigandMPNN y ProteinMPNN (Baker lab, IPD UW)

- **LigandMPNN** publicado en Nature Methods, marzo 2025.
- **Qué hace LigandMPNN:** inverse folding *dado contexto de ligando*. Sequence recovery cerca de moléculas pequeñas **63.3%** (vs 50.4% Rosetta, 50.4% ProteinMPNN); cerca de nucleótidos **50.5%**; cerca de metales **77.5%**.
- **Resultado destacado:** LigandMPNN aumentó la afinidad de unión de cholic acid **100×** vs complejo diseñado.
- **Apto para Paraguay:** complemento perfecto de Boltz-2. Usa Boltz-2 para predecir el complejo proteína+ligando, luego LigandMPNN para diseñar secuencia que estabilice la interfaz. Loop AI end-to-end.
- **Repos:** [github.com/dauparas/LigandMPNN](https://github.com/dauparas/LigandMPNN), [github.com/dauparas/ProteinMPNN](https://github.com/dauparas/ProteinMPNN)

### Otras herramientas de diseño de proteínas

- **RFdiffusion** (Baker lab) — generación de backbone de novo. [github.com/RosettaCommons/RFdiffusion](https://github.com/RosettaCommons/RFdiffusion)
- **Chroma** (Generate Biomedicines) — modelo generativo de proteínas
- **AlphaDesign** — usa AlphaFold como motor de diseño (paper 2025)
- **FrameDiff**, **Genie/Genie2** — otros modelos generativos
- **EVEscape** (OATML) — predicción de escape inmune viral

---

## §2. Química y descubrimiento de fármacos

### ChemBERTa-3 (ecosistema DeepChem)

- **Publicado:** Digital Discovery, enero 2026.
- **Licencia:** código abierto en DeepChem; artículo bajo CC BY-NC.
- **Qué hace:** infraestructura unificada y reproducible para entrenar y comparar modelos fundacionales químicos en tareas MoleculeNet. Pesos abiertos, configuraciones de entrenamiento, workflows de despliegue.
- **Arquitecturas benchmarkeadas:** ChemBERTa, MoLFormer, GROVER, InfoGraph, InfoMax3D.
- **Apto para Paraguay:** si BioProsNat quiere entrenar modelos custom en productos naturales paraguayos, ChemBERTa-3 es el stack de entrenamiento abierto.
- **Repo:** [github.com/deepchem/deepchem](https://github.com/deepchem/deepchem) (6k+ stars)

### TDC (Therapeutics Data Commons)

- **Qué es:** datasets benchmark para AI drug discovery (ADMET, binding, efficacy, toxicity).
- **Apto para Paraguay:** evaluación estandarizada para cualquier modelo que CEDIC/BioProsNat/Tesabio construya. Sin TDC, no se pueden comparar resultados honestamente.
- **Site:** [tdcommons.ai](https://tdcommons.ai/)

### Otras herramientas químicas

- **RDKit** ([github.com/rdkit/rdkit](https://github.com/rdkit/rdkit)) — navaja suiza de cheminformatics
- **OpenFF + OpenFE** — pipelines FEP abiertos (el gold standard contra el que Boltz-2 se compara)
- **REINVENT4** — química generativa
- **DiffDock** — docking molecular basado en difusión (MIT)
- **MegaMolBART**, **Chemformer** — transformers generativos de moléculas
- **MolGPT, GraphAF** — modelos generativos
- **TorchDrug** — framework PyTorch para drug discovery
- **MoleculeNet** — suite de benchmarks

---

## §3. LLMs clínicos y médicos

### MedGemma (Google Health AI Developer Foundations)

- **Released:** mayo 2025 (4B + 27B text), julio 2025 (27B multimodal update).
- **Arquitectura:** Gemma 3 (4B o 27B), encoder visual = SigLIP 400M fine-tuneado médicamente.
- **Licencia:** wrapper en **Apache 2.0**; pesos bajo **Health AI Dev Foundations License** (uso permisivo, no rebranding, hay use-restriction policy). **Gratis para investigación y comercial**.
- **Rendimiento:**
  - **MedGemma 4B multimodal:** 64.4% en MedQA.
  - **MedGemma 27B text:** 87.7% en MedQA (a 3 puntos de DeepSeek R1, ~10% del costo de inferencia).
  - **81%** de informes de rayos X de MedGemma 4B juzgados por radiólogo certificado como suficientemente precisos para manejo similar al original.
  - 2.6–10% mejora en medical multimodal QA out-of-distribution.
  - 15.5–18.1% mejora en clasificación de hallazgos de rayos X.
  - 50% reducción de errores en retrieval de EHR tras fine-tuning.
- **Componentes:**
  - **MedGemma 4B** (multimodal)
  - **MedGemma 27B text**
  - **MedGemma 27B multimodal** (julio 2025)
  - **MedGemma 1.5 4B** — actualización con mejor procesamiento de documentos médicos y EHR
  - **MedSigLIP** — encoder visual médico standalone
- **Apto para Paraguay:** **el modelo de mayor fit para deployment hospitalario**. Fine-tuneable en una sola GPU. Base español-capaz. **Este es el modelo para fine-tunear en notas clínicas paraguayas.**
- **Repos:** [github.com/google-health/medgemma](https://github.com/google-health/medgemma), [HF collection](https://huggingface.co/collections/google/medgemma)
- **Paper técnico:** arxiv:2507.05201 (julio 2025)
- **HF Dev license terms:** [developers.google.com/health-ai-developer-foundations/terms](https://developers.google.com/health-ai-developer-foundations/terms)

### OpenMedLM (Yi 34B prompting)

- **Logros:** **72.6%** en MedQA, **81.7%** en MMLU medical subset — primer LLM abierto en romper80% en MMLU médico, **sin fine-tuning, solo prompting**. Superó Med-PaLM (540B) en MedQA.
- **Implicaciones:** **prompting puede igualar fine-tuning**. Para Paraguay: un LLM general bien prompted (Yi 34B, Llama 3, Mistral) puede ser suficientemente bueno para muchas tareas clínicas de NLP, sin costoso fine-tune médico.
- **Apto para Paraguay:** RAG sobre guías clínicas paraguayas + Yi-34B bien prompted podría superar un small fine-tune. Barato para arrancar.

### Meditron (Chen et al.)

- **Qué hace:** Llama 2 70B fine-tuneado en corpus médico. Top open medical LLM pre-MedGemma.
- **Apto para Paraguay:** fallback si MedGemma licensing no encaja.

### RadFM (Radiology Foundation Model)

- **Publicado:** Nature Communications, 2025.
- **Qué hace:** **primer FM que soporta radiología 2D + 3D** (rayos X, CT, MRI, PET) + texto interleaved. Preentrenado en 16M scans (MedMD), fine-tuneado en 3M scans radiológicos (RadMD). Maneja multi-imagen, multi-modalidad.
- **Apto para Paraguay:** relevante si Paraguay digitaliza radiología (INCAN aún no). Largo plazo.

### LLaVA-Med, Med-Flamingo, BiomedCLIP

- **LLaVA-Med** — asistente multimodal médico temprano; baseline ampliamente usado.
- **Med-Flamingo** — few-shot multimodal médico.
- **BiomedCLIP** — vision-language contrastivo sobre 15M pares imagen-texto de PMC. **Mejor retrieval zero-shot para imágenes médicas.**
- **Apto para Paraguay:** BiomedCLIP para estandarizar image retrieval / zero-shot classification; LLaVA-Med si se necesita image+text generation.

### Otros medical LLMs

- **BioMistral** — Mistral fine-tune, 7B
- **Asclepius** — medical LLM reciente
- **MedLM** (Google) — cerrado
- **Med-PaLM / Med-PaLM 2** (Google) — cerrado, benchmark setter
- **MAIRA-2** (Microsoft) — generación de informes radiológicos, MSRLA (research only)
- **RadVLM** — alternativa abierta para radiología

---

## §4. Modelos fundacionales de patología

El área más densa y de mayor movimiento (2024–2025). El benchmark Nature Biomedical Engineering 2025 de **19 modelos sobre 6,818 pacientes** estableció el campo.

| Modelo | Top en | Notas |
|---|---|---|
| **CONCH** | Top general (AUROC) | Vision-language, Mahmood Lab (Harvard/BWH). 1.17M pares imagen-texto. |
| **Virchow2** | Cerca 2° general | Vision-only, Paige + Microsoft, 3.1M slides, ViT-H/632M. Aug 2024. |
| **UNI2-h** | Mejor en low-data | Mahmood Lab, enero 2025, ViT-H/681M. |
| **H-optimus-0/1** | Mejor para staining shifts | Bioptimus, ViT-giant/1.1B, 500K+ WSIs. Robusto PLISM. |
| **PathOrchestra** | Mejor cross-task | Shanghai AI Lab, marzo 2025, ViT-L/304M. 112 tareas. |
| **KEEP** | Conocimiento estructurado | Shanghai AI Lab + SJTU, enero 2026. Grafo de 11,454 enfermedades + 139,143 atributos. |
| **TITAN** | Slide-level FM | Construido sobre CONCH1.5. |
| **mSTAR** | Multimodal | Smart Lab, julio 2024. |
| **GPFM** | General pathology | Smart Lab, julio 2024. |
| **Midnight** | Repro abierta de modelos propietarios | MedARC / Sophont. ViT-G/14, ~12K WSIs de TCGA por **~$1.6k**. |
| **OpenMidnight** | Midnight totalmente abierta | Mismo approach, totalmente reproducible. |
| **CHIEF** | WSI | Wang et al., Nature 2024. |
| **Prov-GigaPath** | WSI | Xu et al., Nature 2024. |
| **Kaiko** | ViT tile encoders | kaiko.ai, DINO/DINOv2 sobre TCGA. |
| **ATLAS** | 1.2M WSIs | Mayo + Charité, enero 2025. |
| **Phikon** | ViT | Mahmood Lab, basado en iBOT. |
| **Hibou-B/-L** | Hibou family | Variantes para pathology. |

### Dónde empezar (Paraguay)

- **CONCH** para tareas generales de patología (top benchmark).
- **MedSAM** (MIT, [github.com/bowang-lab/MedSAM](https://github.com/bowang-lab/MedSAM)) para segmentación.
- **Midnight / OpenMidnight** si se quiere entrenar desde cero con datos paraguayos (la receta funciona con 12K WSIs).

### Repos curados

- [github.com/georg-wolflein/pathology-foundation-models](https://github.com/georg-wolflein/pathology-foundation-models)
- [github.com/dibalokechanda/PFMs](https://github.com/dibalokechanda/PFMs)

---

## §5. Radiología e imágenes médicas

- **MedSAM** — segmentación universal médica, MIT, funciona en CT/MRI/rayos X/ultrasonido
- **BiomedCLIP** — retrieval, zero-shot classification
- **CheXagent** (Stanford AIMI) — FM de rayos X de tórax, top en clasificación
- **RAD-DINO** (Stanford) — self-supervised, top para segmentación
- **RADFM** — ver §3
- **MAIRA-2** (Microsoft) — generación de informes radiológicos, MSRLA (research only)
- **Path Foundation** (Google) — encoder visual usable en radiología
- **VISTA-3D** (NVIDIA BioNeMo) — segmentación de imagen médica
- **LLaVA-Rad** — extensión para radiología
- **MedFlamingo** — few-shot multimodal médico

---

## §6. Biología unicelular

Ecosistema sorprendentemente profundo en 2025–2026.

### Modelos

- **scGPT** (Wang lab) — preentrenamiento generativo en33M células humanas; checkpoint whole-human.
- **Geneformer** (Theodoris) — V1, V2-104M, V2-104M_CLcancer, V2-316M.
- **scFoundation** — preentrenamiento a gran escala.
- **scBERT** — estilo BERT sobre scRNA-seq.
- **UCE** (Universal Cell Embedding) — 33K genes, 36M células.
- **LangCell** — embeddings de células alineados con lenguaje.
- **SCimilarity** — búsqueda cross-atlas scRNA-seq.
- **CellFM, Cell2Sentence, scCello, CellPLM, GenePT, scPRINT, CellPLM** — todos 2024–2025.
- **TESLA** — single-cell.

### Frameworks

- **scFoundry** (agosto 2026) — **el recomendado**. Framework Nextflow unificado. Un solo comando corre 15+ modelos en containers pinned. Incluye transfer, finetune, benchmark, geometry probes. Funciona en workstation o HPC.
- **scPEFT** — parameter-efficient fine-tuning sobre scGPT/scBERT/scFoundation/Geneformer.
- **scFM-Bench** (Microsoft) — framework de evaluación zero-shot.
- **nano-Geneformer**, **nano-scGPT** — reimplementaciones PyTorch mínimas para inferencia rápida.

### Por qué importa para Paraguay

IICS/CEDIC no tienen trabajo single-cell actualmente. Si se quiere añadir: **scFoundry + Geneformer es el camino de menor fricción**. Podría ser un proyecto de entrenamiento cruzado con el área 8 (capacitación médica).

---

## §7. Agentes de IA para ciencia

### Frameworks

- **NVIDIA BioNeMo Agent Toolkit** — el más relevante para biología.
  - Open-source (CC BY 4.0).
  - Skills para protein folding, docking, química generativa, genómica, drug design, biomarker discovery.
  - Se conecta con Claude, Codex, cualquier runtime de agente.
  - NVIDIA reporta: agentes sin skills completan 57% de tareas, con skills 100%.
  - Cada skill = SKILL.md + scripts, instalable con `npx skills add NVIDIA-BioNeMo/bionemo-agent-toolkit`.
  - Bajo el capó: NVIDIA NIM microservices (gratis para prototyping, cap 40 RPM).
  - Agent-agnostic.
- **LangGraph** — framework basado en grafos de LangChain; usado por BioMedTools.
- **AutoGen** (Microsoft) — conversaciones multi-agente.
- **CrewAI, OpenAgents, MetaGPT, AgentVerse** — general-purpose.
- **ChemCrow** (Bran et al., Nat Mach Intell 2024) — LLM + 18 herramientas químicas incluyendo RDKit, PubChem, retrosynthesis, robotic synthesis. **Primer chem AI agent.** Pero dormido desde diciembre 2024.
- **Robin** (FutureHouse) — orquestación end-to-end de drug discovery.
- **BioMedTools** — agente AI biomédico basado en Qwen3-32B + LangGraph.
- **Virtual Lab** (Stanford) — diseño de nanobodies, publicado en Nature.

### Agentes "AI Scientist" específicos de ciencia

- **Sakana AI Scientist v2** — producción totalmente automatizada de papers, ~$15/paper. Primer paper AI-generado aceptado en ICLR 2025 workshop. **Dormido desde diciembre 2025.**
- **Google DeepMind AI Co-Scientist** — multi-agente Gemini 2.0, generate-debate-evolve, ranking Elo por torneos.
- **K-Dense** — multi-agente sobre Gemini 2.5 Pro. Acaba de publicar "guided multi-agent AI invents highly accurate, uncertainty-aware transcriptomic aging clocks."
- **AgentLaboratory, AI-Researcher, Auto-Deep-Research, MDCrow, BioMedAgent, FreePhDLabor** — múltiples proyectos, la mayoría duermen tras publicación (el patrón de "20,857 stars de capacidad científica sentada idle" de claw4science.org).
- **Periodic Labs** — startup recién levantada con $300M para AI scientist de materiales.

### Apto para Paraguay

**NVIDIA BioNeMo Agent Toolkit es el entry point obvio** — único con skills abiertos específicos para biología, funciona con cualquier agente runtime, gratis para prototyping. Podría emparejarse con un LLM paraguayo o usarse directamente.

Proyecto concreto: **agente autónomo de drug discovery para Chagas** que extrae productos naturalas de BioProsNat, consulta Boltz-2 para afinidad de unión, rankea candidatos, produce reportes paper-ready. Las skills de BioNeMo cubren la mayor parte de este stack.

---

## §8. Capa de infraestructura — NVIDIA BioNeMo + NIM

### Qué es BioNeMo

- **BioNeMo Framework** — framework de entrenamiento open-source para modelos biomoleculares (protein LMs, generadores de moléculas), optimizado para clusters GPU NVIDIA. Modelos de3B parámetros protein entrenables en días sobre cientos de GPUs.
- **NIM microservices** — modelos pre-entrenados containerizados. Cada uno = container Docker con REST API.
- **NIMs disponibles:** AlphaFold2, ESMFold, **OpenFold**, Boltz-1 (no aún Boltz-2), ProtGPT2, **MolMIM** (generación de moléculas pequeñas), **DiffDock**, RFDiffusion, VISTA-3D (segmentación de imagen médica).

### Qué es gratis vs pagado

- **BioNeMo Framework código** — open source
- **Imágenes de container, pesos, NIM microservices** — gratis para desarrollo en DGX Spark, **producción requiere NVIDIA AI Enterprise license** ($4,500/GPU/año después de trial de90 días)
- **Endpoints hosted en build.nvidia.com** — gratis para prototyping, cap de 40 RPM
- **NGC API key** — gratis, requerido para pull de NIM containers

### Por qué importa

Un equipo paraguayo podría:
1. Registrarse en NGC free tier
2. Usar Boltz-1, MolMIM, DiffDock vía NIM API gratis para prototyping
3. Correr experimentos localmente en cualquier GPU NVIDIA
4. Aplicar a acceso DGX Spark gratis vía programas NVIDIA (Inception, grants académicos)

Esto bypassea la dependencia de HIVE BUZZ para muchas tareas.

**Site:** [build.nvidia.com](https://build.nvidia.com)

---

## §9. Cómo encaja todo en Paraguay

Un stack que recomiendo realmente, rankeado por **paraguay-fit**:

### Layer A — Estructura & diseño (mayor fit: drug discovery)

```
Input: SMILES de BioProsNat + secuencia de diana parasitaria de IICS/CEDIC
   ↓
Boltz-2 (MIT, pesos abiertos) → estructura proteica + complejo small-molecule + score de afinidad
   ↓
LigandMPNN (abierto) → si se diseña nueva proteína para unir el ligando
   ↓
RDKit + TDC → validación contra benchmarks de bioactividad
   ↓
Wet lab en CEDIC/BioProsNat → confirmación experimental
```

**Por qué este stack:** cada herramienta es MIT/Apache. Sin bloqueos de licensing. Corre en un solo A100 o H100. Loop cerrado posible localmente.

### Layer B — Interpretación de variantes de ADN (mayor fit: CEDIC × Galatea)

```
Input: variant calls WGS paraguayos (de CEDIC × Galatea)
   ↓
AlphaGenome API (no comercial) → scores de efecto de variante across modalities
   ↓
AlphaGenome Atlas → scores precomputados para 9B SNVs
   ↓
Combinar con datos de fenotipo locales → identificar variantes funcionales en respuesta a Chagas, predisposición a cáncer, etc.
```

**Por qué:** AlphaGenome es API-only y non-commercial, pero el uso académico/clínico paraguayo encaja.

### Layer C — NLP clínico & EHR (mayor fit: Hospital de Clínicas)

```
Input: Notas de Hospital de Clínicas (papel o escaneadas) + texto clínico en español paraguayo
   ↓
Whisper (ASR para dictado médico, fine-tune guaraní) → texto
   ↓
BiomedCLIP / MedSigLIP (clasificación zero-shot de imágenes médicas)
   ↓
MedGemma 4B (Apache 2.0 wrapper) → fine-tune en notas clínicas paraguayas para triaje/resumen
   ↓
RAG sobre guías clínicas MSPBS + prompting OpenMedLM
   ↓
Deploy vía cluster HIVE BUZZ GPU o servidor local
```

**Por qué MedGemma:** mejor open medical FM ahora, Apache 2.0 wrapper, base español-capaz, fine-tuneable en una sola GPU.

### Layer D — Patología & radiología (fit medio: INCAN futuro)

```
Input: Slides H&E (necesita adquirir scanner primero, ~$15–50k)
   ↓
CONCH (vision-language, top en benchmark 2025) → detección zero-shot de tumor
   ↓
MedSAM (segmentación, MIT) → bordes de tumor
   ↓
UNI2-h o Virchow2 → backup vision-only
   ↓
Validar contra patólogos de INCAN
```

### Layer E — Vigilancia genómica viral (mayor fit: LCSP)

```
Input: secuencias dengue / SARS-CoV-2 / MPXV / Chagas de LCSP Illumina + MinION
   ↓
Nextclade (abierto) → asignación de clado
   ↓
Augur + Auspice (Nextstrain) → filogenia + visualización
   ↓
nf-core/viralrecon (Nextflow) → pipeline reproducible
   ↓
Deploy en servidor local o workstation de LCSP
   ↓
Dashboard público auto-actualizado cuando llegan nuevas secuencias
```

**Papers paraguayos ya usan partes de esto ad hoc; la oportunidad es estandarizar.**

### Layer F — Automatización de investigación agéntica (fit medio, gran upside)

```
Usar NVIDIA BioNeMo Agent Toolkit + LangGraph
   ↓
Skills: Boltz-2 afinidad + DiffDock + RDKit + TDC + búsqueda de literatura científica
   ↓
Correr localmente o en HIVE BUZZ
   ↓
Aplicado a: screening de drug discovery para Chagas, predicción de resistencia AMR, descubrimiento de biomarcadores
```

**Por qué:** BioNeMo es genuinamente el stack de biología agéntica más accesible — gratis para prototyping, agent-agnostic, tiene skills ya construidos.

---

## §10. Tabla maestra de licencias

| Modelo/Herramienta | Licencia | ¿Comercial OK? | ¿Pesos locales? |
|---|---|---|---|
| AlphaFold 3 (código) | Apache 2.0 | ✓ | — |
| AlphaFold 3 (pesos) | Custom (no comercial) | ✗ | ✓ gated |
| **Boltz-2** | **MIT** | **✓** | **✓** |
| Boltz-1 | MIT | ✓ | ✓ |
| Chai-1 / Chai-2 | Apache 2.0 | ✓ | ✓ |
| ESM3 1.4B | Cambrian Non-Commercial | ✗ | ✓ |
| ESM3 7B/98B | API only | ✓ vía BioNeMo/SageMaker | ✗ |
| ESM C (300M/600M) | Open (Cambrian terms) | ✓ | ✓ |
| AlphaGenome | Non-commercial API | ✗ | ✗ (API) |
| Nucleotide Transformer | Apache 2.0 | ✓ | ✓ |
| HyenaDNA / Caduceus / Evo | Open (paper-specific) | ✓ | ✓ |
| LigandMPNN / ProteinMPNN | Open | ✓ | ✓ |
| RFdiffusion | Open | ✓ | ✓ |
| MedGemma wrapper | Apache 2.0 | ✓ | — |
| MedGemma pesos | Health AI Dev Foundations | ✓ (terms) | ✓ |
| MedSigLIP | Apache 2.0 | ✓ | ✓ |
| MedSAM | MIT | ✓ | ✓ |
| BiomedCLIP | MIT | ✓ | ✓ |
| CONCH / UNI / Virchow | Research use | (varía) | ✓ |
| Variantes Med-CLIP | Open | ✓ | ✓ |
| OpenMedLM (Yi 34B base) | Apache 2.0 | ✓ | ✓ |
| Meditron | Llama community | ✓ | ✓ |
| RadFM | (paper-specific) | (verificar) | ✓ |
| ChemBERTa-3 | CC BY-NC (artículo), código open | varía | ✓ |
| TDC | Open | ✓ | — |
| scGPT, Geneformer, etc. | Open | ✓ | ✓ |
| scFoundry | Apache 2.0 | ✓ | — |
| BioNeMo Framework | Open | ✓ | ✓ |
| BioNeMo NIMs | NVIDIA AI Enterprise | ✓ (con licencia) | ✓ en containers |
| BioNeMo Agent Toolkit | CC BY 4.0 | ✓ | ✓ |
| LangGraph / AutoGen | Apache 2.0 / MIT | ✓ | ✓ |

---

## §11. Brechas honestas

1. **AF3 no es comercialmente usable.** Si cualquier equipo paraguayo planea traducción comercial, **default a Boltz-2**. AF3 está bien para publicaciones académicas.
2. **ESM3 > 1.4B es API-only.** Si se necesitan las variantes 7B/98B, es vía AWS SageMaker o BioNeMo. No es descarga todo-en-uno.
3. **AlphaGenome es API + no comercial.** Sin pesos locales. Los output terms aplican. Bien para uso académico paraguayo; problemático para comercialización biotech.
4. **Producción en NVIDIA NIM es cara.** $4,500/GPU/año para self-hosted. HIVE BUZZ o X8 Cloud podrían absorberlo; los labs locales no.
5. **La mayoría de FMs de patología tienen datos de entrenamiento propietarios.** Midnight (12K WSIs de TCGA) prueba que la receta escala hacia abajo — pero los modelos entrenados con slides propietarios grandes (Virchow, UNI, H-optimus) son los que top benchmarks. **Entrenar un FM de patología paraguayo desde cero es plausible** con la receta de Midnight; tomaría ~290K WSIs equivalentes.
6. **Ningún FM de patología ha sido validado específicamente en H&E paraguayo.** Distribution shift es real. Piloto requerido.
7. **Agentes "AI Scientist" están en su mayoría dormidos.** Sakana AI Scientist, AI-Researcher, ChemCrow todos callaron. El BioNeMo Toolkit es el más activamente mantenido.
8. **NLP en guaraní es genuinamente delgado.** Casi no hay modelos fundacionales en guaraní. Whisper fine-tune es la opción realista, requiere construir corpus local.
9. **La mayoría de benchmarks son US/europeos.** Un dataset paraguayo para evaluación de LLM clínico no existe públicamente.
10. **El acceso a GPU sigue siendo el cuello de botella.** HIVE BUZZ y X8 Cloud son el cómputo local realista; todo lo demás es cloud.
11. **LatAm genomes están subrepresentados en datos de entrenamiento** — aplicar modelos globales directamente puede no funcionar bien para variantes paraguayas. Necesario validación local antes de deployment.
12. **No hay clearance regulatorio para IA clínica en Paraguay.** Resolución 367/2020 endosa IA en telesalud, pero no hay pathway de aprobación. Vacío regulatorio = riesgo legal + oportunidad de ayudar a diseñar el marco.

---

## §12. Tres recomendaciones principales para Paraguay

Si tuviera que elegir **tres herramientas de IA open-source** que más moverían la investigación médica paraguaya, ahora mismo:

### 1. **Boltz-2** (MIT, full open)

**Infraestructura de drug discovery. Mayor gap-closer único para el pipeline CEDIC × BioProsNat × Tesabio.** Predicción de afinidad es la pieza faltante para drug discovery de Chagas/Leishmania.

### 2. **MedGemma 4B** (Apache wrapper, base Gemma 3)

**Infraestructura de NLP clínico. Mejor entry point para pilotos LLM en Hospital de Clínicas.** Español-capaz, fine-tuneable en una sola GPU, corre en HIVE BUZZ.

### 3. **NVIDIA BioNeMo Agent Toolkit** (CC BY 4.0)

**Único framework de agentes bio activamente mantenido, agent-agnostic, open.** Gratis para prototyping. Hace las otras herramientas componibles. Podría anclar un agente nacional de discovery para Chagas.

### Menciones honrosas que también deberían estar en el radar

- **AlphaGenome** para interpretación de variantes (cuando los datos de CEDIC × Galatea Bio estén listos)
- **scFoundry + Geneformer** si cualquier lab paraguayo quiere arrancar trabajo single-cell
- **Midnight / OpenMidnight** pathology FM si algún equipo paraguayo quiere entrenar el suyo desde datos públicos
- **CONCH** si INCAN avanza en patología digital

---

## §13. Referencias y verificación

### Verificación independiente hecha para este documento

- AF3 v3.0.3 release notes confirma Apache 2.0 en código, weights terms separados
- Boltz-2 release confirmado vía MIT Jameel Clinic y CSAIL newsroom
- MedGemma release confirmado vía infoq.com (mayo 2025) y arxiv:2507.05201
- LigandMPNN publicado en Nature Methods, marzo 2025
- AlphaGenome publicado en Nature, enero 2026, API en deepmind.google
- Pathology FMs benchmark en Nature Biomedical Engineering 2025 (19 modelos, 6,818 pacientes)
- Tesabio SAB confirmado vía tesabio.ai/news announcements
- CONACYT PROCIENCIA II ticket sizes confirmados vía feei.gov.py
- Ley 7593/2025 confirmada vía bacn.gov.py

### Recursos para profundizar

- [Bio+Med+AI Slack](https://biomedai-slack.herokuapp.com) — comunidad curada
- [Papers with Code](https://paperswithcode.com) — implementación tracking
- [Hugging Face](https://huggingface.co) — modelos, datasets
- [OpenAlex](https://openalex.org) — papers
- [GWAS Catalog AI section](https://catalog.gwaslab.org) — pathology/medical FMs indexados

---

## §14. Google DeepMind + HAI-DEF — catálogo detallado

Google es el **vendor único más importante** para IA médica/biomédica abierta. Su portafolio se divide en tres capas:

- **Google DeepMind** — investigación frontera (AlphaFold 3, AlphaGenome, AI Co-Scientist, Gemini 2.5).
- **Health AI Developer Foundations (HAI-DEF)** — modelos open-weight con fine-tuning médico (MedGemma, TxGemma, HeAR, Path/CXR/Derm Foundation, MedASR, MedSigLIP).
- **Gemma family** — base general (Gemma 3 → MedGemma, PaliGemma 2).

**Términos HAI-DEF (verificados):**

- Código (recipe + inference + training + utility): **Apache 2.0**.
- Weights: open-weight con [Health AI Dev Foundations License](https://developers.google.com/health-ai-developer-foundations/terms). Investigación + comercial OK.
- **Prohibido**: usos restringidos por [Prohibited Use Policy](https://developers.google.com/health-ai-developer-foundations/prohibited-use-policy); cualquier uso que haga que Google sea considerado "manufacturer" de un dispositivo médico; violación de leyes aplicables.
- **Requerido**: incluir restricciones §3.2 como acuerdo ejecutable; notificar a usuarios downstream; acompañar distribuciones con archivo "Notice".
- Google puede terminar el acuerdo o restringir uso remotamente.

### §14.1 AlphaFold 3 + AlphaFold Server + AlphaFold DB

- **AF3 v3.0.4** (jul 2025), **v3.0.3** (jun 2025, Apache 2.0 code).
- **Pesos**: **custom non-commercial** — universidades, ONGs, gobierno, periodismo. **Comercial prohibido**.
- **AlphaFold Server**: ~10–20 jobs/día por usuario académico.
- **AlphaFold Database**: 200M+ estructuras, CC0, gratis comercial.

**Apto Paraguay:**
- ✅ IICS / CEDIC / Hospital de Clínicas / BioProsNat — uso académico libre.
- ✅ AlphaFold Server para uso educativo sin GPU local.
- ❌ Tesabio — pesos de AF3 no son comercialmente usables; usar **OpenFold3** o **Boltz-2**.

### §14.2 OpenFold3 (Apache 2.0 — la mejor alternativa abierta a AF3)

- **Released**: preview 28 oct 2025. Licencia **Apache 2.0** (código + pesos).
- **Desarrolladores**: AlQuraishi Lab (Columbia) + OpenFold Consortium + LLNL + Steinegger Lab Seoul.
- **Performance**: competitivo con AF3; **único modelo open que iguala AF3 en monomeric RNA**.
- **Disponible via**: HuggingFace, Docker, NVIDIA NIM.
- **Production model**: OpenBind-0 (jun 2025 cutoff).

**Por qué importa para Paraguay:** si BioProsNat/Tesabio quieren usar estructura AF3-class para drug discovery con downstream comercial, **OpenFold3 es la única opción abierta**.

- Repo: [github.com/aqlaboratory/openfold-3](https://github.com/aqlaboratory/openfold-3)
- HF: [huggingface.co/OpenFold/OpenFold3](https://huggingface.co/OpenFold/OpenFold3)
- NIM: [build.nvidia.com/openfold/openfold3](https://build.nvidia.com/openfold/openfold3)

### §14.3 AlphaGenome (API no comercial)

- **Released**: 25 jun 2025. **Nature**: enero 2026.
- Predice miles de propiedades regulatorias desde 1 Mb de ADN. 22/24 en tareas de secuencia, 24/26 en tareas de variantes vs SOTA externos.
- **AlphaGenome Atlas**: predicciones precomputadas para **9 mil millones** de SNVs en genoma humano.
- API: gratis no comercial, hasta ~1M predicciones razonables.

**Apto Paraguay:** ✅ CEDIC × Galatea Bio biobank; ✅ IICS molecular biology para variantes hereditarias. ❌ No comercial.

- Repo: [github.com/google-deepmind/alphagenome](https://github.com/google-deepmind/alphagenome)
- API: [deepmind.google/science/alphagenome](https://deepmind.google/science/alphagenome)
- Atlas: [deepmind.google/science/alphagenome/atlas](https://deepmind.google/science/alphagenome/atlas)

### §14.4 AI Co-Scientist

- **Released**: diciembre 2024; Nature 2026.
- Multi-agent sobre Gemini 2.0 con agentes Supervisor + Generation + Reflection + Ranking (Elo tournament) + Evolution + Proximity + Meta-review.
- Tres casos validados: drug repurposing AML, liver fibrosis targets, AMR mechanism.
- **No producto público**; solo via Trusted Tester.

**Apto Paraguay:** ⏸ **Futuro**. Cuando se abra el acceso, el proyecto natural es drug repurposing para Chagas (siguiendo el playbook AML). Pre-posicionamiento con propuestas listas.

- Blog: [research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- Nature: [doi.org/10.1038/s41586-026-10644-y](https://doi.org/10.1038/s41586-026-10644-y)

### §14.5 Gemini 2.5 Pro / Flash (closed)

- Gemini 2.5 Pro top en benchmarks clínicos publicados (nephrology reasoning 7.57/10, beats GPT-o3). Pasó el examen de especialización polaco de ginecología a 96.63%.
- Multimodal nativo (image + text + audio + video hasta3h), thinking mode, 1M+ context.
- API + Vertex AI en GCP. Pagado.

**Apto Paraguay:** ✅ como asistente de research (literatura, código, brainstorming). ❌ para clinical use (cerrado, sin fine-tune específico).

### §14.6 MedGemma (HAI-DEF) — LLM clínico

- Mayo 2025 (4B + 27B text), julio 2025 (27B multimodal), MedGemma 1.5 actualizado.
- Gemma 3 base + SigLIP-400M médico. 64.4% MedQA (4B), 87.7% MedQA (27B). 81% de informes CXR del 4B juzgados suficientes para manejo similar.
- 50% reducción de errores en retrieval de EHR tras fine-tune.

**Apto Paraguay: ⭐⭐ EL MÁS ALTO FIT.** Fine-tuneable en español paraguayo en una sola GPU. Deploy en HIVE BUZZ.

- Repo: [github.com/google-health/medgemma](https://github.com/google-health/medgemma)
- HF: [huggingface.co/collections/google/medgemma](https://huggingface.co/collections/google/medgemma)
- Notebook: [colab.research.google.com/github/google-health/medgemma](https://colab.research.google.com/github/google-health/medgemma/blob/main/notebooks/quick_start_with_hugging_face.ipynb)

### §14.7 MedSigLIP (HAI-DEF) — encoder visual médico

- SigLIP-400M fine-tuned en CXR, CT, MRI, dermatología, oftalmología, histopathology.
- **Casos de uso**: zero-shot classification, data-efficient classification, semantic image retrieval.

**Apto Paraguay:** ✅ INCAN pathology; ✅ TB screening por CXR; ✅ Hospital de Clínicas radiology.

### §14.8 TxGemma — LLM terapéutico (sleeper hit para Paraguay)

- **Released**: 25 marzo 2025. Fine-tune de Gemma 2 sobre Therapeutics Data Commons (66 tasks, 7M ejemplos, 15M data points).
- **Tamaños**: 2B / 9B / 27B. Variantes Predict (tareas narrow) y Chat (9B/27B, multi-turn con explicaciones).
- **Performance**: supera SOTA generalista en 45/66 tareas, especialista en 26/50. Humanity's Last Exam (Chem/Bio) +9.8% sobre o3-mini.
- **Inputs**: SMILES de moléculas, secuencias de proteínas, ácidos nucleicos, descripciones de enfermedades, líneas celulares.

**Apto Paraguay: ⭐⭐ EL MÁS ALTO FIT para CEDIC + BioProsNat + Tesabio.**

Pipeline recomendado:
1. **TxGemma-Chat 9B** — query en español sobre ADMET de productos naturales paraguayos.
2. **Boltz-2** (MIT, comercial OK) — estructura 3D + afinidad de los hits predichos.
3. **CEDIC** — validación experimental in vitro.

Aplicaciones concretas:
- Predicción de toxicidad de productos naturales paraguayos.
- Penetración de barrera hematoencefálica.
- Afinidad de unión proteína-ligando para targets de *T. cruzi* / *Leishmania*.
- Generación de combinaciones sinérgicas.

- Model card: [developers.google.com/health-ai-developer-foundations/txgemma/model-card](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card)
- Blog: [developers.googleblog.com/introducing-txgemma](https://developers.googleblog.com/introducing-txgemma-open-models-improving-therapeutics-development/)

### §14.9 Path Foundation (HAI-DEF) — histopathology encoder

- Embeddings para patches de histopathology. Data-efficient classification.
- **Apto Paraguay**: ✅ INCAN pathology digitalization pilot. ⚠️ requiere validación en H&E paraguayo (distribution shift).

### §14.10 CXR Foundation (HAI-DEF) — chest X-ray encoder

- Embeddings para CXR.
- **Apto Paraguay**: ✅ TB screening, cardiomegaly/pneumonia classification, ER triage.

### §14.11 Derm Foundation (HAI-DEF) — dermatology encoder

- Embeddings para imágenes de piel.
- **Apto Paraguay**: ✅ Chagas cutáneo (chagoma, signo de Romaña); ✅ teledermatología rural.

### §14.12 HeAR — health acoustics embeddings (⭐ sleeper hit para TB)

- **Released**: 2024. Embeddings 512-d para clips de audio de 2 segundos. Entrenado sobre 300M+ clips (tos, respiración, carraspeo, risa, habla).
- **Linear probing** en 33 health acoustic tasks — SOTA en la mayoría.
- **Performance benchmarked** para: COVID-19, tuberculosis, COPD, asma pediátrico, neumonía.

**Apto Paraguay: ⭐⭐⭐ ALTÍSIMO. La aplicación más concreta:**

- Paraguay es **hiperendémico para TB** (en Chaco y en indígenas).
- Atención primaria rural **no tiene acceso a chest X-ray**.
- HeAR + clasificador lineal + smartphone = **screening de TB por tos** deployable en Chaco.

Proyecto concreto: app móvil donde agente de salud comunitaria graba la tos del paciente → embedding HeAR → clasificador (entrenado en datos locales o SPRSound/COUGHVID) → probabilidad de TB → referral al Hospital de Clínicas.

- HF: [huggingface.co/google/hear](https://huggingface.co/google/hear)
- Paper: [arxiv.org/abs/2403.02522](https://arxiv.org/abs/2403.02522)

### §14.13 MedASR — medical speech recognition

- **Released**: diciembre 2025. Conformer 105M params. 5,000+ horas de dictado médico (radiología, internal medicine, family medicine).
- **4.6% WER** en radiology dictation (con 6-gram LM). 5× mejor que Whisper v3 Large. Beats Gemini 2.5 Pro/Flash.
- **English only.**

**Apto Paraguay:** ⚠️ Limitado por idioma. ✅ Sirve como template para construir un Spanish/Guaraní medical ASR (arquitectura + pipeline disponibles).

- HF: [huggingface.co/google/medasr](https://huggingface.co/google/medasr)
- Paper: [arxiv.org/pdf/2605.16555](https://arxiv.org/pdf/2605.16555)
- Sitio: [medasr.org](https://medasr.org)

### §14.14 PaliGemma 2 — general VLM (Gemma 2 based)

- 3B / 10B / 28B. Capacidades: captioning, VQA, object detection, OCR.
- **Apto Paraguay:** ⚠️ General — no médico-tuned. Usar como backup si MedGemma no encaja.

---

## §15. Matriz maestra de licencias actualizada (incluye Google + OpenFold3)

| Modelo/Herramienta | Licencia | ¿Comercial OK? | ¿Pesos locales? | ¿Apto Paraguay? |
|---|---|---|---|---|
| AlphaFold 3 (código) | Apache 2.0 | ✓ | — | ✓ académico |
| AlphaFold 3 (pesos) | Custom (no comercial) | ✗ | ✓ gated | ✓ académico / ✗ comercial |
| AlphaFold Database | CC0 | ✓ | n/a | ✓ |
| AlphaGenome | Non-commercial API | ✗ | ✗ (API) | ✓ académico |
| **OpenFold3** | **Apache 2.0** | **✓** | **✓** | **✓✓ mejor alternativa open a AF3** |
| **Boltz-2** | **MIT** | **✓** | **✓** | **✓✓ default drug discovery** |
| Boltz-1 | MIT | ✓ | ✓ | ✓ |
| Chai-1 / Chai-2 | Apache 2.0 | ✓ | ✓ | ✓ |
| ESM3 1.4B | Cambrian Non-Commercial | ✗ | ✓ | limitado |
| **MedGemma 4B/27B** | **HAI-DEF** | **✓** | **✓** | **✓✓ default clínico** |
| MedSigLIP | HAI-DEF | ✓ | ✓ | ✓ |
| **TxGemma 2B/9B/27B** | **Gemma terms** | **✓** | **✓** | **✓✓ default terapéutico** |
| Path Foundation | HAI-DEF | ✓ | ✓ | ✓ |
| CXR Foundation | HAI-DEF | ✓ | ✓ | ✓ |
| Derm Foundation | HAI-DEF | ✓ | ✓ | ✓ |
| **HeAR** | **HAI-DEF** | **✓** | **✓** | **✓✓✓ default TB cough screening** |
| MedASR | HAI-DEF (English only) | ✓ | ✓ | ⚠️ template, no deploy directo |
| PaliGemma 2 | Gemma terms | ✓ | ✓ | ⚠️ backup general |
| Gemini 2.5 Pro/Flash | Closed | ✓ (paid API) | ✗ | ✓ research assistant |
| ESM C (300M/600M) | Open (Cambrian terms) | ✓ | ✓ | ✓ |
| Nucleotide Transformer | Apache 2.0 | ✓ | ✓ | ✓ |
| HyenaDNA / Caduceus / Evo | Open (paper-specific) | ✓ | ✓ | ✓ |
| LigandMPNN / ProteinMPNN | Open | ✓ | ✓ | ✓ |
| RFdiffusion | Open | ✓ | ✓ | ✓ |
| RadFM | (paper-specific) | (verificar) | ✓ | ✓ |
| ChemBERTa-3 | CC BY-NC (artículo), código open | varía | ✓ | ✓ |
| TDC | Open | ✓ | — | ✓ |
| scGPT, Geneformer, etc. | Open | ✓ | ✓ | ✓ |
| scFoundry | Apache 2.0 | ✓ | — | ✓ |
| BioNeMo Framework | Open | ✓ | ✓ | ✓ |
| BioNeMo NIMs | NVIDIA AI Enterprise | ✓ (con licencia) | ✓ en containers | ✓ |
| BioNeMo Agent Toolkit | CC BY 4.0 | ✓ | ✓ | ✓ |
| LangGraph / AutoGen | Apache 2.0 / MIT | ✓ | ✓ | ✓ |

---

## §16. Top-5 recomendaciones actualizadas para Paraguay

1. **MedGemma 4B** — clinical NLP, Hospital de Clínicas. **(HAI-DEF, Apache wrapper)**
2. **TxGemma 27B-Chat** — drug discovery con BioProsNat + Tesabio + CEDIC. **(Gemma terms)**
3. **HeAR** — TB cough screening en Chaco, smartphone-deployable. **(HAI-DEF)**
4. **Boltz-2 + OpenFold3** — structure prediction con licencia comercial OK. **(MIT + Apache 2.0)**
5. **NVIDIA BioNeMo Agent Toolkit** — orquestación de todos los anteriores. **(CC BY 4.0)**

Honorable mentions: AlphaGenome (variant interpretation para CEDIC × Galatea), MedASR (template para Spanish medical ASR), CXR/Derm/Path Foundation (image embeddings para INCAN/Hospital de Clínicas).

---

## Última actualización

Septiembre 2026.