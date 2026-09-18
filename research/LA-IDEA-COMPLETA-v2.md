# LA IDEA COMPLETA v2 — corregida con el org AI Whisperers real

> **Qué es este archivo:** la corrección del capstone tras dos aclaraciones críticas: (1) **Iván NO es odontólogo** — es el fundador de AI Whisperers, pura capacidad de IA/sistemas/digital, cero conocimiento dental; (2) el org de GitHub de AIW contiene infraestructura real que cambia el plan: ya existe un sistema de transcripción Whisper en producción, una enciclopedia estratégica dental de 400 archivos, un motor de captación de pacientes con 1,090 leads pre-scored, y una plataforma de agentes con 116 agentes y 79 cron jobs.
>
> **Última actualización:** septiembre 2026.

---

## §0 — Correcciones al documento anterior

| Antes (erróneo) | Ahora (correcto) |
|---|---|
| "Iván: odontólogo 20+ años" | **Iván: fundador de AI Whisperers — IA/sistemas/digital. Cero conocimiento dental.** |
| "El puente clínica-tecnología en una sola persona" | El puente son DOS personas: Gabi (toda la clínica) + Iván (toda la tecnología). Y ya funcionan así — Ometz Dental lo prueba. |
| Red genérica de "colegas" | La red existe Y YA ESTÁ OPERANDO: Ometz Dental en lanzamiento, leads ya scoreados, sitio live, WhatsApp ya en marcha. |
| Emppezar de cero con Label Studio | **Ya hay**: transcriptor Whisper large-v3 en producción (API+CLI+SPA), 1,090 leads con WhatsApp URLs, plantillas WhatsApp, infra Docker Swarm + Hermes + 116 agentes. |

**La corrección no debilita el plan — lo fortalece.** El plan anterior subestimaba lo que ya existe.

---

## §1 — Lo que el org de GitHub revela (el inventario real)

### 1.1 Infraestructura técnica YA construida

| Repos | Qué es | Relevancia para el plan dental |
|---|---|---|
| **`transcriptor-agent`** | Sistema de transcripción en producción: Whisper large-v3, CLI + API + SPA React, TDD, CI/CD | **ES el copiloto #5 ya medio construido.** Whisper large-v3 transcribe español excelentemente. Falta: capa LLM → nota SOAP odontológica + vocabulario dental en el prompt. Es un fine-tune de prompt, no un proyecto nuevo. |
| **`aiw-org`** | Plataforma org: 116 agentes, 79 cron jobs, Docker Swarm, Hermes, KPI stacks, $93.61/día de burn LLM medido | **La fábrica.** Cualquier pipeline dental (procesar audios, agendar recalls, generar informes) se monta como agente + cron de esta infraestructura. Ya corre 24/7. |
| **`paragu-ai-platform` + `site-template` + `client-kit`** | Site builder Next.js 16, WhatsApp-first, Paraguay-first | **La app "boca paraguaya" tiene su base.** Next.js + WhatsApp integrado ya existe como template |
| **`code-agent` + `code-agent-ui`** | Agente de código self-hosted (Quarkus/Java) + management UI | Capacidad de desarrollo autónomo interno |
| **`linkedin-mcp` + `linkedin-content-system` + workers OAuth** | Distribución LinkedIn/Instagram automatizada | Canal de marketing ya construido |
| **`saved-transcriptions`** | Storage de transcripciones | Parte del pipeline del copiloto |
| **`ContractAnalizer`** | Contract intelligence framework | Reutilizable para análisis de contratos de prepagas (idea N5) |

### 1.2 El negocio dental YA en marcha

| Repos | Qué es |
|---|---|
| **`dentist`** | **OMETZ DENTAL** — la práctica de Gabi. 400 archivos: estrategia, pricing, modelo financiero, investigación de mercado/competidores/compliance, análisis de audios de Gaby, GTM corporativo/institucional/referrals, CRM, rutinas clínicas, legal/bioseguridad, marketing completo, branding, WhatsApp Business, templates de recalls/referrals. **Sitio live: ometzdental.com** |
| **`gaby-client-engine`** | Motor de captación: **1,090 leads pre-scored** en 15km de Mburucuyá + 6 colegas dentales, 6 plantillas WhatsApp por play, 15 plays priorizados, tracker CRM-lite, CI validator |
| **`Odontology`** (archived) | Template de sitio dental multi-clínica — para reventa |

### 1.3 Lo que esto significa

**El plan anterior presupuestaba construir desde cero cosas que ya existen:**

