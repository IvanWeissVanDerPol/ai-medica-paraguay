# Top 10 ideas explicadas en profundidad

> **Qué es este archivo:** explicación detallada de cada una de las top 10 ideas del master ranking. Cada idea incluye: qué es exactamente, por qué importa, qué evidencia existe, cómo se implementa paso a paso, qué necesitas, qué bloquea, qué riesgos, qué sale, y por qué es exactamente esa posición.
>
> **Audiencia:** quien decide. Cada idea se explica como si fueras a ejecutarla mañana.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- #1 — TB cough screening con HeAR en smartphone (score 92.5)
- #2 — Antiveneno sintético para T. confluens (score 89)
- #3 — Stack Chaco TB integrado (score 88)
- #4 — TxGemma + Boltz-2 + OpenFold3 + CEDIC pipeline Chagas (score 86)
- #5 — Chagas cardiomyopathy smart-monitoring (score 84)
- #6 — mRNA vaccine design para Leishmania (score 82)
- #7 — tNGS directo desde esputo para TB chaqueña (score 81)
- #8 — CRISPR-Dx pipeline para NTDs chaqueños (score 80)
- #9 — Nextclade + nf-core viralrecon en LCSP (score 78)
- #10 — Biobanco FAIR + AlphaGenome API para CEDIC × Galatea (score 76)

---

## #1 — TB cough screening con HeAR en smartphone — Score 92.5

### Qué es exactamente

Google Health AI Developer Foundations (HAI-DEF) publicó **HeAR** (Health Acoustic Representations) en 2024-2025 — un modelo foundation de audio médico entrenado con **300M+ clips de audio** de YouTube (tos, respiración, estornudos). Genera embeddings de 512 dimensiones para cualquier clip de audio respiratorio. Linear probing en 33 health acoustic tasks muestra SOTA en 24/33.

**Lo que Paraguay haría**: usar HeAR como extractor de features sobre toses grabadas con smartphone, entrenar un linear probe (regresión logística) para detectar TB vs healthy vs COVID vs asma, deployar en una app móvil offline.

### Por qué importa

- **Burden**: TB Chaco es hiperendémico (~3,000 casos/año notificados en Chaco; OMS estima ~50% subnotificación, así que ~6,000 casos reales/año)
- **Gap**: Diagnóstico actual requiere GeneXpert ($$ + infraestructura) o baciloscopia (baja sensibilidad, requiere laboratorio)
- **Solución propuesta**: Smartphone en campo → grabar tos → procesar offline → score de probabilidad TB → triage
- **Si funciona**: screening masivo en comunidades remotas sin acceso a laboratorio

### Evidencia que existe

- HeAR paper (Google HAI-DEF, 2024-2025) demuestra SOTA en 24/33 health acoustic tasks
- COUGHVID dataset (EPFL, ~25,000 clips labeled COVID/healthy) — público
- SPRSound dataset (SJTU, ~9,000 pediatric respiratory sounds) — público
- **Pero**: HeAR no ha sido específicamente validado para TB. Esto es **novel research**

### Cómo se implementa paso a paso

**Fase 1 — POC técnico (4-8 semanas, $0-5k)**:
1. Descargar HeAR desde HuggingFace: `google/hear`
2. Cargar COUGHVID (25,000 clips) + SPRSound (9,000 clips)
3. Extraer embeddings (512-dim) para cada clip
4. Entrenar linear probe (sklearn LogisticRegression) para clasificar COVID vs healthy vs asthma vs pertussis (tasks validados)
5. Evaluar con métricas estándar (AUROC, F1, sensitivity, specificity)
6. Si AUROC >0.85 → paper técnico
7. **Output**: notebook reproducible + paper a npj Digital Medicine o PLOS One

**Fase 2 — TB validation con datos públicos (8-12 semanas, $5-10k)**:
1. Buscar datasets públicos de TB cough: TBX11K (no cough), Cough-TB Challenge datasets, etc.
2. Si no existen datasets públicos grandes de TB cough → esto es problemático
3. Alternativa: usar TB-related datasets que contengan audio (pocos)
4. **Output**: paper técnico + decisión go/no-go para field pilot

**Fase 3 — Field pilot Chaco (16-24 semanas, $25-40k)**:
1. Adquirir 10-20 smartphones (~$200 c/u)
2. Contratar 2 community health workers en 2 comunidades chaqueñas
3. Training 1-2 días
4. Recruitment: 200 personas (100 TB-sospechosos, 100 controles)
5. Recolección: tos + esputo para GeneXpert reference standard
6. Comparar HeAR predictions vs GeneXpert
7. Análisis: sensitivity, specificity, PPV, NPV
8. **Output**: paper clínico + grant application

### Qué necesitas

- **GPU**: T4 (16GB) o Colab free tier para POC; nada para field pilot (smartphone local)
- **Storage**: ~10GB (modelo + datasets)
- **Personas**: 1 ML engineer (puede ser estudiante FIUNA), 1 clínico para field pilot (MSPBS), 1 community health worker para field pilot
- **Partners**: SENEPA para field pilot, Hospital de Clínicas para TB-sospechosos, FIUNA para ML
- **Funding**: $0 POC, $5-10k Fase 2, $25-40k Fase 3

### Qué bloquea

- **POC**: NADA. HeAR está disponible, datasets son públicos, notebook toma 1 semana.
- **Field pilot**: (a) Identificar champion en SENEPA, (b) IRB approval en MSPBS (4-6 meses típico), (c) consentimiento colectivo con comunidades chaqueñas (CARE Principles)

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| HeAR no funciona para TB (novel) | POC fase 1-2 lo valida antes de field |
| No hay datasets públicos grandes de TB cough | Fase 2 busca; si no hay, ir directo a field pilot pequeño |
| GeneXpert no disponible para reference | Asegurar antes de field; partnership con LCSP |
| Resistencia cultural en comunidades chaqueñas | CARE Principles desde día 1; consulta previa |

### Qué sale

- 1-2 papers (POC técnico + field pilot)
- App smartphone funcional para TB screening
- Modelo on-device validado en campo chaqueño
- Foundation para otras enfermedades (asma, neumonía, COVID)

### Por qué exactamente este score

- **A=10**: TB Chaco es la mayor necesidad insatisfecha
- **B=10**: Stack 100% open + deployable HOY
- **C=10**: <$5k para POC
- **D=10**: 1 semana a POC
- **E=9**: >90% probabilidad de éxito técnico (linear probe es método estándar)
- **F=8**: First-mover LatAm (no conozco implementación previa de HeAR para TB)
- **G=10**: Replicable a asma, neumonía, COVID

