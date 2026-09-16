# Áreas de investigación prioritarias

Documento vivo. Cada área se desarrolla en su carpeta propia dentro de `areas/`.

---

## Cómo leer este documento

Para cada área listamos:

- **Problema concreto en Paraguay** — qué duele hoy.
- **Capacidades locales existentes** — quién ya trabaja en esto y con qué.
- **Herramientas de código abierto relevantes** — qué existe, qué se puede bajar y correr.
- **Primer proyecto concreto** — el deliverable más pequeño que probaría valor.
- **Vacíos de información** — qué no sabemos todavía y cómo investigarlo.

La priorización sigue tres ejes: (a) impacto real en salud pública paraguaya, (b) factibilidad con las capacidades locales actuales, (c) ventana de tiempo antes de que otro actor tome la oportunidad.

---

## 1. Vigilancia genómica de patógenos

**Problema.** Paraguay tiene vigilancia genómica activa (LCSP opera Illumina MiSeq y nanopore para dengue, SARS-CoV-2, monkeypox, rotavirus) pero el análisis depende de pipelines ad-hoc, no estandarizados, no reproducibles. Cada outbreak requiere reconstruir el flujo bioinformático desde cero.

**Capacidades locales.**

- LCSP (Ministerio de Salud Pública) opera la Red de Vigilancia Genómica (Resolución Ministerial 875) que incluye IICS, FCQ-UNA, UNCA, CEDIC y Cyrlab.
- IICS tiene experiencia publicada en filodinámica de dengue (99 genomas 2014–2022), secuenciación de MPXV (30 genomas línea IIb), espiroquetas de Chagas.
- CONACYT financió un MinION portátil para IICS durante la emergencia COVID-19 (demuestra que el sistema puede moverse rápido).

**Herramientas de código abierto.**

- **Nextclade** — asignación de clado, ya usado en la publicación paraguaya de MPXV.
- **Augur + Auspice** (Nextstrain) — visualización filodinámica estándar.
- **nf-core/viralrecon** — pipeline automatizado para virus respiratorios.
- **nf-core/ampliseq** — amplicones (lo que usa LCSP para SARS-CoV-2).
- **Pangolin** — linaje SARS-CoV-2.
- **Genome Detective** — usado por LCSP en publicaciones previas.
- **ViralFlow, V-pipe** — alternativas de pipeline completo.

**Primer proyecto concreto.** Instalar Nextclade + Augur + nf-core/viralrecon en un servidor de LCSP, escribir SOPs en español, correr un taller de 2 días para bioinformáticos del LCSP/IICS. Entregable: dashboard público actualizado cuando llegue un nuevo genoma. Costo estimado: bajo (~$5k viajes + honorarios facilitador externo, p.ej. CABANA).

**Vacíos de información.**

- ¿Cuántas secuencias crudas tiene LCSP sin publicar?
- ¿Qué pipeline usan actualmente? ¿Galaxy? ¿línea de comandos?
- ¿Hay capacidad local para mantener un servidor Nextstrain?
- ¿Cuál es el ancho de banda real de LCSP?

---

## 2. Descubrimiento de fármacos para enfermedades desatendidas

**Problema.** Paraguay tiene alrededor de 165.000 personas infectadas con *Trypanosoma cruzi* (Chagas) y es endémico en leishmaniasis. La mayoría de los fármacos actuales tienen décadas, son tóxicos y la resistencia está creciendo. La estructura de dianas terapéuticas para *T. cruzi* y *Leishmania* está pobremente caracterizada. Las herramientas modernas de estructura de proteínas y docking recién se están abriendo como código abierto.

**Capacidades locales.**

- CEDIC hace tamizaje in vitro explícito sobre *T. cruzi*, *Leishmania* y líneas tumorales; screening experimental e *in silico*.
- BioProsNat (CEMIT-UNA) aisla productos naturales bioactivos con potencial antifúngico, antimicrobiano y antiparasitario, con vínculos consolidados con UFPB, UFG, UFMA, FIOCRUZ (Brasil).
- IICS mantiene líneas de cultivo y modelos animales para Chagas.
- Tesabio.ai (FIUNA + Harvard/Broad/Cornell) ya hace descubrimiento de fármacos con IA, enfocado en redes de microARN.

**Herramientas de código abierto.**

