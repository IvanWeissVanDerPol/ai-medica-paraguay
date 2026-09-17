# Top 5 en detalle completo — guía de ejecución

> **Qué es este archivo:** la explicación definitiva de las 5 ideas mejor rankeadas del master ranking. Cada idea se desarrolla a nivel de protocolo: epidemiología, arquitectura técnica exacta, estado del arte, fases semana a semana, presupuesto línea por línea, equipo, socios, ética, riesgos, criterios de éxito y de corte (kill criteria), outputs y alineación con financiamiento.
>
> **Audiencia:** quien ejecutaría estos proyectos. Escrito como si se arrancara mañana.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- #1 — Tamizaje de tos TB con HeAR en smartphone — score 92.5
- #2 — Antiveneno sintético para Tityus confluens — score 89
- #3 — Stack Chaco integrado (TB + Chagas + vigilancia) — score 88
- #4 — Pipeline TxGemma + Boltz-2 + OpenFold3 + CEDIC contra Chagas — score 86
- #5 — Monitoreo inteligente de miocardiopatía chagásica — score 84
- §6 — Secuencia de ejecución recomendada (12 meses)
- §7 — Comparativa final

---

# #1 — Tamizaje de tos TB con HeAR en smartphone — Score 92.5

## 1.1 Resumen ejecutivo

Una persona tose 5 veces frente a un teléfono celular en una comunidad del Chaco sin laboratorio a menos de 200 km. En 10 segundos, un modelo de IA instalado en el teléfono estima la probabilidad de tuberculosis activa. Los casos probables se derivan con prioridad a baciloscopia/GeneXpert. El POC técnico cuesta menos de $5,000 y se hace en 4 semanas con datos públicos. El piloto de campo cuesta ~$30,000 y toma 6 meses. Es el proyecto con la mejor relación impacto/costo/riesgo/tiempo de toda la cartera.

## 1.2 El problema de salud (epidemiología)

- Paraguay notifica ~3,000 casos de TB al año; la OMS estima subregistro de ~40-50%, con lo cual los casos reales rondan 5,000-6,000/año.
- El Chaco (Boquerón, Presidente Hayes) y regiones vecinas (Caaguazú, San Pedro, Amambay) concentran la mayor incidencia: poblaciones dispersas, pobreza estructural, poblaciones indígenas con acceso geográfico limitado.
- Cadena diagnóstica actual:
 1. Sintomático respiratorio (tos >2 semanas) → visita al centro de salud más cercano (puede ser a 50-150 km).
 2. Baciloscopia: rápida pero sensibilidad 50-60% en adultos, mucho menor en niños y VIH+.
 3. GeneXpert MTB/RIF: mejor sensibilidad pero equipo centralizado, cartuchos ~$10-15, mantenimiento.
 4. Cultivo: gold standard, 4-6 semanas.
- El cuello de botella NO es el tratamiento (hay programa DOTS de SENEPA/MSPBS): es **encontrar los casos**. El tamizaje actual es solo por síntomas, que es poco específico (toda tos crónica parece TB en zonas donde abundan EPOC, asma, post-COVID).
- Un tamizador comunitario barato en manos de agentes comunitarios movería el punto de entrada del sistema de salud del centro de salud a la comunidad.

## 1.3 La tecnología (arquitectura exacta)

**HeAR (Health Acoustic Representations)** — Google Health AI Developer Foundations, publicado 2024-2025:
- Modelo foundation de audio médico: encoder tipo Perceiver entrenado con ~300 millones de clips de audio de YouTube (tos, respiración, estornudos, voz con y sin patología).
- Produce **embeddings de 512 dimensiones** para cualquier clip de audio respiratorio de ~5-10 segundos.
- El paper reporta que linear probing sobre estos embeddings alcanza estado del arte en 24 de 33 tareas de acústica de salud (detección de COVID, asma, EPOC, etiquetas respiratorias, etc.).
- Disponible en HuggingFace como `google/hear`. Licencia HAI-DEF: **permite investigación; prohíbe uso clínico directo sin validación y despliegue regulado** — exactamente el marco de un estudio de investigación.

**Por qué la tos TB puede tener firma acústica:**
- La TB pulmonar produce tos predominantemente productiva, con características espectrales (energía en bandas bajas, duración de fase expiratoria, patrón en series/racimos) distintas de tos seca asmática, tos post-viral o tos de EPOC exacerbada.
- Estudios previos con features acústicos manuales (MFCCs, espectrogramas + CNNs pequeñas, grupos en India, África del Sur y el consorcio Cough-TB) reportan AUROC 0.6-0.8 en datasets pequeños (300-1,000 sujetos). El gap que HeAR llena: representaciones preentrenadas masivas que funcionan con poca data.

**Pipeline de decisión técnica:**
1. Extracción: `google/hear` encoder → embedding 512-d por clip.
2. Clasificador: regresión logística o XGBoost sobre el embedding (se entrena en CPU en minutos; no hace falta fine-tunear el encoder).
3. Despliegue de campo: dos opciones —
 - **Opción A (offline-first, recomendada):** quantizar el encoder a TFLite y correr on-device en el smartphone. Ventaja: funciona sin conectividad (el Chaco tiene cobertura intermitente).
 - **Opción B (híbrida):** grabar offline, procesar cuando hay señal. Más simple de ingeniería, pierde feedback inmediato.
4. Protocolo de grabación estandarizado: 5 tos consecutivas, 10 segundos, ambiente tranquilo, 30 cm del micrófono. La estandarización del protocolo es tan importante como el modelo.

## 1.4 Estado del arte global

