# LA IDEA COMPLETA — Sistema de IA odontológica de red privada paraguaya

> **Qué es este archivo:** el documento definitivo que ata todo: la oportunidad, el sistema, cada componente en detalle, la secuencia, los números, los riesgos y la visión a 5 años. Escrito para que alguien que no leyó nada del repo entienda todo de una pasada — y para que la red lo use como documento fundacional.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- PARTE I — La oportunidad (por qué esto, por qué ahora, por qué ustedes)
- PARTE II — El sistema completo (arquitectura explicada)
- PARTE III — Los 5 proyectos en detalle completo
- PARTE IV — Los 12 proyectos que emergen solos
- PARTE V — La secuencia de construcción (18 meses)
- PARTE VI — Los números (costos, ingresos, escenarios)
- PARTE VII — Riesgos y cómo se manejan
- PARTE VIII — La visión a 5 años (el final del camino)
- PARTE IX — Qué se necesita para empezar el lunes

---

# PARTE I — La oportunidad

## 1.1 El contexto mundial (30 segundos)

La IA médica cruzó el umbral de lo utilitario. En odontología específicamente, en los últimos 24 meses se publicaron:

- Modelos que detectan caries en radiografías panorámicas con **F1 0.85 y recall 0.96** (Scientific Reports 2025)
- Modelos que clasifican lesiones orales en fotos de celular con **AUC 0.867** usando una app hecha en Chile rural / India con herramientas sin código (DiagnOCe)
- Datasets públicos con **16,000+ radiografías panorámicas y 13,500 fotos de lesiones orales ya anotadas** (CariesXrays AAAI 2024, OdontoAI Brasil, Egipto BDJ 2025, Sri Lanka 2024)
- Apps de teledentología por WhatsApp con **efectos grandes demostrados** (r=0.42-0.59, JMIR 2026)

**Todo eso es abierto y gratuito.** Lo que NO es abierto ni gratuito es lo único que la industria no puede fabricar: **ojos clínicos expertos con décadas de criterio, dispuestos a etiquetar, validar y dirigir.**

## 1.2 El contexto paraguayo (60 segundos)

- 63% de prevalencia de caries; 42.7% de niños con caries no tratada; poblaciones indígenas con 5-9x la carga nacional (CPOD 10.5-18.8 documentado en Maká)
- Cáncer oral con la firma local perfecta: mate muy caliente (IARC grupo 2A, estudios con datos paraguayos) + tabaco + sol — y supervivencia que salta de 40% a 86% según cuándo se detecta
- La vía institucional es lenta: FOUNA (la facultad estatal) es ineficiente en la experiencia directa de la red; los programas públicos existen pero no digitalizan
- **No existe UN solo dataset odontológico paraguayo**. Ni público ni privado. Las empresas del mundo entrenan IA con datos asiáticos que no representan esta población.

## 1.3 El activo que tiene la red (lo que cambia todo)

| Quién | Qué aporta | Por qué es escaso |
|---|---|---|
| **Iván** | Odontólogo 20+ años **+** capacidad técnica de IA/ingeniería | El puente clínica-tecnología en una sola persona. Normalmente eso son dos contrataciones y una torre de Babel |
| **Gabi** | Operatoria + estética dental, 20 años clínicos, doctorado | Es EXACTAMENTE el perfil de anotadora experta que la industria de IA dental contrata y no consigue |
| **Colegas "análogos a patólogos"** | Lectura especializada multi-área | La capa de ground truth — el segundo lector, el validador, el circuito de confirmación |
| **Profesionales dentales de la red** | Consultorios, pacientes, volumen | Sitios de validación multicéntricos naturales, sin burocracia |
| **Grupo de trabajo activo** | Coordinación probada (el caso O3 lo demuestra: 442 preguntas respondidas, 9 horas de cuestionario, expediente completo) | Capacidad de ejecución documentada |

