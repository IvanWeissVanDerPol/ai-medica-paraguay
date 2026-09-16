# Área 2 — Descubrimiento de fármacos para enfermedades desatendidas

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§1-genómica-y-estructura-de-proteínas) · [research findings](../docs/research-findings.md) · [Google dedicado](../docs/google-deepmind-paraguay.md)

---

## Problema

Paraguay tiene ~165.000 personas infectadas con *Trypanosoma cruzi* (Chagas) y es endémico en leishmaniasis. La mayoría de los fármacos actuales tienen décadas, son tóxicos, y la resistencia está creciendo. La estructura de dianas terapéuticas para *T. cruzi* y *Leishmania* está pobremente caracterizada. Las herramientas modernas de estructura de proteínas y docking se han abierto como código abierto en los últimos 24 meses.

## Capacidades locales

- **CEDIC** — tamizaje *in vitro* explícito sobre *T. cruzi*, *Leishmania*, líneas tumorales; screening experimental e *in silico*.
- **BioProsNat (CEMIT-UNA)** — bioprospección de productos naturales bioactivos; screening antimicrobiano, antifúngico, antiparasitario. Vínculos consolidados con UFPB, UFG, UFMA, FIOCRUZ (Brasil).
- **IICS-UNA Producción + Bioterio** — modelos animales para Chagas y toxoplasmosis.
- **Tesabio.ai** — startup paraguaya de IA para descubrimiento de fármacos, con SAB de Harvard/Broad/Cornell.

### Tesabio — perfil completo