- HeAR (Google HAI-DEF 2024-2025): validado en 33 tareas, ninguna específicamente TB con datasets grandes públicos. **La aplicación a TB es investigación novel.**
- Datasets públicos de tos:
 - **COUGHVID** (EPFL): ~25,000 clips etiquetados COVID/sano — el dataset de tos más grande público.
 - **SPRSound** (SJTU): ~9,000 sonidos respiratorios pediátricos.
 - **Coswara** (IISc Bangalore): ~1,500+ sujetos con tos/respiración/voz, COVID.
 - **ICBHI 2017**: ~5,000 ciclos respiratorios (crackle/wheeze).
 - **Tos específica TB**: existen datasets pequeños de consorcios de investigación (Cough-TB challenge de la UFH/India, datos de África del Sur, estudios de Uganda); la mayoría requieren acuerdo de data sharing. Ninguno es LatAm. **No existe ningún dataset de tos paraguaya.**

## 1.5 Diseño del proyecto, fase por fase

**Fase 0 — Setup (semana 1, $0)**
- Colab/Kaggle gratis (T4 16GB alcanza sobrado).
- Cargar `google/hear`, descargar COUGHVID.

**Fase 1 — Sanity check (semanas 2-4, $0-500)**
- Linear probe COVID vs sano sobre COUGHVID. Objetivo: AUROC ≥0.80 (el paper de HeAR reporta ~0.85 en esta tarea).
- Esto valida que el pipeline completo (audio → embedding → clasificador → métricas) funciona antes de tocar TB.
- Output: notebook reproducible en GitHub.

**Fase 2 — Robustez (semanas 5-10, $500-2,000)**
- Validación cruzada de datasets: entrenar en COUGHVID, testear en Coswara/SPRSound. Medir cuánto degrada (domain shift).
- Augmentations de campo: ruido de viento, micrófonos baratos, distancia variable. El audio rural chaqueño no es audio de Suiza: hay que simularlo.
- Output: conocimiento de la degradación esperada en campo (crítico para fijar expectativas del piloto).

**Fase 3 — TB específico (semanas 11-16, $2,000-5,000)**
- Ruta A: conseguir dataset público de tos TB con acuerdo de data sharing (contactar autores de papers de Cough-TB; ofrecer co-autoría).
- Ruta B (si A falla): diseño del piloto de colección propia con n pequeño (100 sujetos) y análisis tipo caso-control.
- Gate de continuidad: AUROC interno ≥0.70 en TB.

**Fase 4 — Piloto de campo (meses 4-6, $20,000-28,000)**
- Sitio: 2 comunidades del Chaco (1 indígena, 1 criolla/menonita) coordinadas con SENEPA.
- Reclutamiento: 200 personas ≥15 años (100 sintomáticos respiratorios + 100 controles).
- Procedimiento por persona: consentimiento → grabación protocolizada de tos → muestra de esputo → GeneXpert (reference standard) + baciloscopia.
- Análisis: sensibilidad, especificidad, PPV, NPV, AUROC; sub-análisis por VIH, edad, carga bacteriana.
- Ética: IRB del MSPBS/UNA (iniciar trámite en semana 1 — tarda 2-3 meses), consentimiento comunitario previo (reunión con líderes), consentimiento individual informado en guaraní y español.

**Fase 5 — Publicación y scale (meses 6+)**
- Paper: PLOS Global Public Health / npj Digital Medicine / Int J Tuberc Lung Dis.
- Grant para scale: Google.org AI for Social Good, Wellcome, FAPESP-CONACYT.

## 1.6 Presupuesto detallado

| Ítem | Costo |
|---|---|
| Fases 0-3 (compute, storage) | $2,000-5,000 |
| 10 smartphones (~$250 c/u) | $2,500 |
| Estipendios 2 agentes comunitarios (6 meses) | $3,000 |
| GeneXpert: 200 tests × ~$15 | $3,000 |
| Logística Chaco (viajes, combustible) | $4,000 |
| IRB, traducción de consentimientos, materiales | $1,500 |
| Coordinación y M&E | $4,000 |
| Contingencia 20% | $4,000 |
| **Total** | **~$30,000** |

## 1.7 Equipo mínimo

- 1 ML engineer (estudiante de maestría IA de FIUNA o Politécnica — hay base: Carlos Méndez Gaona, Diego Galeano).
- 1 epidemiólogo mentor (IICS o SENEPA).
- 1 técnico de campo (SENEPA regional).
- 2 agentes comunitarios locales (hablantes de guaraní/nivaclé según comunidad).

## 1.8 Socios y champions

- **SENEPA / Programa Nacional TB**: acceso a comunidades, marco operacional. Champion ideal: epidemiólogo 30-45 años con experiencia chaqueña.
- **LCSP**: GeneXpert y confirmación.
- **FIUNA**: talento ML.

## 1.9 Ética y regulatorio

- HAI-DEF terms: investigación permitida; el resultado del piloto NO se usa para decisiones clínicas individuales — es solo medir performance.
- **CARE Principles** (Collective benefit, Authority to control, Responsibility, Ethics): consentimiento comunitario antes del individual; los datos de audio de comunidades indígenas quedan bajo gobernanza acordada; retorno de resultados agregados a la comunidad.
- **Ley 7593/2025** (vigencia nov 2027): anonimización en captura, DPIA planificado.

## 1.10 Riesgos y mitigación

| # | Riesgo | Prob. | Mitigación |
|---|---|---|---|
| 1 | HeAR no discrimina TB (solo fue validado en COVID etc.) | Media | Los gates de las fases 1-3 lo detectan antes de gastar en campo; resultado negativo también es publicable |
| 2 | No hay dataset público TB suficiente | Alta | Ruta B (colección propia); acuerdos con grupos de India/África ofreciendo co-autoría |
| 3 | Ruido de campo degrada el modelo | Alta | Fase 2 de robustez lo cuantifica; protocolo de grabación estandarizado |
| 4 | IRB tarda más de lo previsto | Media | Iniciar semana 1; paralelizar con fases técnicas |
| 5 | Adopción por agentes comunitarios | Media | App de 1 botón; training de 1 día; feedback inmediato en pantalla |
| 6 | Cobertura/cambio de autoridades SENEPA | Media | 2 champions, no 1; documentación de procesos |

