# Marco regulatorio y ético para proyectos de IA médica en Paraguay

Documento vivo. Cualquier proyecto del repositorio debe cumplir este marco antes de operar sobre datos reales.

---

## 1. Ley 7593/2025 — Protección de Datos Personales

**Aprobada:** 5 de noviembre de 2025. **Publicada:** 27 de noviembre de 2025. **Vigencia:** 24 meses después (noviembre de 2027).

### Cláusulas relevantes para proyectos de este repositorio

- **Datos genéticos = datos sensibles** (Art. 2.5). Aplica a todo dato derivado de muestras biológicas (secuencias, variantes, anotaciones).
- **Datos de salud = datos sensibles** (Art. 2.7). Aplica a notas clínicas, imágenes médicas, registros EHR.
- **Principio de diligencia debida** (Art. 4.2) — privacidad desde el diseño, privacidad por defecto, evaluación de impacto a la protección de datos (DPIA), designación de un oficial de protección de datos.
- **Principio de seguridad** (Art. 4.3) — medidas técnicas y organizativas que eviten alteración, pérdida, tratamiento o acceso no autorizado.
- **Principio de confidencialidad** (Art. 4.4) — obligado incluso después de finalizadas relaciones.
- **Transferencias internacionales** (Art. 6) — solo a países con nivel de protección adecuado, con excepciones para estudios epidemiológicos anonimizados.
- **Tratamiento de datos sensibles permitido** (Art. 20.7, 20.8) — interés público en salud, investigación médica por profesional bajo secreto profesional, formulación de reclamos.

### Implicaciones operativas por proyecto

| Proyecto del repo | Datos sensibles | DPIA | DPO | Transferencia internacional |
|---|---|---|---|---|
| Vigilancia genómica | Sí (genéticos, salud) | Obligatoria | Obligatorio si volumen alto | Solo con anonimización adecuada |
| Descubrimiento de fármacos | Posible (modelos entrenados con datos genómicos) | Si usa datos paraguayos | Si procesa datos paraguayos | Caso por caso |
| LLMs clínicos | Sí (salud) | Obligatoria | Obligatorio | Solo con anonimización |
| Patología digital | Sí (salud, posiblemente genéticos) | Obligatoria | Obligatorio | Solo con anonimización |
| Resistencia antimicrobiana | Posible | Si datos a nivel paciente | No obligatorio | Solo con anonimización |
| Salud mental | Sí (salud, sensibles) | Obligatoria | Obligatorio | Solo con anonimización |
| Telemedicina | Sí (salud, posiblemente genéticos) | Obligatoria | Obligatorio | Solo con anonimización |
| Capacitación investigación | Generalmente no | No | No | N/A |

### Checklist DPIA mínimo (para adaptar por proyecto)

- Descripción del tratamiento: qué datos, qué fines, qué volumen, qué duración.
- Evaluación de necesidad y proporcionalidad.
- Evaluación de riesgos para derechos y libertades de los titulares.
- Medidas de mitigación: anonimización, seudonimización, agregación, cifrado, control de acceso.
- Salvaguardas para transferencias internacionales.
- Mecanismos de notificación de incidentes (72 horas a la nueva Agencia Nacional).
- Procedimientos de ejercicio de derechos por titulares (acceso, rectificación, supresión, oposición, portabilidad).

### Estado de la Autoridad de Aplicación

A crear: la ley establece la **Agencia Nacional de Protección de Datos Personales**, con autonomía funcional. Pendiente de implementación efectiva. Probable ventana de oportunidad para participar en el diseño del marco secundario.

---

## 2. Política Nacional de Ética en Investigación en Salud (agosto 2024)

PAHO/WHO anunció en agosto de 2024 que Paraguay adoptó esta política. **Texto completo pendiente de lectura** (es el primer documento que debemos digerir antes de diseñar proyectos).

Lo que sabemos por el anuncio de PAHO:

