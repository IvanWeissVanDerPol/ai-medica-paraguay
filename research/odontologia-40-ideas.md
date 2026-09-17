# 40 ideas de IA en odontología y salud bucal para Paraguay — investigadas y rankeadas

> **Qué es este archivo:** catálogo de 40 ideas de IA/salud digital aplicadas a odontología y salud bucal en Paraguay, con el mismo sistema de scoring de 7 dimensiones del master ranking (impacto 25%, viabilidad técnica 20%, costo 15%, tiempo 15%, riesgo 10%, first-mover 10%, replicabilidad 5%).
>
> **Audiencia:** quien decide qué construir. Cada idea incluye qué es, evidencia que la respalda, y score desglosado.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — Contexto epidemiológico paraguayo (por qué estas ideas importan)
- §2 — Stack técnico disponible (datasets abiertos + modelos)
- §3 — Las 40 ideas rankeadas (tabla master)
- §4 — Tier S/A (78+): las 8 mejores explicadas en detalle
- §5 — Tier B (70-77)
- §6 — Tier C (60-69)
- §7 — Tier D (<60)
- §8 — Anti-recomendaciones
- §9 — Tesis final

---

## §1 — Contexto epidemiológico paraguayo

### 1.1 Carga nacional (ENSABUD PY 2017 + WHO Country Profile 2022)

| Indicador | Valor | Fuente |
|---|---|---|
| CPO-D a los 12 años | 2.07 (etapa consolidación) | ENSABUD 2017 |
| Prevalencia de caries (general) | 63.31% | ENSABUD 2017 |
| Prevalencia rural vs urbana | 74.58% vs 57.75% | ENSABUD 2017 |
| ceo-d a los 5-6 años | 3.88 | ENSABUD 2017 |
| CPO-D a los 15 años | 3.14 | ENSABUD 2017 |
| Caries no tratada en dentición temporal (1-9 años) | 42.7% | WHO 2022 (GBD 2019) |
| Caries no tratada en permanentes (5+ años) | 26.7% | WHO 2022 |
| Enfermedad periodontal severa (15+ años) | 15.1% | WHO 2022 |
| Edentulismo (20+ años) | 8.2% | WHO 2022 |

**Dato estructural**: solo el 1.4% de la fuerza laboral dental mundial atiende a países de ingreso bajo (WHO). La brecha no se cierra sumando odontólogos — se cierra con tecnología de tamizaje y prevención.

### 1.2 La inequidad extrema: poblaciones indígenas

| Población | Indicador | Valor | Comparación |
|---|---|---|---|
| Maká 12-15 años (Mariano Roque Alonso) | CPO-D | **10.5** | 5x el nacional |
| Maká 20-35 años | CPO-D | **18.8** | 9x el nacional |
| Maká 12-15 años | gingivitis | 94.9% | — |
| Maká 12-15 años | fluorosis | 30.5% | — |
| Pykasú (Guaraní Ñandeva, Chaco) 3-13 años | ceo-d temporal | **5.06** | alto WHO |
| Pykasú | sangrado al sondaje >10% superficies | **94.8%** | — |
| Meta-análisis global indígena (95 estudios) | dmft/DMFT | 3.75 / 2.36 | sin mejora en 60 años |

Los niños indígenas paraguayos tienen **5-9 veces** la carga de caries del promedio nacional, con acceso casi nulo a servicios (Pykasú: "la comunidad no recibe atención odontolológica y en varias ocasiones solicitaron dicho servicio y no obtuvieron respuestas").

### 1.3 La ventana institucional crítica

- **FOUNA está construyendo su Hospital Odontológico (2026-2031) con financiamiento KOICA** (Agencia de Cooperación Coreana). Proyecto "Establecimiento del Hospital Odontológico de FOUNA y Fortalecimiento de Capacidades para Mejorar la Salud Bucodental de la Población del Paraguay". Un hospital nuevo que se diseña HOY puede nacer digital-nativo e IA-ready — o nacer obsoleto. Esta es la ventana de diseño más importante de la década para la odontología paraguaya.
- **Programas MSPBS existentes**: "Paraguay Sonríe" (clínicas móviles), "Salvemos al Primer Molar", Dirección de Salud Bucodental (DSBD) con cultura de calibración epidemiológica ENSABUD.
- FOUNA = "Alma Mater de la Odontología Paraguaya", 80+ años, con práctica clínica estudiantil (175 estudiantes con pacientes en 2021).

