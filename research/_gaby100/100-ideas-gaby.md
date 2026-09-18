# 100 ideas para Gaby — fundamentadas en corpus de investigación real

> **Qué es este archivo:** catálogo de 100 ideas de IA/digital para la práctica de Gaby (Ometz Dental), generado sobre un corpus de **131+ papers** recolectados vía 5 APIs académicas (PubMed/E-utilities, OpenAlex, Europe PMC, CORE, Unpaywall — keys en BWS). Cada idea se ancla al track del plan maestro (A = hace prosperar Ometz HOY; B = construye el foso). Las evidencias clave se citan con referencias del corpus.
>
> **Última actualización:** 18 septiembre 2026.

---

## Evidencias clave del corpus (el fundamento)

| Hallazgo | Referencia | Citas | Implicación |
|---|---|---|---|
| Detección de caries en **fotos de smartphone** con deep learning | "Deep Learning Application in Dental Caries Detection Using Intraoral Photos Taken by Smartphones" | 108 | La app de screening (B3) tiene base publicada directa |
| Segmentación de caries en fotos intraorales | "Caries detection with tooth surface segmentation on intraoral photographic images" | 114 | Detección por superficie — granularidad clínica |
| **Auditoría clínica de sistema de simulación de sonrisa con IA** (estudio prospectivo) | "Clinical audit of an AI empowered smile simulation system" | 18 | A4 no es hipótesis — ya se auditó clínicamente en otro lado |
| Shade matching ML contra metamerismo en luces clínicas | "ML-based tooth shade assessment to prevent metamerism" | 6 | El match VITA por foto tiene paper específico |
| Detección de cáncer oral en **imágenes de smartphone** | "Automatic detection of oral cancer in smartphone-based images using deep learning" | 178 | B4 validado en literatura |
| Lesiones orales potencialmente malignas por deep learning | "Automated Detection and Classification of Oral Lesions..." | 374 | Base sólida del clasificador |
| **Manejo de miedo y ansiedad en clínica dental** (review) | "Management of fear and anxiety in the dental clinic" | 593 | El diferenciador "Te escucho" tiene base científica masiva |
| Odontología de intervención mínima | "Minimal intervention dentistry for managing dental caries – a review" | 529 | La filosofía conservadora de Ometz = escuela con 529 citas |
| Detección de placa en dientes primarios por DL vs clínica | "Deep learning-based dental plaque detection on primary teeth" | 191 | Módulo pediátrico factible |
| LLMs multimodales moldeando el futuro de la odontología | "ChatGPT for shaping the future of dentistry" | 327 | El copiloto (A2) está en la ola actual |
| Pérdida ósea periodontal radiográfica por DL | "Deep Learning for the Radiographic Detection of Periodontal Bone Loss" | 514 | Extensión periodoncia validada |
| Dientes comprometidos: predicción por CNN | "Diagnosis and prediction of periodontally compromised teeth" | 511 | Predictor de pronóstico dental |
| Caries interproximal en bitewings por CNN | "Diagnosis of interproximal caries lesions with deep CNN in bitewing" | 152 | Extensión radiográfica |
| IA en radiología dental maxilofacial (performance) | "The use and performance of AI applications in dental and maxillofacial radiology" | 391 | Panorama general validado |
| Revisiones sistemáticas de IA en odontología | "Developments, application, and performance of AI in dentistry – systematic review" | 666 | El campo está maduro |

*(Corpus completo: `research/_gaby100/corpus_dental.json` — 56 papers dentales filtrados de 131 brutos.)*

---

## Las 100 ideas — por categoría y track

Leyenda: **[A]** = Track A (Ometz prospera HOY) · **[B]** = Track B (foso) · ⭐ = evidencia directa del corpus

### I. COPILOTO CLÍNICO Y DOCUMENTACIÓN (1-12)

