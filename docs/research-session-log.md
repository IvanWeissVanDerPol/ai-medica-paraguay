# Log cronológico de sesiones de investigación

Documento histórico. Por qué existe: este repo se construyó a través de múltiples sesiones de conversación. Cada sesión tenía contexto limitado. Este log preserva qué se investigó, qué se decidió, y qué cambió entre sesiones.

---

## Sesión 1 — Análisis inicial del landscape médico AI

**Fecha:** septiembre 2026
**Pregunta del usuario:** "analiza el latest AI medical news tech repos y opensource things like alpha fold and alpha genome etc"

**Actividad:**
- Búsqueda web sobre AlphaFold 3, AlphaGenome, AI medical imaging open source, BiomedCLIP/MedSAM/CheXagent/Path Foundation Model 2025
- Compilación de ~30+ herramientas open source categorizadas
- Output: respuesta en chat con tabla estructurada

**Hallazgos clave:**
- AF3 relicensed a Apache 2.0 (jun 2025) — cambio mayor.
- AlphaGenome released 25 jun 2025; paper Nature enero 2026.
- Boltz-2 con FEP-class affinity prediction (9 jun 2025).
- Path FMs liderados por CONCH, Virchow2, UNI.

**Output:** respuesta en chat (no persistida en repo).

---

## Sesión 2 — Research landscape de Paraguay

**Fecha:** septiembre 2026
**Pregunta del usuario:** "analyze what labs in paraguay are doing what labs in paraguay exists..."

**Actividad:**
- Búsqueda sobre IICS, CEDIC, LCSP, INCAN, CEMIT/BioProsNat, FIUNA, Hospital de Clínicas.
- Identificación de Tesabio.ai como actor clave.
- Mapeo de financiamiento (PROCIENCIA, JICA, IDB, FAPESP).
- Conexión con Nagasaki, Galatea Bio, GABRIEL network.
- Output: respuesta larga con mapa de instituciones + contactos.

**Hallazgos clave:**
- Tesabio.ai es serio: pre-seed GridX, SAB Harvard/Broad/Cornell, Beheshti CSO.
- IICS-UNA es el hub central, 10 departamentos, capacidades wet-lab reales.
- LCSP tiene Illumina + MinION, opera Red Nacional de Vigilancia Genómica.
- Diego Galeano (FIUNA) es el bridge figure.

---

## Sesión 3 — Proyectos concretos + ways to help

**Fecha:** septiembre 2026
**Pregunta del usuario:** "what projects and ways to help we could do to work with labs and improve them"

**Actividad:**
- Diseño de 3 tiers de proyectos (Tier 1 fast wins, Tier 2 strategic, Tier 3 long-horizon).
- Identificación de proyectos flagship:
  1. Pipeline Nextclade en LCSP
  2. MedGemma fine-tune en Hospital de Clínicas
  3. Boltz-2 + BioProsNat + CEDIC para Chagas
  4. TB resistance ML
  5. INCAN pathology digital pilot
- Output: respuesta con 10 proyectos priorizados.

---

## Sesión 4 — Deep research sobre lo que falta

**Fecha:** septiembre 2026
**Pregunta del usuario:** "research more in deapth and all key findings so far"

**Actividad:**
- Drill-down en Chagas (165k infectados, Chaco hiperendémico, DTUs TcII/III/V/VI).
- Drill-down en dengue (hiperendémico, olas cada 2–5 años, origen Brasil).
- Confirmación de PROCIENCIA II ticket sizes (Gs. 90M ≈ $12k para iniciación).
- Identificación de la convocatoria FAPESP-CONACYT-CONICET 2026 AMR.
- Hallazgo de HIVE BUZZ GPU cluster + X8 Cloud MOU.
- Output: brief estructurado con comparaciones regionales.

**Hallazgos clave nuevos:**
- La convocatoria 2026 FAPESP-CONACYT-CONICET AMR es la mejor oportunidad de co-financiamiento internacional específica.
- PROCIENCIA II caps at $12k USD — más pequeño de lo que esperaba.
- Paraguay fue pionero regional en eliminación de transmisión vectorial de Chagas (2018).

---

## Sesión 5 — Restricción a medical only + recon

**Fecha:** septiembre 2026
**Pregunta del usuario:** "we want in the medical area not geo data"

**Actividad:**
- Reconocimiento focalizado en medical-only.
- Búsqueda de nuevos hallazgos:
  - **Política Nacional de Ética en Investigación en Salud (agosto 2024)** — anuncio PAHO. **No sabía de este documento**.
  - CONAREM (23 unidades formadoras, ~500 residentes).
  - Hospital de Clínicas: 1.150 visitas/día, 45+ especialidades.
  - 78% de residentes nunca tomó metodología de investigación posgrado.
- Output: brief revisado con hallazgos nuevos.

**Hallazgos clave nuevos:**
- Paraguay adoptó Política Nacional de Ética en Investigación en Salud (agosto 2024) — no estaba en el radar inicial.
- El training gap de residentes es masivo: 78% sin metodología posgrado, 1 semestre de bioestadística.
- Eso es **oportunidad**: herramientas de IA que resuelvan el dolor de tesis obligatoria en residentes serán adoptadas.

---

## Sesión 6 — Creación del repo + landing page

**Fecha:** septiembre 2026
**Pregunta del usuario:** "lets make a repo and explain what the main resaerch areas would be?"

