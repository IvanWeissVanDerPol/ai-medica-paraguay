# EL PLAN MAESTRO — AI Whisperers × Ometz Dental: la vertical salud

> **Qué es este archivo:** la síntesis FINAL, re-derivada desde cero con el contexto real completo internalizado: quién es quién, qué existe ya, qué es Ometz, qué papel juega cada pieza del org, y el plan secuenciado correcto. Este documento reemplaza mentalmente a v1 y v2 (que quedan como historial).
>
> **Última actualización:** 17 septiembre 2026.

---

## §1 — El modelo mental correcto (internalizado)

### 1.1 Quién es quién

```
┌────────────────────────────┐        ┌────────────────────────────┐
│ GABY                       │        │ IVÁN / AI WHISPERERS       │
│ Dra. Gabriella González    │        │ Fundador. IA, sistemas y   │
│ Pane — MSPBS 3618          │        │ digital. CERO conocimiento │
│                            │        │ dental.                    │
│ 20+ años clínicos          │        │                            │
│ Operatoria + Estética +    │        │ La fábrica completa:       │
│ Doctorado                  │        │ 100 repos, 116 agentes,    │
│                            │        │ 79 crons, Docker Swarm +   │
│ TODA la odontología:       │◄──────►│ Hermes, Whisper en prod,   │
│ criterio, protocolos,      │"¿esto  │ site builder, OAuth,       │
│ anotación, validación,     │está    │ distribución LinkedIn/IG   │
│ pacientes, colegas,        │bien?"  │                            │
│ estándares clínicos        │        │ TODA la tecnología:        │                            │        │ modelos, apps, pipelines,  │
│                            │        │ automatización, infra      │
└────────────────────────────┘        └────────────────────────────┘
```

**La regla de oro**: Gaby jamás toca un deploy. Iván jamás valida una lesión. Todo modelo, todo informe clínico, todo output que toca un paciente pasa por el gate de Gaby. Esa combinación — fábrica de IA + criterio clínico con autoridad de veto — es el activo que ninguna empresa de IA pura ni ninguna clínica tradicional puede replicar.

### 1.2 Qué existe YA (no construir, usar)

| Activo | Estado | Rol en el plan |
|---|---|---|
| **Ometz Dental** (`dentist`, ometzdental.com) | Sitio live, marca completa (אומץ = coraje, "Te escucho"), estrategia/pricing/compliance/GTM/CRM/marketing/WhatsApp — 400 archivos. **Apertura bloqueada en 6 datos de Gaby** | El beachhead. El primer cliente. La fuente de datos. La prueba de concepto |
| **gaby-client-engine** | 1,090 leads pre-scored (15km de Mburucuyá) + 6 colegas dentales + 6 plantillas WhatsApp + 15 plays + tracker CRM | El motor de captación — armado y listo para disparar cuando haya fecha de apertura |
| **transcriptor-agent** | Whisper large-v3 EN PRODUCCIÓN (CLI + API + SPA, TDD, CI/CD) | El 70% del copiloto clínico y del generador de segundas opiniones |
| **aiw-org** | 116 agentes, 79 crons, Hermes, Docker Swarm, burn $93.61/día medido | La fábrica 24/7 — todo pipeline dental se monta como agente+cron |
| **paragu-ai-platform / site-template / client-kit** | Next.js 16 WhatsApp-first Paraguay-first | La base de la futura app clínica |
| **Odontology** (archived) | Template dental multi-clínica | El producto de reventa cuando haya caso de éxito (Ometz) |
| **Red de colegas de Gaby** | Diagnosticadores multi-especialidad ("análogos a patólogos") | La capa de ground truth y el circuito de confirmación (fase posterior) |

### 1.3 El contexto de vida (por qué ahora)

Gaby está en transición profesional: 12.5 años en Odontología 3 terminaron en despido y caso laboral (cuantificación esperada ₲1,000-1,500M). En vez de volver a ser empleada, **está construyendo lo propio** — Ometz Dental, con toda la estrategia ya montada por AIW. Ese capital (si llega) es acelerador potencial, no plan A. El plan A es: **clínica abierta, llena de pacientes, con IA haciendo el trabajo pesado.**

---

## §2 — La tesis estratégica (una página)

**AIW ya tiene un modelo probado**: construir la presencia digital de pymes paraguayas (24+ sitios cliente: gimnasios, peluquerías, restaurantes, estudios jurídicos). Lo que AIW nunca tuvo es **profundidad de dominio** — en esos negocios, la IA hace marketing y nada más.