---

## §2 — Stack técnico disponible (todo abierto/público)

### 2.1 Datasets públicos de imágenes dentales

| Dataset | Contenido | Acceso |
|---|---|---|
| **CariesXrays** (AAAI 2024) | 6,000 panorámicas, 13,783 instancias de caries anotadas por 3+ profesionales | GitHub: Binz-Chen/AAAI2024_CariesXrays |
| **OdontoAI Open Panoramic** (IvisionLab, Brasil) | 4,000 panorámicas con dientes/restauraciones/aparatos anotados + plataforma de benchmark online | Request vía GitHub |
| **Multi-center dental dataset** (Ningxia+Shenzhen) | 6,536 panorámicas: 2,555 impactados, 2,735 periodontitis, 1,246 caries | GitHub: qinxin99/qinxini |
| **Bitewing Mendeley** | 100 bitewings con caries anotadas por 8 odontólogos (COCO) | Mendeley Data |
| AAOF Legacy (cefalometría) | 110+ cefalogramas laterales | AAOF |

**Total público: >16,000 imágenes panorámicas anotadas.** Suficiente para entrenar/adaptar sin recolectar una sola imagen local para el POC.

### 2.2 Modelos y performance reportada

| Tarea | Performance SOTA | Referencia |
|---|---|---|
| Caries en panorámicas (multi-etapa) | F1 0.85, accuracy 0.93, recall 0.96 | Sci Rep 2025 (Mahidol) |
| Caries en **fotos smartphone** | accuracy 0.92 | revisado en Sci Rep 2025 |
| Caries en fotos intraorales | accuracy 0.92 | idem |
| Periodontitis staging AAP 2017 (YOLOv8) | precision 0.95-0.97, recall 0.94-0.96 | PubMed 2025 (Vietnam) |
| Cefalometría automática (MS-YOLOV3) | SDR 95% dentro de 4mm | PMC 2023 |
| Cáncer oral app smartphone (DiagnOCe) | AUC 0.867, F1 86.4%, kappa 0.88 | J Indian Acad Oral Med Radiol 2025 |
| Índice de placa por foto (YOLOv8Seg) | DSC 95%, precision 98% | EPMA J 2025 |
| Gingivitis por foto | AUC 87% | revisión sistemática PMC |
| Anemia por foto gingival | demostrado | JIAOMR 2025 |

### 2.3 Intervenciones digitales validadas

- **Teledentología WhatsApp** (JMIR 2026, Chile rural): 4 módulos educativos por video → efectos grandes en conocimiento de caries (r=0.49), actitudes (r=0.42) y periodoncia (r=0.59). Blueprint directo para Paraguay.
- **LLMs en educación dental**: 31% de educadores globales ya usa IA; materiales generados por LLM alcanzan estándares PEMAT con revisión humana (BDJ Open 2025).
- **Biomarcadores salivales + IA para periodontitis**: AUC 0.93-0.96 con aMMP-8, IL-1β, calprotectina; microbioma salival con firmas persistentes.

---

## §3 — Las 40 ideas rankeadas (tabla master)