- **Equipo fundador:**
  - Sebastián Ortiz Chamorro — CEO
  - Dr. Diego Galeano (FIUNA, PhD Royal Holloway) — CTO. ORCID [0000-0002-1748-7148](https://orcid.org/0000-0002-1748-7148).
  - Dr. Afshin Beheshti (Broad Institute / U. Pittsburgh) — CSO.
- **Pre-seed:** GRIDX.
- **SAB:** Frank Slack (Harvard), Charles Vanderburg (Broad), Christopher Mason (Weill Cornell), Alberto Paccanaro (FGV/Royal Holloway).
- **Foco:** pequeñas moléculas que reprograman redes de microARN.
- **Aplicaciones:** oncología, hematología, neurodegeneración, disorders inmunes.

## Herramientas de código abierto — el stack recomendado

| Capa | Herramienta | Función | Licencia | Notas |
|---|---|---|---|---|
| **Estructura (default)** | **[Boltz-2](https://github.com/jwohlwend/boltz)** | Estructura proteica + afinidad de unión proteína-ligando | **MIT** | **Modelo por defecto.** AF3-class, 1000× más rápido que FEP. jun 2025. |
| **Estructura (open AF3 alt)** | **[OpenFold3](https://github.com/aqlaboratory/openfold-3)** | AF3-class structure prediction | **Apache 2.0** | Único AF3-class open con pesos **comercialmente usables**. Para Tesabio. |
| **Estructura (académico)** | [AlphaFold 3](https://github.com/google-deepmind/alphafold3) | Estructura proteica | Apache 2.0 (código) / non-commercial (pesos) | Para IICS, CEDIC, BioProsNat — uso académico. **NO para Tesabio.** |
| **Estructura (binding, alpha)** | [Chai-1](https://github.com/chaidiscovery/chai-lab) / Chai-2 | Estructura proteica | Apache 2.0 | Validación cruzada. |
| **Diseño de novo** | [ESM3](https://github.com/evolutionaryscale/esm) 1.4B | Diseño *de novo* de proteínas | Cambrian Non-Commercial | 1.4B corre en una sola GPU. |
| **Diseño con contexto de ligando** | [LigandMPNN](https://github.com/dauparas/LigandMPNN) | Inverse folding con contexto de ligando | Open | **Compañero perfecto de Boltz-2 / OpenFold3.** |
| **Diseño de backbone** | [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) | Diseño de backbone *de novo* | Open | |
| **ADMET / propiedades terapéuticas** | **[TxGemma 27B-Chat](https://developers.google.com/health-ai-developer-foundations/txgemma/model-card)** | Predicción de toxicidad, BBB penetration, CYP, afinidad desde SMILES | **Gemma terms** | **Sleeper hit.** Conversacional, query en español. |
| **Química generativa** | [REINVENT](https://github.com/MolecularAI/REINVENT), [MolGPT](https://github.com/...), [GraphGraph](](https://github.com/...)) | Generación de moléculas | Open | |
| **Cheminformatics** | [RDKit](https://github.com/rdkit/rdkit) | Navaja suiza | BSD | |
| **ML para química** | [DeepChem](https://github.com/deepchem/deepchem) + [ChemBERTa-3](https://github.com/deepchem/deepchem) | Framework + chemical FMs | Open | |
| **Benchmarks** | [TDC](https://tdcommons.ai/) | Estandariza evaluación | Open | |
| **Docking** | [DiffDock](https://github.com/gcorso/diffdock) | Docking proteína-ligando SOTA | MIT | |
| **Infraestructura NIM** | [NVIDIA BioNeMo](https://build.nvidia.com) | NIM microservices (Boltz-1, MolMIM, DiffDock) | Mixto | Gratis prototyping, $4.5k/GPU/año producción |
| **Agentes bio** | [NVIDIA BioNeMo Agent Toolkit](https://github.com/NVIDIA-BioNeMo/bionemo-agent-toolkit) | Skills agentic para biología | CC BY 4.0 | Gratis prototyping. |
| **Bases de datos patógeno** | [TrypanoDB / TriTrypDB](https://tritrypdb.org) | *T. cruzi*/*Leishmania* específicos | — | |

### Por qué este stack

1. **Boltz-2 + OpenFold3 + AlphaFold 3** — tres alternativas de estructura AF3-class; **siempre usa la comercial-OK (Boltz-2 u OpenFold3) para Tesabio**.
2. **TxGemma 27B-Chat** — para queries terapéuticas en lenguaje natural. **Complementa, no reemplaza, a Boltz-2/OpenFold3**.
3. **LigandMPNN** — diseño de secuencia dado un ligando conocido.
4. **NVIDIA BioNeMo** — entry point para prototyping gratis + agente agentic para orquestar todo.
5. **TDC + RDKit + DeepChem** — validación estándar contra benchmarks de bioactividad.

## Primer proyecto concreto (recomendado)

> Pipeline end-to-end con TxGemma + Boltz-2 + CEDIC wet-lab:
>
> 1. CEDIC selecciona dianas prioritarias de *T. cruzi* (cruzipaína, trans-sialidasa, TcGAPDH, etc.).
> 2. OpenFold3 / Boltz-2 predice estructura 3D de cada diana.
> 3. BioProsNat entrega ~1000 productos naturales paraguayos como SMILES.
> 4. **TxGemma-Chat 27B** — query en español para ADMET (toxicidad, BBB penetration, CYP inhibition) y binding affinity priorization.
> 5. **Boltz-2** — affinity prediction estructural para los hits priorizados.
> 6. **CEDIC** — validación experimental in vitro.
> 7. Paper conjunto CEDIC + BioProsNat + FIUNA + Tesabio.

**Entregables**:
- Paper con hit list priorizada para Chagas.
- Pipeline reproducible (open source).
- Aplicación a la **convocatoria 2026 FAPESP-CONACYT-CONICET AMR** (extiende a antiparasitarios).
- Opcional: paper separado sobre TxGemma fine-tuneado con datos paraguayos.

## Vacíos de información

- ¿Qué dianas específicas prioriza CEDIC para screening?
- ¿Cuántos compuestos naturales tiene caracterizados BioProsNat?
- ¿Cuál es la capacidad de cómputo real disponible localmente?
- ¿Quién mantiene actualmente la infraestructura de Tesabio?
- ¿Hay datos paraguayos de expresión génica de *T. cruzi*/*Leishmania* accesibles?

## Próximo paso inmediato

Hablar con **Dr. Diego Galeano** (FIUNA + Tesabio CTO) sobre modelo de partnership académico. Específicamente: ¿cómo encaja este proyecto con el roadmap de Tesabio (microARN) vs. el de CEDIC/BioProsNat (Chagas)?

## Notas regulatorias

- Si usamos datos genómicos paraguayos → aplica Ley 7593/2025 (datos genéticos = sensibles).
- Cualquier resultado publicado debe seguir CARE Principles para datos derivados de comunidades chaqueñas.
- Modelos entrenados con datos paraguayos → abiertos por defecto (compromiso del repo).
- Si se usan pesos de AF3 en outputs publicados → output terms aplican; alternativa es OpenFold3.
- **TxGemma, Boltz-2, OpenFold3, OpenFold2, RDKit, DeepChem, TDC, NVIDIA BioNeMo** — todos comercialmente usables. Sin bloqueos legales para Tesabio o cualquier spin-off.
- **AlphaFold 3 weights, AlphaGenome API, ESM3 >1.4B** — NO comercialmente usables. Solo académico.