1. ⭐**[A] Nota SOAP por dictado** — Whisper (transcriptor-agent ya en prod) + LLM con el formato que Gaby define. Base: "ChatGPT for shaping the future of dentistry" [327].
2. **[A] Informe de segunda opinión escrita automático** — EL diferenciador de Ometz: el dictado genera el documento profesional en 10 min en vez de 40.
3. **[A] Historia clínica odontológica estructurada searchable** — cada nota cae a base de datos; "¿qué pacientes tienen POA en 36?" en un query.
4. **[A] Ficha de ingreso pre-consulta por WhatsApp** — el paciente llena anamnesis ANTES de llegar (formularios conversacionales); Gaby llega a la consulta ya sabiendo.
5. **[A] Resumen automático de historia previa** — paciente nuevo con 20 años de tratamientos en otros lados → el sistema resume lo relevante.
6. **[A] Instrucciones post-procedimiento personalizadas** — generadas de la nota, enviadas por WhatsApp (extracción, blanqueamiento, resina).
7. **[A] Consentimientos informados explicados** — el LLM traduce el consentimiento a lenguaje llano + audio para pacientes ansiosos. Base: manejo de miedo [593].
8. **[B] Detector de términos en el dictado** — el sistema escucha "fumador", "mate muy caliente", "diabético" y agrega flags de riesgo solo.
9. **[B] Codificación automática de diagnósticos (CDT/CIE-10-SA)** — para prepagas y estadística.
10. **[B] Control de calidad de notas** — checklist automático: ¿falta diente? ¿falta material? ¿falta control?
11. **[A] Traducción guaraní de instrucciones** — el diferencial lingüístico paraguayo.
12. **[B] Archivo docente de casos** — las mejores notas anónimas como material para futuros residentes/estudiantes que roten por Ometz.

### II. CAPTACIÓN Y CRECIMIENTO (13-24)

13. **[A] Disparo del motor de 1,090 leads** — ya construido en gaby-client-engine; falta fecha de apertura.
14. **[A] Seguimiento automatizado de leads** — agentes AIW manejan respuestas y agendan.
15. **[A] Contenido educativo semanal automático** — blog/IG con temas que el corpus respalda (ansiedad dental, intervención mínima).
16. **[A] Campaña "segunda opinión escrita"** — el servicio distintivo como gancho de captación.
17. **[A] Google Business Profile optimizado + reseñas** — sistema de pedido de reseña post-visita.
18. **[A] Landing de ansiedad dental** — página específica para el paciente miedoso (593 citas de literatura lo justifican) con el mensaje "Te escucho".
19. **[A] Calculadora de tratamiento en el sitio** — estimado de precio por procedimiento antes de la consulta.
20. **[A] FAQ generada de las preguntas reales** — el sistema aprende qué preguntan por WhatsApp y publica las respuestas.
21. **[B] Casos clínicos (anonimizados) como contenido** — cada caso documentado = contenido de marketing con consentimiento.
22. **[A] Recordatorio de "hace 6 meses no venís"** — reactivación de la base.
23. **[A] Programa de referidos estructurado** — el paciente que refiere recibe beneficio; trackeado por el CRM.
24. **[B] Índice de reputación** — monitoreo automático de menciones/resñas de Ometz.

### III. EXPERIENCIA DEL PACIENTE (25-36)

25. ⭐**[A] Simulación de sonrisa en consulta** — auditado clínicamente en literatura [18]. Foto → resultado. La herramienta de venta #1.
26. ⭐**[A] Match de color VITA por foto** — contra el metamerismo [6]. El dolor de cabeza #1 de estética resuelto con el celular.
27. **[A] Foto antes/después del MISMO paciente en pantalla** — comparación lado a lado en cada control.
28. **[A] Espejo bucal digital** — pantalla donde el paciente ve SU boca ampliada mientras Gaby explica. Aceptación sube.
29. **[A] Plan de tratamiento visual** — timeline gráfico de qué se hace cuándo y cuánto cuesta.
30. **[A] Módulo anti-miedo** — contenido pre-visita para el paciente ansioso (técnicas de la literatura de 593 citas): qué va a pasar, cuánto duele realmente, señales para pausar.
31. **[A] Recordatorios con foto del consultorio/rostro** — humaniza el reminder.
32. **[A] Post-consulta: "¿cómo seguís?"** — follow-up automatizado a 24-48h post-procedimiento.
33. **[A] Encuesta NPS automática** — mide y responde a la experiencia.
34. **[A] Sala de espera digital** — contenido educativo en pantalla mientras esperan.
35. **[B] Perfil de paciente completo** — preferencias (música, hora de cita, temas sensibles) capturados y recordados. "Te escucho" sistematizado.
36. **[A] Confirmación de cita por WhatsApp con 1 botón** — sí/no/reprogramar.

### IV. SCREENING Y DOCUMENTACIÓN CLÍNICA (37-52) — el foso de datos