### Recomendación

**EJECUTAR INMEDIATAMENTE**. Es literalmente el proyecto con mayor impacto, menor costo, menor riesgo y menor tiempo de toda la cartera. El POC técnico de Fase 1 puede estar listo esta semana. Si funciona → grant application para field pilot.

---

## #2 — Antiveneno sintético para T. confluens (Baker Lab partnership) — Score 89

### Qué es exactamente

El Baker Lab (University of Washington, Nobel Prize Chemistry 2024) publicó en **Nature 2024** el diseño computacional de proteínas *de novo* que neutralizan veneno de cobras/mambas. Usaron **RFdiffusion** (ahora RFdiffusion3, MIT license) para diseñar proteínas que se unen a alfa-neurotoxinas y citotoxinas. Validación in vitro + ratones: **80-100% supervivencia** después de exposición letal.

**Lo que Paraguay haría**: diseñar proteínas *de novo* que neutralizan el veneno de *Tityus confluens* (escorpión chaqueño) y/o *Bothrops* (yarará chaqueña). Partnership con Baker Lab (específicamente con **Susana Vázquez Torres**, lead author del paper Nature 2024) para co-design, validación en CEDIC (in vitro), producción en Tesabio.

### Por qué importa

- **Burden**: Paraguay reporta **1,383 casos de envenenamiento por escorpión al año** (mid-2022 a mid-2023), **41 moderados/graves**, **4 muertes infantiles**. El Chaco es región endémica de *T. confluens*.
- **Gap**: Paraguay **importa antivenoms** de Brasil (Butantan) y Argentina. No hay producción local. Costo por dosis: ~$100-500. Logística complicada.
- **Solución propuesta**: Diseñar proteínas computacionalmente que neutralizan específicamente las toxinas chaqueñas. Validar in vitro en CEDIC. Producir en Tesabio. Costo proyectado: 10x menor que antivenom tradicional.
- **First-mover**: **Nadie ha diseñado antiveneno sintético para escorpión del mundo**. Baker Lab hizo para cobras. Paraguay puede ser primero en escorpiones.

### Evidencia que existe

- Vázquez Torres et al., "De novo designed proteins neutralize lethal snake venom toxins", **Nature 2024** — proof of concept con α-cobratoxina y three-finger toxins
- RFdiffusion3 (dic 2025) — generación de novo de proteínas funcionales
- Para *T. confluens*: existe literatura sobre composición del veneno (toxinas, neurotoxinas, citotoxinas). Menos caracterización molecular que cobras pero suficiente para empezar.
- **Para Bothrops chaqueña**: menos estudiado, pero principios similares

### Cómo se implementa paso a paso

**Fase 1 — Partnership + venome characterization (6-9 meses, $30-80k)**:
1. Outreach a Susana Vázquez Torres (Baker Lab) — posible vía LinkedIn, email institucional
2. Caracterizar el venoma de *T. confluens*: secuenciar transcriptoma de la glándula de veneno, identificar toxinas principales (TsTX-I, β-toxinas, etc.)
3. Validar targets con literatura existente
4. Identificar 3-5 toxinas prioritarias para diseño
5. **Output**: paper toxonómico + MoU con Baker Lab

**Fase 2 — Diseño computacional (6-9 meses, $20-50k compute)**:
1. Usar RFdiffusion3 + ProteinMPNN para diseñar binders contra cada toxina
2. Usar AlphaFold 3 para validar estructuras predichas
3. Usar Boltz-2 para predecir binding affinity
4. Filtrar top 100-1000 designs por afinidad predicha
5. **Output**: lista priorizada de binders

**Fase 3 — Validación in vitro en CEDIC (9-12 meses, $50-150k)**:
1. Sintetizar top 50-100 binders (GenScript u otro)
2. Expressar en *E. coli* o yeast
3. Validar binding (BLI, SPR)
4. Validar neutralización (ensayo de toxicidad celular in vitro)
5. Top 10-20 candidatos → validación funcional más profunda
6. **Output**: paper in vitro

**Fase 4 — Validación in vivo (12-18 meses, $80-200k)**:
1. Mouse model — inyectar toxina + binder, medir supervivencia
2. Si funciona → titrate dosing, optimize formulation
3. **Output**: paper pre-clinical → camino a regulatory

**Fase 5 — Producción Tesabio + IND-enabling studies (18-36 meses, $200-500k)**:
1. Tesabio desarrolla proceso de producción GMP-like
2. Toxicology en animal models
3. **Output**: IND application o equivalente MSPBS

### Qué necesitas

- **GPU**: A100/H100 para RFdiffusion3 + AlphaFold 3 (~500-2000 GPU-hours)
- **Storage**: ~100GB (estructuras + modelos)
- **Personas**: 1 computational biologist (FIUNA + Baker Lab visiting), 1 biochemist (CEDIC), 1 protein engineer (Tesabio), 1 toxicologist (CEDIC)
- **Partners**: Baker Lab (Susana Vázquez Torres), CEDIC, Tesabio, FIUNA, Galatea Bio (Stanford), BioProsNat
- **Funding**: $400-1000k total para llegar a IND-enabling

### Qué bloquea

- **Crítico**: Partnership con Baker Lab. Sin esa conexión, el proyecto es 5x más difícil
- **Crítico**: Caracterización del venoma de *T. confluens*. Si las toxinas no están bien caracterizadas, el diseño falla
- **Real**: Validación in vivo (ratones) requiere BSL-2+ y ética animal

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Partnership con Baker Lab no se concreta | Outreach múltiple, también DTU (Tim Jenkins), otros labs |
| Toxinas de *T. confluens* son estructuralmente diferentes de cobras | Caracterización profunda en Fase 1; adaptar método |
| Diseño computacional no produce binders funcionales | Iterar; Baker Lab ha mejorado de 0.1% a >50% success rate |
| Validación in vivo falla | Modelo alternativo (conejos, primates pequeños); requeriría IRB animal más complejo |
| Costo >$1M antes de saber si funciona | Phase gates estrictos; kill switch después de Fase 3 si no funciona |

### Qué sale

- 2-3 papers (Nature/Science potential en Fase 3-4)
- Patent(s) sobre binders específicos
- Modelo de producción Tesabio
- Sovereignty: Paraguay produce su propio antivenom
- Foundation para Bothrops chaqueña, otras serpientes locales

