# Mapa de sinergias y extensiones — top 5 Gabi + catálogo completo

> **Qué es este archivo:** el análisis sistémico de las 5 ideas para Gabi: qué puede agregar cada una, cómo se alimentan entre sí, qué sinergias cruzan con el catálogo general (médico + odontológico), y qué proyectos nuevos emergen de las combinaciones. La tesis central: **no son 5 proyectos — es un sistema con un motor central, un volante de datos y cuatro salidas.**
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — La arquitectura del sistema (cómo encajan las 5)
- §2 — Análisis idea por idea: extensiones + sinergias específicas
- §3 — Matriz de sinergias (quién alimenta a quién)
- §4 — 12 proyectos nuevos que emergen de las combinaciones
- §5 — Sinergias con el catálogo general (médico)
- §6 — El orden correcto de construcción (secuencia dependencias)

---

## §1 — La arquitectura del sistema

Las 5 ideas no son paralelas — tienen roles funcionales distintos:

```
                    ┌─────────────────────────────┐
                    │  #1 ANOTACIÓN/VALIDACIÓN    │  ← MOTOR CENTRAL
                    │  (equipo calibrado kappa)   │    produce ground truth
                    └──────────┬──────────────────┘
                               │ etiquetas expertas
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
   ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
   │ #3 CARIES   │      │ #4 CÁNCER   │      │ #2 ESTÉTICA │  ← SALIDAS
   │ screening   │      │ ORAL        │      │ suite       │    (ingreso, impacto,
   └──────┬──────┘      └──────┬──────┘      └──────┬──────┘     publicación)
          │ fotos + casos      │ lesiones +         │ casos antes/
          │                     │ histopatología     │ después
          └────────────────────┼────────────────────┘
                               ▼
                    ┌─────────────────────────────┐
                    │ #5 COPILOTO HISTORIA CLÍNICA│  ← VOLANTE DE DATOS
                    │ (dictado → SOAP)            │    genera datos clínicos
                    └──────────┬──────────────────┘    estructurados solos
                               ▼
                    ┌─────────────────────────────┐
                    │ DATASET PARAGUAYO (N7)      │  ← ACTIVO ACUMULADO
                    │ + app "boca paraguaya" (N8) │
                    └─────────────────────────────┘
```

**Los roles:**
- **#1 es el motor**: sin equipo calibrado no hay validación de nada. Pero una vez calibrado, validar #2/#3/#4 es incremental.
- **#5 es el volante**: cada consulta documentada genera datos estructurados sin esfuerzo adicional — el único proyecto que produce datos EN CONTINUO.
- **#2/#3/#4 son las salidas**: ingreso comercial, impacto en salud, y publicación científica respectivamente (con superposición).
- **El dataset (N7) es el activo**: todo converge ahí, y su valor crece con cada proyecto.

---

## §2 — Análisis idea por idea

### #1 — Estudio de anotación y validación experta

**Extensiones adicionales:**

| Extensión | Qué agrega | Esfuerzo |
|---|---|---|
| **Pre-etiquetado con IA (expert-in-the-loop)** | El modelo pre-etiqueta, el experto solo corrige → 3-5x velocidad → precio más competitivo | Medio — requiere un modelo base entrenado con los datasets públicos |
| **Tiering de calidad** | Anotación simple (1 lector) / premium (2 lectores + adjudicación) / gold (consenso de 3) → tres niveles de precio | Bajo — es proceso, no tecnología |
| **Servicio de calibración (kappa-as-a-service)** | Vender la calibración de equipos de investigación propios de otros grupos (universidades extranjeras con residentes que necesitan calibrar) | Bajo |
| **Extensión multi-especialidad** | Los colegas "análogos a patólogos" anotan ortodoncia (cefalometría), periodoncia (pérdida ósea), endodoncia (lesiones periapicales) → oferta completa | Medio — crece con la red |
| **Cursos de anotación para dentistas** | "Cómo etiquetar para IA" — formación paga que además recluta anotadores | Bajo |
| **Extensión no-dental** | La misma infraestructura sirve dermatología, heridas, retinografía si la red médica crece | Futuro |

