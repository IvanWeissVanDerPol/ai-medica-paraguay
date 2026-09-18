# EL SISTEMA OMETZ COMPLETO — top 10 ideas explicadas + arquitectura final

> **Qué es este archivo:** la explicación profunda de las 10 primeras ideas (con su evidencia) y la arquitectura completa del sistema Ometz que emerges de combinar el plan maestro + el corpus de investigación de 5 APIs + las 100 ideas. Este es el documento operativo del sistema.
>
> **Última actualización:** 18 septiembre 2026.

---

## PARTE 1 — LAS TOP 10 IDEAS EXPLICADAS

### #1 — El Copiloto Clínico (dictado → nota SOAP)

**Qué es**: Gaby termina la consulta, presiona un botón, y dicta en español natural: "Paciente de 45 años, control semestral, POA en 36 oclusal distal, se realiza resina composite, oclusal ajustada, sin complicaciones. Higiene regular, se refuerza técnica de cepillado. Control en 6 meses." El sistema entrega la nota clínica estructurada lista para firma.

**Qué hay construido**: `transcriptor-agent` — Whisper large-v3 en producción (CLI + API + SPA). Transcribe español con precisión clínica suficiente. Falta solo la capa LLM que transforma transcripción → SOAP.

**Qué falta (2-3 semanas)**: prompt médico-odontológico con el formato que Gaby defina (1 sesión), template de salida, integración con WhatsApp/archivo.

**El número**: 45-90 min/día de documentación → ~10 min. Para una clínica unipersonal, es una hora clínica recuperada cada día — hora que se factura.

**Por qué es #1**: es la base de TODO. Sin nota estructurada no hay dataset (B1), no hay segunda opinión automática (#2), no hay recalls (#8), no hay detector de términos de riesgo. Cada pieza del sistema posterior consume lo que esta produce.

---

### #2 — El Informe de Segunda Opinión Escrita (EL diferenciador)

**Qué es**: el mismo dictado, con el comando "segunda opinión", genera un documento profesional: resumen del caso, evaluación del plan de tratamiento propuesto por otro profesional, recomendación con fundamento, y referencias bibliográficas.

**Por qué es oro puro**: Ometz ya declara la segunda opinión escrita como su servicio distintivo ("Te escucho" + práctica conservadora). Hoy ese informe cuesta 40 min de redacción manual. Con el copiloto: 10 min de revisión. **El sistema no ahorra tiempo — multiplica la capacidad de vender el servicio que diferencia a Ometz de toda otra clínica.**