**Gaby es la primera socia de dominio**: experta clínica real, con su propio consultorio como cliente ancla y su red de colegas como mercado siguiente. Con ella, AIW no hace el sitio de una dentista — hace **la vertical salud completa**: captación + operaciones + documentación clínica + (después) IA clínica real + datos.

**La secuencia lógica**:

1. **Ometz abre llena** → el motor de captación (ya construido) dispara + la IA operativa (copiloto, recalls) le da a Gaby tiempo que ninguna dentista sola tiene
2. **La IA clínica se valida en Ometz** → segundas opiniones escritas asistidas, simulación de sonrisa, screening documentado
3. **El dataset paraguayo se acumula solo** → cada consulta, cada foto, cada informe
4. **La vertical se empaqueta** → lo que funcionó en Ometz se vende a la red de colegas (el template Odontology desempolvado), con Gaby como estándar clínico
5. **AIW = la capa de inteligencia digital de la salud privada paraguaya** — odontología primero porque la doctora ya es socia; las verticales de los colegas "análogos a patólogos" después

**El final del camino**: un negocio de tecnología con foso de verdad — los modelos son públicos, pero el conjunto "fábrica de IA + doctora socia con criterio + único dataset clínico paraguayo + primer caso de éxito funcionando" no se copia.

---

## §3 — Los dos tracks (el error que v1/v2 cometían)

El plan anterior arrancaba por la visión (anotación, screening, ciencia). El plan correcto arranca por **las dos necesidades reales de Ometz en su fase actual**:

### TRACK A — Que Ometz abra y prospere (semanas 1-16)
*Todo lo que sirve a la clínica AHORA. Criterio: ¿trae pacientes, ahorra tiempo de Gaby, o aumenta aceptación de tratamiento?*

### TRACK B — El activo de largo plazo (meses 2-18)
*Lo que construye el foso: dataset, calibración, modelos validados, ciencia. Se monta SOBRE el flujo de Track A, nunca compitiendo con él por el tiempo de Gaby.*

**La regla**: Track B solo consume tiempo de Gaby en micro-dosis (10-20 min/semana de validación). Si algo del Track B exige más, se reprograma — porque sin Ometz llena no hay dataset, no hay caso de éxito, no hay nada.

---

## §4 — TRACK A en detalle: las 4 armas de Ometz

### A1 — El motor de captación (YA construido, solo ejecutar)

- 1,090 leads con score y URLs de WhatsApp listas + 6 plays + plantillas + tracker
- **Qué falta**: los 6 datos de Gaby que bloquean la apertura → fecha → cronograma de disparo (AIW agents pueden mandar/trackear por lotes semanales)
- **Rol de Gaby**: responder los 6 datos + atender a los que respondan
- **Rol AIW**: todo lo demás

### A2 — El copiloto clínico (sobre transcriptor-agent — la primera pieza nueva)

**Qué es exactamente**: Gaby termina la consulta, presiona un botón del teléfono, y dicta en español lo que pasó. El sistema entrega: (a) la nota clínica estructurada (SOAP) lista para firmar, (b) el informe de segunda opinión escrita — **que es EL diferenciador de Ometz según su propia estrategia** — generado como documento profesional, (c) instrucciones post-consulta para el paciente por WhatsApp, (d) el recall programado si mencionó "recontrol en 6 meses".

**Por qué es LA primera pieza**: una dentista abriendo sola su consultorio tiene el tiempo como enemigo número uno. 45-90 min/día de documentación → 10. Y el servicio diferenciador (segunda opinión escrita) que tomaría 40 min por informe → 10 de revisión. **El copiloto no ahorra tiempo: crea la capacidad de vender el servicio distintivo.**

**Arquitectura**: transcriptor-agent (ya corre) + prompt LLM con el vocabulario y formato que GABY define (una sesión de 1 hora donde ella dicta ejemplos y corrige los outputs) + template del informe Ometz + WhatsApp API.

- **Costo**: casi cero (infra propia + créditos LLM)
- **Timeline**: 2-4 semanas a uso real
- **Gate de Gaby**: 1 hora de definición + 15 min/semana de corrección inicial

### A3 — El motor de retención (sobre aiw-org crons + WhatsApp)

- Confirmaciones de cita, recordatorios 24h, instrucciones post-procedimiento, recalls automáticos a 3/6/12 meses, reactivación de inactivos
- El dentist repo YA tiene los templates (09_TEMPLATES) — solo automatizarlos como agentes
- **Retención = el ingreso barato de una clínica nueva** (un paciente que vuelve vale 10x menos que uno nuevo)
- **Costo**: casi cero. **Timeline**: paralelo a A2.

