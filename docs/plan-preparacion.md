# Plan de preparación — qué falta investigar antes de iniciar trabajo real

Documento vivo. Cada ítem tiene: (a) qué es, (b) por qué importa, (c) cómo investigarlo, (d) estimado de esfuerzo.

---

## Principio rector

Antes de escribir una propuesta, hacer una llamada de alcance, o publicar un demo, necesitamos cerrar los vacíos de información listados aquí. Cada vacío no resuelto es un riesgo de que un proyecto arranque mal.

---

## Fase 1 — Lectura de documentos clave (1 semana)

### 1.1 Política Nacional de Ética en Investigación en Salud (2024)

- **Qué es.** Documento anunciado por PAHO en agosto 2024. Marco de gobernanza ética para investigación en salud.
- **Por qué importa.** Toda propuesta clínica necesita alinearse con esta política.
- **Cómo investigarlo.** Búsqueda en MSPBS, Dirección de Investigación, repositorio de comités de ética. Probablemente disponible en [mspbs.gov.py](https://www.mspbs.gov.py).
- **Esfuerzo.** 2–3 horas de lectura + resumen ejecutivo de 1 página.
- **Output esperado.** 1 página: cláusulas que aplican a cada proyecto del repo + checklist operativo.

### 1.2 Ley 7593/2025 — texto completo

- **Qué es.** Ley de Protección de Datos Personales, en vigencia noviembre 2027.
- **Por qué importa.** Define marco obligatorio para cualquier proyecto con datos paraguayos.
- **Cómo investigarlo.** PDF en [bacn.gov.py](https://www.bacn.gov.py) (17 MB), leer secciones relevantes.
- **Esfuerzo.** 3–4 horas de lectura selectiva.
- **Output esperado.** DPIA template adaptado a cada proyecto + tabla de cláusulas sensibles.

### 1.3 Convocatorias PROCIENCIA II 2026

- **Qué es.** Calls activos del programa principal de financiamiento de CONACYT.
- **Por qué importa.** Determina qué proyectos pueden financiarse y con qué ticket.
- **Cómo investigarlo.** [conacyt.gov.py](https://www.conacyt.gov.py), [feei.gov.py/prociencia-2-convocatorias](https://feei.gov.py/prociencia-2-convocatorias/), publicaciones en el diario oficial.
- **Esfuerzo.** 2 horas.
- **Output esperado.** Tabla: nombre del call, ticket, fecha cierre, requisitos, fit por proyecto.

### 1.4 Convocatoria FAPESP-CONACYT-CONICET AMR 2026

- **Qué es.** Llamado específico para resistencia antimicrobiana en producción animal.
- **Por qué importa.** Único financiamiento internacional con co-financiamiento Paraguayo-Argentino-Brasileño que se ajusta a las prioridades del repo.
- **Cómo investigarlo.** [fapesp.br/en](https://fapesp.br/en), Call 14/2026.
- **Esfuerzo.** 1 hora.
- **Output esperado.** Ficha completa: elegibilidad, requisitos, calendario, fit con proyectos 2 y 5.

---

## Fase 2 — Reconocimiento de personas (1 semana)

### 2.1 Mapeo de investigadores en formación (postdocs y residentes)

- **Qué es.** Lista de 15–30 personas en IICS, CEDIC, INCAN, LCSP que serían usuarios reales de las herramientas.
- **Por qué importa.** Los directores firman; los postdocs y residentes ejecutan. Sin esta capa, los proyectos no tienen adopters.
- **Cómo investigarlo.**
  - Minar publicaciones 2023–2025 de cada institución, autores no correspondientes.
  - LinkedIn: "IICS" + Python / bioinfo / NGS keywords.
  - ORCID: afiliación "Universidad Nacional de Asunción" + "Paraguay" + año > 2022.
- **Esfuerzo.** 1 día completo.
- **Output esperado.** Tabla: nombre, rol, institución, contacto, intereses, expertise computacional.

### 2.2 Estado actual del equipo Tesabio.ai

- **Qué es.** Capacidad real, modelo de colaboración, espacio para socios académicos.
- **Por qué importa.** Si Tesabio no quiere colaboradores académicos, el proyecto 2 se rediseña.
- **Cómo investigarlo.** LinkedIn del equipo, reciente GridX announcement, emails directos.
- **Esfuerzo.** 1 día.
- **Output esperado.** Memo de 1 página: qué ofrecen, qué buscan, cómo encajaría el repo.

### 2.3 Estado del biobanco CEDIC × Galatea Bio

- **Qué es.** Lo que el comunicado 2025 llamaba "recién iniciado" — qué significa en 2026.
- **Por qué importa.** Es el activo de datos genéticos paraguayos más prometedor actualmente; determina si el proyecto 2 puede usar datos locales reales.
- **Cómo investigarlo.** Contacto directo con Galatea (Stanford-based, equipo LatAm) + CEDIC.
- **Esfuerzo.** 2–3 días (considerar tiempo de respuesta).
- **Output esperado.** 1 página: tamaño, tipos de datos, acceso para investigación, IRB.

### 2.4 Champions clínicos en Hospital de Clínicas e INCAN

- **Qué es.** Persona(s) que serían champions internos para pilotos clínicos.
- **Por qué importa.** Sin un champion interno, un piloto externo no sobrevive al primer cambio de turno.
- **Cómo investigarlo.** LinkedIn de médicos, papers conjuntos IICS + Hospital de Clínicas, conversaciones en eventos académicos.
- **Esfuerzo.** 2 días.
- **Output esperado.** 3–5 candidatos priorizados con justificación.

---

## Fase 3 — Reconocimiento de datos e infraestructura (1 semana)

### 3.1 Inventario de datos existentes

- **Qué es.** Cuántos genomas virales, datos AMR, slides de patología, notas clínicas, muestras, existen en Paraguay y dónde.
- **Por qué importa.** Determina qué proyectos son viables hoy vs. necesitan años de recolección.
- **Cómo investigarlo.**
  - NCBI / GISAID para virus paraguayos.
  - PubMed para papers recientes con datasets.
  - Pregunta directa a cada institución.
- **Esfuerzo.** 2 días.
- **Output esperado.** Tabla: dataset, institución, tamaño estimado, accesibilidad.

### 3.2 Infraestructura de cómputo disponible

- **Qué es.** GPUs, servidores, capacidad de almacenamiento, ancho de banda.
- **Por qué importa.** Determina si los modelos grandes se entrenan localmente o en la nube.
- **Cómo investigarlo.**
  - Contacto con HIVE BUZZ (potencial partner de cómputo).
  - IT de cada institución.
  - X8 Cloud (estado del data center).
- **Esfuerzo.** 2–3 días.
- **Output esperado.** 1 tabla: institución, hardware, red, posible partner.

### 3.3 Recursos de NLP en guaraní

- **Qué es.** Qué datos y modelos existen para procesamiento de guaraní (español + guaraní).
- **Por qué importa.** Cualquier proyecto rural/toxoplasmosis/Chaco lo necesita.
- **Cómo investigarlo.** Búsqueda en Hugging Face "guarani", GitHub, papers en Workshop on NLP for Indigenous Languages.
- **Esfuerzo.** 1 día.
- **Output esperado.** 1 página: estado del arte, datasets disponibles, gaps.

---

## Fase 4 — Pre-posicionamiento de assets (2 semanas)

### 4.1 Demo MedGemma 4B en español paraguayo

- **Qué es.** Notebook que toma notas clínicas sintéticas en español paraguayo y produce un resumen estructurado.
- **Por qué importa.** Es el artefacto concreto que abre conversaciones.
- **Cómo.** Finetune mínimo sobre MedGemma 4B con datos sintéticos generados por LLM + revisados por un médico paraguayo.
- **Esfuerzo.** 1–2 semanas (depende de la calidad del dato sintético).
- **Output esperado.** Repo en GitHub con notebook ejecutable + README bilingüe.

### 4.2 Pipeline Nextclade para dengue (sin datos)

- **Qué es.** Pipeline genérico que toma FASTA + referencia y produce un dashboard Nextstrain.
- **Por qué importa.** Demostración concreta a LCSP de cómo sería su análisis estandarizado.
- **Cómo.** Adaptar nf-core/viralrecon a dengue.
- **Esfuerzo.** 3–5 días.
- **Output esperado.** Repo con pipeline ejecutable + SOP en español.

### 4.3 Página landing en español

- **Qué es.** Una página web estática que explique el repositorio y sus 8 áreas en español paraguayo.
- **Por qué importa.** Es el recurso que se envía a cualquier persona interesada antes de una conversación larga.
- **Cómo.** GitHub Pages con Jekyll o Hugo.
- **Esfuerzo.** 1 día.
- **Output esperado.** `index.md` + 1 página por área.

### 4.4 Templates de correo de outreach

- **Qué es.** 5 correos personalizados para los primeros contactos.
- **Por qué importa.** Reduce tiempo de redacción y asegura consistencia.
- **Cómo.** Borradores específicos para: director IICS, bioinformático LCSP, champion Hospital de Clínicas, Tesabio, investigador en formación.
- **Esfuerzo.** 1 día.
- **Output esperado.** 5 plantillas en español + inglés.

---

## Fase 5 — Primer contacto (1 semana, solapado con Fase 4)

### 5.1 Envío de 3 correos a contactos prioritarios

- Dr. Cynthia Vazquez (LCSP).
- Dr. Diego Galeano (FIUNA + Tesabio).
- Dr. Edmundo Granada (IICS).

### 5.2 Conversación exploratoria con Tesabio sobre modelo de partnership académico.

### 5.3 Aplicación a una convocatoria externa

- CZI EOSS, Google.org, Fogarty, o Wellcome — la que mejor encaje con el demo construido.

---

## Fase 6 — Decisión Go / No-Go (después de Fase 5)

Criterios para iniciar un proyecto real:

- Al menos 1 contacto con respuesta positiva y champion identificado.
- Al menos 1 fuente de financiamiento viable identificada.
- Demo concreto disponible para mostrar.
- Compliance check del proyecto contra Ley 7593/2025 + Política Ética 2024 completo.
- Al menos 1 coinvestigador paraguayo confirmado.

Si los criterios no se cumplen: continuar reconocimiento, ajustar enfoque, o descartar el proyecto.

---

## Última actualización

Septiembre 2026.