| Rank | # | Idea | Score | Tier |
|---|---|---|---|---|
| 1 | 1 | ENSABUD-AI: CPO-D automático desde panorámicas para vigilancia nacional | 84.5 | S |
| 2 | 2 | App de tamizaje de caries con fotos smartphone para agentes comunitarios | 82.5 | S |
| 3 | 3 | Teledentología WhatsApp educativa bilingüe (español-guaraní) | 82.5 | S |
| 4 | 4 | Chatbot de educación oral en español + guaraní | 80.5 | S |
| 5 | 5 | Tamizaje escolar masivo con fotos + IA (alineado a ENSABUD/DSBD) | 79.0 | A |
| 6 | 6 | Detector de caries en panorámicas para FOUNA/Hospital Odontológico | 79.0 | A |
| 7 | 7 | Periodontitis: staging AAP 2017 automático (YOLOv8) | 77.0 | A |
| 8 | 8 | Programa de salud bucal indígena del Chaco con IA (tamizaje+teledentología) | 75.5 | A |
| 9 | 9 | Tamizaje de cáncer oral con smartphone (blueprint DiagnOCe) | 74.5 | A |
| 10 | 10 | Hospital Odontológico FOUNA digital-nativo: EHR odontológico open source desde el día 1 | 74.0 | A |
| 11 | 11 | Cefalometría automática open source para ortodoncia FOUNA | 72.5 | B |
| 12 | 12 | Detección de fluorosis por foto (30.5% en Maká) | 72.0 | B |
| 13 | 13 | Registro de placa bacteriana por foto para prevención personalizada | 71.5 | B |
| 14 | 14 | Detección de anemia por fotografía gingival (tamizaje incidental) | 71.0 | B |
| 15 | 15 | Detección de terceros molares incluidos + supernumerarios | 70.5 | B |
| 16 | 16 | Modelo predictivo geoespacial de caries por distrito | 70.0 | B |
| 17 | 17 | Triaje radiográfico offline para clínicas móviles "Paraguay Sonríe" | 69.5 | B |
| 18 | 18 | Pacientes virtuales con LLM para entrenamiento clínico FOUNA | 69.0 | B |
| 19 | 19 | Historia clínica odontológica + dashboard de vigilancia DSBD | 68.5 | B |
| 20 | 20 | Control de calidad automático de radiografías panorámicas | 68.0 | B |
| 21 | 21 | Recordatorios + adherencia post-quirúrgica por WhatsApp | 67.5 | B |
| 22 | 22 | Chatbot de triage de dolor dental (urgencia vs espera) | 67.0 | B |
| 23 | 23 | Modelo de riesgo individual de caries (CAMBRA+ML) en escuelas | 66.5 | B |
| 24 | 24 | Detector de lesiones periapicales (PAI automático) | 66.0 | B |
| 25 | 25 | Análisis de escaneos 3D intraorales para ortodoncia | 65.0 | C |
| 26 | 26 | Evaluación automática de preparaciones dentales de estudiantes | 64.5 | C |
| 27 | 27 | Generación de materiales educativos con LLM validados PEMAT | 64.0 | C |
| 28 | 28 | Optimización de rutas de clínicas móviles con IA operativa | 63.5 | C |
| 29 | 29 | Predicción de no-show a citas odontológicas | 63.0 | C |
| 30 | 30 | Panel salival aMMP-8 + IA para periodontitis activa | 62.5 | C |
| 31 | 31 | Primer catálogo del microbioma oral paraguayo (16S) | 62.0 | C |
| 32 | 32 | Plataforma OdontoAI-paraguaya: hub de datos anotados locales | 61.5 | C |
| 33 | 33 | Electiva de IA en odontología FOUNA | 61.0 | C |
| 34 | 34 | Tamizaje bucal offline con audio/íconos en lenguas indígenas | 60.5 | C |
| 35 | 35 | Detección de caries oclusal por foto sin fluorescencia | 60.0 | C |
| 36 | 36 | Registro nacional de cáncer oral + linkage hospitalario | 59.5 | C |
| 37 | 37 | Diseño generativo de prótesis (CAD/CAM asistido por IA) | 55.0 | D |
| 38 | 38 | Protocolo CARE de gobernanza de datos para tamizaje indígena | 54.5 | D |
| 39 | 39 | Detección de xerostomía/trastornos salivales por IA | 50.0 | D |
| 40 | 40 | Asistente LLM de codificación de diagnósticos odontológicos (CDT/CIE) | 48.0 | D |

---

## §4 — Tier S/A (78+): las 8 mejores explicadas

### #1 — ENSABUD-AI: CPO-D automático desde panorámicas — Score 84.5

**Qué es**: sistema que estima CPO-D/ceo-d automáticamente desde radiografías panorámicas usando modelos pre-entrenados (CariesXrays 6,000 imágenes + OdontoAI 4,000), validado contra calibración ENSABUD, para vigilancia epidemiológica continua en lugar de encuestas cada 10 años.

