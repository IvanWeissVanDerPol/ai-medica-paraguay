# Changelog del repositorio

Historial de cambios significativos al repo `ai-medica-paraguay/`.

---

## 2026-09-16 — Sesión de consolidación

### Agregado

- **`docs/ai-stack-reference.md`** — Catálogo completo del stack IA open source (sección §1 a §13). Cubre AlphaFold 3, Boltz-2, ESM3, AlphaGenome, MedGemma, pathology FMs, BioNeMo, single-cell FMs, agentic frameworks, infrastructure layer. Tabla maestra de licencias, gaps honestos, top-3 recomendaciones.
- **`docs/research-findings.md`** — Hallazgos consolidados de investigación sobre Paraguay. Datos cuantitativos (165k Chagas, 1.7M en riesgo, 1.150 visitas/día Hospital de Clínicas, etc.), carga de enfermedad, capacidades locales, conectores internacionales, comparaciones regionales.
- **`docs/research-session-log.md`** — Log cronológico de las sesiones de conversación que construyeron el repo. Por qué existe cada decisión.
- **`docs/research-sources.md`** — Bibliografía verificada con URLs, fechas de verificación, y qué claim sustenta cada fuente.
- **`INDEX.md`** — Tabla de navegación rápida con tiempos estimados de lectura.

### Modificado

- **`README.md`** — Reorganizado para referenciar los nuevos docs. Tres recomendaciones principales ahora en el landing.
- **`docs/mapa-actor-instituciones.md`** — Tesabio ampliado con SAB completo + indicadores de credibilidad. PROCIENCIA II cap ahora explícito en USD.
- **`areas/drug-discovery/README.md`** — Reescrito para destacar **Boltz-2 como default** (no AF3) por licencia. Incluida nota sobre por qué AF3 no es comercialmente usable.
- **`areas/clinical-llms/README.md`** — Reescrito con **MedGemma 4B como default** + variante de menor costo con **OpenMedLM prompting + RAG** antes de hacer fine-tune.

### Decisiones de diseño tomadas

- **AI stack** y **research findings** son documentos separados porque el primero es perenne (herramientas), el segundo es específico del contexto paraguayo.
- **Session log** separado de findings porque es histórico (cómo llegamos aquí), no el estado actual.
- **Top-3 recomendaciones** puestas en el landing page directamente — el lector que llega debe saber cuál es la apuesta del repo en 30 segundos.

### Verificaciones de licencias hechas

- AlphaFold 3 v3.0.3: código Apache 2.0, **pesos non-commercial only** (corregido vs respuesta previa que sugería open weights).
- Boltz-2: MIT (modelo + pesos + training code + data). Comercial OK.
- MedGemma: wrapper Apache 2.0, pesos Health AI Dev Foundations License (research + comercial).
- ESM3 1.4B: Cambrian Non-Commercial License. 7B/98B API only.
- AlphaGenome: API no commercial only. Pesos no públicos.

---

## 2026-09-15 — Creación inicial del repo

### Agregado

- **`README.md`** — Landing page inicial.
- **`docs/research-areas.md`** — 8 áreas de investigación con descripción, herramientas, proyectos, vacíos.
- **`docs/mapa-actor-instituciones.md`** — Personas e instituciones.
- **`docs/marco-regulatorio.md`** — Marco regulatorio.
- **`docs/plan-preparacion.md`** — Plan de investigación previa.
- **`areas/{8 carpetas}/README.md`** — Descripción por área.

### Notas

- Versión inicial con 13 archivos, ~1,360 líneas.
- Enfoque en 8 áreas de investigación médica con justificación específica para Paraguay.
- Stack IA identificado pero no exhaustivo.

---

## Próxima entrada esperada

Cuando se complete cualquiera de:

- Lectura de la Política Nacional de Ética en Investigación en Salud (2024).
- Confirmación de contactos (Galeano, Vazquez, Granada).
- Construcción del demo MedGemma 4B en español paraguayo.
- Confirmación del estado del biobanco CEDIC × Galatea Bio.
- Aplicación a una convocatoria externa.