**El diferencial científico**: cada informe puede citar literatura real vía las 5 APIs ya conectadas (idea #10). Nadie en Paraguay entrega segundas opiniones con referencias verificables.

**Evidencia del corpus**: "Management of fear and anxiety in the dental clinic" [593 citas] — el paciente que busca segunda opinión suele ser el paciente ansioso/inseguro; el servicio distintivo ataca exactamente el segmento más grande de demanda insatisfecha. "Minimal intervention dentistry" [529] — la filosofía conservadora que Gaby practica es la escuela correcta para segundas opiniones (evitar sobre-tratamiento).

---

### #3 — La Ficha Pre-Consulta por WhatsApp

**Qué es**: cuando un paciente agenda, recibe por WhatsApp un formulario conversacional (o audio para menos letrados digitales): motivo, historia médica, medicamentos, alergias, ansiedad (preguntas validadas tipo IDG-6/DAS), expectativas. Llega a la agenda ANTES de la visita; Gaby abre la consulta ya sabiendo quién entra.

**Por qué importa**: (a) la anamnesis completa consume 10-15 min de consulta — se hace antes, asíncrona; (b) el módulo de ansiedad identifica al paciente miedoso ANTES de que entre por la puerta — Gaby puede preparar el abordaje (base: 593 citas); (c) los datos estructurados alimentan el expediente desde el minuto cero.

**Qué hay**: WhatsApp Business API ya integrada en la infra AIW + plantillas existentes en `dentist/08_WHATSAPP`.

**Costo**: casi cero. **Semana**: 2-3.

---

### #4 — El Motor de Captación (disparo de los 1,090 leads)

**Qué es**: `gaby-client-engine` ya tiene 1,090 negocios pre-scored en 15 km de Mburucuyá, con URLs de WhatsApp listas, 6 plantillas por tipo de playbook (colegas, mamás, empresas, estética, gimnasios, hoteles), y tracker CRM.

**Qué falta**: fecha de apertura → cronograma de disparo por lotes semanales (los agentes AIW mandan, trackean respuestas, escalan a Gaby solo los leads calientes).

**Por qué es #4 y no #1**: está 100% construido; su único bloqueo es la fecha de apertura (los 6 datos de Gaby). Es el que convierte todo el sistema en ingresos.

**La sinergia oculta**: cada lead que responde entra directo al flujo #3 (ficha pre-consulta) → el pipeline de captación alimenta el pipeline clínico sin costura.

---

### #5 — El Módulo Anti-Miedo ("Te escucho" sistematizado)

**Qué es**: la sistematización tecnológica del diferenciador de marca de Ometz:
1. **Detección**: la ficha pre-consulta (#3) incluye el instrumento de ansiedad → cada paciente llega con su "nivel de miedo" visible
2. **Preparación**: contenido pre-visita automático por WhatsApp según nivel — qué va a pasar paso a paso, cuánto duele realmente (spoiler: menos de lo que creen), la señal acordada para pausar
3. **En consulta**: protocolo de Gaby apoyado (música, señas, explicación antes de cada paso — ella ya lo hace; el sistema lo estandariza)
4. **Post**: seguimiento empático a 24h

**La evidencia masiva**: "Management of fear and anxiety in the dental clinic" [**593 citas**] — la ansiedad dental es EL determinante de evasión de tratamiento en odontología. La evasión por miedo es la fuente más grande de pacientes perdidos. Y casi NINGUNA clínica lo sistematiza — lo dejan al carisma individual del dentista.

**Por qué es estratégico**: convierte el claim de marca ("Te escucho") en un protocolo medible y diferenciante de verdad. El marketing dice "te escucho"; el sistema DEMUESTRA que se te escucha desde antes de que llegues.

---

### #6 — Fotos Estandarizadas + Espejo Bucal Digital

**Qué es**: protocolo simple de 6-8 fotos en TODA primera consulta (misma app, misma guía en pantalla) + pantalla donde el paciente ve SU boca ampliada mientras Gaby explica lo que ve.

**Dos funciones en una**:
- **Ventas**: el paciente no entiende "POA en 36"; entiende SU foto ampliada con la lesión marcada. La literatura de cámaras intraorales documenta hace 20 años que la visualización sube la aceptación de tratamiento. Es la herramienta de conversión más barata que existe.
- **El foso**: cada foto estandarizada es un dato. En 6-12 meses, cientos de fotos → el dataset paraguayo (B1) empieza solo.

**Qué hay**: el protocolo ya está diseñado (catálogo odontológico #2/#37); la app de captura se monta sobre site-template.

**El detalle que importa**: regla milimetrada en el encuadre → las fotos se vuelven medibles (idea #45).

---

### #7 — Simulación de Sonrisa + Match VITA por Foto

**Qué es**: dos herramientas de la suite estética:
- **Simulación**: foto del paciente → modelo generativo fine-tuneado con los 20 años de casos de Gaby → el paciente VE su sonrisa futura antes de aceptar
- **Match VITA**: foto estandarizada del diente → clasificador → escala de color comunicada al laboratorio sin el dolor del metamerismo

**La evidencia que cambia el juego**: el corpus encontró una **auditoría clínica publicada de un sistema de simulación de sonrisa con IA** [18 citas] — es decir, esto ya se probó clínicamente en otro lado. Y el shade matching ML tiene paper específico contra el metamerismo [6]. No son hipótesis: son tareas resueltas que falta adaptar al fenotipo local.

**Por qué vende**: en estética, el paciente acepta cuando VE. La aceptación de tratamiento ES el ingreso de una clínica nueva. Y los casos históricos de Gaby — que ninguna base de datos pública representa — son el entrenamiento.

**Costo**: <$5k. **Momento**: meses 2-3 (cuando hay flujo de pacientes).

---

### #8 — Post-Consulta Automática (instrucciones + follow-up + recall)

**Qué es**: de la nota del copiloto salen solos:
- **Instrucciones post-procedimiento** personalizadas por WhatsApp (post-extracción, post-blanqueamiento, post-resina — en español, versión guaraní opcional)
- **Follow-up empático a 24-48h**: "¿cómo seguís?" — detecta complicaciones temprano y DEMUESTRA cuidado
- **Recall automático**: la nota dice "control en 6 meses" → el sistema agenda el recordatorio solo, para TODA la base de pacientes, para siempre

**El número que importa**: en una práctica nueva, la retención vale 10x más barato que la captación. El paciente que vuelve es el negocio. Y el recordatorio automático de 6/12 meses es el mecanismo de retención más simple y probado que existe en salud.

**Qué hay**: plantillas ya en `dentist/09_TEMPLATES` + crons AIW. Solo ensamblar.

---

### #9 — Detector de Caries sobre las Fotos de Rutina

**Qué es**: cuando hay 200+ fotos estandarizadas acumuladas (#6), se entrena/fine-tunea el detector sobre fotos de smartphone [base publicada: 108 y 114 citas] y corre como segundo lector en el flujo: foto → modelo marca lesiones → **Gaby confirma o corrige** (ella es el estándar de oro) → la confirmación alimenta el dataset.

**El orden correcto** (internalizado): PRIMERO el flujo de fotos (gratis, útil para ventas), DESPUÉS el modelo (cuando hay con qué entrenarlo). Nunca al revés.

**Lo que produce**: (a) herramienta clínica de documentación; (b) el paper publicable — validación de detección de caries por smartphone en población paraguaya (nadie lo hizo); (c) el dataset etiquetado — el activo.

---

### #10 — El Asistente de Evidencia + Alertas de Literatura (¡ya construido!)

**Qué es**: en consulta, Gaby pregunta "¿tasa de éxito de resina en POA a 5 años?" y recibe respuesta con citas. Y cada semana, un agente le manda por WhatsApp las 3-5 novedades de literatura relevantes a SU práctica.

**Lo especial**: esto NO es una idea a construir — **es el harness que montamos ayer, ya funcionando**. Las 5 APIs conectadas (PubMed, OpenAlex, Europe PMC, CORE, Unpaywall) + el script de queries = el asistente de evidencia existe. Solo falta la interfaz de consulta amigable y el cron de alertas configurado a los temas de Gaby.

**Efecto en la segunda opinión (#2)**: los informes pasan de "opinión experta" a "opinión experta con referencias verificables" — un nivel que ninguna otra práctica del país puede ofrecer.

---

## PARTE 2 — EL SISTEMA OMETZ COMPLETO (arquitectura final)

Las 10 piezas no son una lista — son **capas de un solo sistema**:

```
FUERA DEL CONSULTORIO (captar y preparar)
┌──────────────────────────────────────────────────────────────┐
│  #4 MOTOR DE CAPTACIÓN          #3 FICHA PRE-CONSULTA        │
│  1,090 leads → WhatsApp →       anamnesis + ansiedad +       │
│  agenda (agentes AIW)           expectativas ANTES de llegar │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
DENTRO DEL CONSULTORIO (atender y vender)
┌──────────────────────────────────────────────────────────────┐
│  #5 ANTI-MIEDO         #6 FOTOS + ESPEJO      #7 SIMULACIÓN  │
│  protocolo según       estandarizadas +       de sonrisa +   │
│  nivel detectado       boca ampliada          VITA match     │
│  en la ficha           en pantalla                          │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
DESPUÉS DE LA CONSULTA (documentar y fidelizar)
┌──────────────────────────────────────────────────────────────┐
│  #1 COPILOTO SOAP      #2 SEGUNDA OPINIÓN    #8 POST-CONSULTA│
│  dictado → nota +      → informe con          instrucciones + │
│  firma (10 min)        referencias (#10)      follow-up +     │
│                                             recall eterno    │
└──────────────────────────┬───────────────────────────────────┘
                           ▼
EL POZO SE LLENA SOLO (el foso)
┌──────────────────────────────────────────────────────────────┐
│  Cada nota → dato estructurado                              │
│  Cada foto → imagen estandarizada del fenotipo paraguayo    │
│  Cada confirmación de Gaby (#9) → etiqueta de calidad       │
│  = PRIMER DATASET ODONTOLÓGICO PARAGUAYO                    │
│    → papers → validaciones → la plataforma vendible         │
└──────────────────────────────────────────────────────────────┘
```

### La secuencia de construcción (lo que ya podemos agregar, en orden)

| Semana | Se agrega | Estado |
|---|---|---|
| 1 | Sesión de desbloqueo (6 datos) + formato de notas con Gaby | **bloqueo único real** |
| 2-3 | #1 Copiloto SOAP v1 | transcriptor ya corre; falta capa LLM |
| 3-4 | #3 Ficha pre-consulta + #8 post-consulta/recalls | plantillas existen; ensamblar |
| 4-5 | #4 Disparo de leads por lotes | 100% construido; falta fecha |
| 5-6 | #5 Anti-miedo (instrumento + contenido) + #6 protocolo de fotos | diseño listo |
| 6-8 | #10 Interfaz de evidencia + cron de alertas | harness ya funciona |
| Mes 2-3 | #7 Simulación + VITA | fine-tune con casos de Gaby |
| Mes 4-6 | #9 Detector de caries (cuando hay 200+ fotos) | datasets públicos listos |

**Inversión total de las 10**: <$15k (la mayoría es ensamblar piezas que ya corren).

### Lo que el sistema completo produce, acumulando

- **Mes 1**: clínica abierta con documentación en 10 min, pacientes que llegan fichados, leads disparándose
- **Mes 3**: estética vendiendo con simulación, retención automática, evidencia en cada informe
- **Mes 6**: cientos de fotos + notas → primer modelo propio validado → paper en camino
- **Mes 12**: el dataset paraguayo existe, la segunda opinión con referencias es EL producto distintivo del país, y el sistema empaquetable es visible
- **Mes 16+**: "el sistema Ometz" se vende al primer colega

### El porqué del foso (explícito)

Cada capa refuerza a las demás y ninguna es copiable sola:
- Las apps son públicas → sí, pero el **formato clínico es de Gaby** (su criterio codificado)
- Los modelos son públicos → sí, pero el **entrenamiento local** (fenotipo + práctica paraguaya) no existe en otro lado
- El marketing es copiable → sí, pero **"Te escucho" con sistema que lo demuestra** es experiencia, no eslogan
- Y la acumulación es **temporal**: el dataset crece desde el día 1; quien empiece 2 años después va 2 años atrás

---

## Documentos relacionados

| Doc | Rol |
|---|---|
| `EL-PLAN-MAESTRO.md` | La estrategia general (tracks A/B, secuencia 16 meses) |
| `_gaby100/100-ideas-gaby.md` | El catálogo completo con evidencia |
| `_gaby100/corpus_dental.json` | Los 56 papers |
| `LA-IDEA-COMPLETA-v2.md` | Inventario del org AIW aplicado |

## Última actualización

18 septiembre 2026.