**Por qué es #1**:
- **A=8**: la vigilancia actual es un censo cada década (ENSABUD 2008 → 2017 → próximo ~2027). Con IA, cada panorámica tomada en cualquier servicio del país alimenta el sistema de vigilancia. Cambia la granularidad de país-cada-10-años a distrito-continuo.
- **B=9**: 10,000+ imágenes públicas anotadas + modelos con F1 0.85 publicados. El POC es fine-tuning sobre datos públicos + validación con 200-500 panorámicas locales calibradas por odontólogos ENSABUD (que ya tienen cultura de calibración kappa).
- **C=9**: <$5k el POC (Colab + datos públicos).
- **D=9**: notebook en 2-4 semanas.
- **E=8**: el riesgo principal es domain shift (radiógrafos paraguayos vs asiáticos) — mitigable con fine-tuning ligero.
- **F=7**: ningún país de la región ha automatizado su vigilancia bucal con IA.
- **G=9**: el mismo sistema sirve para periodontitis, lesiones apicales, edentulismo.

**Implementación**: (1) entrenar detector en CariesXrays/OdontoAI; (2) validar en 300 panorámicas FOUNA anotadas por 2 odontólogos calibrados (kappa objetivo >0.8); (3) paper de validación; (4) deploy en servicios DSBD con dashboard. **Champion**: DSBD-MSPBS + FOUNA (los mismos que hacen ENSABUD).

**Costo**: $5-10k POC; $30-60k deploy. **Output**: 1-2 papers + primer sistema de vigilancia bucal continua de LatAm.

---

### #2 — App de tamizaje de caries con fotos smartphone — Score 82.5

**Qué es**: app móvil (offline-first) donde un agente comunitario o docente fotografía los dientes de un niño y el modelo (accuracy 0.92 reportado en literatura para fotos smartphone) estima lesiones visibles de caries → lista de derivación priorizada.

**Por qué es #2**:
- **A=9**: 42.7% de niños 1-9 con caries no tratada; el tamizaje actual requiere odontólogo itinerante. Un teléfono en manos de un promotor multiplica la cobertura de detección 10-100x.
- **B=8**: accuracy 0.92 demostrada en fotos smartphone (literatura 2024-2025); datasets públicos de fotos intraorales existen (menores que los radiográficos, pero suficientes para POC).
- **C=9, D=8**: POC $3-5k en 1-2 meses.
- **E=7**: fotos de campo con iluminación variable — mitigable con protocolo estandarizado de captura (flash, distancia, retractor).
- **F=7, G=9**: el mismo modelo escala a fluorosis, gingivitis, cáncer oral.

**Implementación**: (1) fine-tune en datasets públicos de fotos intraorales; (2) protocolo de captura estandarizado; (3) validación en 300 niños FOUNA con examen odontológico como gold standard; (4) app APK offline (TFLite). **Champion**: DSBD + FOUNA extensión.

---

### #3 — Teledentología WhatsApp educativa bilingüe — Score 82.5

**Qué es**: réplica paraguaya del ensayo chileno JMIR 2026 (La Araucanía rural): 4 módulos educativos en video (autocuidado, caries, periodoncia, cáncer oral) entregados por WhatsApp durante 2 semanas post-tamizaje, con versión en guaraní.

**Por qué es #3**:
- **A=8**: la caries es enfermedad de comportamiento; el tamizaje sin educación no baja incidencia. El estudio chileno mostró efectos GRANDES (r=0.42-0.59) con intervención de costo casi cero.
- **B=9**: blueprint metodológico completo publicado (módulos, validación I-CVI, PEMAT-AV). Solo adaptar contenido + traducir a guaraní + grabar.
- **C=9**: <$5k (producción de videos + plataforma WhatsApp Business API).
- **D=8**: 2-3 meses a ensayo piloto.
- **E=8**: el efecto ya está demostrado en población similar (rural LatAm).
- **F=7**: primera teledentología WhatsApp bilingüe español-guaraní.
- **G=8**: replicable a cualquier tema de salud.

**Implementación**: (1) adaptar los 4 módulos al contexto paraguayo (dieta, algarrobo, acceso); (2) traducción guaraní con revisión comunitaria; (3) videos de 5 min; (4) ensayo en 2 comunidades con medición pre/post conocimiento. **Champion**: FOUNA extensión + DSBD.

---

### #4 — Chatbot de educación oral en español + guaraní — Score 80.5

**Qué es**: chatbot (WhatsApp o web) con LLM open (Gemma/Llama fine-tuned o RAG sobre guías DSBD/OMS) que responde dudas de salud bucal en español y guaraní, con disclaimer de no-diagnóstico y derivación.