**La pieza que nadie más en Paraguay tiene**: criterio clínico calibrado + capacidad técnica + decisión privada. Las universidades tienen el criterio pero no la agilidad ni la técnica. Las tech companies tienen la técnica pero no el criterio ni los pacientes. La red tiene los tres.

## 1.4 La tesis en una frase

**Convertir el criterio clínico acumulado de la red (40+ años combinados) en la infraestructura de IA odontológica del país — empezando por servicios que generan ingreso inmediato (anotación/validación para la industria global), pasando por herramientas propias para los consultorios de la red, y terminando como los dueños del único dataset clínico paraguayo y la plataforma de salud bucal de referencia.**

---

# PARTE II — El sistema completo

## 2.1 El diagrama maestro

```
                        INGRESO EXTERNO
                              ▲
                              │ contratos de anotación/validación
                ┌─────────────┴──────────────┐
                │   #1 ESTUDIO DE ANOTACIÓN  │  ← EL MOTOR
                │   Y VALIDACIÓN EXPERTA     │
                │   (equipo calibrado κ>0.8) │
                └─────────────┬──────────────┘
                              │ produce ground truth
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  ┌───────────┐        ┌───────────┐        ┌───────────┐
  │ #2 ESTÉTICA│        │ #3 CARIES │        │ #4 CÁNCER │  ← LAS SALIDAS
  │ suite IA  │        │ screening │        │ ORAL      │
  │ (ingreso) │        │ (volumen) │        │(legitimidad│
  └─────┬─────┘        └─────┬─────┘        └─────┬─────┘
        │  pacientes + fotos │  mismo flujo  │     │
        └────────────────────┼───────────────┘     │
                             ▼                     │
                ┌────────────────────────┐         │
                │ #5 COPILOTO H. CLÍNICA │ ← EL VOLANTE
                │ (dictado → SOAP)       │         │
                └───────────┬────────────┘         │
                            ▼                      ▼
                ┌─────────────────────────────────────┐
                │ N7 DATASET PARAGUAYO                │  ← EL ACTIVO
                │ (crece por gravedad, todos hacia él)│
                └─────────────────────────────────────┘
                            ▼
                ┌─────────────────────────────────────┐
                │ N8 APP "BOCA PARAGUAYA"             │  ← LA PLATAFORMA
                │ + informe anual + verticales nuevas │
                └─────────────────────────────────────┘
```

## 2.2 Los cuatro roles, explicados

### El MOTOR (#1): el estudio de anotación y validación

Todo modelo de IA médica vale lo que valen sus etiquetas. La industria global de IA dental (empresas de EE.UU., Europa, Israel que hacen software de detección) tiene un cuello de botella permanente: conseguir **odontólogos especialistas que anoten miles de imágenes con criterio consistente**. Pagan $0.5-3 por imagen experta y $5-25k por proyectos de validación clínica.

El estudio de la red convierte el ojo de Gabi y los colegas en ese servicio:
1. Se calibran como equipo (protocolos + medición kappa, el estándar de acuerdo interobservador que ENSABUD ya usa en Paraguay)
2. Con kappa documentado >0.8, son contratables internacionalmente HOY
3. El pre-etiquetado con IA (el modelo etiqueta primero, el experto corrige) multiplica la velocidad 3-5x

**Por qué es el motor**: (a) genera ingreso desde el primer contrato sin inversión; (b) calibra al equipo en exactamente las tareas que después validan en los proyectos propios; (c) cada imagen local anotada entra al dataset propio — el negocio de terceros financia el activo propio.

### El VOLANTE (#5): el copiloto de historia clínica

Cada odontólogo pierde 45-90 minutos diarios documentando. El copiloto: el dentista dicta al final de la consulta (o del turno), Whisper transcribe, un LLM lo convierte en nota SOAP odontológica estructurada en español, el dentista revisa y firma.