37. ⭐**[B] Foto estandarizada de TODA primera consulta** — protocolo de 6-8 fotos (el flujo que alimenta todo lo demás).
38. ⭐**[B] Detector de caries sobre las fotos de rutina** — smartphone, validado en literatura [108, 114].
39. **[B] Gaby como gold standard** — cada detección del modelo la confirma la doctora → dataset etiquetado de calidad.
40. ⭐**[B] Screening de lesiones de mucosa en la misma foto** — base [374, 178].
41. **[B] Registro fotográfico longitudinal** — la misma pieza en cada control → change detection futuro.
42. ⭐**[B] Módulo placa bacteriana por foto** — validado en dientes primarios [191]; feedback visual de higiene al paciente.
43. **[B] Score de riesgo de caries individual** — con datos acumulados (CAMBRA+ML).
44. **[B] Detector de bruxismo por fotos seriadas** — desgaste visible en fotos consecutivas.
45. **[B] Documentación de lesiones con regla milimetrada** — el protocolo que hace las fotos medibles.
46. **[B] Archivo radiográfico estructurado** — si Ometz toma radiografías, entran al mismo expediente digital.
47. ⭐**[B] Extensión periodoncia** — pérdida ósea radiográfica por DL [514] cuando haya radiografías.
48. ⭐**[B] Predictor de dientes comprometidos** — pronóstico por CNN [511]: ¿salvar o extraer? Segunda opinión basada en datos.
49. ⭐**[B] Caries interproximal en bitewings** [152] — cuando Ometz tenga radiografía intraoral.
50. **[B] Sonrisa completa 3D desde fotos** — fotogrametría simple (sin escáner).
51. **[B] Mapa dental visual del paciente** — odontograma digital interactivo alimentado por fotos.
52. **[B] Análisis de arco de sonrisa por foto** — proporciones estéticas cuantificadas.

### V. ESTÉTICA INTELIGENTE (53-64)

53. **[A] Biblioteca de casos de Gaby digitalizada** — 20 años de antes/después indexados visualmente.
54. **[A] "Casos similares al tuyo"** — mostrar al paciente nuevo resultados de casos parecidos (de su propia historia).
55. ⭐**[A] Simulación antes/después en el primer contacto WhatsApp** — gancho de conversión antes de la visita.
56. **[A] Simulación de blanqueamiento con slider** — niveles de blanco ajustables en pantalla.
57. **[A] Análisis de proporciones dentales por foto** — golden proportion, Bolton-like desde foto frontal.
58. ⭐**[A] Seguimiento del color en el tiempo** — el mismo diente en cada visita → degradación de resinas detectada temprano.
59. **[A] Presupuesto automático del plan estético** — de la simulación al presupuesto en 1 clic.
60. **[B] Dataset estético paraguayo** — el único con fenotipo local; nadie lo tiene.
61. **[B] Score estético objetivo (PES/WES) por foto** — resultados medibles y publicables.
62. **[A] Galería de sonrisas por tipo** — el paciente navega resultados por "tipo de sonrisa inicial similar a la mía".
63. **[A] Video del caso para el paciente** — mini-video del antes/después para compartir (marketing orgánico con consentimiento).
64. **[B] Modelo de expectativa vs resultado** — ¿la simulación predijo el resultado real? Medir y publicar (nadie lo hizo localmente).

### VI. OPERACIONES DE CLÍNICA (65-78)

65. **[A] Agenda inteligente** — tipos de turno con duraciones correctas; el sistema aprende cuánto tarda Gaby realmente.
66. **[A] Gestión de insumos por vision** — foto del inventario → stock estimado; alerta de reorden.
67. **[A] Dashboard diario** — pacientes de hoy, pendientes, cobros, faltantes.
68. **[A] Recordatorio de vencimientos** — materiales, sterilización, mantenimientos del equipamiento.
69. **[A] Protocolos de bioseguridad checklist digital** — firma diaria, trazabilidad.
70. **[A] Precios dinámicos por datos** — qué procedimientos piden más, qué horarios llenan.
71. **[A] Predicción de no-show** — con historial simple (día/hora/paciente) → overbooking inteligente cuando toque.
72. **[A] Caja y facturación simplificada** — del procedimiento en la nota al ticket.
73. **[B] Analytics de práctica** — procedimientos por mes, ticket promedio, fuentes de pacientes.
74. **[A] Turnos de mantenimiento del consultorio** — todo lo físico también en el sistema.
75. **[A] Onboarding de asistente/auxiliar** — cuando Gaby contrate, los protocolos ya están digitalizados.
76. **[A] Respuestas automáticas fuera de horario** — el bot de WhatsApp responde urgencias comunes y agenda.
77. **[B] Cumplimiento normativo MSPBS** — checklist digital de requisitos de práctica.
78. **[B] Ley 7593 ready** — consentimientos, anonimización y DPIA desde el día 1.

### VII. CONOCIMIENTO Y SEGUNDA OPINIÓN (79-88)