**Sinergias específicas:**
- → **#3**: el equipo calibrado EN caries es exactamente el equipo validador del screening. Sinergia total: las 500 imágenes de calibración son también el banco de prueba del modelo.
- → **#4**: mismo equipo, tarea de mucosa. La calibración en lesiones orales es un módulo adicional del mismo proceso.
- → **#2**: los casos antes/después de estética requieren curación y etiquetado (¿qué resultado es "bueno"?) — Gabi define el estándar, el equipo lo aplica a escala.
- → **#5**: las notas SOAP generadas necesitan QA → anotadores verifican calidad de salida → circuito de mejora del modelo.
- → **N7**: cada imagen anotada local (con consentimiento) entra al dataset propio. El negocio de anotar para terceros financia la construcción del activo propio.

**Insight clave**: el expert-in-the-loop (pre-etiquetado IA) crea un círculo virtuoso — más anotación → mejor modelo → pre-etiquetas mejores → anotación más rápida → más contratos. El que tiene el mejor ciclo gana el mercado.

---

### #2 — Suite de IA estética

**Extensiones adicionales:**

| Extensión | Qué agrega | Esfuerzo |
|---|---|---|
| **Análisis facial automático** | Proporciones, línea de sonrisa, exposición gingival — tareas publicadas; agrega rigor al diagnóstico estético | Medio |
| **Seguimiento del color en el tiempo** | El mismo diente fotografiado en cada visita → degradación de resinas/revela fracasos temprano → argumento de retratamiento | Bajo |
| **Generador de contenido para redes** | Los casos antes/después (con consentimiento) → contenido de marketing automático para las clínicas de la red | Bajo — muy valioso comercialmente |
| **Visualización de plan con costos** | Simulación + presupuesto automático → tasa de aceptación sube (la evidencia de smile design comercial lo muestra) | Medio |
| **Galería de casos buscable** | "Muéstreme casos similares a este paciente" — 20 años de casos de Gabi indexados visualmente | Medio |
| **Integración CAD/CAM** | Conectar con laboratorios digitales (modelo Tecnodent existe en PY) → archivo digital del caso directo al laboratorio | Futuro |