**Por qué es el volante**: es el único proyecto que produce datos **continuamente y sin esfuerzo adicional**. Cada consulta documentada es un registro estructurado (hallazgos, diagnósticos, tratamientos, factores de riesgo) que cae al dataset por gravedad. Los otros proyectos producen datos por esfuerzo; este los produce como subproducto del trabajo diario. Y mientras gira, ahorra tiempo facturable a toda la red desde el primer mes.

### LAS SALIDAS (#2, #3, #4): perfiles complementarios

- **#2 Estética** = la salida de INGRESO. Los pacientes pagan por ver su sonrisa futura. Es el canal de adquisición: nadie llega por "tamizaje", pero llegan por estética — y en la visita se captura todo lo demás.
- **#3 Caries** = la salida de VOLUMEN. Cada paciente de cada consulta diaria pasa por el flujo. El volumen alimenta el dataset y la práctica.
- **#4 Cáncer oral** = la salida de LEGITIMIDAD. El proyecto con vidas salvadas medibles (86% vs 40%), publicaciones, prensa, y el ángulo científico único mundial (mate muy caliente). Es el que da nombre público al sistema.

Los tres comparten UNA app de captura estandarizada, UN protocolo de fotos, UN circuito de derivación interna. **El mismo paciente, la misma visita, tres salidas.**

### El ACTIVO (N7): el dataset paraguayo

Hoy no existe ningún dataset odontológico paraguayo. Con consentimiento informado de los pacientes de la red, todo lo que el sistema toca (fotos, radiografías, notas SOAP, factores de riesgo, resultados de tratamiento) converge en el primer dataset clínico paraguayo, doblemente anonimizado, FAIR, con gobernanza definida.

**Por qué es el activo**: quien tiene los datos locales controla el desarrollo de modelos locales. Las empresas que hoy entrenan con datos asiáticos necesitarán datos de esta población — y habrá exactamente una fuente. Además: es el insumo de la epidemiología privada paraguaya (el informe anual) y la base de cualquier vertical futura.

## 2.3 Los principios del sistema