- **AlphaFold 3** (Apache 2.0 desde junio 2025) — predicción de estructura biomolecular.
- **Boltz-1 / Boltz-2** (MIT Jameel) — alternativa abierta a AF3, totalmente abierta con pesos.
- **Chai-1** (Chai Discovery) — otra alternativa abierta a AF3.
- **ESMFold** — predicción rápida de estructura a partir de secuencia.
- **DiffDock** — docking proteína-ligando estado del arte.
- **RoseTTAFold-AA / RFdiffusion** — diseño y docking.
- **REINVENT, MolGPT, GraphAF** — química generativa.
- **RDKit, DeepChem** — cheminformatics.
- **TrypanoDB / TriTrypDB** — bases de datos específicas de *T. cruzi* y *Leishmania*.
- **Therapeutics Data Commons (TDC)** — datasets de bioactividad.

**Primer proyecto concreto.** Predicción con Boltz-2 de las estructuras de cruzipaína y otras dianas de *T. cruzi* validadas en CEDIC, luego screening virtual contra la biblioteca de productos naturales de BioProsNat. Entregable: paper con coautoría CEDIC + BioProsNat + FIUNA, potenciales hits candidatos a validación experimental. Aplicar a la convocatoria 2026 FAPESP-CONACYT-CONICET sobre resistencia antimicrobiana (extiende naturalmente a antiparasitarios).

**Vacíos de información.**

- ¿Qué dianas específicas prioriza CEDIC para screening?
- ¿Cuántos compuestos naturales tiene caracterizados BioProsNat?
- ¿Cuál es la capacidad de cómputo real disponible localmente?
- ¿Quién mantiene actualmente la infraestructura de Tesabio?

---

## 3. Modelos de lenguaje clínico en español paraguayo

**Problema.** Los LLM médicos abiertos (MedGemma, Meditron, OpenMedLM) están entrenados mayormente en inglés y español neutro. Paraguay tiene un español con modismos propios, jerga clínica local, y un componente importante de guaraní. No existe un modelo fundacional médico en español paraguayo. Mientras tanto, los médicos del Hospital de Clínicas atienden 1.150 pacientes ambulatorios por día con registros frecuentemente en papel.

**Capacidades locales.**

- Hospital de Clínicas (UNA) — 45+ especialidades, 1.150 visitas/día, registro predominantemente en papel.
- INCAN — sistema de registro electrónico incipiente, programa RACAM de navegación de pacientes oncológicos.
- Resolución 367/2020 del MSPBS **endosa explícitamente IA/ML en telesalud** — sin pathway de aprobación definido.
- HIVE Digital Technologies opera un cluster GPU (BUZZ AI Cloud) en Asunción desde marzo 2026 en alianza con Columbia University.
- X8 Cloud firmó MOU con ANDE por $8 mil millones para centro de datos 50 → 500 MW.

**Herramientas de código abierto.**

- **MedGemma 4B / 27B** (Google, Apache 2.0 wrapper) — base Gemma 3 con fine-tuning médico.
- **MedSigLIP** — codificador visual médico.
- **OpenMedLM / Meditron** (Llama-based).
- **BioMistral** — Mistral-based.
- **Whisper** + fine-tuning para ASR guaraní (corpus a construir).

**Primer proyecto concreto.** Fine-tune MedGemma 4B sobre notas clínicas sintéticas en español paraguayo (generadas con LLM + revisión por médicos locales) para tareas de triaje y resumen. Desplegar en HIVE BUZZ. Evaluar con gold-standard creado por residentes del Hospital de Clínicas. Entregable: modelo de pesos abiertos, paper de evaluación, piloto de despliegue en una sala del Hospital de Clínicas.

**Vacíos de información.**

- ¿Existe un corpus de texto clínico paraguayo disponible para investigación?
- ¿Quién sería el champion clínico para un piloto en Hospital de Clínicas?
- ¿Cuál es la postura del IRB del Hospital de Clínicas sobre proyectos de IA?
- ¿HIVE BUZZ acepta investigación médica académica o solo comercial?

---

## 4. Patología digital e imágenes médicas

**Problema.** Paraguay no tiene patología digital sistemática. INCAN procesa biopsias para cáncer (especialmente colorrectal por el trabajo publicado de MassARRAY OncoCarta) pero los slides son físicos, no digitalizados. Los modelos fundacionales de patología (UNI, CONCH, Virchow2, Path Foundation) podrían detectar y segmentar tumores con cero o poco entrenamiento adicional.

**Capacidades locales.**

- INCAN — perfil molecular del cáncer colorrectal paraguayo, parte del consorcio LEGACY (UE-LATAM) para cáncer gástrico.
- City Cancer Challenge (C/Can) — Asunción es una de las 4 primeras ciudades "learning", desde 2017.
- Programa RACAM (ASCO 2025) — navegación de pacientes oncológicos.
- Asociación con Hospital Italiano de Buenos Aires (referente regional en IA clínica).

