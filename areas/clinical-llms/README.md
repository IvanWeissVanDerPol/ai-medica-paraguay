# Área 3 — Modelos de lenguaje clínico en español paraguayo

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§3-llms-clínicos-y-médicos) · [research findings](../docs/research-findings.md)

---

## Problema

Los LLM médicos abiertos (MedGemma, Meditron, OpenMedLM) están entrenados mayormente en inglés y español neutro. Paraguay tiene un español con modismos propios, jerga clínica local, y un componente importante de guaraní. No existe un modelo fundacional médico en español paraguayo.

Mientras tanto, el Hospital de Clínicas atiende ~1.150 pacientes ambulatorios por día con registros predominantemente en papel. Los residentes (CONAREM, 23 unidades) están obligados a presentar investigación, pero carecen de herramientas.

### El training gap es masivo

- Solo **1 semestre** de bioestadística en pregrado (FCM-UNA).
- **78% de residentes** nunca cursó metodología de investigación posgrado.
- **24% ha publicado** nacionalmente, **14% internacionalmente**.
- Pero **70% cree que la formación en investigación debe ser obligatoria** y **95% que la investigación mejora atención al paciente**.

Hay talento y motivación. Faltan tiempo protegido, mentores y herramientas.

## Capacidades locales

- **Hospital de Clínicas (UNA)** — 45+ especialidades, 1.150 visitas/día, registro en papel.
- **INCAN** — registro electrónico incipiente, programa RACAM.
- **Resolución 367/2020 (MSPBS)** — endosa explícitamente IA/ML en telesalud.
- **HIVE BUZZ AI Cloud** (Asunción) — cluster GPU live desde marzo 2026, en alianza con Columbia University.
- **X8 Cloud MOU con ANDE** — centro de datos $8 mil millones (50 → 500 MW).
- **FCM-UNA / CONAREM** — 23 unidades formadoras, ~500 residentes.

## Herramientas de código abierto — el stack recomendado

| Herramienta | Función | Tamaño | Licencia | Notas |
|---|---|---|---|---|
| **[MedGemma 4B](https://github.com/google-health/medgemma)** | Multimodal médico (Gemma 3 + SigLIP médico) | 4B | Apache wrapper + Health AI Dev Foundations | **Modelo default.** 64.4% MedQA. |
| [MedGemma 27B](https://huggingface.co/collections/google/medgemma) | Texto médico | 27B | Apache wrapper + Health AI Dev Foundations | 87.7% MedQA. ~10% costo de DeepSeek R1. |
| [MedGemma 27B multimodal](https://developers.google.com/health-ai-developer-foundations/medgemma) | Multimodal | 27B | Apache wrapper + Health AI Dev Foundations | Nuevo jul 2025; longitudinal EHR. |
| [MedGemma 1.5 4B](https://developers.google.com/health-ai-developer-foundations/medgemma) | Multimodal actualizado | 4B | Apache wrapper | Mejor lab report + EHR parsing. |
| [MedSigLIP](https://huggingface.co/collections/google/medgemma) | Codificador visual médico | 400M | Apache 2.0 | Standalone, mobile-deployable. |
| [OpenMedLM](https://github.com/OpenMedLM) | Plataforma de prompting (Yi 34B) | 34B base | Apache 2.0 | 81.7% MMLU medical sin fine-tuning. **Prompting > fine-tuning.** |
| [Meditron](https://huggingface.co/collections/OpenMedLM/meditron) | Llama 2 medical fine-tune | 70B | Llama community | Fallback. |
| [BioMistral](https://huggingface.co/BioMistral) | Mistral biomedical | 7B | Apache 2.0 | Compacto. |
| [Whisper](https://github.com/openai/whisper) | ASR multilingüe | — | MIT | Base para guaraní fine-tune. |

### Por qué MedGemma es el default

- **Apache 2.0 wrapper** + Health AI Dev Foundations License (research + comercial OK).
- **Español-capaz** (Gemma 3 base).
- **Fine-tuneable en una sola GPU** (4B en workstation; 27B con H100).
- **Rinde bien sin fine-tuning**: 81% de informes de rayos X del MedGemma 4B juzgados suficientes para manejo similar por radiólogo certificado.
- **Mejora tras fine-tuning**: 50% reducción de errores en retrieval de EHR.

### Por qué OpenMedLM importa

**Prompting puede igualar fine-tuning.** OpenMedLM con Yi 34B logra 72.6% en MedQA, 81.7% en MMLU medical subset — **sin fine-tuning**, solo prompting. Superó Med-PaLM (540B!) en MedQA.

**Implicación para Paraguay:** un LLM general bien prompted + RAG sobre guías clínicas paraguayas puede ser bueno, **antes de hacer un costoso fine-tune médico**.

## Primer proyecto concreto

> Fine-tune MedGemma 4B sobre notas clínicas sintéticas en español paraguayo (generadas con LLM + revisadas por médicos locales) para tareas de triaje y resumen. Desplegar en HIVE BUZZ. Evaluar con gold-standard creado por residentes del Hospital de Clínicas.

Entregables:
- Modelo de pesos abiertos en Hugging Face.
- Paper de evaluación (intrínseca + clínica).
- Piloto de despliegue en una sala del Hospital de Clínicas (con IRB + DPIA).
- Material de transferencia para que IICS pueda reproducir localmente.

## Variante de menor costo (arrancar primero)

> Antes del fine-tune de MedGemma, hacer un piloto con **OpenMedLM prompting + RAG sobre guías MSPBS** sobre notas anonimizadas. Evaluar performance. Si el gap es aceptable, parar aquí. Si no, ir a fine-tune.

## Vacíos de información

- ¿Existe un corpus de texto clínico paraguayo disponible para investigación?
- ¿Quién sería el champion clínico para un piloto en Hospital de Clínicas?
- ¿Cuál es la postura del IRB del Hospital de Clínicas sobre proyectos de IA?
- ¿HIVE BUZZ acepta investigación médica académica o solo comercial?
- ¿Qué GPUs hay realmente disponibles y a qué costo?
- ¿Existe ya un corpus de preguntas médicas paraguayas (similar a MedQA)?
- ¿Hay texto clínico en guaraní disponible?

## Próximo paso inmediato

Construir el **demo mínimo viable**: notebook ejecutable que toma notas clínicas sintéticas (generadas con un LLM con supervisión médica) y produce un resumen estructurado. Subirlo a GitHub como artefacto público.

## Notas regulatorias

- Aplican todas las cláusulas de la Ley 7593/2025 (datos de salud = sensibles).
- DPIA obligatoria antes de cualquier piloto con datos reales.
- DPO obligatorio si el volumen escala.
- Coordinación con la nueva Agencia Nacional de Protección de Datos Personales una vez operativa.
- Hospital de Clínicas requiere aprobación del Comité de Ética institucional.
- Política Nacional de Ética en Investigación en Salud (2024) — verificar cláusulas específicas para IA.