**Sinergias específicas:**
- ← **#1**: casos etiquetados con criterio experto = dataset de fine-tuning generativo de calidad.
- → **#3**: la misma app de captura estandarizada de fotos intraorales sirve para caries. **Protocolo de captura compartido** — se diseña una vez, sirve para todo.
- → **Marketing del sistema entero**: la estética es lo "vendible" que abre puertas. Un paciente entra por simulación de sonrisa y el mismo flujo capta fotos para tamizaje (#3, #4). **La estética financia el tamizaje** — clínicamente y comercialmente.
- → **#5**: cada caso estético documentado con el copiloto → el dataset de resultados estéticos longitudinales (nadie en el mundo lo tiene bien).
- → **N8**: la suite estética es el módulo "premium" de la app boca paraguaya.

**Insight clave**: la estética es el **caballo de Troya comercial**. Ningún paciente paga por "tamizaje de caries" pero sí por "mirá cómo quedaría tu sonrisa" — y en esa visita se captura todo lo demás.

---

### #3 — Red de tamizaje de caries entre pares

**Extensiones adicionales:**

| Extensión | Qué agrega | Esfuerzo |
|---|---|---|
| **Extensión radiográfica** | El mismo servicio con panorámicas de los consultorios (los datasets públicos ya existen) → detección caries + lesiones periapicales + cálculo | Medio |
| **Tamizaje escolar privado** | Escuelas privadas primero (sin ministerio): colegios pagan el tamizaje anual → ingreso + datos pediátricos | Medio |
| **Predicción individual de riesgo** | Con datos longitudinales (visitas repetidas), modelo CAMBRA+ML: ¿qué pacientes desarrollarán caries nuevo? → prevención selectiva | Alto — requiere 12+ meses de datos |
| **Segunda opinión remota como servicio** | Marketplace interno: cualquier dentista de la red manda el caso y recibe opinión del especialista (Gabi en operatoria) → ella monetiza su criterio | Bajo |
| **Módulo de aceptación de tratamiento** | Mostrar al paciente SU foto ampliada con la lesión marcada → la aceptación de tratamiento sube (documentado en literatura de intraoral cameras) | Bajo — solo UX |

**Sinergias específicas:**
- ← **#1**: equipo validador calibrado.
- ← **#2**: mismos pacientes, mismas fotos, misma app.
- → **#4**: el flujo de tamizaje de caries incluye fotos de mucosa → **detección incidental de lesiones sospechosas** en la misma visita. El circuito de cáncer oral se alimenta del flujo de caries sin costo adicional.
- → **#5**: cada screening documentado con el copiloto → epidemiología de la práctica privada paraguaya (nadie la tiene).
- → **N7**: fotos + examen = dataset de caries paraguayo.
- → **Aseguradoras/prepagas**: con volumen, los datos de tamizaje permiten estratificar riesgo de caries de poblaciones → producto para prepagas (que necesitan controlar costo de tratamientos). Conexión con N5.

**Insight clave**: el screening de caries es el **generador de volumen**. Cada paciente de cada consulta diaria es una oportunidad de captura. El volumen alimenta el dataset, el dataset mejora los modelos, los modelos valen más.

---

### #4 — Circuito privado de cáncer oral

**Extensiones adicionales:**

| Extensión | Qué agrega | Esfuerzo |
|---|---|---|
| **Monitoreo fotográfico de lesiones** | La misma lesión fotografiada en cada visita → detección de CAMBIO (la señal real de malignización) → modelo de series temporales | Medio — único en el mundo |
| **Registro de OPMD con seguimiento** | La historia natural de las lesiones paraguayas (con el ángulo mate) → dataset longitudinal único | Automático con lo anterior |
| **Estudio de temperatura real del mate** | Termómetro + hábitos en la anamnesis → el primer dato real de exposición térmica poblacional (la literatura usa auto-reporte) | Bajo — diferencial científico absoluto |
| **Módulo de cesación tabáquica** | Integración WhatsApp con apoyo de cese (los programas de cesación duplican la eficacia del tamizaje) | Bajo |
| **Derivación estructurada a oncología** | Convenios puntuales con INCAN/cirujanos para los casos confirmados | Relacional |

**Sinergias específicas:**
- ← **#3**: el flujo de pacientes ya viene por caries; el cáncer oral viaja gratis en la misma visita.
- ← **#1**: lectores calibrados en mucosa.
- ← **#2**: la visita estética del paciente >40 es oportunidad perfecta de tamizaje de mucosa.
- → **#5**: anamnesis estructurada de factores de riesgo (tabaco, alcohol, mate con temperatura) dictada al copiloto → el factor de riesgo queda capturado sistemáticamente → habilita el modelo multimodal (foto + riesgo).
- → **Reputacional**: es el proyecto con mayor valor narrativo/público. Un solo caso detectado temprano y publicado legitima todo el sistema.

**Insight clave**: el cáncer oral es el **proyecto de legitimidad**. Comercialmente es el menor, pero es el que da nombre público, publicaciones, y el argumento moral de "por qué esto importa" — que abre todas las otras puertas (incluidas las institucionales, cuando convenga abrirlas).

---

### #5 — Copiloto de historia clínica odontológica

**Extensiones adicionales:**

| Extensión | Qué agrega | Esfuerzo |
|---|---|---|
| **Códigos de tratamiento automáticos** | La nota dictada → también el código del procedimiento (para prepagas/facturación) | Medio |
| **Instrucciones para el paciente automáticas** | Post-extracción, post-bleaching, etc. en español/guaraní, generadas de la nota → impresas/WhatsApp | Bajo |
| **Sistema de recalls inteligentes** | La nota menciona "recontrol en 6 meses" → agenda automática + recordatorio WhatsApp | Bajo |
| **Dashboard de clínica** | Procedimientos por dentista, materiales, tiempos → gestión de la red misma | Medio |
| **Detectores de riesgo en el dictado** | El copiloto escucha "paciente fumador, mate muy caliente" y agrega automáticamente los flags de tamizaje | Bajo — y conecta con #4 |
| **Extensión a colegas médicos** | Los "análogos de patólogos" en otras áreas usan la misma herramienta → la red médica entera se documenta | Futuro |

**Sinergias específicas:**
- ← **Whisper guaraní/español** (catálogo general #11): el mismo fine-tune de ASR sirve para el copiloto. Inversión compartida.
- → **TODOS**: es el volante. Cada proyecto que pasa por una consulta deja datos estructurados.
- → **N7**: el dataset clínico-tabular paraguayo (hallazgos, tratamientos, resultados) que no existe en ningún lado — ni el MSPBS lo tiene estructurado.
- → **Epidemiología privada**: con 6-12 meses de datos de la red → "El estado de la boca paraguaya en la práctica privada" — informe anual vendible/publicable que NADIE más puede producir.
- → **N5 (auditoría prepagas)**: los datos estructurados de tratamiento son la base del servicio de auditoría.

**Insight clave**: el copiloto es el proyecto más humilde y el más estratégico. No diagnose nada, no publica nada — pero **convierte la práctica diaria de la red en datos**, y los datos son el activo que aprecia con el tiempo. Todos los otros proyectos producen datos por esfuerzo; este los produce por gravedad.

---

## §3 — Matriz de sinergias (quién alimenta a quién)

Lectura: fila alimenta columna. ●●● = sinergia crítica (no hacer uno sin el otro), ●● = fuerte, ● = complementaria.

| ↓ alimenta a → | #1 Anotación | #2 Estética | #3 Caries | #4 Cáncer | #5 Copiloto | N7 Dataset |
|---|---|---|---|---|---|---|
| **#1 Anotación** | — | ●●● (etiquetas de calidad) | ●●● (validación) | ●●● (lectores calibrados) | ● (QA de salida) | ●●● (etiquetas del activo) |
| **#2 Estética** | ● (casos para entrenar anotadores) | — | ●● (pacientes+captura) | ●● (pacientes 40+ capturados) | ● (casos documentados) | ●● (casos antes/después) |
| **#3 Caries** | ● (demanda de anotación) | ● (volumen de pacientes) | — | ●●● (flujo compartido, detección incidental) | ●● (screenings documentados) | ●●● (dataset caries PY) |
| **#4 Cáncer** | ● (demanda de calibración mucosa) | ● (visita estética = tamizaje) | ● (viaja en el mismo flujo) | — | ●● (factores de riesgo capturados) | ●● (registro OPMD único) |
| **#5 Copiloto** | ● (texto para QA de anotación) | ●● (documenta cada caso) | ●● (documenta cada screening) | ●● (anamnesis de riesgo) | — | ●●● (volante continuo) |
| **N7 Dataset** | ●●● (es el activo que valoriza) | ● (casos) | ●●● (valor futuro) | ●● (valor futuro) | ●●● (valor futuro) | — |

**Lectura de la matriz:**
1. **#1 es el nodo más denso** — tres sinergias ●●● salen de él. Confirmación de que es el motor.
2. **La pareja #3↔#4 es inseparable** — el mismo flujo de pacientes, la misma app, la misma visita. Construirlos separados es tirar dinero.
3. **#5 toca todo con ●●** — es pegamento universal.
4. **#2 es la más "individual"** pero su sinergia oculta es la más valiosa: **trae pacientes que no vendrían por salud** — es el canal de adquisición del sistema.

---

## §4 — 12 proyectos nuevos que emergen de las combinaciones

Estos NO estaban ni en el catálogo de 40 ni en las 8 ideas nuevas — solo existen como combinaciones:

1. **"Boca paraguaya" — la app plataforma (N8 formalizado)**: una sola app con módulos (estética / caries / mucosa / documentación) sobre infraestructura compartida de captura + sync + telesoporte. El usuario final: el dentista de la red primero, cualquier dentista después. *Emerge de: #2+#3+#4+#5.*

2. **Informe anual "Estado de la boca paraguaya"**: epidemiología de la práctica privada basada en los datos del copiloto + screenings. Publicable, vendible a prepagas/industria, generador de prensa anual. *Emerge de: #5+#3.*

3. **Modelo multimodal de riesgo caries + cáncer (foto + factores)**: cuando el copiloto captura sistemáticamente tabaco/alcohol/mate-temperatura y las fotos existen, el modelo multimodal (Nivel 3 del protocolo de cáncer oral) se entrena solo. *Emerge de: #3+#4+#5.*

4. **Monitoreo fotográfico longitudinal de lesiones (change detection)**: series de fotos de la misma lesión en visitas sucesivas → detección de cambio = la señal real de malignización. Nadie en el mundo tiene esto operativo en práctica privada. *Emerge de: #4 + pacientes recurrentes de #2/#3.*

5. **El primer estudio de temperatura real del mate**: termómetro digital + hábitos en anamnesis → medir la exposición térmica real (toda la literatura usa auto-reporte). Dataset científicamente único, publicable alto. *Emerge de: #4+#5, costo marginal ~$500.*

6. **Marketplace de segunda opinión especializada**: los casos dudosos del screening van al especialista de la red (Gabi en operatoria, colegas en sus áreas) con fee por opinión. Monetiza la experticia directamente. *Emerge de: #3+#4 + la red.*

7. **Tamizaje escolar privado (sin ministerio)**: colegios privados pagan tamizaje anual con la app → ingreso + datos pediátricos + canal de captación de familias como pacientes. *Emerge de: #3 + protocolo de captura.*

8. **Cursos "IA para dentistas" / academia**: la red enseña lo que está construyendo. Formación paga, reclutamiento de anotadores, y posicionamiento como líderes del tema en PY. *Emerge de: todo el sistema.*

9. **Red de validación clínica como CRO dental**: con equipo calibrado + pacientes + datos, la red puede ofrecer servicios de investigación contractual a la industria (testing de materiales, pastas, adhesivos — ensayos in-situ). El mercado CRO dental global paga Miles de USD por sitio de validación. *Emerge de: #1+N7+los consultorios.*

10. **Módulo pediátrico de la app**: fotos de niños (colegios + consultas) → índices ceo-d automáticos + detección + derivación a odontopediatras de la red. *Emerge de: #3+#7.*

11. **Índice deResultados estéticos reportados por paciente (PES/WES automatizado)**: los scores estéticos validados (Parker's PES, WES) calculados semi-automáticamente de las fotos de seguimiento → medida objetiva de resultado para la red y para publicar. *Emerge de: #2+#5.*

12. **Extensión del copiloto a los colegas "análogos a patólogos" en otras áreas**: la misma herramienta de documentación adaptada a sus flujos → la red médica entera se digitaliza con la misma infraestructura → futuras verticales (dermatología, etc.). *Emerge de: #5 + la red.*

---

## §5 — Sinergias con el catálogo general (médico)

El repositorio médico (master ranking de 130+) también se cruza:

| Idea del catálogo general | Sinergia con el sistema odontológico |
|---|---|
| **Whisper guaraní/español fine-tune (#11)** | Inversión compartida: el mismo ASR alimenta el copiloto odontológico Y el chatbot de salud Y la telemedicina. Un solo fine-tune, tres productos. |
| **HeAR tos TB (#1) — arquitectura offline-first** | La app boca paraguaya hereda la misma arquitectura de captura offline + sync diferido diseñada para el Chaco. Diseño compartido, dos dominios. |
| **App leishmaniasis / fotos dermatológicas (#10)** | Misma base técnica (fotos + clasificador + derivación). El equipo y la infraestructura de anotación sirven para las dos verticales. Los "análogos a patólogos" de otras áreas son exactamente los lectores que la vertical médica necesita. |
| **Teledentología WhatsApp (#3 dental) ↔ chatbot salud (#4)** | El mismo canal WhatsApp Business API, el mismo contenido educativo bilingüe, dos audiencias. |
| **Dataset FAIR / Ley 7593 framework (#10 médico)** | El framework de consentimiento + anonimización + DPIA se diseña una vez para el sistema odontológico y sirve para todo lo médico. |
| **Modelo de red privada como sitio de validación** | El patrón "red de profesionales calibrados = infraestructura de validación clínica" es replicable a cualquier especialidad. Si el sistema odontológico prueba el modelo, la extensión médica es un clon. |

**El punto estratégico mayor**: el sistema odontológico es el **piloto del modelo de negocio de red privada**. Si funciona en odontología (donde los datasets públicos existen y el tamizaje no requiere médico), la misma arquitectura organizacional — red calibrada + copiloto + dataset propio + servicios — se replica en las otras especialidades de la red.

---

## §6 — El orden correcto de construcción (dependencias)

```
FASE 1 (mes 1-2): #1 ANOTACIÓN
   Protocolos + Label Studio + calibración kappa + primeras 500 imágenes
   → no depende de nada, todo depende de él
   EN PARALELO: #5 COPILOTO demo (2-4 semanas, independiente)

FASE 2 (mes 2-4): #5 en uso + #3 CARIES versión validación
   (usa el equipo de #1; el copiloto empieza a generar datos)
   
FASE 3 (mes 3-5): #2 ESTÉTICA POC + #4 CÁNCER validación retrospectiva
   (ambos usan #1; #4 usa archivos de casos; #2 usa casos de Gabi)
   → captura compartida: UNA app de captura estandarizada para #2+#3+#4

FASE 4 (mes 5-9): circuitos de campo
   #3 screening en consultorios + #4 viaja en el mismo flujo + #2 en consulta real
   → N7 dataset creciendo solo (copiloto) + activamente (screenings)

FASE 5 (mes 9-12): consolidación
   App "boca paraguaya" (módulos integrados) + informe anual + 
   decisión de verticales nuevas (médicas) con el modelo probado
```

**Regla de oro**: nunca construir dos veces lo mismo. Una app de captura, un equipo de calibración, un canal WhatsApp, un framework de consentimiento, un dataset. Cada proyecto nuevo debería reutilizar 80% de infraestructura y aportar solo su novedad específica.

---

## Última actualización

Septiembre 2026.