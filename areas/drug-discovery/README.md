# Área 2 — Descubrimiento de fármacos para enfermedades desatendidas

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§1-genómica-y-estructura-de-proteínas) · [research findings](../docs/research-findings.md)

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
  - Dr. Diego Galeano (FIUNA) — CTO
  - Dr. Afshin Beheshti (Broad / U. Pittsburgh) — CSO
- **Pre-seed:** GRIDX.
- **SAB:** Frank Slack (Harvard), Charles Vanderburg (Broad), Christopher Mason (Weill Cornell), Alberto Paccanaro (FGV/Royal Holloway).
- **Foco:** pequeñas moléculas que reprograman redes de microARN.
- **Aplicaciones:** oncología, hematología, neurodegeneración.

## Herramientas de código abierto — el stack recomendado

| Herramienta | Función | Licencia | Notas |
|---|---|---|---|
| **[Boltz-2](https://github.com/jwohlwend/boltz)** | Estructura proteica + **afinidad de unión proteína-ligando** | **MIT** | **Modelo por defecto.** Primer AI en acercarse a FEP; 1000× más rápido. v jun 2025. |
| [Boltz-1](https://github.com/jwohlwend/boltz) | Estructura proteica (sin afinidad) | MIT | Predecesor de Boltz-2; muy usado en industria. |
| [Chai-1](https://github.com/chaidiscovery/chai-lab) / Chai-2 | Estructura proteica | Apache 2.0 | Alternativa / validación cruzada. |
| [AlphaFold 3](https://github.com/google-deepmind/alphafold3) | Estructura proteica | Apache 2.0 (código) / non-commercial (pesos) | Solo para uso académico. NO comercializable. |
| [ESM3](https://github.com/evolutionaryscale/esm) 1.4B | Diseño *de novo* de proteínas | Cambrian Non-Commercial | Genera secuencia + estructura + función. |
| [LigandMPNN](https://github.com/dauparas/LigandMPNN) | Inverse folding con contexto de ligando | Open | **Compañero perfecto de Boltz-2**: diseñá secuencia que estabilice el complejo. |
| [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) | Diseño de backbone *de novo* | Open | Genera estructuras nuevas. |
| [RDKit](https://github.com/rdkit/rdkit) | Cheminformatics | BSD | Navaja suiza. |
| [DeepChem](https://github.com/deepchem/deepchem) + ChemBERTa-3 | ML para química | Open | Framework de entrenamiento reproducible. |
| [TDC](https://tdcommons.ai/) | Benchmarks de bioactividad | Open | Estandariza evaluación. |
| [DiffDock](https://github.com/gcorso/diffdock) | Docking proteína-ligando | MIT | Estado del arte. |
| [NVIDIA BioNeMo](https://build.nvidia.com) | NIM microservices (Boltz-1, MolMIM, DiffDock) | Mixto (framework open, NIM production $$$) | Gratis para prototyping vía API. |
| [TrypanoDB / TriTrypDB](https://tritrypdb.org) | Bases de datos específicas de *T. cruzi*/*Leishmania* | — | Genomas y anotaciones. |

### Por qué Boltz-2 es el default (no AF3)

- **AF3 weights son non-commercial**. Si Tesabio o CEDIC quieren traducir a producto comercial, no pueden usar AF3.
- **Boltz-2 es MIT**: comercial OK, incluye pesos, código de entrenamiento, datos.
- **Boltz-2 hace algo que AF3 no hace**: predice afinidad de unión con precisión cercana a FEP. Esa pieza es la que faltaba para drug discovery.

## Primer proyecto concreto

> Predicción con Boltz-2 de las estructuras de cruzipaína y otras dianas de *T. cruzi* validadas en CEDIC, luego screening virtual contra la biblioteca de productos naturales de BioProsNat.

Entregables:
- Paper con coautoría CEDIC + BioProsNat + FIUNA.
- Hits candidatos priorizados para validación experimental.
- Aplicación a la **convocatoria 2026 FAPESP-CONACYT-CONICET sobre resistencia antimicrobiana** (extiende naturalmente a antiparasitarios).

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
- Si se usan pesos de AF3 en outputs publicados → output terms aplican; alternativa es Boltz-2.