## 1.11 Criterios de decisión (gates)

- **Gate 1 (semana 4):** AUROC ≥0.80 en probe COVID → continuar; si no, depurar pipeline antes de avanzar.
- **Gate 2 (semana 10):** degradación cross-dataset <10% relativo → el modelo es lo bastante robusto para campo.
- **Gate 3 (semana 16):** AUROC TB ≥0.70 interno → piloto de campo; si no, publicar negativo y pivotar (asma/neumonía/COVID con el mismo stack, ~gratis).
- **Gate 4 (mes 6):** sensibilidad de campo ≥0.70 y especificidad ≥0.60 → en tamizaje comunitario la sensibilidad manda (los falsos positivos cuestan una GeneXpert; los falsos negativos cuestan transmisión) → scale-up.

## 1.12 Outputs

- 1-2 papers (POC técnico + piloto de campo).
- Notebook reproducible + modelo + app APK (todo open source).
- Primer dataset de tos paraguaya (si se hace colección).
- Base para replicar el stack a asma, neumonía, COVID, EPOC — mismos embeddings, otro probe.

## 1.13 Por qué score 92.5

A=10 (TB Chaco, máxima necesidad), B=10 (stack abierto y disponible hoy), C=10 (<$5k el POC), D=10 (1 semana al primer resultado), E=9 (riesgo técnico bajo), F=8 (first-mover LatAm), G=10 (replicable a 5+ enfermedades). Es el único proyecto de la cartera con cuatro 10 en las dimensiones de ejecución.

---

# #2 — Antiveneno sintético para Tityus confluens — Score 89

## 2.1 Resumen ejecutivo

El Baker Lab (U. Washington, Nobel de Química 2024) demostró en Nature 2024 que se pueden diseñar proteínas de novo con RFdiffusion que neutralizan toxinas de veneno de cobra, con 80-100% de supervivencia en ratones. Nadie lo ha aplicado a escorpiones. Paraguay tiene carga real de escorpionismo (1,383 casos en un año, 4 muertes infantiles), un escorpión endémico del Chaco (*Tityus confluens*), y el closed loop local (CEDIC para validar, Tesabio para producir, FIUNA para computar). El proyecto diseñaría binders sintéticos contra las toxinas principales del veneno, validándolos in vitro e in vivo. Costo total a fase preclínica: $450k-1M en 24-36 meses. Potencial: primer antivenomo sintético anti-escorpión del mundo, publicación de máximo impacto, soberanía en antivenenos.

## 2.2 El problema de salud

- Paraguay registró **1,383 casos de escorpionismo** entre julio 2022 y julio 2023: 41 moderados/graves y **4 muertes, todas infantiles**.
- El Chaco es zona de *Tityus confluens*; la zona metropolitana tiene *T. trivittatus*. Los niños son los más severos (masa corporal).
- El antivenomo actual es suero heterólogo (hiperinmunización de caballos) **importado de Brasil (Butantan) o Argentina (ANLIS Malbrán)**: caro, cadena de frío, riesgo de reacciones de hipersensibilidad, y dependencia de la producción extranjera.
- Las toxinas de Tityus más relevantes: **β-toxinas y α-toxinas** (moduladores de canales de sodio Nav, el principal determinante de gravedad) y toxinas de potasio (KTx). Son péptidos pequeños ricos en cisteína (30-70 aa, 3-4 puentes disulfuro).

## 2.3 La tecnología (arquitectura exacta)

**Flujo de diseño de novo:**
1. **Estructura de la toxina diana**: desde PDB si existe cristalizada (muchas α/β-toxinas de Tityus tienen estructuras homólogas resueltas — p.ej. Ts1, Ts2 de *T. serrulatus*) o modelo con AlphaFold 3/OpenFold3. Para toxinas disulfuro-ricas, AF3 es razonablemente bueno pero conviene validar contra análogos cristalizados.
2. **Hotspots de unión**: residuos/epitopos funcionales de la toxina — idealmente el sitio que interactúa con el canal de sodio, para que el binder bloquee la función, no solo se adhiera.
3. **RFdiffusion3** (MIT license, abierta): genera miles de backbones proteicos de novo compatibles con unirse al hotspot.
4. **ProteinMPNN**: diseña la secuencia de aminoácidos para cada backbone.
5. **Filtrado in silico**: AlphaFold 3 (complejo binder-toxina) + Boltz-2 (afinidad predicha) → ordenar y quedarse con el top 1%.
6. **Wet lab**: síntesis de genes, expresión en *E. coli* (tesabio/CEDIC), purificación.
7. **BLI/SPR**: afinidad real medida (KD).
8. **Neutralización in vitro**: ensayo funcional de canal (electrofisiología en células que expresan Nav1.4/1.5, o ensayos de citotoxicidad).
9. **In vivo**: modelo ratón (ética animal) — toxina + binder, supervivencia.

**Precedente directo:** Vázquez Torres et al., "De novo designed proteins neutralize lethal snake venom toxins", Nature 2024 (abierto). Contra α-cobratoxina y citotoxinas (3FTx), lograron binders con protección 80-100% en ratones. La autora principal, **Susana Vázquez Torres**, es hispanohablante y publicly approachable — y el co-senior Tim Jenkins (DTU Dinamarca) lidera la parte de antivenenos.

**Por qué escorpión es distinto y factible:**
- Las toxinas de escorpión son más pequeñas que las 3FTx (30-70 aa vs 60-80) y muy rígidas por sus puentes disulfuro — targets estructuralmente estables, bueno para diseño.
- El Baker Lab ya publicó diseño de binders contra **péptidos pequeños bioactivos** (Vázquez Torres et al., Nature 2024b — binders de hélices bioactivas, p.ej. dinorfina, sub-100 pM). La tecnología para targets pequeños existe.
- Desafío real: lograr que el binder bloquee el epitopo funcional (unión al canal). Se mitiga diseñando contra el epitopo funcional y con binder bivalente/multivalente si hace falta.