**Por qué**:
- **A=8**: la búsqueda de información oral la hace hoy Google con calidad variable y sin español paraguayo ni guaraní. 31% de educadores dentales globales ya usa LLMs.
- **B=8**: LLMs abiertos + RAG sobre contenido validado es arquitectura estándar; la literatura BDJ 2025 muestra que con revisión humana el material alcanza estándares PEMAT.
- **C=9, D=8, E=7** (riesgo: respuestas incorrectas → mitigación con RAG estricto + guardrails + revisión odontológica).
- **F=8**: primer chatbot de salud bucal en guaraní del mundo.
- **G=8**.

**Implementación**: (1) corpus de guías DSBD/OMS/FOUNA; (2) RAG + Gemma 2B/9B cuantizado (corre en servidor barato); (3) validación de 200 preguntas frecuentes por panel FOUNA; (4) deploy WhatsApp Business API. **Costo**: $10-20k.

---

### #5 — Tamizaje escolar masivo con fotos + IA — Score 79.0

Extensión operativa de #2: campaña nacional anual de tamizaje bucal escolar donde docentes/promotores fotografían con app estandarizada, generando (a) listas de derivación por escuela y (b) datos de vigilancia CPO-D visual por distrito que alimentan #1. Se alinea a los programas existentes (Salvemos al Primer Molar, clínicas móviles Paraguay Sonríe) y genera el primer dataset escolar longitudinal paraguayo. **Champion**: DSBD + Ministerio de Educación. A=9, B=8, C=8, D=7, E=6 (logística escolar), F=7, G=9.

### #6 — Detector de caries en panorámicas FOUNA — Score 79.0

Versión clínica-asistencial de #1: herramienta de segundo lector para el futuro Hospital Odontológico FOUNA y clínicas de enseñanza — detecta y marca caries multi-etapa (esmalte/dentina/pulpa) en panorámicas con recall 0.96 (prioriza no perder lesiones). Reduce variabilidad inter-observador en la formación de estudiantes. A=8, B=9, C=8, D=8, E=8, F=5 (ya existe comercialmente fuera — el valor local es validación + docencia), G=8.

### #7 — Periodontitis: staging AAP 2017 automático — Score 77.0

Réplica del sistema YOLOv8 vietnamita (precision 0.95-0.97 en hueso alveolar/CEJ): segmenta nivel óseo + CEJ + ejes dentales desde panorámicas y calcula stage/grade AAP 2017 con edad/tabaquismo/diabetes. 15.1% de paraguayos 15+ tiene periodontitis severa y el tamizaje periodontal es el más laborioso (sondaje completo). Radiográfico-automático = tamizaje poblacional. A=8, B=8, C=8, D=7, E=7, F=6, G=8.

### #8 — Programa de salud bucal indígena del Chaco con IA — Score 75.5