**Actividad:**
- Creación de `/opt/data/profiles/ivan/projects/ai-medica-paraguay/`.
- Estructura: README, docs/, areas/{8 áreas}/.
- README bilingüe (español dominante).
- docs/research-areas.md — descripción de las 8 áreas con problemas, herramientas, proyectos concretos, vacíos.
- docs/mapa-actor-instituciones.md — personas e instituciones.
- docs/marco-regulatorio.md — Ley 7593/2025, Resolución 367/2020, etc.
- docs/plan-preparacion.md — fases 1–6 de investigación previa.
- areas/{each}/README.md — descripción detallada por área.

**Output:** 13 archivos, ~1,360 líneas.

---

## Sesión 7 — Deep dive en open source AI stack

**Fecha:** septiembre 2026
**Pregunta del usuario:** "can you research more and explain waht AI opnsourc things we would use? alpha fold etc?"

**Actividad:**
- Drill-down específico en AI tools:
  - **AF3 license clarified**: Apache 2.0 código, pero pesos non-commercial only (a pesar de mi respuesta previa que sugería open weights).
  - **Boltz-2** confirmado MIT con pesos + training code + datos, 1000× faster than FEP.
  - **ESM3** confirmado 1.4B open, 7B/98B API-only, acquired by CZ Biohub nov 2025.
  - **LigandMPNN** Nature Methods marzo 2025.
  - **AlphaGenome** Nature enero 2026, API non-commercial.
  - **MedGemma** confirmado: 4B/27B, Apache wrapper, Health AI Dev Foundations License.
  - **NVIDIA BioNeMo Agent Toolkit** — CC BY 4.0, agent-agnostic, free for prototyping.
  - **scFoundry** — Nextflow-based unified framework para 15+ modelos scFMs.
  - **RadFM** — Nature Communications 2025, primer FM 2D+3D radiology.
- Output: respuesta organizada por capa (§1-§12).

**Hallazgos clave nuevos:**
- AF3 weights siguen siendo non-commercial a pesar del código Apache 2.0 — corrección importante vs respuesta previa.
- NVIDIA BioNeMo Agent Toolkit es el entry point para agentic bio AI.
- Pathology FMs landscape en 2025: CONCH top general, Virchow2 cerca, UNI2-h en low-data.

---

## Sesión 8 — Consolidación (esta sesión)

**Fecha:** septiembre 2026
**Pregunta del usuario:** "document and save all the data and resarch to the repo"

**Actividad:**
- Consolidación de toda la research de las sesiones previas en docs durables.
- Creación de `docs/ai-stack-reference.md` (§1–§13, ~33k caracteres).
- Creación de `docs/research-findings.md` (§1–§10, ~20k caracteres).
- Creación de este log de sesiones.
- Creación de `docs/research-sources.md` — bibliografía consolidada.
- Patches a `areas/drug-discovery/README.md` y `areas/clinical-llms/README.md` con Boltz-2 + MedGemma detalles.
- Output: repo ahora durable.

---

## Decisiones de diseño que evolucionaron entre sesiones

### Sesión 1–3
- Pensé el proyecto en abstracto, sin Paraguay específico.
- Enfoque en "qué herramientas existen".

### Sesión 4–5
- Pivoté a Paraguay específico.
- Hallazgos cuantitativos: 165k Chagas, 1.7M en riesgo, ticket PROCIENCIA $12k.
- Reconocimiento de que la ventana regulatoria está abierta.

### Sesión 6
- Repo materializado.
- 8 áreas definidas con problemas, herramientas, proyectos, vacíos.

### Sesión 7
- AI stack profunda.
- Correcciones de licencias (AF3 weights ≠ open).
- NVIDIA BioNeMo como agente de orquestación.

### Sesión 8
- **Consolidación**.
- Docs durables, separando "AI stack" (perenne) de "research findings" (específico de Paraguay) de "session log" (histórico).

---

## Lecciones metodológicas

1. **El primer "mapa" siempre está incompleto.** Sesiones 4–5 revelaron documentos nuevos (Política Ética 2024). No se puede saltar la fase de recon.
2. **Las licencias importan más que la cobertura mediática.** AF3 se promociona como "open", pero los pesos siguen siendo non-commercial. Hay que leer los términos, no los titulares.
3. **El ecosistema local tiene capacidades reales.** IICS, CEDIC, LCSP, BioProsNat, Tesabio — todos existen y son serios. El gap es orquestación y herramientas.
4. **El cliente regulatorio puede ser el cliente académico.** Cuando el framework no existe, ayudar a construirlo es el proyecto más estratégico.
5. **Documentar todo el proceso (no solo el output) preserva el valor.** Este log existe por esa razón.

---

## Próxima sesión (planeada)

Cuando el usuario regrese, las prioridades abiertas son:

1. **Confirmar/concretar contactos** — cold outreach a Galeano, Vazquez, Granada (template en `plan-preparacion.md`).
2. **Construir el MedGemma 4B Paraguayan-Spanish demo** — el primer artifact tangible.
3. **Confirmar estado del biobanco CEDIC × Galatea Bio** — vía contacto directo.
4. **Aplicar a una convocatoria externa** — CZI EOSS, Google.org, o Fogarty.

---

## Última actualización

Septiembre 2026.