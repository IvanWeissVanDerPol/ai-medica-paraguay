# Área 9 — Health Acoustics & TB Cough Screening (NUEVA)

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§1412-hear--health-acoustics-embeddings--sleeper-hit-para-tb) · [research findings](../docs/research-findings.md) · [Google dedicado](../docs/google-deepmind-paraguay.md)

> **Área nueva** — agregada septiembre 2026 tras descubrir que HeAR (Google HAI-DEF) es deployable ahora para screening de TB en Paraguay.

---

## Problema

Paraguay es **hiperendémico para TB** en comunidades rurales chaqueñas (12–83% de seroprevalencia en comunidades indígenas). La atención primaria rural **no tiene acceso a chest X-ray**. Hay datos publicados de que modelos AI basados en **tos** pueden detectar TB con performance significativa (HeAR + linear probe: SOTA en 33 health acoustic tasks).

**Insight clave**: HeAR (Google Health AI Developer Foundations, 512-d embeddings entrenados en 300M+ clips) puede ejecutarse en un smartphone. Combinado con un clasificador lineal entrenado sobre datos locales, es un sistema de screening TB deployable **hoy** en el Chaco.

## Capacidades locales

- **IICS-UNA** — capacidad de biología molecular + secuenciación.
- **Hospital General de Barrio Obrero** — datos activos de TB IGRA-TB vs QFT-Plus (estudio 2025).
- **SENEPA** (Servicio Nacional de Erradicación del Paludismo) — epidemiology field network.
- **Hospital de Clínicas (UNA)** — clínica TB + neumología.
- **CEDIC** — trabajo de campo en comunidades chaqueñas con pueblos indígenas.

## Herramientas de código abierto

| Herramienta | Función | Licencia | Notas |
|---|---|---|---|
| **[HeAR](https://huggingface.co/google/hear)** | Embeddings 512-d para audio clips de 2s | **HAI-DEF** | **⭐ El componente central.** 300M+ clips de entrenamiento. |
| [Whisper](https://github.com/openai/whisper) | ASR multilingüe | MIT | Para transcripts. |
| [CXR Foundation](https://developers.google.com/health-ai-developer-foundations/cxr-foundation) | Embeddings chest X-rays | HAI-DEF | Backup si HeAR no da suficiente performance. |
| [PyTorch](https://pytorch.org) | Framework ML | BSD | Para entrenar clasificador lineal. |
| [scikit-learn](https://scikit-learn.org) | ML clásico | BSD | Para el clasificador lineal. |
| [TensorFlow Lite](https://www.tensorflow.org/lite) | Mobile inference | Apache 2.0 | Para deploy en smartphone. |
| [ONNX Runtime Mobile](https://onnxruntime.ai) | Mobile inference | MIT | Alternativa TFLite. |
| [React Native](https://reactnative.dev) | Mobile app dev | MIT | Para la app móvil. |

### Por qué HeAR es único

- Entrenado sobre 300M+ clips, cubre tos, respiración, carraspeo, risa, habla.
- Linear probing SOTA en 33 tasks: COVID-19, tuberculosis, COPD, asma, neumonía, sarampión, pertussis.
- Robusto a microfonos no entrenados (generaliza cross-device).
- Embedding por clip: **512-d, computado una vez, reusado** para muchas tareas.
- HeAR corre en smartphones consumer-grade (RTX 4060 8GB o mobile GPU).

### Datasets públicos para bootstrap

| Dataset | Contenido | Tamaño |
|---|---|---|
| COUGHVID | Tos COVID/no-COVID | ~25k clips |
| SPRSound | Sonidos pediátricos respiratorios (sibilancias, crepitaciones, roncus, estridor) | ~9k clips |
| ICBHI 2017 Challenge | Sonidos respiratorios | ~5k clips |
| FluSense | Tos/estornudos | ~50k clips |
| FSD50K | General audio incluyendo respiratorio | ~50k clips |

Para Paraguay específicamente, ideal sería construir un dataset local con etiquetas TB confirmada por microbiología o GeneXpert.

## Primer proyecto concreto

### Fase 1 — Validación técnica (1–3 meses)

1. Cargar HeAR desde HuggingFace (`google/hear`).
2. Linear probe sobre datasets públicos (COUGHVID + SPRSound).
3. Construir clasificador binario: TB probable / TB no probable.
4. Evaluar métricas (AUROC, sensitivity, specificity).
5. **Entregable**: paper de viabilidad técnica.

### Fase 2 — Dataset local (3–6 meses)

1. Coordinar con SENEPA + Hospital de Clínicas + Hospital General de Barrio Obrero.
2. IRB para capturar toses con consentimiento informado (Guaraní + Español).
3. Confirmar TB status por microbiología (GeneXpert o cultivo).
4. 200–500 muestras etiquetadas es suficiente para fine-tune de un clasificador lineal sobre HeAR embeddings.
5. **Entregable**: dataset local etiquetado (con governance CARE si hay pacientes chaqueños).

### Fase 3 — Piloto de app (6–9 meses)

1. App móvil React Native + backend Python.
2. Toser 2 segundos → grabar audio → embedding HeAR on-device → clasificador → mostrar probabilidad TB → referral link.
3. Piloto con community health workers en Chaco (10–50 pacientes).
4. **Entregable**: app + paper de field validation.

## Vacíos de información

- ¿Hay acceso a toses etiquetadas con TB status en Paraguay?
- ¿Cuál es la capacidad técnica de SENEPA en field data collection?
- ¿Cuál es la cobertura de smartphones en comunidades chaqueñas?
- ¿Hay conectividad celular/datos en el interior del Chaco?
- ¿Cuál es la postura del MSPBS para AI-assisted triage?
- ¿Hay partnership posible con Nagasaki o JICA para el Chaco?
- ¿Hay dataset local de TB con etiquetas?
- ¿El Hospital General de Barrio Obero o el Hospital de Clínicas tiene GeneXpert activo?

## Próximo paso inmediato

Hablar con **SENEPA** y con la **Cátedra de Neumología del Hospital de Clínicas** sobre acceso a pacientes TB y posibilidad de captura de toses.

## Notas regulatorias

- **HAI-DEF Prohibited Use**: HeAR no puede usarse como dispositivo médico regulado. **Sí puede asistir al clínico** (decision support, no autonomous diagnosis).
- **Ley 7593/2025**: datos de salud = sensibles; consentimiento explícito necesario.
- **CARE Principles**: si se capturan datos en comunidades indígenas chaqueñas, governance colectivo obligatorio.
- **MSPBS Resolución 367/2020**: endosa IA/ML en telesalud — base legal positiva, pero sin pathway regulatorio definido.
- La app móvil **NO debe reemplazar el diagnóstico** — solo asistir al agente de salud comunitaria en su decisión de derivar al hospital.

## Por qué este proyecto importa

- Es el que **mayor impacto social inmediato** tiene: TB es tratable, Paraguay tiene capacidad de tratamiento, lo que falta es detección temprana.
- Es **técnicamente deployable hoy** — HeAR está disponible, el clasificador es trivial, los smartphones existen.
- Es **económicamente accesible** — sin GPU, sin cloud cost significativo.
- Es **éticamente alineado con CARE** — todo el Chaco se beneficia, las comunidades indígenas son las más vulnerables y las más atendidas.
- Es **replicable** — el modelo funciona para COVID, asma, neumonía, COPD una vez que el pipeline TB exista.