**El de mayor impacto en salud pura de toda la lista** (CPOD 10.5-18.8 = emergencia sanitaria silenciosa), compuesto: tamizaje con app de fotos (#2) por promotores bilingües + teledentología WhatsApp (#3) en guaraní/ñandeva + derivación a clínicas móviles priorizada por IA + registro comunitario con gobernanza de datos (idea #38 incorporada). Score limitado por: E=6 (logística chaqueña, sensibilidad cultural), C=6, D=6. **F=9**: primer programa de salud bucal indígena con IA de LatAm. Champion: DSBD + FOUNA extensión + iglesias/ONGs chaqueñas existentes.

### #9 — Tamizaje de cáncer oral con smartphone — Score 74.5

Blueprint DiagnOCe (India): app que clasifica lesiones orales en fotos → deriva sospechosos. Supervivencia oral cancer 86% localizado vs 40% diseminado; Paraguay tiene carga de factores de riesgo (tabaco, alcohol, mate caliente). A=7, B=8, C=8, D=7, E=7, F=8, G=7. Champion: FOUNA medicina oral + INCAN.

### #10 — Hospital Odontológico FOUNA digital-nativo — Score 74.0

La KOICA está financiando el hospital 2026-2031. Propuesta: que el diseño incluya desde el día 1 (a) EHR odontológico open source (OpenDental/OpenMRS-dental), (b) PACS con interoperabilidad DICOM, (c) pipelines de IA (#1, #6, #7) como segundo lector, (d) dataset de investigación gobernanza-FAIR. Es una ventana que se cierra: un hospital que nace digital cuesta una fracción de digitalizar uno viejo. A=7 (habilitador de todo lo demás), B=7, C=5, D=5, E=7, F=7 (primer hospital odontológico digital-nativo de la región), G=8. **Esta idea es estratégicamente la más importante aunque su score no sea el más alto — sin ella, las demás se quedan sin casa.**

---

## §5 — Tier B (70-77)

| # | Idea | Score | Nota clave |
|---|---|---|---|
| 11 | Cefalometría automática (MS-YOLOV3, SDR 95% a 4mm) | 72.5 | Ahorra 15-30 min por cefalograma en ortodoncia FOUNA; datasets AAOF públicos |
| 12 | Fluorosis por foto (30.5% en Maká) | 72.0 | Vigilancia de fluorosis + mapeo de exposición a agua |
| 13 | Placa bacteriana por foto (DSC 95%) | 71.5 | Prevención personalizada; feedback visual al paciente |
| 14 | Anemia por foto gingival | 71.0 | Tamizaje incidental en campaña dental (sin punción) |
| 15 | Terceros molares incluidos + supernumerarios | 70.5 | Dataset multi-centro público (2,555 casos) |
| 16 | Modelo geoespacial de caries por distrito | 70.0 | Censo + ENSABUD + satélite → priorizar clínicas móviles |
| 17 | Triaje radiográfico offline clínicas móviles | 69.5 | "Paraguay Sonríe" con segundo lector IA sin conectividad |
| 18 | Pacientes virtuales LLM para estudiantes FOUNA | 69.0 | Entrenamiento de anamnesis; ya demostrado con ChatGPT |
| 19 | EHR odontológico + dashboard DSBD | 68.5 | Base de datos nacional (ver #10) |
| 20 | Control de calidad automático de panorámicas | 68.0 | Detecta artefactos/posicionamiento antes de lectura |
| 21 | Recordatorios post-quirúrgicos WhatsApp | 67.5 | Adherencia post-extracción |
| 22 | Chatbot triage dolor dental | 67.0 | Urgencia vs espera; reduce consultas evitables |
| 23 | Riesgo individual de caries (CAMBRA+ML) | 66.5 | Preventivo selectivo en escuelas |
| 24 | Lesiones periapicales (PAI automático) | 66.0 | Endodoncia FOUNA |

## §6 — Tier C (60-69)

| # | Idea | Score | Nota |
|---|---|---|---|
| 25 | Escaneos 3D intraorales → análisis ortodóntico | 65.0 | Requiere escáneres ($$$) — solo FOUNA especialidades |
| 26 | Evaluación automática de preparaciones estudiantiles | 64.5 | CV sobre dientes simulados; feedback objetivo |
| 27 | Materiales educativos LLM validados PEMAT | 64.0 | Blueprint BDJ 2025 |
| 28 | Optimización rutas clínicas móviles | 63.5 | VRP + demanda predicha |
| 29 | Predicción de no-show | 63.0 | Datos requeridos que hoy no existen (depende de #19) |
| 30 | aMMP-8 salival + IA periodontitis activa | 62.5 | POC tests comerciales caros; validación local necesaria |
| 31 | Catálogo microbioma oral paraguayo (16S) | 62.0 | Primer catálogo; costo secuenciación moderado |
| 32 | Hub de datos anotados OdontoAI-PY | 61.5 | Infraestructura de comunidad; crece con #1/#2 |
| 33 | Electiva IA en odontología FOUNA | 61.0 | Formación; multiplicador a largo plazo |
| 34 | App tamizaje con audio/íconos en lenguas indígenas | 60.5 | UX para nivaclé/qom/enxet; parte de #8 |
| 35 | Caries oclusal por foto sin fluorescencia | 60.0 | Solapamiento con #2 |
| 36 | Registro nacional cáncer oral | 59.5 | Epidemiología; requiere regulación de datos |

## §7 — Tier D (<60)

| # | Idea | Score | Por qué baja |
|---|---|---|---|
| 37 | Diseño generativo prótesis CAD/CAM | 55.0 | Requiere infraestructura de impresión/milling que no existe |
| 38 | Protocolo CARE gobernanza datos indígenas | 54.5 | Esencial pero no standalone — se integra en #8 |
| 39 | Xerostomía/trastornos salivales por IA | 50.0 | Caso de uso estrecho; sin datasets |
| 40 | Codificación diagnóstica LLM (CDT/CIE) | 48.0 | Depende de EHR inexistente; mercado pequeño |

---

## §8 — Anti-recomendaciones

| ❌ No hacer | Razón |
|---|---|
| Comprar software comercial de detección de caries cerrado | Los modelos públicos igualan performance y no generan capacidad local |
| Empezar por el chatbot diagnóstico (no educativo) | Responsabilidad clínica sin marco regulatorio; el educativo es seguro y suficiente |
| Diseñar app indígena sin consulta comunitaria previa | Repite el fracaso descrito en Pykasú ("solicitaron el servicio y no obtuvieron respuesta") |
| Recolectar imágenes locales ANTES del POC con datos públicos | 16,000 imágenes públicas disponibles; la local solo para validación |
| Digitalizar el hospital FOUNA después de construirlo | La ventana de diseño KOICA es ahora |

---

## §9 — Tesis final

**La odontología es la especialidad médica donde Paraguay puede capturar valor de IA más rápido**, por cuatro razones:

1. **Los datasets ya existen públicos** (16,000+ panorámicas anotadas) — no hay que esperar biobancos ni consentimientos clínicos para el POC.
2. **La carga es masiva y medible** (63% prevalencia de caries; CPOD indígena 5-9x nacional) — cada punto de mejora es visible.
3. **El tamizaje no requiere médico** — fotos y radiografías las puede tomar personal no odontólogo, así que la IA no reemplaza sino que habilita cobertura donde no hay nadie.
4. **La ventana institucional perfecta**: Hospital Odontológico FOUNA-KOICA 2026-2031 + ENSABUD próxima + programas DSBD activos.

**Portafolio recomendado de arranque (los 4 S + el habilitador):**
1. **#1 ENSABUD-AI** ($5-10k, POC en semanas) — vigilancia
2. **#2 App fotos caries** ($3-5k) — tamizaje comunitario
3. **#3 Teledentología WhatsApp guaraní** ($5k) — prevención con efecto demostrado
4. **#4 Chatbot bilingüe** ($10-20k) — educación
5. **#10 Hospital digital-nativo** ($0 en software open; diseño) — el habilitador estratégico

Y el proyecto de mayor impacto en salud pura: **#8 Programa indígena del Chaco**, que combina #2+#3+#34+#38 sobre la emergencia de CPOD 18.8.

**Total del portafolio S+A: <$150k, 12-18 meses, 6-10 papers, y Paraguay como primer país de la región con vigilancia bucal continua asistida por IA.**

---

## Fuentes principales

- ENSABUD PY 2017 (MSPBS/OPS/OMS) — docs.bvsalud.org/biblioref/2018/11/964767
- WHO Paraguay Oral Health Country Profile 2022 — cdn.who.int
- Sci Rep 2025;15:33491 — caries multistage panorámicas (F1 0.85, recall 0.96)
- CariesXrays AAAI 2024 — github.com/Binz-Chen/AAAI2024_CariesXrays
- OdontoAI Open Panoramic — github.com/IvisionLab/OdontoAI-Open-Panoramic-Radiographs
- Multi-center dataset — github.com/qinxin99/qinxini (PMC11031544)
- YOLOv8 periodontitis staging — PubMed 41088206
- DiagnOCe cáncer oral app — JIAOMR 2025 (AUC 0.867)
- WhatsApp teledentistry Chile — JMIR mHealth 2026;1:e71251
- Pykasú Chaco indígena — Mem Inst Investig Cienc Salud 2016;14(1):40-49
- Maká oral health — Rev Odontoestomatología (medigraphic 94097)
- Global indigenous caries meta-analysis — systematic review 2026 (95 estudios)
- FOUNA Hospital Odontológico KOICA — odo.una.py (agosto 2026)
- LLMs dental education survey — Eur J Dent Educ 2024;28(4)
- Salivary biomarkers + AI — PMC12452651 (AUC 0.93-0.96)
- Placa/gingivitis por foto — EPMA J 2025 (s13167-025-00432-5)

## Última actualización

Septiembre 2026.