## 2.4 Estado del arte y gap

- Antivenomos recombinantes/sintéticos en pipeline global: envenenamiento por serpiente es categoría OMS de alta prioridad; **escorpionismo recibe muchísima menos atención** pese a matar niños en América Latina.
- Nadie ha publicado diseño de novo de binders contra toxinas de escorpión. **Gap de first-mover mundial literal.**
- El venoma de *T. confluens* está parcialmente caracterizado en literatura (composición general, presencia de Na-toxinas); hace falta proteómica fina + transcriptoma — que es exactamente la Fase 1.

## 2.5 Diseño del proyecto, fase por fase

**Fase 1 — Partnership + venoma (meses 1-9, $50-80k)**
- Outreach a Susana Vázquez Torres (Baker Lab) y Tim Jenkins (DTU) con propuesta concreta: Paraguay aporta venoma, validación local y carga clínica; ellos aportan know-how de diseño. Co-autoría y co-patente.
- Colecta de *T. confluens* en Chaco (permisos MADES de vida silvestre; colaboración con aracnólogos/facultades locales).
- **Transcriptoma** de la glándula de veneno (secuenciación Illumina de mRNA; extracción de las toxinas expresadas).
- **Proteómica** del veneno (LC-MS/MS; Facultad de Ciencias Químicas UNA o servicio externo).
- Priorización de 3-5 toxinas: las Na-toxinas dominantes en abundancia y toxicidad.
- Output: paper del venoma (publicable por sí solo) + MoU con Baker Lab.

**Fase 2 — Diseño computacional (meses 6-12, solapada; $20-50k compute)**
- 500-2,000 designs por toxina con RFdiffusion3 en HIVE BUZZ/X8 Cloud (1,000-3,000 GPU-hours).
- Filtrado AF3 + Boltz-2 → top ~100 designs totales.

**Fase 3 — Wet lab (meses 12-18, $80-150k)**
- Síntesis de genes + expresión + purificación (Tesabio/CEDIC).
- BLI: medir KD real → top 20.
- Ensayo funcional in vitro (bloqueo de actividad de la toxina en células).

**Fase 4 — In vivo (meses 18-24, $100-200k)**
- Protocolo de ética animal (CICUAE). Modelo ratón: toxina + binder → supervivencia.
- Titulación de dosis, formulación.

**Fase 5 — Preclínico y producción (meses 24-36, $200-500k)**
- Proceso productivo en Tesabio (GMP-like).
- Toxicología del binder (¿es inmunogénico? ¿estable?).
- Vía regulatoria con DINAVISA.

## 2.6 Presupuesto resumido

| Fase | Monto |
|---|---|
| 1. Venoma + partnership | $50-80k |
| 2. Diseño computacional | $20-50k |
| 3. Wet lab in vitro | $80-150k |
| 4. In vivo | $100-200k |
| 5. Preclínico + producción | $200-500k |
| **Total a fase preclínica** | **$450k-1M** |

Fuentes posibles: Wellcome Discovery Awards, CZI Science, Google.org, FAPESP-CONACYT (vía co-investigador brasilero en venomas), IDB Lab.

## 2.7 Equipo mínimo

- 1 biólogo computacional (FIUNA; co-supervisado por Baker Lab en visitas cortas o virtualmente).
- 1 bioquímico de proteínas (CEDIC).
- 1 ingeniero de expresión/purificación (Tesabio).
- 1 toxicólogo (CEDIC/FCM).
- 1 especialista en colecta/crío de escorpiones.

## 2.8 Ética y regulatorio

- Ética animal (CICUAE) para Fase 4 — protocolo con criterios de finalización humanitaria.
- Permiso MADES para colecta de ejemplares.
- BSL-2 para trabajo con veneno activo.
- Ley 7593 aplica solo en la medida en que se usen datos clínicos de casos (historias de pacientes escorpionados para caracterización epidemiológica — anonimizados).

## 2.9 Riesgos y mitigación

| # | Riesgo | Prob. | Mitigación |
|---|---|---|---|
| 1 | Baker Lab no responde / no hay partnership | Media | RFdiffusion3 es MIT open — se puede correr sin ellos; plan B: DTU (Jenkins), o trainings abiertos del Baker Lab; co-autoría es el incentivo |
| 2 | Venoma de T. confluens insuficientemente caracterizado | Media | Fase 1 existe exactamente para esto; gate antes de diseñar |
| 3 | Binders no expresan o no plegan | Media | Estándar del campo: pantalla decenas; filtrado MPNN/AF reduce tasa de falla |
| 4 | Binder se une pero no neutraliza (epitopo no funcional) | Media | Diseñar contra el epitopo funcional del canal; binders bivalentes; gate temprano con ensayo funcional |
| 5 | Costo se dispara antes de señal | Baja | Phase gates con kill criteria cada fase |
| 6 | Regulación para uso humano lejana | — | El valor se captura antes: papers, patente, capacidad instalada |

## 2.10 Criterios de decisión (gates)

- **Gate 1 (mes 9):** venoma caracterizado (≥3 toxinas mayoritarias secuenciadas) + MoU con partner de diseño.
- **Gate 2 (mes 12):** ≥5% de designs con afinidad predicha <100 nM en Boltz-2.
- **Gate 3 (mes 18):** ≥3 binders con KD medido <50 nM por BLI.
- **Gate 4 (mes 24):** protección ≥80% en modelo murino con al menos un binder.

## 2.11 Outputs