**Herramientas de código abierto.**

- **UNI / UNI2** — visión-only, Mahmood Lab.
- **CONCH / CONCH1.5** — visión-lenguaje, top en benchmark 2025.
- **Virchow / Virchow2** — Paige + Microsoft, muy cerca del top.
- **Path Foundation** — Google.
- **MedSAM** — segmentación universal médica.
- **BiomedCLIP** — retrieval imagen-texto médico.
- **MAIRA-2** (Microsoft) — generación de informes radiológicos, research-use-only.

**Primer proyecto concreto.** Escanear 1.000 slides de H&E retrospectivos del INCAN (con consentimiento + IRB + DPIA). Aplicar CONCH para detección zero-shot de肿瘤, MedSAM para segmentación. Validar contra lecturas de patólogos del INCAN. Entregable: paper de validación, dataset abierto, ruta clínica para despliegue.

**Vacíos de información.**

- ¿Tiene INCAN un escáner de slides digital? ¿Cuál?
- ¿Qué cobertura tiene el archivo patológico?
- ¿Cómo se gestiona el consentimiento para uso secundario de muestras históricas?

---

## 5. Resistencia antimicrobiana

**Problema.** Paraguay carece de un sistema nacional automatizado de vigilancia genómica de resistencia antimicrobiana. IICS opera una red desde 2007 para caracterización molecular de resistencia, con 17 años de datos acumulados pero sin capa de aprendizaje automático. La convocatoria 2026 FAPESP-CONACYT-CONICET está explícitamente dirigida a resistencia antimicrobiana en producción animal — Paraguay es un exportador importante de carne.

**Capacidades locales.**

- IICS opera la Red Nacional de Resistencia Antibiótica desde 2007.
- Hospital General de Barrio Obrero tiene datos activos de TB IGRA (estudio 2025 publicado).
- BioProsNat tiene screening antimicrobiano experimental.
- SENACSA (Servicio Nacional de Calidad y Salud Animal) regula uso veterinario.

**Herramientas de código abierto.**

- **Mykrobe** — predicción de resistencia de *M. tuberculosis* desde WGS.
- **TBProfiler** — mismo nicho, mayor base de datos.
- **AMRFinderPlus (NCBI)** — genes de resistencia desde genomas bacterianos.
- **Staramr** — predicción AMR desde WGS.
- **ResFinder** — base de datos de genes de resistencia.

**Primer proyecto concreto.** Aplicar Mykrobe + AMRFinderPlus sobre el archivo histórico de aislamientos del IICS. Entrenar un clasificador XGBoost sobre los 17 años de datos de la red. Construir un dashboard de vigilancia nacional. Aplicar a la convocatoria 2026 FAPESP-CONACYT-CONICET.

**Vacíos de información.**

- ¿Los datos están en WHONET o en un sistema propio?
- ¿Hay aislados secuenciados disponibles?
- ¿Cuál es la capacidad de cómputo del IICS?

---

## 6. Salud mental y triaje

**Problema.** Paraguay tiene una brecha masiva en detección temprana de depresión e ideación suicida en niños y adolescentes. Un estudio reciente (2026) encontró que solo el 28 % de pediatras paraguayos tiene conocimiento alto, solo el 29,3 % usa herramientas estandarizadas de tamizaje, y la respuesta predominante (85,4 %) es derivación urgente — un reflejo de la falta de capacidad de manejo ambulatorio.

**Capacidades locales.**

- Cátedra de Psiquiatría (FCM-UNA) — programa de telesiquiatría documentado durante COVID.
- Ley 5482/2015 — Programa Nacional de Telesalud.
- Resolución 367/2020 — endosa IA/ML en telesalud.
- mHealth piloto Adhera MejoraCare (PLOS ONE 2022) — viabilidad comprobada.

**Herramientas de código abierto.**

- **MedGemma 4B** — fine-tunable para tamizaje estructurado.
- **Whisper** — transcripción de audio para entrevistas clínicas.
- **OpenMedLM / Meditron** — alternativas LLM médico.
- **RAG sobre guías clínicas paraguayas** (a construir).

**Primer proyecto concreto.** Fine-tune MedGemma 4B sobre un corpus de conversaciones de telesiquiatría del Cátedra de Psiquiatría para detectar señales de depresión/ideación suicida en conversaciones en español paraguayo. Validar contra evaluación psiquiátrica estructurada. Desplegar como asistente del pediatra en atención primaria, no como reemplazo. Entregable: paper de validación, piloto en 3 centros de atención primaria.

**Vacíos de información.**

