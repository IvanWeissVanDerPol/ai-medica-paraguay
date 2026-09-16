# Área 6 — Salud mental y triaje

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§3-llms-clínicos-y-médicos) · [research findings](../docs/research-findings.md)

---

## Problema

Paraguay tiene una brecha masiva en detección temprana de depresión e ideación suicida en niños y adolescentes. Un estudio reciente (2026, IICS SciELO) encontró que solo el **28 %** de pediatras paraguayos tiene conocimiento alto, solo el **29,3 %** usa herramientas estandarizadas de tamizaje, y la respuesta predominante (**85,4 %**) es derivación urgente — reflejo de la falta de capacidad de manejo ambulatorio.

Los residentes de psiquiatría (FCM-UNA, 13/año en clínica + 2/año en niños y adolescentes) ya hacen telesiquiatría pero tienen limitaciones estructurales de hardware y ancho de banda.

## Capacidades locales

- **Cátedra de Psiquiatría (FCM-UNA)** — programa de telesiquiatría documentado durante COVID.
- **Ley 5482/2015** — Programa Nacional de Telesalud.
- **Resolución 367/2020** — endosa IA/ML en telesalud.
- **mHealth piloto Adhera MejoraCare** (PLOS ONE 2022) — viabilidad comprobada para crónicos.
- **Hospital de Clínicas, Psiquiatría** — único servicio público de referencia.

## Herramientas de código abierto

- [MedGemma 4B](https://huggingface.co/collections/google/medgemma) — fine-tunable para tamizaje estructurado.
- [Whisper](https://github.com/openai/whisper) — transcripción de audio para entrevistas clínicas.
- [OpenMedLM](https://github.com/OpenMedLM) / [Meditron](https://huggingface.co/collections/OpenMedLM/meditron) — alternativas LLM médico.
- RAG sobre guías clínicas paraguayas (a construir).
- [BERT multilingual](https://huggingface.co/bert-base-multilingual-cased) — base para modelos en español paraguayo.

## Primer proyecto concreto

> Fine-tune MedGemma 4B sobre un corpus de conversaciones de telesiquiatría del Cátedra de Psiquiatría para detectar señales de depresión / ideación suicida en conversaciones en español paraguayo. Validar contra evaluación psiquiátrica estructurada. Desplegar como asistente del pediatra en atención primaria, **no como reemplazo**.

Entregables:
- Modelo de pesos abiertos.
- Paper de validación con gold-standard psiquiátrico.
- Piloto en 3 centros de atención primaria (urbano + rural).
- Material de capacitación para pediatras.
- Guía de triage con criterios de derivación clara.

## Vacíos de información

- ¿Hay datos de conversaciones psiquiátricas que se puedan usar (con consentimiento)?
- ¿Existe una guía clínica paraguaya validada para depresión pediátrica?
- ¿Cuál es la infraestructura de cómputo del Hospital de Clínicas?
- ¿Hay pediatricians con tiempo protegido para participar en piloto?
- ¿Quién es el champion en la Cátedra de Psiquiatría?

## Próximo paso inmediato

Mapeo de champions en Psiquiatría FCM-UNA. El paper de telesiquiatría COVID (SciELO 2021) lista autores — candidatos naturales para outreach.

## Notas regulatorias

- Datos de salud mental = sensibles (Ley 7593/2025).
- DPIA obligatoria + DPO obligatorio.
- Riesgo específico: **sesgo en detección de suicidio**. Cualquier modelo en este dominio requiere evaluación rigurosa con grupos subrepresentados (lengua indígena, zonas rurales, adolescentes LGBTQ+).
- **Principio de no sustitución**: el modelo asiste al clínico, no lo reemplaza. Diseño centrado en el clínico.
- La Resolución 367/2020 endosa el uso pero no establece validación clínica obligatoria — vacío regulatorio a llenar.

## Riesgos éticos

- Riesgo de falsos negativos en detección de suicidio = daño grave.
- Riesgo de falsos positivos = saturación de derivaciones que ya están saturadas.
- Sesgo de representación: si el modelo se entrena solo en español urbano, falla en rural/guaraní.
- Privacidad: conversaciones psiquiátricas son datos ultrasensibles.