- 2-3 papers de alto impacto (venoma; diseño+in vitro; in vivo).
- Patente(s) sobre secuencia de binders.
- Capacidad instalada de proteína de diseño en Tesabio/CEDIC — reutilizable para Chagas, Leishmania, diagnósticos.
- Base para extender a *Bothrops* (yarará) y *Crotalus* (cascabel) paraguayas.

## 2.12 Por qué score 89

A=6 (carga menor que TB pero con muertes infantiles evitables), B=8 (tecnología abierta y demostrada en analogo cercano), C=4 (caro), D=4 (lento), E=6 (novel), **F=10 (first-mover mundial, potencial Nature/Science)**, G=6 (replicable a Bothrops y otros escorpiones). El score refleja que el costo y plazo altos se compensan con el upside de visibilidad científica y soberanía.

---

# #3 — Stack Chaco integrado (TB + Chagas + vigilancia) — Score 88

## 3.1 Resumen ejecutivo

No es una tecnología sino un **programa regional**: convertir 2-3 comunidades del Chaco en zona demostrativa donde se integran cinco componentes ya validados individualmente — (1) tamizaje de tos con HeAR, (2) diagnóstico POC de TB con CRISPR (SHINE-TB), (3) confirmación y resistencia con tNGS en MinION, (4) tamizaje cardiaco con ECG smartphone (D-Heart) para Chagas, (5) vigilancia genómica con Nextclade/nf-core. Ningún país ha integrado este stack contra TB+Chagas en una región hiperendémica. El valor no está en ninguna pieza sola sino en la integración operativa con datos unificados.

## 3.2 El problema

- El Chaco paraguayo concentra lo peor de tres mundos: TB hiperendémica, seroprevalencia de Chagas elevada en adultos, y leishmaniasis/dengue endémicos — con acceso geográfico terrible.
- Los programas nacionales son **verticales** (Programa TB, Programa Chagas, vigilancia LCSP): cada uno con su personal, su data, sus tiempos.
- Resultado: una persona con tos crónica y Chagas crónico interactúa con el sistema 2-3 veces en formas no conectadas, y el sistema no aprende.

## 3.3 Arquitectura del stack (4 capas)