| Componente del plan | Estado real |
|---|---|
| #5 Copiloto historia clínica (Whisper + LLM) | **70% construido** — transcriptor-agent está en producción; falta la capa SOAP |
| App de captura / plataforma | **50% construido** — site-template Next.js WhatsApp-first existe |
| Canal WhatsApp educativo (#3 catálogo) | **Ya operando** — plantillas de outreach + WhatsApp Business en dentist/ |
| Marketing/leads | **Ya hecho** — 1,090 leads scoreados con URLs de WhatsApp listas |
| Infraestructura de agentes/automatización | **100% hecha** — aiw-org corre 24/7 con 79 crons |

**Lo único genuinamente nuevo por construir**: los modelos de visión (caries/estética/cáncer) y la calibración clínica del equipo. Todo lo demás es ensamblaje de piezas existentes.

---

## §2 — El plan corregido (v2)

### 2.1 Los roles correctos

```
┌──────────────────────┐         ┌──────────────────────┐
│      GABY            │         │      IVÁN            │
│ La doctora           │         │ El de AI             │
│                      │         │                      │
│ TODA la clínica:     │◄───────►│ TODA la tecnología:  │
│ · criterio clínico   │ "¿qué   │ · modelos IA         │
│ · anotación experta  │ significa│ · sistemas           │
│ · validación         │ esto?"  │ · automatización     │
│ · pacientes (Ometz)  │         │ · infraestructura    │
│ · los colegas        │         │ · el org entero      │
└──────────────────────┘         └──────────────────────┘
```

Iván jamás anota una lesión ni valida un modelo. Gabi jamás toca un deploy. **La interfaz entre los dos ya existe y funciona** — se llama Ometz Dental.

### 2.2 La nueva secuencia (mucho más corta)

**FASE 0 — YA HECHA (no construir):** transcriptor, infra, leads, WhatsApp, sitio, branding.

**FASE 1 (semanas 1-4): El copiloto de historia clínica sobre transcriptor-agent**
- Fork de transcriptor-agent + prompt LLM médico-odontológico (vocabulario dental en español que GABY define: términos correctos, estructura SOAP de su práctica, sus abreviaturas)
- Deploy interno: Gaby dicta consultas reales → nota SOAP → ella corrige → el sistema aprende
- **Costo: casi cero** (la infra corre; el LLM son créditos)
- **Entrega ya en semana 4**: herramienta en uso real en Ometz

**FASE 2 (semanas 3-8): El estudio de anotación (motor #1, igual que antes)**
- Label Studio + protocolos que GABY escribe/valida (yo los redacto, ella los aprueba con su criterio)
- Calibración: Gaby + colegas anotan 500 imágenes públicas → kappa
- Outreach con kappa en mano
- **Este es el único proyecto que NO tiene piezas previas — y es el que genera ingreso externo**

**FASE 3 (semanas 6-12): Modelos de visión sobre site-template**
- App de captura estandarizada (site-template Next.js, WhatsApp-first ya existe)
- Modelo caries (datasets públicos) validado por Gaby en Ometz
- Modelo estética: los casos de Gaby + fine-tune
- **Nota crítica**: yo entreno los modelos; GABY define qué es correcto. El error clínico no se tolera — ella es el gate de calidad de todo.

**FASE 4 (meses 3-6): Cáncer oral + circuito completo**
- Protocolo ya escrito; circuito con los colegas de Gaby
- El mate-temperature study como paper único mundial

**FASE 5 (meses 6-12): Plataforma + dataset + escalar**

### 2.3 Qué cambia en el top 5 para Gaby

| Proyecto | Cambio |
|---|---|
| **#1 Anotación** | Igual — pero los protocolos los valida Gaby, no los escribe sola. Es SU criterio el producto. |
| **#2 Estética** | Igual — y ahora con Ometz live, la suite estética es feature del consultorio YA en marcha |
| **#3 Caries** | Igual — validación en Ometz directamente |
| **#4 Cáncer oral** | Igual |
| **#5 Copiloto** | **De 5° a 1° en velocidad** — está 70% construido. La primera entrega real del sistema. |

### 2.4 La pregunta de seguridad que importa

¿Quién revisa que el modelo de caries no diga estupideces? **Gaby.** Siempre. Yo construyo, ella aprueba. Ningún modelo toca un paciente sin su validación explícita — ese es el deal, y es también el activo: la combinación IA + criterio clínico validante es exactamente lo que ninguna empresa de IA pura puede replicar.

---

## §3 — La idea completa, en una página

**La tesis**: AI Whisperers ya construyó la fábrica digital (transcripción, agentes, automatización, captación). Gaby ya tiene la clínica (Ometz Dental, live, con leads). La unión de las dos — **IA operativa sobre práctica dental real, con la doctora como gate clínico** — crea:

1. **Ingreso inmediato** (anotación experta para industria global, mes 2+)
2. **Herramientas propias** que hacen a Ometz el consultorio más avanzado del país (copiloto semana 4, estética mes 2, screening mes 3)
3. **El primer dataset odontológico paraguayo** (por gravedad, vía copiloto + screening)
4. **Publicaciones** (caries PY, cáncer oral + mate, temperatura real del mate)
5. **La plataforma** ("boca paraguaya") replicable a los colegas de Gaby → el modelo AIW de salud digital vertical

**El final del camino**: AI Whisperers como la capa de inteligencia clínica-digital del sector salud privado paraguayo — odontología primero (porque la fábrica ya existe y la doctora ya es socia), otras verticales después (los colegas "análogos a patólogos" de otras áreas).

---

## Última actualización

Septiembre 2026.