- Establece un sistema de gobernanza para la ética en investigación en salud.
- Capaz de coordinar revisión ética multicéntrica.
- Alineado con declaraciones internacionales (Helsinki, CIOMS).

**Acción inmediata:** leer el documento completo (búsqueda pendiente en el repositorio del MSPBS o del Comité de Ética nacional).

---

## 3. Resolución 367/2020 (MSPBS) — Telemedicina con IA

La resolución ministerial **endosa explícitamente** el uso de telemática, telemetría con aplicación de inteligencia artificial (machine learning) y otros métodos tecnológicos aprobados por el MSPBS. Es el marco legal positivo más importante para proyectos de IA clínica.

**Implicaciones operativas.**

- Cualquier proyecto de IA clínica necesita registro de prestadores y personal en la Dirección General de Control de Profesiones, Establecimientos y Tecnología del MSPBS (Art. 5).
- La IA aplica a promoción, prevención, recuperación (diagnóstico y tratamiento), rehabilitación.
- **No hay pathway de aprobación específico para IA** — el vacío regulatorio es a la vez oportunidad y riesgo.

---

## 4. Ley 5482/2015 — Programa Nacional de Telesalud

Define telesalud como "el grupo de actividades, servicios y métodos relacionados con la salud, realizados a distancia con ayuda de TIC". Incluye telemedicina y teleeducación en salud.

Aplicación directa a proyectos de telemedicina con IA en zonas rurales.

---

## 5. Soberanía de datos indígenas

**Vacío identificado.** Paraguay tiene 19 pueblos indígenas, ~43 % de la población del Chaco. La Ley 7593/2025 no aborda explícitamente la gobernanza de datos indígenas. En el derecho internacional emergente, los **Principios CARE** (Collective benefit, Authority to control, Responsibility, Ethics) son el estándar.

**Cualquier proyecto del área 7 (telemedicina/Chaco) debe:**

- Obtener consentimiento colectivo además del individual cuando aplique.
- Establecer gobernanza de datos con las comunidades afectadas.
- Documentar el proceso de negociación de uso secundario.
- Planificar la devolución de resultados a la comunidad, no solo a investigadores.

**Acción inmediata:** buscar protocolos existentes en CEDIC (que trabaja con comunidades Maskoy, Nivaclé, Ayoreo) y otras organizaciones con trabajo de campo indígena.

---

## 6. Otras normas relevantes

- **Ley 1028/97 + Ley 2279/03** — Ley General de Ciencia y Tecnología. Crea CONACYT.
- **Resolución 875 (MSPBS)** — crea la Red Nacional de Vigilancia Genómica.
- **Ley 6534/2020** — Protección de Datos Crediticios Personales (sigue vigente hasta entrada de la 7593/2025).
- **Código Penal, Art. sobre sabotaje de sistemas computacionales** — sanción penal para acceso no autorizado a bases de datos.

---

## 7. Pathway regulatorio para IA clínica (vacío = oportunidad)

Paraguay **no tiene** pathway equivalente a FDA/EMA para aprobar IA clínica. Esto representa:

1. **Riesgo legal** — desplegar un modelo sin marco puede generar responsabilidad.
2. **Oportunidad** — ser parte del diseño del marco junto con MSPBS + MITIC.

**Acción sugerida (Tier 3):** white paper o propuesta técnica al MSPBS / MITIC proponiendo un framework ligero basado en riesgo (similar al de la FDA para Software as a Medical Device). Co-autoría con academia paraguaya + internacional.

---

## 8. Recursos para profundizar

- Texto completo Ley 7593/2025 — [bacn.gov.py](https://www.bacn.gov.py)
- Guía DLA Piper Paraguay — [dlapiperdataprotection.com](https://www.dlapiperdataprotection.com)
- Anuncio PAHO Política Ética 2024 — [paho.org](https://www.paho.org)

---

## Última actualización

Septiembre 2026.