1. **Nada pide permiso.** Todo arranca adentro de la red, con sus pacientes y su criterio. Las instituciones se suman después, de igual a igual.
2. **Nunca construir dos veces lo mismo.** Una app de captura, un equipo de calibración, un canal WhatsApp, un framework de consentimiento (Ley 7593), un dataset. Cada proyecto nuevo reutiliza 80% de infraestructura.
3. **Cada proyecto debe pagarse a sí mismo o alimentar al que se paga.** El sistema completo es <$100k en 18 meses — pero diseñado para que el motor (#1) y la estética (#2) financien al resto.
4. **El criterio clínico es el moat.** Los modelos son públicos; los datos públicos son públicos; lo que nadie puede copiar es 40 años de ojo clínico calibrado dirigiendo el sistema.

---

# PARTE III — Los 5 proyectos en detalle completo

## #1 — Estudio de anotación y validación experta

**Qué es exactamente**: un servicio profesional que vende anotación de imágenes dentales y validación clínica de modelos de IA a la industria global.

**El producto**:
- Anotación de imágenes (fotos intraorales, panorámicas, bitewings, cefalogramas): bounding boxes, segmentación de lesiones, clasificación por severidad
- Validación de modelos: empresas que entrenan IA necesitan que odontólogos independientes puntúen el rendimiento de su software sobre casos reales
- Calibración de equipos (kappa-as-a-service): grupos de investigación que necesitan sus anotadores calibrados

**Cómo funciona**:
- Label Studio (open source) montado en la infraestructura de Iván
- Protocolos de anotación escritos sobre estándares publicados (ICCMS para caries, AAP 2017 para periodoncia)
- Cada anotador pasa calibración; el equipo mide kappa internamente antes de ofrecer el servicio
- Expert-in-the-loop: un modelo base (entrenado con los datasets públicos) pre-etiqueta; el experto corrige; la velocidad sube 3-5x; cada corrección mejora el modelo propio

**Los números**:
- Inversión: ~$500 (Label Studio + tiempo de calibración)
- Precio de mercado: $0.5-3/imagen simple; más para segmentación; $5-25k proyectos de validación
- Capacidad realista del equipo: 200-500 imágenes/día con pre-etiquetado → $100-1,500/día potencial
- Gate de arranque comercial: kappa >0.8 documentado en 2 tareas

**Los primeros 30 días**:
1. Semana 1-2: protocolos de anotación escritos (3 tareas: caries foto, caries radiográfica, lesiones mucosa) + Label Studio andando
2. Semana 2-4: calibración — cada miembro anota las mismas 500 imágenes públicas; se mide kappa; se discuerda y se resuelve; se re-mide
3. Semana 4: con kappa documentado → portfolio (ejemplos de anotación + metodología) → outreach (plataformas de anotación especializada, contacto directo con startups de IA dental en LinkedIn, Upwork especializado)

**Por qué Gabi es la pieza central**: su especialidad ES la tarea #1 de la industria (operatoria = caries), tiene 20 años de lesiones vistas, doctorado, y (críticamente para este momento de su transición profesional) este trabajo no exige papers ni networks académicos — exige exactamente lo que ella tiene.

---

## #2 — Suite de IA para estética dental

**Qué es exactamente**: tres herramientas de IA para el flujo estético de los consultorios de la red:

1. **Simulación de sonrisa antes/después**: foto del paciente → modelo generativo (Stable Diffusion + ControlNet, fine-tuneado con los casos reales de 20 años de Gabi) → imagen del resultado anticipado. El paciente VE el resultado antes de aceptar el tratamiento.
2. **Match de color VITA por foto**: el eterno dolor de cabeza de la estética — comunicar el color al laboratorio. Clasificador entrenado para predecir la escala VITA desde foto estandarizada.
3. **Visualización de plan**: combinación de ambas + presupuesto generado del plan.

**Por qué funciona comercialmente**: las herramientas comerciales de smile design cuestan miles de dólares al año, están en inglés, y no están calibradas para fototipo/fenotipo latinoamericano. La versión propia, en español, entrenada con casos locales, se vende clínica por clínica — empezando por la red.

**El dataset es gratis**: Gabi tiene 20 años de casos antes/después. Ese archivo ES el entrenamiento del modelo — y no existe en ningún dataset público la representación del fenotipo local.

**Los números**: POC <$5k (fine-tuning + clasificador + app simple). Las métricas: fidelidad de simulación validada por panel de la red; accuracy de color vs consenso de 3 especialistas (o espectrofotómetro si se consigue).

**La sinergia oculta más valiosa**: cada paciente que entra por "quiero ver cómo quedaría mi sonrisa" es capturado por el flujo de fotos estandarizadas → tamizaje de caries (#3) y mucosa (#4) en la misma visita. **La estética es el caballo de Troya que financia y alimenta el tamizaje.**

---

## #3 — Red de tamizaje de caries entre pares

**Qué es exactamente**: el modelo de detección de caries por foto de celular (accuracy 0.92 publicado), validado en población paraguaya y desplegado como herramienta diaria de los consultorios de la red.

**El flujo**: paciente llega a consulta → fotos estandarizadas con la app → el modelo marca lesiones visibles → el dentista confirma con examen (gold standard) → el caso queda documentado con foto + diagnóstico + tratamiento (vía copiloto #5) → todo cae al dataset.

**Las dos salidas simultáneas**:
1. **Publicación**: validación de detección de caries por foto en población paraguaya — nadie lo hizo, se publica sin FOUNA (cualquier comité de ética independiente), y el equipo de #1 ya está calibrado para hacerlo
2. **Herramienta clínica**: el "módulo de aceptación de tratamiento" — mostrarle al paciente SU foto ampliada con la lesión marcada sube la aceptación de tratamiento (documentado en la literatura de cámaras intraorales) → más tratamiento aceptado = más facturación de los consultorios

**Extensiones que ya están en el camino**:
- Versión radiográfica (los 16k datasets públicos existen)
- Tamizaje escolar privado (colegios pagan el tamizaje anual — sin ministerio)
- Predicción individual de riesgo (cuando haya datos longitudinales)
- Extensión a periodoncia (pérdida ósea radiográfica, YOLOv8 publicado)

**Los números**: <$8k hasta validación publicable. 200 fotos de validación en los consultorios de la red (los pacientes ya vienen).

---

## #4 — Circuito privado de detección de cáncer oral

**Qué es exactamente**: el protocolo completo ya escrito (`cancer-oral-smartphone-protocolo.md`) con el circuito de confirmación resuelto internamente:

```
Paciente de riesgo (>40, tabaco/alcohol/mate muy caliente/sol)
   ↓ fotos estandarizadas (misma app de #2/#3)
Modelo clasifica lesiones (entrenado en 13,500 imágenes públicas)
   ↓ semáforo
Lectura por colega de la red (medicina oral/patología)
   ↓ si sospechoso
Derivación a cirujano de la red → biopsia (laboratorio privado)
   ↓
Histopatología = gold standard → tratamiento temprano + datos de validación
```

**Los números que justifican todo**: supervivencia a 5 años 86.3% (localizado) vs 40.4% (diseminado). La lesión precursora es visible AÑOS antes. Cada caso detectado a tiempo es una vida con el doble de probabilidad de sobrevivir — y el circuito completo cuesta menos de $15k de POC.

**El ángulo científico único mundial**: Paraguay es EL país del mate muy caliente (IARC 2A, con estudios caso-control que incluyeron datos paraguayos). Ninguna población del mundo tiene esta firma de riesgo térmico + la posibilidad de detección sistemática. Las extensiones:
- **Change detection de lesiones**: la misma lesión fotografiada en cada visita → el CAMBIO es la señal real de malignización → nadie en el mundo opera esto en práctica privada
- **El primer estudio de temperatura real del mate**: termómetro + hábitos → toda la literatura usa auto-reporte; medir exposición real cuesta ~$500 y es publicable alto
- **Registro de OPMD paraguayo**: hoy no existe ningún dato — la historia natural local es desconocida

**Por qué importa aunque sea el menos comercial**: es el proyecto de legitimidad. Un caso detectado y publicado ("la red privada detectó un cáncer oral temprano que el sistema no habría visto") legitima todo el sistema — y abre las puertas institucionales cuando convenga abrirlas, de igual a igual.

---

## #5 — Copiloto de historia clínica odontológica

**Qué es exactamente**: el dentista termina la consulta, presiona un botón, y dicta: "Paciente de 45 años, controlling, se realizó profilaxis, POA 2 con resina composite en el 36, oclusal distal, se detecta lesión blanca en vestibular del 13, fumador, toma mate muy caliente, recontrol en 6 meses". El sistema entrega: nota SOAP estructurada + flag de lesión para seguimiento + recordatorio programado a 6 meses + instrucciones post-consulta para el paciente por WhatsApp.

**La pila técnica**: Whisper (con el fine-tune español/guaraní ya identificado — misma inversión que el chatbot de salud del catálogo médico) → LLM con las plantillas de la red → revisión humana → firma.

**Por qué es estratégicamente el más importante aunque sea el más humilde**:
1. **Adopción trivial**: no cambia el flujo clínico, lo alivia. No diagnostica (cero fricción regulatoria). Ahorra desde el día 1.
2. **El volante de datos**: cada consulta → registro estructurado. En 12 meses, la red tiene la epidemiología de la práctica privada paraguaya que NADIE tiene (ni el MSPBS tiene sus datos estructurados así).
3. **El detector de riesgo pasivo**: el copiloto escucha "fumador, mate muy caliente" → agrega automáticamente los flags de tamizaje → conecta con #4 sin que nadie haga nada extra.
4. **La extensión natural**: la misma herramienta adaptada a los colegas "análogos a patólogos" de otras áreas → la red médica entera se digitaliza con la misma infraestructura.

**Los números**: demo en 2-4 semanas, <$5k. ROI del primer consultorio: si ahorra 45 min/día a un dentista que factura $50/hora, se paga solo en semanas.

---

# PARTE IV — Los 12 proyectos que emergen solos

Estos no se construyen — **aparecen** cuando el sistema gira:

| # | Proyecto | De dónde emerge | Cuándo |
|---|---|---|---|
| 1 | **App "boca paraguaya"** — la plataforma multi-módulo | #2+#3+#4+#5 integrados | Fase 5 |
| 2 | **Informe anual "Estado de la boca paraguaya"** | datos del copiloto + screenings | mes 12+ |
| 3 | **Modelo multimodal foto+factores de riesgo** | #3+#4+#5 cuando los factores se capturan sistemáticos | mes 9+ |
| 4 | **Change detection longitudinal de lesiones** | #4 + pacientes recurrentes | mes 6+ |
| 5 | **Estudio de temperatura real del mate** | #4+#5 + un termómetro | cuando se quiera |
| 6 | **Marketplace de segunda opinión especializada** | #3/#4 casos dudosos + la red | mes 6+ |
| 7 | **Tamizaje escolar privado** | #3 + protocolo de captura | mes 9+ |
| 8 | **Academia "IA para dentistas"** | todo el sistema | Fase 5 |
| 9 | **La red como CRO dental** (investigación contractual para industria: testing de materiales, pastas, adhesivos) | #1 + dataset + consultorios | año 2 |
| 10 | **Módulo pediátrico** (ceo-d automático) | #3 + colegios/consultas | año 2 |
| 11 | **Scores estéticos PES/WES automatizados** | #2 + fotos de seguimiento | año 2 |
| 12 | **Copiloto para otras especialidades médicas de la red** | #5 + los colegas | año 2-3 |

El punto: **el sistema no es una línea de proyectos — es un árbol que se ramifica solo.** Cada módulo nuevo cuesta una fracción del anterior porque la infraestructura ya existe.

---

# PARTE V — La secuencia de construcción (18 meses)

## Fase 1 (mes 1-2): EL MOTOR + LA DEMO
- Protocolos de anotación + Label Studio + **calibración del equipo (kappa)** — 500 imágenes públicas
- En paralelo: **demo del copiloto #5** (2-4 semanas, independiente de todo)
- **Gate**: kappa >0.8 documentado → abrir el negocio de anotación

## Fase 2 (mes 2-4): EL VOLANTE GIRA + PRIMERA SALIDA
- Copiloto #5 en uso diario en 3-5 consultorios de la red (empieza a generar datos)
- #3 caries: modelo fine-tuneado con datasets públicos + protocolo de validación listo
- Primer outreach comercial de anotación (con el kappa en la mano)

## Fase 3 (mes 3-5): LAS OTRAS DOS SALIDAS
- #2 estética: recopilar los casos de Gabi + fine-tune de simulación + clasificador VITA
- #4 cáncer: validación retrospectiva con los archivos de casos de la red + modelo entrenado
- **UNA sola app de captura estandarizada para #2+#3+#4** — se diseña una vez

## Fase 4 (mes 5-9): CIRCUITOS DE CAMPO
- #3 screening en consultorios (los pacientes ya vienen) — 200+ casos validados → paper
- #4 viaja en el mismo flujo (detección incidental de mucosa)
- #2 en consulta real (simulaciones a pacientes que pagan)
- El dataset N7 creciendo: solo (copiloto) + activo (screenings)

## Fase 5 (mes 9-18): CONSOLIDACIÓN
- Integración en la app "boca paraguaya"
- Primer informe anual "Estado de la boca paraguaya"
- Papers publicados (caries PY + cáncer oral PY + temperatura del mate)
- Decisión informada de verticales: ¿extender el modelo a otra especialidad de la red?

**Marcadores de éxito**:
- Mes 3: kappa documentado + copiloto en uso + primeros ingresos de anotación
- Mes 6: 200 screenings validados + estética en consulta real + dataset >1,000 casos
- Mes 12: paper(s) sometido(s) + informe anual + sistema auto-sostenido
- Mes 18: plataforma integrada + decisión de expansión con datos reales

---

# PARTE VI — Los números

## Inversión total (18 meses)

| Concepto | Monto |
|---|---|
| #1 Motor de anotación (setup + calibración) | $500 |
| #5 Copiloto (desarrollo + deploy) | $5,000 |
| #3 Caries (fine-tune + validación) | $8,000 |
| #2 Estética (fine-tune + clasificador + app) | $5,000 |
| #4 Cáncer oral (POC + validación) | $15,000 |
| Infraestructura compartida (app captura, nube, WhatsApp API) | $10,000 |
| Contingencia | $10,000 |
| **Total** | **~$53,500** |

## Fuentes de ingreso (activables en secuencia)

| Fuente | Cuándo | Potencial anual conservador |
|---|---|---|
| Anotación/validación para industria | mes 2+ | $20-80k (crece con el equipo) |
| Estética: suscripción clínicas + casos | mes 4+ | $10-50k |
| Copiloto: suscripción dentistas | mes 6+ | $10-40k ($15-30/mes × dentistas) |
| Tamizaje escolar privado | mes 9+ | $10-30k |
| Segunda opinión especializada | mes 6+ | variable |
| CRO dental (investigación contractual) | año 2 | $50-200k por estudio |
| Informe anual (prepagas/industria) | año 2 | $5-20k |

**Escenario conservador**: el sistema se autofinancia desde el mes 4-6 (anotación + estética cubren todo).
**Escenario medio**: año 1 termina con $50-100k de ingresos acumulados y el dataset paraguayo en construcción.
**Escenario alto**: el dataset + la plataforma interesan a un actor mayor (aseguradora, grupo de clínicas, empresa de IA) — y la red negocia desde la propiedad.

## El retorno no monetario

- **Para Gabi**: una posición profesional nueva construida sobre sus 20 años (no a pesar de ellos) — experta de referencia en IA dental clínica en Paraguay, con ingresos propios y un rol que ninguna clínica le puede quitar.
- **Para Iván**: el puente clínica-IA materializado en un sistema real, con publicaciones y la posición de "el que lo construyó".
- **Para la red**: la infraestructura propia — y la opción de escalar a sus otras áreas.
- **Para Paraguay**: el primer dataset odontológico del país, detección temprana de cáncer oral que hoy no existe, y un modelo demostrable de innovación médica privada.

---

# PARTE VII — Riesgos y cómo se manejan

| Riesgo | Prob. | Mitigación |
|---|---|---|
| El negocio de anotación tarda en despegar | Media | El sistema no depende de un solo ingreso; el copiloto ahorra costo desde el día 1 aunque no venda nada |
| Calidad de fotos variable en consultorios | Alta | Protocolo de captura guiado en la app (mitad del rendimiento es captura); calibración del flujo en Fase 2 |
| Carga de trabajo del equipo (todos tienen práctica) | Alta | Expert-in-the-loop reduce el esfuerzo por imagen; división clara: Iván técnico, Gabi criterio, colegas lectores puntuales |
| PPV bajo del tamizaje de cáncer → muchas derivaciones | Media | Filtro de dos niveles (IA → lector especializado → biopsia); reportar y ajustar umbrales |
| Regulatorio (uso de IA en salud) | Baja hoy | Todo es investigación/documentación/asistencia — no diagnóstico autónomo; framework Ley 7593 diseñado desde el inicio |
| Alguien copia la idea | Media | El moat no es la idea — es el equipo calibrado, los casos históricos de Gabi, y el dataset acumulado. Eso no se copia |
| Fatiga / abandono (proyecto paralelo a la vida clínica) | Alta | Fases cortas con gates; cada fase entrega algo usable YA (demo, herramienta, ingreso); celebrar los marcadores |
| Conflicto con el caso O3 | Baja | Separación estricta de mundos: nada del sistema toca O3 ni su ecosistema; el crecimiento es hacia fuera |

**El meta-riesgo real** es intentar todo a la vez. Por eso la secuencia: **una cosa por fase, cada fase entrega, cada entrega motiva.**

---

# PARTE VIII — La visión a 5 años

**Año 1**: el sistema odontológico funciona y se autofinancia. Primer dataset paraguayo. Primeras publicaciones. La red domina el nicho "IA dental clínica en Paraguay" — que ayer no existía.

**Año 2**: la plataforma "boca paraguaya" es la herramienta de referencia de la red privada. El informe anual es citado. El CRO dental atrae el primer contrato internacional (los sitios de validación calibrados en poblaciones subrepresentadas son escasos y valiosos). El modelo se replica en la PRIMERA especialidad médica de los colegas "análogos a patólogos" — misma arquitectura, otro dominio.

**Año 3**: el dataset paraguayo es el estándar local — las empresas que quieran modelos para esta población negocian con la red. Las instituciones públicas (DSBD, INCAN) se suman como clientes/socios, no como patrones. La academia "IA para clínicos" forma a la siguiente camada.

**Año 5**: la red opera la infraestructura de salud-bucal-digital privada del país: tamizaje, telesalud, documentación, datos, investigación contractual — y el modelo "red de profesionales calibrados + IA + datos propios" está probado como la vía paraguaya de innovación médica, demostrable ante cualquiera.

**El final del camino no es una app — es una posición**: ser la capa de inteligencia clínica del sistema de salud privado paraguayo, construida por los que tienen el criterio, no por los que solo tienen el capital.

---

# PARTE IX — Qué se necesita para empezar el lunes

1. **Decisión de la red** (Iván + Gabi + 2-3 colegas): arrancar Fase 1. Reunión de 2 horas.
2. **De Iván**: montar Label Studio (1 día), redactar los 3 protocolos de anotación (3-4 días), seleccionar las 500 imágenes públicas de calibración (1 día).
3. **De Gabi y colegas**: 2 sesiones de calibración de 3 horas (anotar juntos, discutir discrepancias) + 2 sesiones independientes → medir kappa.
4. **De nadie más**. No hay permisos, no hay comités, no hay compras >$100, no hay institucionalidad.

**Si el kappa sale >0.8 en la semana 4, el negocio abre ese mismo mes. Si sale <0.8, se discute, se re-calibra y se vuelve a medir — ese proceso ES el producto.**

Todo lo demás — copiloto, estética, screening, cáncer, dataset, plataforma — está diseñado, presupuestado y secuenciado en este repo, esperando su turno.

---

## Documentos de soporte en este repositorio

| Doc | Qué contiene |
|---|---|
| `research/odontologia-40-ideas.md` | El catálogo completo de 40 ideas rankeadas + epidemiología PY |
| `research/red-privada-odontologia-top5-gabi.md` | El re-rank por red privada + las 8 ideas nuevas |
| `research/sinergias-top5-extensiones.md` | El mapa de sinergias + los 12 proyectos emergentes |
| `research/cancer-oral-smartphone-protocolo.md` | El protocolo completo de #4 (listo para ejecutar) |
| `research/master-ranking.md` y demás | El catálogo médico general (130+ ideas) para las verticales futuras |

## Última actualización

Septiembre 2026.