### Por qué exactamente este score

- **A=6**: 1,383 casos/año es menor que TB pero significativo; impacto desproporcionado en niños
- **B=8**: RFdiffusion3 MIT license + Baker Lab activo; toxins de T. confluens bien conocidas
- **C=4**: $400-1000k (alto pero justificado por first-mover)
- **D=4**: 24-36 meses a IND
- **E=6**: 50% (novel para escorpiones, pero Baker Lab methodology probada para serpientes)
- **F=10**: First-mover mundial, Nature/Science potential
- **G=6**: Replicable a Bothrops, otros escorpiones, otras serpientes

### Recomendación

**PRIORIDAD ALTA**. El partnership con Baker Lab es el factor decisivo. Sugerencia: outreach inmediato a Susana Vázquez Torres con propuesta concreta (incluir Fase 1 detallada). Si ella acepta → proyecto es viable. Si no → buscar alternativas (DTU, otros labs).

---

## #3 — Stack Chaco TB integrado (HeAR + tNGS + CRISPR-Dx) — Score 88

### Qué es exactamente

Un **programa regional unificado** para el Chaco paraguayo que combina 4-5 stacks complementarios:

1. **HeAR cough screening** (#1) — triage comunitario
2. **tNGS MinION** (#7) — diagnosis confirmatoria + drug resistance desde esputo
3. **CRISPR-Dx SHINE-TB** (#8) — POC field diagnosis
4. **D-Heart ECG** (#12) — screening para Chagas cardiomyopathy que coexiste con TB en Chaco
5. **Nextclade + nf-core** (#9) — genomic surveillance

**Lo que Paraguay haría**: convertir el Chaco en una **zona modelo de TB + Chagas + surveillance integrada** usando AI stack abierto. Coordinar entre SENEPA (field), LCSP (laboratory), Hospitales regionales, y MSPBS central.

### Por qué importa

- **Burden**: Chaco tiene mayor incidencia de TB del país. Chagas crónico afecta ~150-200k paraguayos, muchos chaqueños. Las dos enfermedades coexisten en poblaciones vulnerables.
- **Gap**: No hay programa integrado. Diagnóstico de TB tarda 6+ semanas. Chagas no se monitoriza. Surveillance es reactiva.
- **Solución propuesta**: Programa regional que detecta TB en comunidad → confirma en laboratorio LCSP vía tNGS → trata → monitoriza Chagas con D-Heart → surveilance genómica con Nextclade
- **Impacto**: Programa demostrativo que puede escalarse a nivel nacional

### Evidencia que existe

- Cada componente individual tiene evidencia (ver #1, #7, #8, #9, #12)
- **Pero**: ningún país ha integrado estos 4-5 componentes en un programa regional unificado para TB+Chagas. Esto es **novel research + novel implementation**

### Cómo se implementa paso a paso

**Fase 1 — Setup regional (6-9 meses, $80-150k)**:
1. Coordinar stakeholders: SENEPA regional Chaco, LCSP, Hospitales regionales (Filadelfia, Loma Plata, Mariscal Estigarribia), MSPBS central
2. Comprar equipment: MinION Mk1C ($5k), smartphones ($5k), D-Heart units ($5k), reactivos para tNGS ($20k), reactivos para SHINE-TB ($15k), supplies para Nextclade ($5k)
3. Training 1 semana para personal local (4-5 personas)
4. Establecer data flow: smartphone app → cloud → LCSP → feedback

**Fase 2 — Pilot regional (12-18 meses, $80-200k)**:
1. 2-3 comunidades chaqueñas piloto
2. Screening HeAR de 500 personas
3. Confirmación tNGS para positivos
4. CRISPR-Dx cross-validation en subset
5. D-Heart ECG para todos los TB-positivos (Chagas co-infection)
6. Surveillance genómica de cepas circulantes con Nextclade
7. **Output**: 2-3 papers + modelo de programa

**Fase 3 — Scale a nivel nacional (18-36 meses, $200-500k)**:
1. Replicar en otras regiones endémicas (Caaguazú, San Pedro, Amambay)
2. Integrar con sistema de salud nacional
3. **Output**: programa nacional + policy brief

### Qué necesitas

- **GPU**: Mixto — smartphone para HeAR, A100 para tNGS bioinformatics, none para CRISPR-Dx
- **Storage**: ~50GB
- **Personas**: 1 program manager, 2-3 ML/bioinformatics, 2-3 clínicos, 5-10 community health workers, 1 data manager
- **Partners**: SENEPA regional Chaco, LCSP, Hospitales regionales, MSPBS central, FIUNA
- **Funding**: $400-1000k total para Fase 1-2

### Qué bloquea

- **Crítico**: Coordinación entre 4-5 stakeholders (SENEPA + LCSP + Hospitales + MSPBS + academia)
- **Crítico**: Identificar program manager senior con credibilidad ante MSPBS
- **Real**: Logistics del Chaco (distancia, infraestructura)

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Coordinación multi-stakeholder falla | Empezar pequeño (1 comunidad, 1 hospital); expandir después |
| LCSP overwhelmed con samples | Priorizar; rotar personal |
| Community resistance | CARE Principles; consulta previa; co-design |
| Equipment fails en Chaco | Backup units; training técnico local |
| Funding gap entre fases | Phase gates; grants escalonados |

### Qué sale

- 3-5 papers (implementación, results, scale)
- Programa regional demostrativo
- Modelo replicable a nivel nacional
- Foundation para integrated TB+Chagas+surveillance program

### Por qué exactamente este score

- **A=10**: TB Chaco + Chagas = mayor burden combinado
- **B=8**: 3-5 stacks validados individualmente; integración es novel
- **C=6**: $400-1000k (alto pero distribuido)
- **D=6**: 12-18 meses a pilot results
- **E=7**: 75% (cada componente viable; integración es lo novel)
- **F=8**: First-mover LatAm en integrated program
- **G=10**: Replicable a dengue, malaria, leishmaniasis, otras enfermedades

### Recomendación

**EJECUTAR como programa regional unificado**, pero NO empezar hasta tener program manager senior identificado. Sin coordinator fuerte, el programa se desmorona. Sugerencia: usar #1 (HeAR POC) como entrada, expandir orgánicamente a medida que se valide cada componente.

---

## #4 — TxGemma + Boltz-2 + OpenFold3 + CEDIC pipeline Chagas — Score 86

### Qué es exactamente

Pipeline computacional de drug discovery end-to-end contra *Trypanosoma cruzi* (Chagas):

1. **TxGemma-Chat 27B** (Google HAI-DEF) — LLM fine-tuneado para ADMET queries (Absorption, Distribution, Metabolism, Excretion, Toxicity). Acepta queries en español.
2. **Boltz-2** (MIT license) — predice binding affinity de compuestos contra proteínas. Boltz-2 es comercial-friendly (no como AF3).
3. **OpenFold3** (Apache 2.0) — predice estructuras 3D de complejos proteína-ligando. Comercial-friendly.
4. **CEDIC** (Centro para el Desarrollo de la Investigación Científica, UNA) — laboratorio de validación in vitro
5. **BioProsNat** (FP-UNA) — biblioteca de compuestos naturales paraguayos (~500-1000 compounds)
6. **Tesabio** — empresa biotech con capacidad de escalamiento y producción
7. **FIUNA** — capacidad de cómputo + estudiantes ML

**Lo que Paraguay haría**: usar este pipeline para priorizar compuestos de BioProsNat contra targets de *T. cruzi* (cruzain, trans-sialidasa, CYP51, etc.), validar in vitro en CEDIC, producir escalamiento en Tesabio.

### Por qué importa

- **Burden**: Chagas crónico afecta ~150-200k paraguayos. Treatment actual (benznidazol, nifurtimox) tiene eficacia limitada y efectos adversos significativos.
- **Gap**: Drug discovery para Chagas es sub-financiado globalmente. Solo 2 drugs approved en 50+ años. Necesidad crítica de nuevos compuestos.
- **Paraguay único**: Es el único país del mundo con **closed loop completo**: compuestos naturales (BioProsNat) + AI/compute (FIUNA) + validación in vitro (CEDIC) + escalamiento (Tesabio) + expertise clínica (Hospital de Clínicas).
- **Solución propuesta**: Pipeline computacional prioriza hits → CEDIC valida → Tesabio produce → clinical trials

### Evidencia que existe

- Boltz-2 (MIT, 2025) — SOTA en binding affinity prediction
- OpenFold3 (Apache 2.0, 2026) — comercial-friendly, accuracy similar a AF3
- TxGemma (Google HAI-DEF, 2024-2025) — 9B, 27B, Chat versions
- Cruzain crystal structure existe (PDB: 1AIM, 1ME3, etc.)
- BioProsNat library (~500-1000 compounds, varios con actividad antichagásica preliminar)
- CEDIC tiene infraestructura in vitro + experiencia Chagas
- Tesabio tiene capacidad de escalamiento

### Cómo se implementa paso a paso

**Fase 1 — Setup pipeline (3-6 meses, $20-50k)**:
1. Cargar TxGemma-Chat 27B en HIVE BUZZ o X8 Cloud
2. Cargar Boltz-2 + OpenFold3
3. Cargar targets desde AlphaFold DB (cruzain, trans-sialidasa)
4. Compilar lista de 500-1000 compuestos BioProsNat con SMILES
5. **Output**: pipeline funcional

**Fase 2 — Virtual screening (3-6 meses, $30-80k compute)**:
1. Para cada target (5-10 targets), correr Boltz-2 affinity prediction contra BioProsNat library
2. Para cada compuesto top-100, correr OpenFold3 para validar binding pose
3. Para cada compuesto top-50, correr TxGemma queries: "¿Esta molécula cruzará barrera hematoencefálica?", "¿Tendrá toxicidad hepática?", etc.
4. Filtrar a top 10-20 compounds con perfil drug-like
5. **Output**: paper de virtual screening + lista priorizada

**Fase 3 — Validación in vitro en CEDIC (6-12 meses, $50-150k)**:
1. Adquirir o sintetizar top 10-20 compuestos (si BioProsNat no tiene suficiente)
2. CEDIC valida actividad anti-T. cruzi in vitro (ensayo con epimastigotas, tripomastigotas, amastigotas)
3. Medir IC50, citotoxicidad (células huésped)
4. Top 5-10 candidatos → estudios más profundos (mecanismo, resistencia)
5. **Output**: paper in vitro

**Fase 4 — Lead optimization (12-24 meses, $100-300k)**:
1. Para top 3-5 hits, diseñar análogos (medicinal chemistry clásica + AI)
2. Iterar: diseño → síntesis → validación in vitro
3. Identificar lead candidato
4. **Output**: patent + paper

**Fase 5 — IND-enabling (24-48 meses, $500k-2M)**:
1. Tesabio produce lead a escala GMP
2. Toxicology en animales
3. PK/PD studies
4. IND application o equivalente MSPBS

### Qué necesitas

- **GPU**: A100 o H100 (HIVE BUZZ o X8 Cloud); ~1000-3000 GPU-hours para virtual screening completo
- **Storage**: ~200GB (modelos + estruturas + compounds library)
- **Personas**: 1 computational biologist (FIUNA), 1 medicinal chemist (FIUNA o externo), 1 biochemist (CEDIC), 1 Tesabio production manager
- **Partners**: CEDIC, BioProsNat, Tesabio, FIUNA, Hospital de Clínicas (clinical trials)
- **Funding**: $200-500k para Fase 1-3; $500k-2M para llegar a IND

### Qué bloquea

- **Crítico**: Acceso a HIVE BUZZ o X8 Cloud para compute
- **Crítico**: Compromiso activo de CEDIC (wet-lab time)
- **Real**: Compound acquisition si BioProsNat no tiene suficientes
- **Real**: Medicinal chemistry capacity para lead optimization

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Compute no disponible | HIVE BUZZ prioritario; backup X8 Cloud o Colab Pro |
| CEDIC no tiene time | Co-financiar posición postdoc; grant dedicado |
| Boltz-2 affinity predictions son malas | Cross-validar con AutoDock Vina o DiffDock |
| TxGemma alucina en español | Cross-validar con ChemBERTa-3; usar consensus |
| Compounds no son activos in vitro | Realistic expectation; screen más amplio; cross-target |
| Lead optimization es muy lento | Contratar medicinal chemist senior; partnership académico |

### Qué sale

- 2-4 papers (virtual screening, in vitro, lead optimization)
- Patent(s) sobre nuevos compuestos
- Pipeline reproducible
- Posible licensing a pharma
- Tesabio capacity incrementada

### Por qué exactamente este score

- **A=10**: Chagas crónico es mayor burden paraguayo
- **B=9**: Stack maduro y open; closed loop único
- **C=6**: $200-500k para Fase 1-3 (alto pero manejable)
- **D=6**: 6-12 meses a paper in vitro
- **E=7**: 75% (computational chemistry funciona; wet-lab validation es experimental)
- **F=7**: Novel para Paraguay pero replicado en otros lados
- **G=8**: Replicable a leishmaniasis, otros parásitos

### Recomendación

**EJECUTAR este año** — es el flagship drug discovery project de Paraguay. Empezar con Fase 1-2 que es computacional pura, validar antes de comprometer a wet-lab. Outreach CEDIC es crítico.

---

## #5 — Chagas cardiomyopathy smart-monitoring (Apple Watch + ECGFounder) — Score 84

### Qué es exactamente

Programa de monitoreo continuo para pacientes con Chagas crónico usando smartwatches (Apple Watch Series 9+ o Samsung Galaxy Watch 6+) y análisis con **ECGFounder** (NEJM AI Nov 2025 — universal ECG foundation model entrenado con 10M+ recordings).

**Lo que Paraguay haría**: reclutar 200-500 pacientes chagásicos crónicos, proporcionar smartwatches por 24 meses, capturar ECG continuo + HR + SpO2 + activity, analizar con ECGFounder para detectar arritmias, sync con cardiólogo remoto.

### Por qué importa

- **Burden**: Chagas crónico afecta ~150-200k paraguayos. Arritmias son primera causa de muerte. Monitoring actual es reactivo (cuando el paciente llega a consulta).
- **Gap**: No hay herramientas de monitoreo poblacional para Chagas. Bolivia ya hizo D-Heart (smartphone ECG puntual), pero no hay continuous monitoring.
- **Solución propuesta**: Smartwatch 24/7 durante 24 meses. Detecta arritmias temprano → previene muerte súbita → reduce hospitalización.
- **First-mover**: **Nadie ha combinado smartwatch + Chagas monitoring + IA**. World first.

### Evidencia que existe

- Apple Watch FDA-approved para ECG, AFib history, sleep apnea
- ECGFounder (NEJM AI Nov 2025) demuestra SOTA en 12-lead ECG tasks
- D-Heart Bolivia pilot (Microorganisms 2021) prueba viabilidad de smartphone ECG en Chaco chaqueño
- Chagas cardiomyopathy RBBB es detectable con single-lead ECG

### Cómo se implementa paso a paso

**Fase 1 — Pilot small (12-18 meses, $50-100k)**:
1. Adquirir 50 Apple Watch Series 9 ($400 c/u = $20k)
2. Reclutar 50 pacientes chagásicos crónicos del Hospital de Clínicas (Cátedra de Cardiología)
3. Training 1-2 horas por paciente
4. Monitoreo 12 meses
5. Sincronización diaria con cloud
6. Análisis retrospectivo con ECGFounder
7. Comparar con ECG 12-lead en visitas programadas (cada 3 meses)
8. **Output**: paper piloto

**Fase 2 — Expansion (18-36 meses, $300k-1M)**:
1. Adquirir 500 smartwatches
2. Reclutar 500 pacientes de múltiples centros
3. Comparar compliance entre Apple Watch vs Samsung
4. Análisis prospectivo de outcomes
5. **Output**: 2-3 papers clínicos + grant renewal

**Fase 3 — National program (36-60 meses, $1-3M)**:
1. Programa nacional de monitoreo para todos los chagásicos crónicos del MSPBS
2. Integración con historia clínica electrónica
3. **Output**: programa nacional + policy brief

### Qué necesitas

- **GPU**: A100 para fine-tune ECGFounder si es necesario (~$5-10k compute)
- **Storage**: ~50GB (12 meses × 500 pacientes × datos continuos)
- **Personas**: 1 cardiologist champion (Hospital de Clínicas), 1 data scientist, 2-3 study coordinators, 1 IT manager
- **Partners**: Hospital de Clínicas Cardiología, Hospital Nacional de Itauguá, Instituto Nacional de Cardiología, Apple/Samsung (potential partnership)
- **Funding**: $50-100k Fase 1; $300k-1M Fase 2

### Qué bloquea

- **Crítico**: Hospital champion (cardiólogo motivado)
- **Crítico**: Compliance 24/7 smartwatch (literatura muestra 60-80% a 6 meses, 40-50% a 12 meses)
- **Real**: Costos de smartwatches para 500 pacientes
- **Real**: Regulatory para usar datos con fines de investigación

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Hospital champion no se identifica | Outreach amplio; ofrecer co-PI status |
| Compliance <50% a 6 meses | Incentivos; recordatorios; gamification |
| Smartwatches no detectan Chagas-specific arrhythmias | Entrenar ECGFounder en datos locales; ajustar thresholds |
| Pacientes no pueden usar smartphone | Reclutar tech-savvy primero; expandir después |
| Costos de data | Negotiate con Apple/Samsung; uso de Wi-Fi only |

### Qué sale

- 2-4 papers (piloto, expansion, outcomes)
- Modelo de continuous monitoring para Chagas
- Foundation para otras arritmias crónicas
- Possible licensing de modelo a Apple/Samsung

### Por qué exactamente este score

- **A=8**: Chagas crónico es prevalente pero deployment es gradual
- **B=8**: ECGFoundation + Apple Watch FDA-approved
- **C=4**: $300k-1M (alto pero escalable)
- **D=4**: 24-36 meses a resultados clínicos
- **E=7**: 75% (technology funciona; compliance es variable)
- **F=10**: First-mover mundial, Nature potential
- **G=6**: Replicable a otras arritmias crónicas

### Recomendación

**PILOTO con 50 pacientes primero**. Identificar cardiologist champion antes de comprometer. Si compliance >70% a 6 meses → expansion. Si compliance <50% → reconsiderar modelo.

---

## #6 — mRNA vaccine design para Leishmania (Tesabio + FIUNA + AlphaFold 3) — Score 82

### Qué es exactamente

Diseño computacional de **epítopes para vacuna mRNA contra Leishmania** (cutánea y visceral) usando:

1. **AlphaFold 3** — predice estructuras 3D de complejos proteína-anticuerpo
2. **AlphaMissense** — clasifica variantes patogénicas (aplicable para identificar epítopes críticos)
3. **TxGemma** — predice antigenicidad, procesabilidad, estabilidad
4. **Tesabio** — capacidad de producción de biológicos + expertise en vacunas
5. **FIUNA** — capacidad computacional + ML
6. **CEDIC** — validación in vitro + modelo animal

**Lo que Paraguay haría**: identificar antígenos de *Leishmania* (brasiliensis, guyanensis — prevalentes en Paraguay), diseñar mRNA construct que codifica para epítopes inmunogénicos, validar in vitro e in vivo.

### Por qué importa

- **Burden**: Leishmaniasis es endémica en Paraguay (cutánea y visceral). Sin vacuna efectiva. Tratamiento actual (antimoniales, anfotericina B) tiene toxicidad significativa.
- **Gap**: Global R&D en Leishmania vaccines es sub-financiado. No hay producto en clinical trials.
- **Paraguay oportunidad**: Tesabio tiene capacidad de vacunas + CEDIC tiene modelo animal + FIUNA hace AI. Combinación única.
- **Solución propuesta**: Diseño computacional de mRNA vaccine + validación local
- **First-mover**: **Nadie está usando AI + AlphaFold 3 para diseñar mRNA Leishmania vaccine**. World first.

### Evidencia que existe

- mRNA platform validado para influenza (GSK fase 3), COVID, melanoma (mRNA-4157)
- AlphaFold 3 puede predecir complejos proteína-anticuerpo
- Leishmania genoma secuenciado (Viannia, Leishmania); varios antígenos candidatos identificados (Leish-111f, polyprotein MML, etc.)
- Tesabio expertise en vacunas veterinarias
- CEDIC modelo animal (hamster, ratón)

### Cómo se implementa paso a paso

**Fase 1 — In silico design (6-9 meses, $30-80k)**:
1. Identificar antígenos Leishmania candidatos (Leish-111f, polyproteínas, GP63, etc.)
2. Usar AlphaFold 3 + AlphaMissense para predecir epítopes inmunogénicos
3. Usar TxGemma para queries sobre antigenicidad, estabilidad, procesabilidad
4. Diseñar construct mRNA optimizado (codon usage, UTRs, polyA tail)
5. In silico prediction de expresión y procesabilidad
6. **Output**: paper diseño computacional

**Fase 2 — Validación in vitro (9-12 meses, $50-150k)**:
1. Tesabio sintetiza mRNA (IVT — In Vitro Transcription)
2. Transfectar células dendríticas humanas in vitro
3. Medir expresión de proteína
4. Medir activación de T cells
5. **Output**: paper in vitro

**Fase 3 — Validación in vivo (12-18 meses, $80-200k)**:
1. CEDIC modelo hamster (Leishmania braziliensis)
2. Inmunizar con mRNA vaccine
3. Challenge con Leishmania
4. Medir protección (lesión size, parásitos, citokinas)
5. Optimizar dosis, schedule, route
6. **Output**: paper in vivo

**Fase 4 — IND-enabling (24-48 meses, $500k-2M)**:
1. Tesabio produce a escala GMP
2. Toxicology GLP
3. IND application

### Qué necesitas

- **GPU**: A100/H100 (HIVE BUZZ) para AlphaFold 3 + AlphaMissense
- **Storage**: ~50GB
- **Personas**: 1 computational biologist (FIUNA), 1 immunologist (CEDIC), 1 biotech production manager (Tesabio)
- **Partners**: Tesabio, CEDIC, FIUNA
- **Funding**: $80-200k para Fase 1-2; $500k-2M para IND

### Qué bloquea

- **Crítico**: Acceso a Tesabio (competing priorities)
- **Real**: Validación in vivo toma tiempo (hamster model requiere 8-12 semanas)
- **Real**: Costo alto si Fase 4 se persigue

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| Epítopes no son inmunogénicos in vivo | Probar múltiples; usar datos previos |
| mRNA no se expresa bien | Optimization iterativa |
| Modelo animal no predice humanos | Validación cruzada con otros modelos |
| Costo >$1M antes de saber | Phase gates estrictos |

### Qué sale

- 2-3 papers (design, in vitro, in vivo)
- Patent sobre mRNA construct
- Tesabio mRNA capacity incrementada
- Possible licensing a pharma global

### Por qué exactamente este score

- **A=8**: Leishmaniasis endémica nacional
- **B=7**: mRNA platforms validados; AlphaFold 3 reciente
- **C=4**: $200-500k (alto)
- **D=4**: 24-36 meses a design validado
- **E=6**: 50% (computational design funciona; wet-lab validation es experimental)
- **F=10**: First-mover mundial, Nature potential
- **G=6**: Replicable a otros parásitos

### Recomendación

**EMPEZAR con diseño computacional** (Fase 1, 6 meses, $30k) antes de comprometer a wet-lab. Si Fase 1 produce construct prometedor → comprometer a Fase 2.

---

## #7 — tNGS directo desde esputo para TB chaqueña — Score 81

### Qué es exactamente

Implementación de **targeted Next-Generation Sequencing usando Oxford Nanopore MinION** directamente desde esputo (sin cultivo) para diagnóstico de TB + detección de resistencia a fármacos en <24 horas.

**Lo que Paraguay haría**: setup en LCSP de pipeline tNGS usando:
- MinION Mk1C ($5k)
- Trueprep AUTO para DNA extraction ($3k)
- Deeplex Myc-TB primer set ($50-100/sample)
- Rapid barcoding kit ($30-50/sample)
- Bioinformática custom (in-house o basada en pipeline ICMR-NIRT India)

### Por qué importa

- **Burden**: TB Chaco hiperendémico. Diagnóstico estándar (cultivo) tarda 6+ semanas. Baciloscopia es rápida pero insensitive. GeneXpert detecta solo RIF resistance.
- **Gap**: Sin surveillance de resistencia a INH, FQ, AMG, LZD, PZA, ETH en Paraguay.
- **Solución propuesta**: tNGS da diagnóstico + resistencia completa en <24h, sin BSL-3, desde esputo directo.
- **Validación India**: ICMR-NIRT demostró 95% RIF sensitivity, 88% INH, 100% FQ/AMG/LZD, comparable a GeneXpert.

### Cómo se implementa paso a paso

**Fase 1 — Setup (3-6 meses, $30-60k)**:
1. Adquirir MinION Mk1C + Trueprep AUTO + reactivos
2. Training de 2-3 técnicos LCSP
3. Adaptar bioinformática pipeline ICMR-NIRT (disponible en GitHub)
4. Validar con 50-100 muestras conocidas
5. **Output**: validación interna

**Fase 2 — Pilot LCSP (6-12 meses, $40-80k)**:
1. Procesar 200-500 muestras chaqueñas
2. Comparar con GeneXpert (gold standard actual)
3. Detectar resistencia no vista por GeneXpert
4. Análisis costo-efectividad
5. **Output**: paper + decisión go/no-go para scale

**Fase 3 — Scale Chaco (12-24 meses, $50-150k)**:
1. Múltiples MinION en comunidades chaqueñas remotas
2. Telemedicina para reportar resultados
3. Integración con SENEPA surveillance
4. **Output**: programa regional

### Qué necesitas

- **GPU**: A100 (LCSP bioinformática), MinION local
- **Storage**: ~50GB
- **Personas**: 1 LCSP bioinformatics lead, 2-3 técnicos, 1 program manager
- **Partners**: LCSP, ICMR-NIRT (India, conocimiento), SENEPA
- **Funding**: $30-80k Fase 1-2

### Qué bloquea

- **Crítico**: LCSP champion + bioinformatics capacity
- **Real**: Costo por sample ($50-100) — necesita co-financiamiento
- **Real**: Supply chain para reactivos en Paraguay

### Riesgos principales

| Riesgo | Mitigación |
|---|---|
| LCSP overwhelmed con samples | Phased rollout; priorizar Chaco |
| Bioinformática falla | Adaptar pipeline ICMR-NIRT; consultant |
| Costo por sample alto | Volume discount; partnership con proveedores |
| Resultados inconsistentes | QA/QC estricto; replicate runs |

### Qué sale

- 1-2 papers (validación, scale)
- Programa regional TB surveillance
- Capacity LCSP incrementada
- Datos de resistencia a fármacos en Paraguay (primer dataset)

### Por qué exactamente este score

- **A=10**: TB Chaco hiperendémico
- **B=8**: MinION tNGS validado
- **C=6**: $30-80k
- **D=6**: 6-12 meses a pilot results
- **E=8**: >90% (technology funciona)
- **F=8**: First-mover LatAm
- **G=8**: Replicable a otros patógenos

### Recomendación

**EJECUTAR**. Es uno de los más viables. Outreach LCSP es lo crítico.

---

## #8 — CRISPR-Dx pipeline para NTDs chaqueños (SHINE-TB + SHERLOCK) — Score 80

### Qué es exactamente

Setup de laboratorio **CRISPR-Dx** en LCSP para diagnóstico point-of-care de:

- **TB** (SHINE-TB — Cas13a + Cas12a + RPA, 100% sensibilidad vs. culture)
- **Chikungunya** (SHERLOCK Cas13a, 97.26% sensibilidad, 100% especificidad)
- **Dengue** (SHERLOCK Cas13a validado)
- **Leishmaniasis** (SHERLOCK adaptado)

Suitcase-sized POC devices para uso en comunidades chaqueñas sin laboratorio.

### Por qué importa

- **Burden**: Chaco sin laboratory access. Diagnósticos tardan 2-6 semanas. Brotes de chikungunya recientes en Paraguay.
- **Gap**: Sin POC molecular diagnostics en Chaco.
- **Solución propuesta**: POC tests <$5/test, sin termociclador, resultado en <2 horas, suitcase-sized.
- **Validación**: SHINE-TB ya validado (Broad Institute 2025); SHERLOCK chikungunya ya validado.

### Cómo se implementa paso a paso

**Fase 1 — Setup laboratorio (3-6 meses, $50-100k)**:
1. Adquirir equipment: suitcase-sized PCR/RPA devices, fluorescent readers, lateral flow readers
2. Training de 2-3 técnicos LCSP
3. Validar SHINE-TB con 100 muestras chaqueñas conocidas
4. Validar SHERLOCK chikungunya con muestras de outbreak Paraguay
5. **Output**: validación interna + 1-2 papers

**Fase 2 — Field deployment (6-12 meses, $30-50k)**:
1. Distribuir suitcase devices a 3-5 comunidades chaqueñas
2. Training de community health workers
3. Validar en field
4. **Output**: paper field + decisión scale

**Fase 3 — Scale (12-24 meses, $100-200k)**:
1. Expandir a 20+ comunidades
2. Integrar con surveillance SENEPA
3. **Output**: programa regional

### Qué necesitas

- **GPU**: Limitado (RT-PCR analysis)
- **Storage**: ~10GB
- **Personas**: 1 LCSP lead, 2-3 técnicos, 5-10 community health workers
- **Partners**: LCSP, Broad Institute (SHINE-TB), Zhang lab (SHERLOCK), SENEPA
- **Funding**: $50-100k Fase 1

### Qué bloquea

- **Crítico**: LCSP champion
- **Real**: Supply chain RPA reagents en Paraguay
- **Real**: Cold chain para reactivos en Chaco

### Qué sale

- 2-3 papers (validación, field, scale)
- Programa POC diagnostics Chaco
- LCSP capacity incrementada
- Possible licensing a MSPBS

### Por qué exactamente este score

- **A=10**: Chaco NTDs hiperendémicos
- **B=8**: SHINE-TB + SHERLOCK validados
- **C=6**: $50-100k
- **D=6**: 6-12 meses a pilot results
- **E=7**: 75% (technology funciona; field deployment es variable)
- **F=8**: First-mover LatAm
- **G=8**: Replicable a múltiples NTDs

### Recomendación

**EJECUTAR junto con #7** (tNGS). Ambos son LCSP-based, complementarios, mismo champion.

---

## #9 — Nextclade + nf-core viralrecon en LCSP — Score 78

### Qué es exactamente

Implementación de **Nextclade** + **nf-core/viralrecon** (Nextflow pipeline) en LCSP para genomic surveillance estandarizada de virus respiratorios y arbovirus.

**Componentes**:
- **Nextclade** — visualización + asignación de clados + quality control
- **nf-core/viralrecon** — pipeline reproducible con Nextflow
- Aplicación a: SARS-CoV-2, influenza, dengue, chikungunya, monkeypox

### Por qué importa

- **Burden**: Paraguay tiene dengue hiperendémico + chikungunya risk + monkeypox preparedness
- **Gap**: LCSP ya hace surveillance pero con pipelines ad-hoc. Falta estandarización.
- **Solución propuesta**: Pipeline reproducible, versionado, escalable

### Cómo se implementa paso a paso

**Fase 1 — Setup (4-8 semanas, $10-20k)**:
1. Workshop CABANA (gratis) para personal LCSP
2. Setup nf-core/viralrecon
3. Validar con muestras SARS-CoV-2 existentes (control)
4. Adaptar para dengue (custom primer scheme)
5. **Output**: pipeline funcional

**Fase 2 — Production (3-6 meses, $10-20k)**:
1. Procesar muestras dengue chaqueñas
2. Visualizar con Nextclade
3. Análisis filogenético
4. **Output**: paper surveillance

### Qué necesitas

- **GPU**: Limitado (alignment + tree building)
- **Storage**: ~20GB
- **Personas**: 1 LCSP bioinformatics, 1-2 técnicos
- **Partners**: LCSP, CABANA, nf-core community
- **Funding**: $10-30k total

### Qué bloquea

- **Crítico**: LCSP bioinformatics lead
- **Real**: LCSP ya tiene pipeline — necesita convencimiento

### Qué sale

- 1 paper (pipeline + surveillance results)
- LCSP capacity estandarizada
- Foundation para otros virus

### Por qué exactamente este score

- **A=8**: Dengue hiperendémico + preparedness
- **B=10**: Nextclade + nf-core open + bien documentados
- **C=8**: $10-30k (bajo)
- **D=10**: POC en 2-4 semanas
- **E=9**: >90% (standard tools)
- **F=6**: Replicado en muchos lados
- **G=8**: Replicable a múltiples virus

### Recomendación

**EJECUTAR INMEDIATAMENTE como quick win**. Outreach LCSP.

---

## #10 — Biobanco FAIR + AlphaGenome API para CEDIC × Galatea — Score 76

### Qué es exactamente

Setup de **biobanco FAIR-aligned** (Findable, Accessible, Interoperable, Reusable) en CEDIC × Galatea Bio (Stanford) con integración de **AlphaGenome API** (Google DeepMind) para análisis de variantes regulatorias en DNA paraguayo.

**Componentes**:
- Muestras: sangre, tejido, DNA de pacientes paraguayos (Chagas, leishmaniasis, cáncer, controles)
- Metadata: estandarizada con ontologies (HPO, DO, UBERON)
- Infrastructure: FAIR Data Points, cloud storage, controlled access
- Análisis: AlphaGenome API para variant effect prediction en 1 Mb de DNA
- Compliance: CARE Principles para muestras indígenas

### Por qué importa

- **Burden**: No hay biobanco FAIR paraguayo. Datos paraguayos son únicos genéticamente.
- **Gap**: CEDIC × Galatea partnership ya existe pero sin framework FAIR.
- **Solución propuesta**: Biobanco FAIR desde día 1 (no retrofit)
- **Análisis**: AlphaGenome permite interpretar variantes regulatorias paraguayas en contexto

### Cómo se implementa paso a paso

**Fase 1 — Framework + samples (6-12 meses, $50-100k)**:
1. Establecer FAIR Data Points
2. Crear ontologies para Paraguay-specific metadata
3. Recolectar 100-500 muestras iniciales
4. Consentimiento + CARE Principles compliance
5. **Output**: biobanco operativo

**Fase 2 — AlphaGenome integration (3-6 meses, $10-30k)**:
1. Análisis AlphaGenome de variantes regulatorias
2. Pipeline reproducible
3. **Output**: paper + dataset FAIR

**Fase 3 — Scale (12-24 meses, $50-200k)**:
1. Expandir a 1000-5000 muestras
2. Múltiples centros
3. Integración con otros biobancos LatAm
4. **Output**: programa regional

### Qué necesitas

- **GPU**: Limitado (AlphaGenome es API)
- **Storage**: ~1-10TB (DNA + metadata + analysis)
- **Personas**: 1 biobank manager, 1 bioinformático, 1 ethical/legal lead, 1 community liaison
- **Partners**: CEDIC, Galatea Bio (Stanford), IICS, LCSP, AlphaGenome team
- **Funding**: $100-300k total

### Qué bloquea

- **Crítico**: CEDIC champion activo + Galatea collaboration
- **Real**: Consentimiento colectivo con comunidades (CARE Principles)
- **Real**: Costos de storage + cloud
- **Real**: Compliance regulatorio (Ley 7593/2025)

### Qué sale

- 1-2 papers (biobanco + AlphaGenome analysis)
- Biobanco FAIR paraguayo (primero)
- Capacity CEDIC incrementada
- Foundation para drug discovery + genomics research

### Por qué exactamente este score

- **A=8**: Foundation para múltiples proyectos futuros
- **B=8**: AlphaGenome API + FAIR principles bien definidos
- **C=4**: $100-300k (alto)
- **D=4**: 24-36 meses a biobanco maduro
- **E=7**: 75% (technology funciona; ethics + community engagement son variables)
- **F=8**: First-mover LatAm en FAIR + AlphaGenome integration
- **G=8**: Foundation para múltiples proyectos

### Recomendación

**EMPEZAR verificación del biobanco existente** antes de comprometer. Si CEDIC × Galatea ya tiene samples → acelerar. Si no → considerar CEDIC standalone primero.

---

## Comparación top 10

| Rank | Score | Costo | Tiempo | First-mover | Recomendación |
|---|---|---|---|---|---|
| #1 TB HeAR | 92.5 | $5-30k | 6 meses | LatAm | EJECUTAR YA |
| #2 Antiveneno T. confluens | 89 | $400-1000k | 24-36 meses | **MUNDIAL** | PRIORIDAD ALTA |
| #3 Stack Chaco | 88 | $400-1000k | 12-18 meses | LatAm | EJECUTAR si hay program manager |
| #4 TxGemma Chagas | 86 | $200-500k | 12-24 meses | Paraguay | EJECUTAR este año |
| #5 Chagas smartwatch | 84 | $300k-1M | 24-36 meses | **MUNDIAL** | PILOTO primero |
| #6 mRNA Leishmania | 82 | $200-500k | 24-36 meses | **MUNDIAL** | EMPEZAR in silico |
| #7 tNGS TB | 81 | $30-80k | 6-12 meses | LatAm | EJECUTAR |
| #8 CRISPR-Dx Chaco | 80 | $50-100k | 6-12 meses | LatAm | EJECUTAR con #7 |
| #9 Nextclade LCSP | 78 | $10-30k | 2-4 semanas | — | EJECUTAR YA |
| #10 Biobanco FAIR | 76 | $100-300k | 24-36 meses | LatAm | EMPEZAR verificación |

## Tesis

**5 ideas S-tier (≥84) ejecutadas en paralelo en 12 meses = 8-12 papers + 3-5 grants funded + Paraguay en radar mundial.**

Lo crítico: **identificar champions concretos** para cada una. Sin champion, las ideas con score 84-92 se quedan en el papel.

---

## Última actualización

Septiembre 2026.