### A4 — La suite estética (la herramienta de venta)

- **Simulación de sonrisa**: foto del paciente → resultado anticipado. Para una clínica nueva, la aceptación de tratamiento ES el ingreso — y el paciente acepta cuando ve el resultado
- Match de color, visualización de plan con presupuesto
- Los casos históricos de Gaby (20 años) son el entrenamiento
- **Timeline**: meses 2-3 (después de apertura, cuando hay flujo)
- **Costo**: <$5k

---

## §5 — TRACK B en detalle: el foso (montado sobre el flujo de A)

### B1 — El dataset paraguayo (por gravedad, gratis)

Cada consulta de Ometz pasa por el copiloto (A2) → nota estructurada. Cada caso estético pasa por la suite (A4) → fotos antes/después. Cada informe de segunda opinión queda documentado. **En 12 meses de clínica normal, Ometz produce el primer dataset odontológico clínico paraguayo sin esfuerzo adicional.** Consentimiento informado desde el día 1 (framework Ley 7593 ya diseñado en el repo médico).

### B2 — El estudio de anotación y validación (el ingreso externo + la calibración)

- La industria global de IA dental paga $0.5-3/imagen por anotación experta y $5-25k por validación clínica — y no consigue odontólogas especialistas
- **Secuencia correcta (internalizada)**: PRIMERO interno (el equipo se calibra anotando para NUESTROS modelos — los 13,500+ datasets públicos de entrenamiento) → DESPUÉS externo (con kappa documentado, outreach comercial)
- Empieza mes 2-3, sin apuro: su mejor cliente inicial es el propio sistema
- **Micro-dosis de Gaby**: 2-3 sesiones de calibración + validaciones puntuales

### B3 — Screening caries + documentación visual (meses 3-6)

- Foto estandarizada en el flujo de consulta → modelo marca lesiones → Gaby confirma (gold standard) → foto ampliada para el paciente → aceptación sube + caso documentado
- Validación en población paraguaya publicable (nadie lo hizo)

### B4 — Cáncer oral (meses 6-12, el proyecto legado)

- Protocolo completo ya escrito (`cancer-oral-smartphone-protocolo.md`)
- Necesita el circuito de colegas (lectores → cirujano → biopsia) — se activa cuando Ometz es estable
- El ángulo científico único: mate muy caliente + detección temprana (86% vs 40% supervivencia) + primer estudio de temperatura real
- Es el proyecto de reputación pública — se hace último porque exige lo más escaso: coordinación multi-persona

---

## §6 — La secuencia maestra (16 meses)

| Cuándo | Track A (Ometz) | Track B (foso) | Tiempo Gaby/sem |
|---|---|---|---|
| **Semanas 1-2** | Desbloquear 6 datos → fecha apertura. Copiloto: definición de formato con Gaby | Framework de consentimiento listo | 2h total |
| **Semanas 3-6** | **Copiloto en uso** (notas + informes). Recalls automatizados. Apertura | — | 30 min |
| **Semanas 7-10** | **Motor de captación dispara** (lotes semanales de los 1,090) | B2 arranca interno: primeras sesiones de calibración | 1h |
| **Meses 3-4** | Suite estética live (simulación en consulta real) | Calibración κ; fotos de screening empiezan en el flujo | 1h |
| **Meses 5-8** | Optimización: no-shows, dashboard de clínica, precios por datos | **κ>0.8 → outreach de anotación**. Screening: 200 casos → paper | 1h |
| **Meses 9-12** | Ometz en régimen. Casos de éxito documentados | Dataset creciendo. Cáncer oral: circuito de colegas activa. Paper mate-temperatura | 1-2h |
| **Meses 13-16** | **Empaquetado**: template multi-clínica (Odontology) + oferta a los 6 colegas + red | La vertical se vende: "el sistema Ometz" como producto |决策 |

**Marcadores de éxito**: mes 2 = Ometz abre con copiloto y recalls andando · mes 4 = captación disparada + estética en consulta · mes 6 = 200 screenings + κ documentado · mes 12 = paper sometido + ingresos de anotación + dataset propio · mes 16 = primer colega cliente del sistema empaquetado.

---

## §7 — Los números (honestos)

**Inversión nueva total (16 meses)**: ~$30-40k
- Copiloto + recalls: ~cero (infra propia, créditos LLM)
- Suite estética: <$5k
- Screening + validación: <$8k
- Cáncer oral: <$15k (cuando toque)
- Infra compartida + contingencia: $10k

