# Área 7 — Telemedicina y atención primaria rural

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§7-agentes-de-ia-para-ciencia) · [research findings](../docs/research-findings.md)

---

## Problema

Paraguay tiene 165.000 infectados con Chagas concentrados en el Chaco, comunidades con acceso limitado a especialistas, y un sistema de telesalud legalmente habilitado (Ley 5482/2015, Resolución 367/2020) pero con adopción baja. La telemedicina con IA podría extender alcance sin nuevos especialistas.

La combinación de español + guaraní +Chaco remoto crea un problema único de NLP multilingüe + salud rural.

## Capacidades locales

- **Ley 5482/2015** — Programa Nacional de Telesalud.
- **Resolución 367/2020** — endosa IA/ML en telesalud.
- **DGVS (Dirección General de Vigilancia de la Salud)** — sistema de semáforo de medicamentos (2019).
- **Hospital de Clínicas** — telesiquiatría documentada.
- **CEDIC** — trabajo de campo en comunidades chaqueñas con pueblos indígenas (Maskoy, Nivaclé, Ayoreo).
- **19 pueblos indígenas** en Paraguay, ~43 % de la población del Chaco.

## Herramientas de código abierto

- [MedGemma 4B](https://huggingface.co/collections/google/medgemma) — asistente conversacional.
- [Whisper](https://github.com/openai/whisper) — base para ASR multilingüe (guaraní a construir).
- RAG sobre protocolos MSPBS (a construir).
- [OpenMRS](https://github.com/openmrs/openmrs) / [Bahmni](https://github.com/Bahmni/bahmni-mart) — EHR open source para telemedicina.
- [CommCare](https://github.com/dimagi) — formularios móviles para trabajo de campo.
- [RapidPro](https://github.com/rapidpro) — plataforma SMS/WhatsApp para flujos de salud.
- [Glific](https://github.com/glific/glific) — chatbot WhatsApp open source para ONG.

## Primer proyecto concreto

> Asistente conversacional multilingüe (español + guaraní) para agentes de salud comunitaria en el Chaco, entrenado sobre protocolos de Chagas y leishmaniasis. Desplegar vía WhatsApp Business API o CommCare. Medir: triage accuracy vs gold-standard de médico remoto.

Entregables:
- App funcional (WhatsApp o CommCare).
- Paper de field-trial.
- Material de capacitación para agentes de salud comunitaria.
- **Aplicable a la convocatoria 2026 FAPESP-CONACYT-CONICET sobre AMR** (paralelismo con salud animal en Chaco).

## Vacíos de información

- ¿Existen datos de audio en guaraní para entrenamiento ASR?
- ¿Qué herramientas usa actualmente el trabajo de campo de CEDIC?
- ¿Cómo se regulan los datos de pacientes en comunidades indígenas bajo la Ley 7593/2025?
- ¿Hay conectividad celular/datos en el Chaco?
- ¿Cuál es la política del MSPBS sobre telesalud rural?

## Próximo paso inmediato

Hablar con CEDIC sobre su trabajo de campo en el Chaco. Específicamente: ¿qué herramientas digitales usan actualmente los agentes de salud comunitarios? ¿Qué problemas concretos resolvería una herramienta de IA conversacional?

## Notas regulatorias

- Datos de salud + posiblemente genéticos (Chagas) = sensibles (Ley 7593/2025).
- **Soberanía de datos indígenas**: Ley 7593/2025 no aborda explícitamente. Aplicar Principios CARE (Collective benefit, Authority to control, Responsibility, Ethics).
- Consentimiento colectivo además del individual cuando aplique (comunidad, no solo individuo).
- Gobernanza de datos con las comunidades afectadas.
- Devolución de resultados a la comunidad, no solo a investigadores.
- Resolución 367/2020 endosa la IA — pero el pathway de aprobación está vacío.

## Riesgos

- **Falsa confianza**: un agente de salud comunitaria con un chatbot puede sentirse autorizado a hacer cosas que no debe. Diseño debe incluir "sabe cuándo no sabe".
- **Desplazamiento cultural**: el modelo debe respetar saberes médicos tradicionales, no reemplazarlos.
- **Brecha digital**: si solo funciona en smartphones modernos, deja afuera a los más vulnerables.
- **Internet**: el Chaco tiene cobertura limitada. Cualquier diseño debe asumir operación offline-first.