- ¿Hay datos de conversaciones psiquiátricas que se puedan usar?
- ¿Existe una guía clínica paraguaya validada para depresión pediátrica?

---

## 7. Telemedicina y atención primaria rural

**Problema.** Paraguay tiene 165.000 infectados con Chagas concentrados en el Chaco, comunidades con acceso limitado a especialistas, y un sistema de telesalud legalmente habilitado (Ley 5482/2015, Resolución 367/2020) pero con adopción baja. La telemedicina con IA podría extender alcance sin nuevos especialistas.

**Capacidades locales.**

- Paraguay ya tiene el marco legal (Ley 5482/2015, Resolución 367/2020).
- DGVS (Dirección General de Vigilancia de la Salud) — sistema de semáforo de medicamentos (2019).
- Hospital de Clínicas — telesiquiatría documentada.
- CEDIC hace trabajo de campo en comunidades chaqueñas con pueblos indígenas.

**Herramientas de código abierto.**

- **MedGemma 4B** — asistente conversacional.
- **Whisper + guaraní ASR** (a construir).
- **RAG sobre protocolos MSPBS** (a construir).
- **OpenMRS / Bahmni** — EHR open source para telemedicina.
- **CommCare** (Dimagi) — formularios móviles para trabajo de campo.

**Primer proyecto concreto.** Asistente conversacional multilingüe (español + guaraní) para agentes de salud comunitaria en el Chaco, entrenado sobre protocolos de Chagas y leishmaniasis. Desplegar vía WhatsApp Business API o CommCare. Medir: triage accuracy vs gold-standard de médico remoto. Entregable: app funcional, paper de field-trial.

**Vacíos de información.**

- ¿Existen datos de audio en guaraní para entrenamiento ASR?
- ¿Qué herramientas usa actualmente el trabajo de campo de CEDIC?
- ¿Cómo se regulan los datos de pacientes en comunidades indígenas bajo la Ley 7593/2025?

---

## 8. Capacitación en investigación clínica

**Problema.** Los residentes médicos paraguayos reciben solo un semestre de bioestadística en pregrado. El 78 % nunca cursó metodología de investigación posgrado. El 24 % ha publicado nacionalmente, solo el 14 % internacionalmente. Sin embargo, el 70 % cree que la formación en investigación debe ser obligatoria y el 95 % que la investigación mejora atención al paciente. Hay talento y motivación; faltan tiempo protegido, mentores y herramientas.

**Capacidades locales.**

- Facultad de Ciencias Médicas (UNA) — 9.000 docentes, hospital escuela.
- CONAREM — 23 unidades formadoras, ~500 residentes.
- IICS ofrece Maestrías y Doctorado en Ciencias Biomédicas, además de Maestría en Ingeniería Biomédica.
- Hospital de Clínicas tiene programa de residencia en Medicina Familiar con requisito de tesis.

**Herramientas de código abierto.**

- **Galaxy** — interfaz web sin instalación para análisis bioinformático.
- **nf-core** — pipelines reproducibles.
- **RMarkdown / Quarto** — informes reproducibles.
- **Bioconductor** — recursos R para biología.
- **Scikit-learn, PyTorch** — para cursos introductorios.

**Primer proyecto concreto.** Taller "Bioinformática y Análisis Clínico con Galaxy" para 30 residentes del Hospital de Clínicas, en alianza con IICS y la red SoIBio/AB3C. Programa: 5 sesiones, enseñar Galaxy + RMarkdown + lectura crítica. Materiales abiertos en español. Acreditar como curso de educación médica continua.

**Vacíos de información.**

- ¿Qué cursos de educación médica continua existen ya?
- ¿Quién sería el champion en CONAREM?
- ¿Hay financiamiento específico para este tipo de capacitación?

---

## Priorización

Si tuviéramos que empezar **un solo proyecto** hoy, sería:

> **Taller Nextclade + nf-core en LCSP** — costo bajo, valor inmediato, construye relación con el actor más estratégico del sistema de vigilancia genómica, y produce entregables visibles (dashboards, SOPs, papers de métodos) que abren la puerta a los otros 7 proyectos.

Si tuviéramos que empezar **dos**:

> Lo anterior + **Fine-tune MedGemma 4B para triaje en español paraguayo** — un paper de evaluación sólido publicado abre la conversación nacional sobre IA clínica.

Los **proyectos 4 y 5 (patología digital y AMR)** son los más necesitados de co-financiamiento externo y los más apropiados para las convocatorias internacionales identificadas.

---

## Última actualización

Septiembre 2026. Este documento se revisará a medida que se cierre la investigación previa listada en `docs/plan-preparacion.md`.