79. **[A] Asistente de evidencia en consulta** — "¿cuál es la tasa de éxito de resina en POA a 5 años?" → respuesta citada (PubMed API ya conectada por este proyecto).
80. **[A] Alertas de literatura** — agentes AIW monitoreanPubMed/OpenAlex semanalmente por temas de la práctica de Gaby.
81. **[A] Segunda opinión documentada con evidencia** — el informe incluye las referencias que respaldan la recomendación.
82. **[B] Guías clínicas propias** — los protocolos de Gaby escritos + versionados.
83. **[B] Biblioteca de decisiones** — archivo de casos difíciles y cómo se resolvieron.
84. **[A] Traducción de informes de otros dentistas** — el paciente llega con radiografías/informes de otros; el sistema los estructura.
85. **[A] Chatbot de preguntas post-consulta** — responde dudas comunes del post-operatorio con criterio de Gaby pre-aprobado.
86. **[B] Segunda opinión remota como servicio** — paciente de otro departamento manda fotos + radiografías → informe escrito (teleconsultoría).
87. **[B] Colaboración con colegas en casos** — espacio compartido de caso para el colega que deriva.
88. **[B] Archivo docente** — de la idea 12: material para estudiantes que roten.

### VIII. EL FOSO CIENTÍFICO Y DE DATOS (89-100)

89. ⭐**[B] Primer dataset odontológico paraguayo** — por gravedad: cada consulta, foto y nota (con consentimiento).
90. ⭐**[B] Validación de caries por smartphone en población paraguaya** — paper publicable [base 108, 114].
91. ⭐**[B] Validación de simulación de sonrisa en población local** — auditoría clínica como la publicada [18], con fenotipo paraguayo.
92. **[B] Estudio del mate: temperatura real y salud oral** — el ángulo científico único mundial.
93. ⭐**[B] Estudio de ansiedad dental paraguaya** — instrumento validado + datos locales (593 citas de base).
94. **[B] Estudio epidemiológico de práctica privada** — "Estado de la boca del paciente privado paraguayo": el informe que nadie puede producir.
95. **[B] Estudio de anotación experta** — el trabajo de calibración (κ) de Gaby como co-autora de validaciones de IA.
96. **[B] Colaboración con grupos de IA dental internacionales** — ofrecer Ometz como sitio de validación clínica en poblaciones subrepresentadas.
97. **[B] Detección de cáncer oral — protocolo completo** (ya escrito en este repo) cuando el circuito de colegas active.
98. **[B] Dataset licenciable** — bajo acuerdo de investigación, el activo a largo plazo.
99. **[B] Publicación de caso: "la clínica unipersonal asistida por IA"** — Ometz mismo como case study (modelo organizacional novedoso).
100. **[B] La plataforma empaquetada** — "el sistema Ometz" vendido a colegas: sitio + captación + copiloto + recalls + screening (el template Odontology desempolvado con caso de éxito real).

---

## Priorización sugerida (las 12 primeras)

| # | Idea | Por qué primera |
|---|---|---|
| 1-2 | Copiloto (notas + segunda opinión) | La base de TODO; 70% construida |
| 4 | Ficha pre-consulta WhatsApp | Reduce fricción desde el día 1 |
| 13 | Disparo de leads | Ya está; falta fecha |
| 37 | Fotos estandarizadas de primera consulta | Inicia el foso sin esfuerzo extra |
| 25-26 | Simulación + VITA | La herramienta de venta |
| 6 | Instrucciones post-consulta | Valor inmediato al paciente |
| 30 | Módulo anti-miedo | El diferenciador "Te escucho" sistematizado |
| 38 | Detector de caries en fotos de rutina | Cuando haya 200+ fotos acumuladas |
| 80 | Alertas de literatura | Los agentes AIW ya lo pueden correr |

**Regla del plan maestro**: nada de esto le roba a Gaby más de 1-2 h/semana. Track A primero; Track B crece montado sobre el flujo.

---

## Apéndice: infraestructura de investigación (reutilizable)

Este proyecto dejó montado y verificado:
- **5 APIs académicas conectadas** (PubMed con key 10 req/s, OpenAlex con key, Europe PMC, CORE, Unpaywall) — keys en BWS, cargadas por `credential-redacted-grep`
- **Harness reutilizable**: `research/_gaby100/harness.py` + `queries.json` → cualquier tema nuevo se investiga en minutos
- **Corpus**: `corpus_dental.json` (56 dental-relevant) + `corpus_pass1.json` (131 brutos)
- Caso de uso inmediato: la **idea 79-80** (asistente de evidencia + alertas) usa exactamente esta infraestructura en producción

## Última actualización

18 septiembre 2026.