**Capa 1 — Tamizaje comunitario (en la comunidad, agente comunitario):**
- App de tos HeAR (proyecto #1) → score TB.
- D-Heart ECG smartphone (~$150-300/unidad, validado en piloto boliviano del Chaco para tamizaje de cardiopatía chagásica: RBBB, bloqueos) → score cardiaco.
- SHINE-TB (CRISPR-Cas13a/Cas12a + RPA, Broad Institute 2025, publicado en bioRxiv/PMC): esputo directo, sin termociclador, lectura lateral-flow o fluorescencia, ~1 hora, sensibilidad/especificidad 100% vs cultivo en la serie publicada (n=13; necesita validación local más grande — ese es exactamente el rol del piloto).
- Todo offline-first; sync cuando hay señal.

**Capa 2 — Confirmación y resistencia (nodo regional o LCSP):**
- tNGS con MinION Mk1C ($5k + ~$50-100/muestra): Deeplex Myc-TB o esquema custom; detecta resistencia a RIF/INH/FQ/AMG/LZD/etc. directamente del esputo sin cultivo ni BSL-3 (validado por ICMR-NIRT, India: sensibilidad 95% RIF, 88% INH, 100% FQ/AMG/LZD vs pDST).
- Turnaround: <24-48h vs 4-6 semanas del cultivo.

**Capa 3 — Vigilancia genómica (LCSP):**
- Nextclade + nf-core/viralrecon para dengue/SARS-CoV-2/MPXV; árboles filogenéticos regionales alimentando decisiones de SENEPA.

**Capa 4 — Datos y gobernanza:**
- Dashboard unificado SENEPA/MSPBS: cada persona tamizada tiene un registro (tos score + ECG score + SHINE-TB resultado + tNGS si llegó a confirmación).
- Anonimizado en captura; datos de comunidades indígenas bajo gobernanza CARE (acuerdo comunitario de uso de datos).

## 3.4 Diseño del programa (3 fases)

**Fase 1 — Setup (meses 1-9, $150-200k)**
- Comité directivo: SENEPA + Región Sanitaria Boquerón + LCSP + UNA + representantes comunitarios.
- Compras: MinION Mk1C ($5k), flowcells ($10k), reactivos tNGS ($25k), SHINE-TB reactivos ($15k), 10 D-Heart ($3k), smartphones/tablets ($8k), app development HeAR ($10k).
- IRB unificado multi-componente (un solo protocolo paraguas — más rápido que 4 protocolos separados).
- Consulta comunitaria previa en las comunidades seleccionadas.
- Training: 1 semana para 3 técnicos (tNGS + SHINE-TB) + 6 agentes comunitarios (app tos + D-Heart).

**Fase 2 — Piloto (meses 9-24, $250-300k)**
- 3 comunidades (p.ej. 1 nivaclé, 1 qom, 1 criolla — diversidad de contextos).
- 500 personas tamizadas; seguimiento 12 meses.
- Endpoints operacionales: % casos TB detectados vs línea base histórica, tiempo de diagnóstico (objetivo: <48h del primer contacto a resultado con resistencia), % chagásicos con ECG anormal derivados, cobertura de tamizaje.
- Sub-estudio: concordancia SHINE-TB vs GeneXpert vs tNGS (paper metodológico).

**Fase 3 — Scale (meses 24-36, $200-500k)**
- 20 comunidades; evaluación de efectividad; policy brief para MSPBS; modelo de costeo para decisión de escala nacional.

## 3.5 Presupuesto Fase 1-2 consolidado

| Componente | Monto |
|---|---|
| Equipamiento (MinION, D-Heart, smartphones, suitcase lab) | $80k |
| Reactivos (tNGS, SHINE-TB, flowcells) | $60k |
| Desarrollo de app + dashboard + cloud | $35k |
| Personal (PM 0.5 FTE, 3 técnicos, 6 agentes, 18 meses) | $150k |
| Logística chaqueña (viajes, combustible, estadias) | $40k |
| IRB, comunidad, M&E | $30k |
| Contingencia | $45k |
| **Total Fase 1-2** | **~$440k** |

## 3.6 Riesgos principales

| Riesgo | Prob. | Mitigación |
|---|---|---|
| Coordinación multi-actor fracasa | Alta | PM senior con credibilidad MSPBS; comité con sesiones mensuales; empezar con 1 comunidad y expandir |
| Rotación de personal de salud pública | Alta | Documentación de procesos; training redundante (2 personas por rol mínimo) |
| Sobrecarga de LCSP | Media | El tNGS puede montarse en nodo regional (Filadelfia) con soporte remoto LCSP |
| Cadena de frío / reactivos en Chaco | Alta | Liofilización de reactivos SHINE-TB (el paper demuestra compatibilidad con liofilización); calendarización de viajes |
| Equipos fallan en campo | Media | Training técnico local + kits de repuesto |
| Gap de financiamiento entre fases | Media | Phase gates; diseño modular (cada componente aporta valor solo) |

## 3.7 Outputs

- 3-5 papers (integración metodológica; resultados TB; resultados Chagas; costo-efectividad; validación SHINE-TB en campo).
- Modelo operativo replicable + dashboard.
- Policy brief para escala nacional.
- El Chaco como referencia mundial de zona demostrativa de stack abierto contra TB+Chagas.

## 3.8 Por qué score 88

A=10 (la mayor carga combinada), B=8 (piezas validadas; la integración es lo novel), C=6, D=6, E=7 (cada pieza funciona; el riesgo es operacional), F=8 (first-mover LatAm en integración), G=10 (el modelo se replica a cualquier región/patología). Pierde contra #1/#2 porque exige coordinación institucional compleja — su riesgo principal no es técnico sino político-operacional.

---

# #4 — Pipeline TxGemma + Boltz-2 + OpenFold3 + CEDIC contra Chagas — Score 86

## 4.1 Resumen ejecutivo

Paraguay es posiblemente el único país del mundo con el ciclo completo del descubrimiento de fármacos en un radio de 30 km: una biblioteca de compuestos naturales propios (BioProsNat, FP-UNA), capacidad de bioensayos in vitro contra *T. cruzi* (CEDIC), una biotech capaz de escalar (Tesabio), talento de IA (FIUNA) y el mayor hospital docente (Hospital de Clínicas). Lo que falta es el motor computacional que priorice qué compuestos probar. Ese motor hoy es abierto y gratuito: Boltz-2 (MIT) para afinidad, OpenFold3 (Apache 2.0) para estructuras, TxGemma (Google HAI-DEF) para ADMET. El proyecto criba la biblioteca BioProsNat contra 5 dianas validadas de *T. cruzi*, valida los mejores hits en CEDIC y optimiza hasta un lead.

## 4.2 El problema

- Chagas crónico: ~150,000-200,000 paraguayos infectados. El tratamiento (benznidazol/nifurtimox) tiene 60 días, efectos adversos frecuentes y eficacia discutida en fase crónica.
- El descubrimiento mundial de fármacos anti-Chagas está crónicamente sub-financiado (DNDi es casi el único actor serio). En 50 años: 2 fármacos.
- Los productos naturales son la fuente histórica de antichagásicos (la lapachol/beta-lapachona viene de tabebuia — árboles que abundan en la región) y BioProsNat tiene ~500-1,000 compuestos caracterizados de biodiversidad paraguaya, varios con actividad antichagásica preliminar.

## 4.3 Las herramientas (qué hace cada una exactamente)

- **Boltz-2** (MIT license, 2025): co-pliega complejos proteína-ligando y predice afinidad de unión (ΔG) con estimación de incertidumbre. Permite screening de miles de compuestos por diana sin dockar uno por uno con física clásica. Es la alternativa comercial-friendly de AlphaFold 3 (cuyos pesos son no-comerciales — regla del repo: AF3 solo para investigación, Boltz-2/OpenFold3 para todo lo que pueda escalar).
- **OpenFold3** (Apache 2.0, 2026): re-entrenamiento abierto del arquitecto AlphaFold 3 con accuracy comparable. Para estructuras de dianas y de complejos.
- **TxGemma** (HAI-DEF, 2B/9B/27B): LLM terapéutico entrenado en >200 tareas de Therapeutics Data Commons (clasificación ADMET: BBB, hERG, hepatotoxicidad, etc.). Acepta prompts en español. La versión -Chat razona sobre moléculas (DrugChat).
- **Control de calidad**: cross-validar predicciones ADMET con ChemBERTa-2/3 o MoDKiT; verificar que el screening computacional "recupera" fármacos conocidos activos contra T. cruzi (benznidazol, nifurtimox, posaconazol) antes de confiar en rankings nuevos.

**Dianas de T. cruzi (criterio: validadas + estructuras disponibles):**
1. **Cruzain** (cisteín-proteasa, PDB múltiples: 1AIM, 1ME3, etc.) — la diana clásica.
2. **TcCYP51** (14α-desmetilasa) — posaconazol actúa aquí.
3. **Trans-sialidasa** — única del parásito.
4. **TcTR** (triperredoxina reductasa).
5. **Cruzipaina-like / TcCATB** como secundarias.

## 4.4 Diseño (5 fases)

**Fase 1 — Setup del pipeline (meses 1-3, $20-50k)**
- Montar Boltz-2 + OpenFold3 + TxGemma-9B en HIVE BUZZ / X8 Cloud.
- Compilar SMILES de la biblioteca BioProsNat (+ libraries públicas de refuerzo: CO-ADD anti-T. cruzi screening set, que es pública y tiene datos de actividad — perfecta para validar el pipeline).
- Descargar estructuras de dianas (AlphaFold DB).

**Fase 2 — Screening virtual (meses 3-6, $30-80k compute)**
- Boltz-2: afinidad predicha de cada compuesto × cada diana (5-10 dianas × 500-2,000 compuestos).
- **Validación del pipeline**: ¿el ranking recupera los activos conocidos de CO-ADD? (enrichment factor). Si no recupera, el pipeline no sirve y hay que depurarlo antes de seguir — este es el gate metodológico más importante del proyecto.
- Top-100 → OpenFold3 para poses de unión razonables.
- Top-50 → TxGemma ADMET (BBB no necesaria; sí hERG, hepatotox, citotoxicidad general).
- Output: lista priorizada top-20 + paper de screening.

**Fase 3 — Validación in vitro en CEDIC (meses 6-12, $60-120k)**
- Adquisición/síntesis de top-20 (si BioProsNat no tiene stock suficiente).
- Ensayos estándar anti-T. cruzi:
 - IC50 sobre epimastigotas (cepa Y o cl1-16).
 - Actividad sobre amastigotas intracelulares (células Vero/L6) — la que importa farmacológicamente.
 - Citotoxicidad en células mamarias (L6) → índice de selectividad SI = CC50/IC50.
- Criterio de hit: IC50 amastigotas <10 µM y SI >50.
- Output: paper in vitro.

**Fase 4 — Optimización de leads (meses 12-24, $100-300k)**
- Química medicinal asistida por IA: generación de análogos (REINVENT o similar) → síntesis → SAR → lead.
- Criterio de lead: IC50 <1 µM, SI >100, ADMET limpio, novedad patentable.

**Fase 5 — Preclínico (meses 24-48, $500k-2M)**
- Producción Tesabio, PK/PD, toxicología animal, vía hacia ensayos clínicos (aquí ya se necesitaría consorcio internacional — DNDi es el socio natural).

## 4.5 Riesgos y gates

| Riesgo | Mitigación |
|---|---|
| Predicciones de afinidad no correlacionan con actividad | Gate de enriquecimiento con CO-ADD antes de gastar en wet lab; dockar también con AutoDock Vina/DiffDock como consenso |
| TxGemma alucina en español | Cross-check con modelos secundarios; usar outputs como ranking, no como verdad |
| BioProsNat: poco stock/poca diversidad | Complementar con CO-ADD y libraries de productos naturales comerciales |
| CEDIC saturado | Co-financiar un postdoc dedicado al proyecto |
| Muertes por optimización lenta (química med) | Partner externo de síntesis (Argentina/Brasil cercanos) |

**Gates:** (mes 3) pipeline corriendo + dianas listas; (mes 6) enrichment factor >3 vs azar en recuperación de activos conocidos; (mes 12) ≥3 hits con IC50 <10 µM y SI >50; (mes 24) lead con perfil completo.

## 4.6 Outputs

- 2-4 papers (screening, SAR, hits).
- Pipeline reproducible open source (GitHub) — reutilizable para leishmaniasis (mismo stack, otras dianas).
- Patente sobre serie química.
- Posible acuerdo de licensing con pharma/DNDi.
- Capacidad instalada de química computacional en FIUNA.

## 4.7 Por qué score 86

A=10 (máximo burden), B=9 (stack maduro y abierto), C=6, D=6 (paper in vitro al año), E=7, F=7 (novel para Paraguay; el mundo ya hace cribados virtuales), G=8 (replicable a Leishmania y otros parásitos). Es el proyecto insignia de mediano plazo: alto impacto, riesgo acotado por gates metodológicos.

---

# #5 — Monitoreo inteligente de miocardiopatía chagásica — Score 84

## 5.1 Resumen ejecutivo

La miocardiopatía chagásica crónica mata por arritmias y muerte súbita décadas después de la infección, y hoy solo se monitorea con una consulta cada 6-12 meses y un ECG puntual de 12 derivaciones. Este proyecto entrega smartwatches con ECG continuo a una cohorte de 50 (fase piloto) → 500 (fase 2) pacientes chagásicos crónicos paraguayos, analiza los ritmos con modelos de fundación de ECG (ECGFounder, NEJM AI 2025) y deriva alertas al cardiólogo. Sería la **primera cohorte mundial de monitoreo continuo en Chagas**.

## 5.2 El problema

- ~150,000-200,000 paraguayos con Chagas crónico; una fracción significativa desarrolla cardiopatía (10-30%).
- El sustrato: denervación y fibrosis miocárdica → bloqueo de rama derecha (RBBB), extrasístoles ventriculares (EVAs), taquicardia ventricular, muerte súbita.
- El ECG de 12 derivaciones en consulta es una muestra de 10 segundos de un proceso de años. Los eventos interconsultas se pierden.
- El manejo depende de detectar a tiempo: marcapasos, desfibrilador, antiarrítmicos.

## 5.3 La tecnología

- **Hardware**: Apple Watch (ECG single-lead validado FDA para AFib, notificaciones de ritmo irregular, ~$250-400) o Samsung Galaxy Watch (equivalente, más barato). El single-lead detecta RBBB, EVAs frecuentes, y arritmias sostenidas.
- **ECGFounder** (NEJM AI, nov 2025): modelo de fundación entrenado con >10M ECGs de 12 derivaciones; sirve como representación para fine-tuning de tareas locales (aquí: firma chagásica).
- **Arquitectura**: watch → app de investigación (ResearchKit-like Android/iOS) → cloud local (cumplimiento Ley 7593: datos en jurisdicción) → tres capas de análisis: (1) algoritmos nativos del watch (AFib), (2) modelo fine-tuned para RBBB/EVA/TV en single-lead, (3) ECGFounder para representaciones profundas y detección de firmas sutiles.
- **Referencia parcial**: Holter 24h basal y ECG 12-derivaciones trimestral en paralelo — permite medir cuánto agrega el monitoreo continuo.

## 5.4 Diseño (3 fases)

**Fase 1 — Piloto 50 pacientes (meses 1-18, ~$140-160k)**
- Reclutamiento desde Cátedra de Cardiología del Hospital de Clínicas + Instituto Nacional de Cardiología + Hospital Nacional de Itauguá (los tres centros con la mayor carga chagásica del país; contactos institucionales ya mapeados).
- Criterios de inclusión: 30-70 años, Chagas crónico confirmado (serología doble + ECG), forma indeterminada o cardiopatía leve-moderada (los que más se benefician de detectar progresión).
- 12 meses de monitoreo; visitas trimestrales.
- Endpoints: adherencia (% días con ≥1 ECG/sync), detección de arritmias nuevas, tiempo desde evento hasta detección, seguridad.

**Fase 2 — Expansión 500 (meses 18-36, $300k-1M)**
- Multicéntrico; brazo comparativo Android vs iOS (equidad); análisis de outcomes clínicos.
- Fine-tune definitivo del modelo sobre la data Py → paper del modelo.

**Fase 3 — Programa nacional (meses 36+)**
- Integración con cartera de servicios del MSPBS; evaluación económica.

## 5.5 Presupuesto Fase 1

| Ítem | Monto |
|---|---|
| 50 smartwatches | $15-20k |
| Desarrollo app + cloud local | $30-40k |
| Holters basales/trimestrales (arriendo/servicio) | $8k |
| Personal (coordinador 0.5 FTE, cardiólogo consultor, data scientist parcial) | $80k |
| Logística/pacientes (transporte, recargas) | $10k |
| **Total** | **~$140-160k** |

## 5.6 Riesgos y gates

| Riesgo | Mitigación |
|---|---|
| No surge cardiólogo champion | Outreach a las 3 cátedras con co-PI; es el bloqueo #1 del proyecto |
| Adherencia cae <50% a 6 meses | Incentivos, recordatorios WhatsApp, gamificación, contrato de depósito del equipo |
| Sesgo de selección (solo urbanos tech-savvy) | Fase 1 urbana (San Lorenzo/Asunción); Fase 2 incorpora rural con Android barato + tutor de tecnología |
| Single-lead se pierde arritmias sutiles | Complemento con Holter basal/trimestral; aceptar que detecta un subconjunto — que ya es más que el estándar actual |
| Pérdida/robo de equipos | Depósito, seguro, contrato |

**Gates:** reclutamiento ≥80% en 3 meses; adherencia ≥65% a 6 meses; ≥20 arritmias nuevas detectadas en la cohorte al año → expansión.

## 5.7 Outputs

- 2-3 papers (cohorte/observacional; modelo single-lead chagásico; outcomes).
- Infraestructura de investigación clínica digital reutilizable.
- Primer dataset mundial de ECG continuo en Chagas (con consentimiento para investigación futura — activo enorme).

## 5.8 Por qué score 84

A=8, B=8 (hardware validado + modelo publicado), C=4 (caro en hardware), D=4 (resultados clínicos a 18-24 meses), E=7, **F=10 (first-mover mundial absoluto: nadie ha hecho monitoreo continuo en Chagas)**, G=6. Su riesgo dominante es humano (champion + adherencia), no técnico.

---

# §6 — Secuencia de ejecución recomendada (12 meses)

| Mes | #1 HeAR | #2 Antiveneno | #3 Stack Chaco | #4 TxGemma Chagas | #5 Smartwatch |
|---|---|---|---|---|---|
| 1 | Fase 0-1 (POC) | Outreach Baker + inicio venoma | Comité + IRB paraguas | Setup pipeline HIVE BUZZ | Outreach cátedras cardio |
| 2-3 | Robustez + TB interno | Colecta + transcriptoma | Compras + training | Screening Boltz-2 | Protocolo + IRB |
| 4-6 | **Piloto campo** | Proteómica + priorización | Piloto 1 comunidad | Validación enriquecimiento → envío top-20 a CEDIC | Reclutamiento 50 |
| 7-9 | Paper + grant scale | Diseño RFdiffusion3 | Piloto 3 comunidades | Ensayos CEDIC in vitro | Seguimiento mes 1-6 |
| 10-12 | Scale-ready | Expresión + BLI | Datos + análisis | Paper in vitro | Análisis interino |
| Output año 1 | 1-2 papers | paper venoma + gate | 1 paper metodológico | 1-2 papers | cohorte andando |

**Regla de oro**: solo #1, #4 y #9 (Nextclade, del top 10) arrancan sin ninguna dependencia externa. #2 depende del outreach, #3 del comité, #5 del champion cardiológico. Arrancar las independientes ya; las dependentes activan su gestión desde el mes 1 pero su ejecución cuando se desbloqueen.

---

# §7 — Comparativa final

| Dimensión | #1 HeAR | #2 Antiveneno | #3 Stack Chaco | #4 Chagas in silico | #5 Smartwatch |
|---|---|---|---|---|---|
| Score | 92.5 | 89 | 88 | 86 | 84 |
| Costo total | $30k | $450k-1M | $440k | $200-450k (F1-3) | $140k-1M |
| Primer resultado | 4 semanas | 9 meses | 9 meses | 6 meses | 18 meses |
| First-mover | LatAm | **Mundial** | LatAm | Paraguay | **Mundial** |
| Riesgo dominante | Técnico (bajo) | Experimental (medio) | Operacional (medio) | Metodológico (bajo-medio) | Humano (medio) |
| Dependencia crítica | Ninguna | Baker Lab | PM senior | CEDIC + compute | Cardiólogo champion |
| Valor replicable | Muy alto | Alto | Muy alto | Alto | Medio |

---

## Última actualización

Septiembre 2026.