**Las tres fuentes de ingreso en orden de llegada**:
1. **Ometz mismo** (mes 1+): la clínica de Gaby funcionando es el motor financiero de todo — el AI le da tiempo y aceptación de tratamiento, la clínica genera el flujo
2. **Anotación/validación externa** (mes 6+): $20-80k/año potencial con el equipo calibrado
3. **La vertical empaquetada** (mes 16+): el sistema Ometz vendido a colegas (sitio + captación + copiloto + recalls) — el modelo AIW de 24 clientes, ahora con profundidad clínica y ticket mayor

**Y lo que NO se cuenta como ingreso pero vale**: el dataset paraguayo (el único), las publicaciones, el caso O3 (acelerador si llega, nunca supuesto del plan).

---

## §8 — Riesgos (reales, con el contexto internalizado)

| Riesgo | Realidad | Manejo |
|---|---|---|
| **Ometz no abre** (los 6 datos siguen bloqueados) | ES el riesgo #1 — todo depende de la apertura | Este es trabajo de relación, no técnico: la sesión de desbloqueo es la próxima acción concreta. Mientras tanto, copiloto y recalls se terminan igual (útiles para cualquier fecha) |
| **Tiempo de Gaby** (apertura + caso O3 + clínica) | Escasísimo | Regla de las micro-dosis: nada le exige >2h/semana. Track B se reprograma, Track A se automatiza |
| **Gaby satura de tecnología** | Probable si se mal ordena | Orden correcto: primero lo que le AHORRA tiempo (copiloto/recalls), después lo que le VENDE (estética), al final lo que la hace CIENTÍFICA (screening/papers) |
| Caso O3 consume energía | Timeline se superpone | El plan soporta pausas: cada pieza es independiente |
| Un modelo dice algo clínicamente tonto | Inaceptable | Gate de Gaby en TODO. Los modelos asisten; la doctora firma |
| Burn AIW ($94/día) sigue sin contrapartida | Real | Track A genera la contrapartida (Ometz como cliente ancla real de la vertical) |

---

## §9 — La visión (internalizada, sin humo)

**Año 1**: Ometz abre llena y funciona como ninguna clínica del país — documentación en minutos, segundas opiniones escritas como servicio distintivo, recalls automáticos, simulación de sonrisa, y cada consulta generando el dataset. Gaby practica odontología 100% de su tiempo clínico; la fábrica hace el resto.

**Año 2**: el sistema Ometz se empaqueta y se vende a los primeros colegas. La anotación experta genera ingreso externo. Primer paper. El cáncer oral arranca su circuito.

**Año 3**: AIW tiene la vertical salud: sitio + captación + operaciones + copiloto + screening + datos, con Gaby como directora clínica del estándar y la red de colegas como mercado. Las verticales médicas de los "análogos a patólogos" usan el mismo molde.

**El final**: no es una app ni un modelo — es una posición. **La capa de inteligencia digital de la salud privada paraguaya, construida por la fábrica que ya existe y la doctora que ya es socia.** El foso: criterio clínico con autoridad + datos únicos + caso de éxito funcionando + fábrica propia. Copiable por partes; el conjunto, no.

---

## §10 — La próxima acción concreta (esta semana)

**La sesión de desbloqueo de Ometz**: 1 llamada con Gaby para (a) resolver los 6 datos que bloquean la apertura (están listados en `dentist/docs/MASTER-TODO-RESTANTE.md`), (b) fijar fecha objetivo de apertura, (c) agendar la sesión de 1 hora donde define el formato de sus notas e informes para el copiloto.

Todo lo demás (copiloto, recalls, captación) ya tiene el camino técnico despejado y arranca en paralelo. **El cuello de botella no es tecnología — es esa llamada.**

---

## Documentos que alimentan este plan

| Doc | Aporta |
|---|---|
| `dentist` (org AIW) | La estrategia completa de Ometz + los 6 datos bloqueantes |
| `gaby-client-engine` (org AIW) | Los 1,090 leads y las plantillas listas |
| `transcriptor-agent` (org AIW) | La base del copiloto |
| `research/odontologia-40-ideas.md` | El catálogo completo + epidemiología PY |
| `research/cancer-oral-smartphone-protocolo.md` | El protocolo del proyecto legado (B4) |
| `research/red-privada-odontologia-top5-gabi.md` + `sinergias-top5-extensiones.md` | El análisis de red y sinergias |
| `research/LA-IDEA-COMPLETA.md` (v1) y `-v2.md` | Versiones anteriores (historial del razonamiento) |

## Última actualización

17 septiembre 2026.