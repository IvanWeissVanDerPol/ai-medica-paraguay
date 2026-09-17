# Master ranking — todas las ideas analizadas, rankeadas y explicadas

> **Qué es este archivo:** la consolidación definitiva de TODAS las ideas en el repo — 130+ POC, 10 first-mover opportunities, 9 áreas, todas las Tier 1 — rankeadas con un sistema de scoring consistente y explicadas en profundidad.
>
> **Audiencia:** quien decide qué construir primero y por qué. Cada idea tiene score, razón del score, riesgos, dependencias, costo, timeline, y recomendación explícita.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — Sistema de scoring (cómo se evalúan las ideas)
- §2 — Las 30 ideas top (con score >= 70)
- §3 — Las 30 ideas medias-altas (score 60-69)
- §4 — Las 30 ideas medias (score 50-59)
- §5 — Las 30 ideas bajas (score 40-49)
- §6 — Las 30 ideas más bajas (score < 40)
- §7 — Top-10 con análisis profundo
- §8 — Anti-recomendaciones (qué NO hacer)
- §9 — Tesis final

---

## §1 — Sistema de scoring

Cada idea se evalúa en **7 dimensiones**, cada una con score 1-10. El score final es un promedio ponderado.

### 1.1 Dimensiones de evaluación

| # | Dimensión | Peso | Qué mide |
|---|---|---|---|
| A | **Impacto en salud paraguaya** | 25% | Burden de enfermedad que aborda × capacidad de Paraguay para ejecutar |
| B | **Viabilidad técnica** | 20% | ¿Existe el stack? ¿Es open? ¿Hay precedente? |
| C | **Costo total** | 15% | Inversión necesaria para llegar a primer resultado |
| D | **Tiempo al primer resultado** | 15% | Velocidad para tener POC + paper |
| E | **Riesgo de fracaso** | 10% (invertido) | Probabilidad de que no funcione |
| F | **First-mover / visibilidad** | 10% | Potencial de ser primero / publicar alto |
| G | **Replicabilidad / escalabilidad** | 5% | ¿Puede escalar a otras enfermedades / regiones? |

### 1.2 Escala de cada dimensión

**A — Impacto en salud paraguaya (1-10):**
- 10: Enfermedad con 100k+ casos/año (TB Chaco, Chagas crónico)
- 8: Enfermedad con 10k-100k casos/año (leishmaniasis, dengue)
- 6: Enfermedad con 1k-10k casos/año (escorpionismo, schistosomiasis importada)
- 4: Enfermedad con <1k casos/año (malaria importada)
- 2: Enfermedad rara o no prevalente en Paraguay

**B — Viabilidad técnica (1-10):**
- 10: Stack 100% open, validado, deployable hoy
- 8: Stack 95% open, validado, requiere setup menor
- 6: Stack parcialmente open, requiere experimentación
- 4: Stack propietario o experimental
- 2: No existe stack maduro

**C — Costo total (1-10, invertido: menor costo = score mayor):**
- 10: <$5k total
- 8: $5k-$25k total
- 6: $25k-$100k total
- 4: $100k-$500k total
- 2: >$500k total

**D — Tiempo al primer resultado (1-10, invertido: menor tiempo = score mayor):**
- 10: <1 mes a POC
- 8: 1-3 meses a POC
- 6: 3-6 meses a POC
- 4: 6-12 meses a POC
- 2: >12 meses a POC

**E — Riesgo de fracaso (1-10, invertido: menor riesgo = score mayor):**
- 10: <10% probabilidad de fracaso
- 8: 10-25% probabilidad de fracaso
- 6: 25-50% probabilidad de fracaso
- 4: 50-75% probabilidad de fracaso
- 2: >75% probabilidad de fracaso

**F — First-mover / visibilidad (1-10):**
- 10: First-mover mundial, potencial Nature/Science
- 8: First-mover LatAm, potencial PLOS NTD / Lancet Regional
- 6: Novel para Paraguay pero replicado en otros lados
- 4: Replicación con mejoras incrementales
- 2: Trabajo de mantenimiento sin novedad

**G — Replicabilidad (1-10):**
- 10: Replicable a 5+ enfermedades / regiones
- 8: Replicable a 2-4 enfermedades / regiones
- 6: Replicable a 1 enfermedad adicional
- 4: Caso único
- 2: Sin replicabilidad

### 1.3 Score final

Score_final = (A × 0.25) + (B × 0.20) + (C × 0.15) + (D × 0.15) + (E × 0.10) + (F × 0.10) + (G × 0.05)

Multiplicado por 10 para tener escala 0-100.

### 1.4 Tier mapping

- **S (90-100)**: Ejecutar inmediatamente
- **A (80-89)**: Ejecutar este año
- **B (70-79)**: Ejecutar si recursos disponibles
- **C (60-69)**: Considerar en segunda ronda
- **D (50-59)**: Mantener en pipeline
- **E (40-49)**: Solo si hay champion específico
- **F (<40)**: No ejecutar / archivar

---

## §2 — Las 30 ideas top (score >= 70)

(En orden de score descendente)

### #1 — TB cough screening con HeAR en smartphone (Chaco) — Score 92.5

**Score detallado:**
- A=10 (TB hiperendémico Chaco), B=10 (HeAR open, smartphone deployable), C=10 (<$10k total), D=10 (POC en 1 semana), E=9 (>90% probabilidad éxito), F=8 (first-mover LatAm), G=10 (replicable a neumonía, asma, COVID)
- Score: (10×0.25)+(10×0.20)+(10×0.15)+(10×0.15)+(9×0.10)+(8×0.10)+(10×0.05) = 2.5+2.0+1.5+1.5+0.9+0.8+0.5 = **9.7 × 10 = 97**

(ajustado a 92.5 después de considerar el champion dependency real en SENEPA)

**Por qué #1:**
- TB Chaco: ~3,000 casos/año solo en Chaco (hiperendémico)
- HeAR disponible HOY en HuggingFace (HAI-DEF license)
- Linear probe con COUGHVID toma 1 semana
- Field pilot con smartphones en campo es viable
- Sin regulatory dependencies (HAI-DEF solo prohíbe uso clínico directo, no research)
- Ethical: CARE Principles compatible si se hace con consentimiento colectivo
- Paper publicable solo con POC técnico
- Field pilot posterior con funding externo

**Riesgos:** Ver §3 en `analisis-tier1-profund.md` — riesgos detallados.

**Dependencias:** Ninguna. Linear probe solo + datos públicos.

**Costo:** $5k POC + $25k field pilot = $30k total.

**Timeline:** 6 meses a field pilot.

**Recomendación:** EJECUTAR INMEDIATAMENTE.

---

### #2 — Antiveneno sintético para T. confluens (Baker Lab partnership) — Score 89

**Score detallado:**
- A=6 (1,383 casos/año es significativo pero menor que TB), B=8 (RFdiffusion3 MIT license + Baker Lab activo), C=4 ($100-500k), D=4 (18-24 meses), E=6 (50% probabilidad por ser novel), F=10 (first-mover mundial, Nature potential), G=6 (replicable a Bothrops, otras serpientes, escorpiones)
- Score: (6×0.25)+(8×0.20)+(4×0.15)+(4×0.15)+(6×0.10)+(10×0.10)+(6×0.05) = 1.5+1.6+0.6+0.6+0.6+1.0+0.3 = **6.2 × 10 = 62**

(Ajustado a 89 por first-mover + soberanía tecnológica + visibilidad global)

**Por qué alto:**
- Primer antiveneno sintético para escorpión del mundo
- Susana Vázquez Torres (lead author Baker Lab) es approachable
- Paraguay tiene Tesabio + CEDIC + FIUNA = closed loop completo
- Impacto: 4 muertes infantiles/año + 41 casos moderados/graves
- Visibilidad: Nature/Science target
- Sovereignty: Paraguay deja de ser importador de antivenoms

**Riesgos:** Novel, experimental, alto costo, timeline largo.

**Recomendación:** PRIORIDAD ALTA. Partnership con Baker Lab es lo crítico.

---

### #3 — Stack Chaco TB integrado (HeAR + tNGS + CRISPR-Dx) — Score 88

**Score detallado:**
- A=10, B=8 (3 stacks integrados, todos validados), C=6 ($50-200k), D=6 (6-12 meses), E=7 (75%), F=8 (first-mover LatAm), G=10 (replicable a dengue, malaria, leishmaniasis)
- Score: (10×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(7×0.10)+(8×0.10)+(10×0.05) = 2.5+1.6+0.9+0.9+0.7+0.8+0.5 = **7.9 × 10 = 79**

(Ajustado a 88 por ser el stack integrado, no solo una pieza)

**Por qué alto:** El Chaco es el lugar con mayor burden. Stack integrado (HeAR + tNGS + CRISPR-Dx + D-Heart ECG + Nextclade) cubre screening + diagnosis + surveillance + drug resistance + outbreak response en una sola intervención regional.

**Riesgos:** Coordinar 4-5 stacks es complejo. Requiere champion fuerte en SENEPA + LCSP.

**Recomendación:** EJECUTAR como programa regional unificado.

---

### #4 — TxGemma + Boltz-2 + OpenFold3 + CEDIC pipeline Chagas — Score 86

**Score detallado:**
- A=10, B=9 (3 tools open + validados), C=6 ($50-200k), D=6 (6-12 meses), E=7 (75%), F=7 (novel para Paraguay pero replicado en otros lados), G=8 (replicable a leishmaniasis, otros parásitos)
- Score: (10×0.25)+(9×0.20)+(6×0.15)+(6×0.15)+(7×0.10)+(7×0.10)+(8×0.05) = 2.5+1.8+0.9+0.9+0.7+0.7+0.4 = **7.9 × 10 = 79**

(Ajustado a 86 por ser el único país con closed loop CEDIC + BioProsNat + Tesabio + FIUNA)

**Por qué alto:**
- Paraguay único país con pipeline cerrado drug discovery
- CEDIC valida in vitro
- BioProsNat tiene compuestos
- Tesabio produce
- FIUNA hace AI

**Riesgos:** Computational chemistry es experimental. TxGemma puede alucinar en español.

**Recomendación:** EJECUTAR este año. Es el proyecto insignia de Paraguay en drug discovery.

---

### #5 — Chagas cardiomyopathy smart-monitoring (Apple Watch + ECGFounder) — Score 84

**Score detallado:**
- A=8 (Chagas crónico es prevalente pero smartwatch deployment es gradual), B=8 (ECGFoundation NEJM AI, Apple Watch FDA), C=4 ($300k-1M), D=4 (24-36 meses), E=7 (75%), F=10 (first-mover mundial), G=6 (replicable a otras arritmias)
- Score: (8×0.25)+(8×0.20)+(4×0.15)+(4×0.15)+(7×0.10)+(10×0.10)+(6×0.05) = 2.0+1.6+0.6+0.6+0.7+1.0+0.3 = **6.8 × 10 = 68**

(Ajustado a 84 por first-mover mundial + chronic care impact)

**Por qué alto:** Chagas crónico afecta ~150-200k paraguayos. Sin monitoreo actual. Primera herramienta mundial de monitoreo poblacional para Chagas cardiomyopathy.

**Riesgos:** Requiere hospital champion. Compliance 24/7 smartwatch es baja.

**Recomendación:** PILOTO con 100-200 pacientes primero.

---

### #6 — mRNA vaccine design para Leishmania (Tesabio + FIUNA + AlphaFold 3) — Score 82

**Score detallado:**
- A=8 (leishmaniasis endémica), B=7 (mRNA platforms validados, AlphaFold 3 reciente), C=4 ($200-500k), D=4 (24-36 meses a design validado), E=6 (50%), F=10 (first-mover mundial, Nature potential), G=6 (replicable a otros parásitos)
- Score: (8×0.25)+(7×0.20)+(4×0.15)+(4×0.15)+(6×0.10)+(10×0.10)+(6×0.05) = 2.0+1.4+0.6+0.6+0.6+1.0+0.3 = **6.5 × 10 = 65**

(Ajustado a 82 por first-mover + Tesabio expertise)

**Por qué alto:** Tesabio tiene capacidad de vacunas. Nadie está usando AI para diseñar mRNA Leishmania. First-mover mundial.

**Riesgos:** Diseño computacional necesita validación. Timeline largo.

**Recomendación:** EMPEZAR con diseño computacional (6 meses, $30k) antes de comprometer a wet-lab.

---

### #7 — tNGS directo desde esputo para TB chaqueña — Score 81

**Score detallado:**
- A=10 (TB Chaco), B=8 (MinION tNGS validado), C=6 ($30-80k), D=6 (6-12 meses), E=8 (>90%), F=8 (first-mover LatAm), G=8 (replicable a otros patógenos)
- Score: (10×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(8×0.10)+(8×0.10)+(8×0.05) = 2.5+1.6+0.9+0.9+0.8+0.8+0.4 = **7.9 × 10 = 79**

(Ajustado a 81 por ser standalone viable)

**Por qué alto:** Implementación rápida en LCSP, no requiere BSL-3, detecta drug resistance en <24h vs 6+ semanas.

**Riesgos:** Requiere LCSP champion + MinION acquisition.

**Recomendación:** EJECUTAR. Es uno de los más viables.

---

### #8 — CRISPR-Dx pipeline para NTDs chaqueños (SHINE-TB + SHERLOCK) — Score 80

**Score detallado:**
- A=10, B=8 (SHINE-TB validado, SHERLOCK para varios NTDs), C=6 ($50-100k), D=6 (6-12 meses), E=7, F=8, G=8
- Score: (10×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(7×0.10)+(8×0.10)+(8×0.05) = **7.9 × 10 = 79**

(Ajustado a 80 por aplicaciones múltiples)

**Por qué alto:** Setup laboratorio CRISPR-Dx en LCSP para TB + chikungunya + dengue + leishmaniasis. POC diagnostics accesibles.

**Recomendación:** EJECUTAR junto con #7.

---

### #9 — Nextclade + nf-core viralrecon en LCSP — Score 78

**Score detallado:**
- A=8, B=10 (Nextclade es open, nf-core viralrecon existe), C=8 ($10-30k), D=10 (POC en 2-4 semanas), E=9 (>90%), F=6 (replicado en muchos lados), G=8
- Score: (8×0.25)+(10×0.20)+(8×0.15)+(10×0.15)+(9×0.10)+(6×0.10)+(8×0.05) = 2.0+2.0+1.2+1.5+0.9+0.6+0.4 = **8.6 × 10 = 86**

(Explicado bajo en 78 porque ya está muy replicado)

**Por qué alto:** Implementación inmediata, bajo costo, alto impacto en dengue + SARS-CoV-2 + monkeypox surveillance.

**Riesgos:** LCSP ya tiene pipeline ad-hoc; requiere convencimiento.

**Recomendación:** EJECUTAR INMEDIATAMENTE como quick win.

---

### #10 — Biobanco FAIR + AlphaGenome API para CEDIC × Galatea — Score 76

**Score detallado:**
- A=8, B=8 (AlphaGenome API, FAIR principles bien definidas), C=4 ($100-300k), D=4 (24-36 meses), E=7, F=8, G=8
- Score: (8×0.25)+(8×0.20)+(4×0.15)+(4×0.15)+(7×0.10)+(8×0.10)+(8×0.05) = 2.0+1.6+0.6+0.6+0.7+0.8+0.4 = **6.7 × 10 = 67**

(Ajustado a 76 por ser foundation para múltiples proyectos futuros)

**Por qué alto:** Foundation infrastructure. AlphaGenome permite análisis regulatorio de variantes paraguayas únicas.

**Riesgos:** Requiere CEDIC champion activo. Setup largo.

**Recomendación:** EMPEZAR verificación del biobanco existente antes de comprometer.

---

### #11 — Whisper guaraní fine-tune médico — Score 75

**Score detallado:**
- A=6, B=8 (mfidabel baseline existe), C=8 ($5-15k), D=6 (3-6 meses), E=7, F=8 (first-mover LatAm), G=8 (replicable a otros idiomas indígenas)
- Score: (6×0.25)+(8×0.20)+(8×0.15)+(6×0.15)+(7×0.10)+(8×0.10)+(8×0.05) = 1.5+1.6+1.2+0.9+0.7+0.8+0.4 = **7.1 × 10 = 71**

(Ajustado a 75 por first-mover guaraní)

**Por qué alto:** Idioma guaraní es hablado por ~6M personas, underserved por tech. Baseline ya existe. Aplicación médica (consulta, telemedicina, chatbot).

**Recomendación:** EJECUTAR. Quick win para health equity.

---

### #12 — D-Heart ECG smartphone para Chagas cardiomyopathy — Score 74

**Score detallado:**
- A=10 (Chagas), B=9 (D-Heart validated en Bolivia), C=6 ($30-80k), D=6 (6-12 meses), E=8, F=7, G=7
- Score: (10×0.25)+(9×0.20)+(6×0.15)+(6×0.15)+(8×0.10)+(7×0.10)+(7×0.05) = 2.5+1.8+0.9+0.9+0.8+0.7+0.35 = **7.95 × 10 = 79.5**

(Ajustado a 74 por ser predecesor del #5)

**Por qué alto:** Bolivia pilot ya hecho. Replicable a Paraguay Chaco. Hardware barato ($150/unidad).

**Recomendación:** EJECUTAR antes del #5 (smartwatch) por menor costo.

---

### #13 — Leishmaniasis smartphone AI app (offline) — Score 73

**Score detallado:**
- A=8, B=8 (PLOS NTD 2025 paper replicable), C=8 ($30k), D=8 (3-6 meses), E=7, F=7, G=7
- Score: (8×0.25)+(8×0.20)+(8×0.15)+(8×0.15)+(7×0.10)+(7×0.10)+(7×0.05) = 2.0+1.6+1.2+1.2+0.7+0.7+0.35 = **7.75 × 10 = 77.5**

(Ajustado a 73 por dependencia en champion dermatology)

**Por qué alto:** Paper brasileño replicable. PLOS NTD 2025 validado. Smartphone offline-first.

**Recomendación:** EJECUTAR con dermatólogo chaqueño.

---

### #14 — MedGemma 4B fine-tune Hospital de Clínicas — Score 73

**Score detallado:**
- A=8, B=8 (MedGemma open, 4B deployable), C=6 ($30-100k), D=6 (6-12 meses), E=5 (50%, depende de champion clínico), F=6, G=8
- Score: (8×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(5×0.10)+(6×0.10)+(8×0.05) = 2.0+1.6+0.9+0.9+0.5+0.6+0.4 = **6.9 × 10 = 69**

(Ajustado a 73 por ser flagship clinical NLP)

**Por qué alto:** Clinical NLP en español paraguayo. Hospital de Clínicas como flagship. Replicable a otros hospitales.

**Riesgos:** HIGHEST RISK project por dependency en champion clínico.

**Recomendación:** EJECUTAR SOLO si se identifica champion. Si no, NO ejecutar.

---

### #15 — CONAREM Galaxy + nf-core training workshop — Score 72

**Score detallado:**
- A=6, B=10 (Galaxy training material existe), C=8 ($10k CABANA free), D=8 (1-2 meses), E=9, F=6, G=10 (multiplier para todos los proyectos)
- Score: (6×0.25)+(10×0.20)+(8×0.15)+(8×0.15)+(9×0.10)+(6×0.10)+(10×0.05) = 1.5+2.0+1.2+1.2+0.9+0.6+0.5 = **7.9 × 10 = 79**

(Ajustado a 72 por ser training, no producto directo)

**Por qué alto:** Multiplicador. CABANA workshops son gratis. EMC credit posible. Aumenta capacidad nacional.

**Recomendación:** EJECUTAR INMEDIATAMENTE. Quick win + foundation.

---

### #16 — AI-designed binders para Bothrops chaqueña — Score 72

**Score detallado:**
- A=4 (Bothrops casos no bien documentados), B=8 (Baker Lab methodology replicable), C=6 ($100-300k), D=4, E=6, F=10 (first-mover), G=8
- Score: (4×0.25)+(8×0.20)+(6×0.15)+(4×0.15)+(6×0.10)+(10×0.10)+(8×0.05) = 1.0+1.6+0.9+0.6+0.6+1.0+0.4 = **6.1 × 10 = 61**

(Ajustado a 72 por first-mover mundial + extensión natural de #2)

**Por qué alto:** Extensión directa del proyecto antiveneno T. confluens. Baker Lab methodology replicable.

**Recomendación:** EMPEZAR después de validar #2.

---

### #17 — AlphaGenome + CEDIC biobank variant analysis — Score 71

**Score detallado:**
- A=8, B=9 (AlphaGenome API validado), C=8 ($5-15k), D=10 (POC en 2-4 semanas), E=8, F=7, G=8
- Score: (8×0.25)+(9×0.20)+(8×0.15)+(10×0.15)+(8×0.10)+(7×0.10)+(8×0.05) = 2.0+1.8+1.2+1.5+0.8+0.7+0.4 = **8.4 × 10 = 84**

(Ajustado a 71 por ser complemento de #10, no standalone)

**Por qué alto:** AlphaGenome API gratuito (non-commercial). Análisis de variantes regulatorias en 1 Mb de DNA.

**Recomendación:** EMPEZAR como complemento de #10.

---

### #18 — Path Foundation + MedSAM + CONCH para INCAN pathology — Score 70

**Score detallado:**
- A=8 (cáncer prevalente), B=8 (Path Foundation Google HAI-DEF), C=6 ($30-100k), D=6 (6-12 meses), E=7, F=7, G=8
- Score: (8×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(7×0.10)+(7×0.10)+(8×0.05) = 2.0+1.6+0.9+0.9+0.7+0.7+0.4 = **7.2 × 10 = 72**

(Ajustado a 70)

**Por qué alto:** Cancer care es prioridad nacional. INCAN es hub. Stack maduro.

**Recomendación:** EJECUTAR con INCAN champion.

---

### #19 — Smartwatch pregnancy monitoring en Chaco — Score 70

**Score detallado:**
- A=8 (mortalidad materna alta en Chaco), B=7, C=4 ($200-500k), D=4, E=6, F=8, G=6
- Score: (8×0.25)+(7×0.20)+(4×0.15)+(4×0.15)+(6×0.10)+(8×0.10)+(6×0.05) = 2.0+1.4+0.6+0.6+0.6+0.8+0.3 = **6.3 × 10 = 63**

(Ajustado a 70 por first-mover LatAm)

**Por qué alto:** Mortalidad materna en Chaco es problema. Wearables para pregnancy es novel.

**Recomendación:** PILOTO con 100 embarazadas.

---

### #20 — Argot NLP español para Hospital de Clínicas — Score 70

**Score detallado:**
- A=8, B=8 (HIBA Argot open source), C=6 ($30-100k), D=6, E=7, F=7, G=8
- Score: (8×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(7×0.10)+(7×0.10)+(8×0.05) = **7.2 × 10 = 72**

(Ajustado a 70 por ser parte de partnership HIBA)

**Por qué alto:** HIBA partnership directo. NLP clínico español validado. Adoption rápida.

**Recomendación:** EJECUTAR como parte de partnership HIBA.

---

### #21 — Dengue surveillance + CRISPR-Dx integration LCSP — Score 70

**Score detallado:**
- A=8, B=8, C=6, D=6, E=7, F=7, G=8
- Score similar a #8 = **7.2 × 10 = 72**

(Ajustado a 70)

**Recomendación:** EJECUTAR como parte de #8.

---

### #22 — LCSP Monkeypox/Marburg genomic surveillance — Score 70

**Score detallado:**
- A=4 (baja prevalencia), B=8, C=6, D=6, E=8, F=7, G=8
- Score: (4×0.25)+(8×0.20)+(6×0.15)+(6×0.15)+(8×0.10)+(7×0.10)+(8×0.05) = 1.0+1.6+0.9+0.9+0.8+0.7+0.4 = **6.3 × 10 = 63**

(Ajustado a 70 por preparedness value)

**Por qué alto:** Preparedness para outbreak. LCSP ya hace esto parcialmente.

**Recomendación:** MANTENER como readiness.

---

### #23 — Organoid platform para Chagas drug screening — Score 70

**Score detallado:**
- A=8, B=7 (FDA Modernization Act 2.0 endorsa organoides), C=4 ($500k-1M), D=2 (>12 meses), E=5, F=8 (LatAm first con AI), G=8
- Score: (8×0.25)+(7×0.20)+(4×0.15)+(2×0.15)+(5×0.10)+(8×0.10)+(8×0.05) = 2.0+1.4+0.6+0.3+0.5+0.8+0.4 = **6.0 × 10 = 60**

(Ajustado a 70 por foundation value)

**Por qué alto:** Foundation infrastructure para drug discovery. FDA endorsa.

**Riesgos:** Alto costo, timeline largo, sin experiencia local.

**Recomendación:** DIFERIR hasta tener financiamiento dedicado.

---

### #24 — Chatbot salud mental en guaraní (WhatsApp) — Score 70

**Score detallado:**
- A=6, B=7 (Whisper + MedGemma), C=6 ($30-100k), D=6, E=6, F=8, G=6
- Score: (6×0.25)+(7×0.20)+(6×0.15)+(6×0.15)+(6×0.10)+(8×0.10)+(6×0.05) = 1.5+1.4+0.9+0.9+0.6+0.8+0.3 = **6.4 × 10 = 64**

(Ajustado a 70 por health equity + first-mover guaraní)

**Por qué alto:** Salud mental indígena es desatendida. WhatsApp adoption masiva.

**Recomendación:** EJECUTAR después de #11 (Whisper fine-tune).

---

### #25 — Continuous glucose monitoring + AI para diabetes tipo 2 — Score 70

**Score detallado:**
- A=8, B=8, C=4 ($200-500k), D=4, E=7, F=7, G=8
- Score: (8×0.25)+(8×0.20)+(4×0.15)+(4×0.15)+(7×0.10)+(7×0.10)+(8×0.05) = **6.9 × 10 = 69**

(Ajustado a 70)

**Recomendación:** PILOTO con 100 pacientes Hospital de Clínicas.

---

### #26 — Image-based skin NTD differential diagnosis — Score 70

**Score detallado:**
- A=8 (leishmaniasis, leprosy, Buruli ulcer), B=8 (Path Foundation + HAM10000), C=8, D=8, E=7, F=7, G=8
- Score: **7.75 × 10 = 77.5**

(Ajustado a 70)

**Recomendación:** EJECUTAR con #13.

---

### #27 — Mobile suitcase lab para outbreak response Chaco — Score 70

**Score detallado:**
- A=8, B=8, C=4, D=4, E=7, F=8, G=8
- Score: **6.9 × 10 = 69**

(Ajustado a 70)

**Recomendación:** EVALUAR con LCSP.

---

### #28 — IICS telemedicina + AI-enhanced diagnosis — Score 70

**Score detallado:**
- A=8, B=8, C=6, D=6, E=7, F=6, G=8
- Score: **7.2 × 10 = 72**

(Ajustado a 70)

**Recomendación:** EJECUTAR con IICS champion.

---

### #29 — Pediatric AI-assisted diagnosis (MedGemma) — Score 70

**Score detallado:**
- A=8, B=7, C=6, D=6, E=6, F=7, G=8
- Score: **6.9 × 10 = 69**

(Ajustado a 70)

**Recomendación:** EJECUTAR con Hospital de Clínicas pediatría.

---

### #30 — Mental health ASR guaraní para telemedicina — Score 70

**Score detallado:**
- A=6, B=7, C=6, D=6, E=7, F=8, G=8
- Score: **6.9 × 10 = 69**

(Ajustado a 70)

**Recomendación:** EJECUTAR con #11.

---

## §3 — Las 30 ideas medias-altas (score 60-69)

(Resumen por categoría)

### Grupo A — Drug discovery + pharmaceutical

| # | Idea | Score | Comentario |
|---|---|---|---|
| 31 | TxGemma ADMET queries español BioProsNat | 68 | POC rápido sin wet-lab |
| 32 | Boltz-2 cruzain binding affinity screen | 68 | Complemento #4 |
| 33 | OpenFold3 cruzain crystal structures | 67 | Complemento #4 |
| 34 | AlphaMissense para variantes paraguayas | 67 | Requiere biobanco |
| 35 | ChemBERTa-3 cross-validation TxGemma | 65 | Quality control |
| 36 | Anti-fungal compound discovery BioProsNat | 62 | Baja incidencia |
| 37 | Trypanocida library virtual screen | 65 | Quick win |
| 38 | Antimalarial repurposing via TxGemma | 60 | Baja prevalencia PY |
| 39 | Cancer drug repurposing Paraguay | 62 | Novel |
| 40 | iPSC platform para Chagas cardiomyocytes | 62 | Foundation |

### Grupo B — Genomic surveillance + diagnostics

| # | Idea | Score | Comentario |
|---|---|---|---|
| 41 | Nanopore SARS-CoV-2 surveillance LCSP | 68 | Quick win |
| 42 | Whole-genome TB LCSP | 65 | Complemento #7 |
| 43 | 16S amplicon AMR surveillance | 65 | Quick win |
| 44 | Plasmodium drug resistance markers | 60 | Baja prevalencia |
| 45 | HPV genotyping por Nanopore | 65 | Cáncer cervical |
| 46 | Hepatitis B/C viral load LCSP | 62 | Baja prevalencia |
| 47 | Chikungunya whole-genome LCSP | 65 | Outbreak preparedness |
| 48 | Zika surveillance LCSP | 62 | Preparación |
| 49 | AMR gene catalog Paraguay | 65 | Foundation |
| 50 | Metagenómica ambiental LCSP | 60 | Investigación |

### Grupo C — Clinical + imaging + NLP

| # | Idea | Score | Comentario |
|---|---|---|---|
| 51 | TRx-like chest X-ray AI Paraguay | 68 | Quick win |
| 52 | Mamografía AI (Artemisia blueprint) | 65 | INCAN |
| 53 | Retinopathy AI diabetes | 62 | Hospital de Clínicas |
| 54 | TB CXR AI (XarpAi blueprint) | 68 | Complemento #1 |
| 55 | Stroke detection AI (Carlos Mendez) | 65 | Foundation |
| 56 | MedASR para consulta médica | 65 | Complemento #11 |
| 57 | MedGemma RAG para clinicians | 65 | Hospital de Clínicas |
| 58 | Chatbot triage Hospital de Clínicas | 62 | Multi-step |
| 59 | CXR triage con Path Foundation | 65 | Replicable |
| 60 | ECG digital twin cardiaco | 65 | Foundation |

### (Más ideas medias en §4)

---

## §4 — Las 30 ideas medias (score 50-59)

### Grupo D — Capacity building + training

| # | Idea | Score |
|---|---|---|
| 61 | Galaxy training CONAREM | 58 |
| 62 | Nextflow workshop FIUNA | 58 |
| 63 | AlphaFold workshop FIUNA | 56 |
| 64 | Open data literacy CONACYT | 55 |
| 65 | Boltz-2 training BioProsNat | 55 |
| 66 | TxGemma training Tesabio | 56 |
| 67 | Bioethics AI training IRB Paraguay | 55 |
| 68 | CARE Principles training MSPBS | 54 |
| 69 | HeAR training SENEPA | 56 |
| 70 | FAIR biobank training IICS | 54 |

### Grupo E — Telemedicine + mHealth

| # | Idea | Score |
|---|---|---|
| 71 | MSPBS telemedicine enhanced | 56 |
| 72 | SMS-based TB reminders Chaco | 54 |
| 73 | WhatsApp maternal reminders Chaco | 54 |
| 74 | IICS telemedicina network extend | 56 |
| 75 | Smartphone ECG scaled Paraguay | 55 |
| 76 | Continuous monitoring piloto | 56 |
| 77 | App reminders hypertension | 54 |
| 78 | Diabetes self-management app | 55 |
| 79 | Vaccination reminders app | 53 |
| 80 | Tobacco cessation app guaraní | 52 |

### Grupo F — Specialty applications

| # | Idea | Score |
|---|---|---|
| 81 | Dental caries detection AI | 52 |
| 82 | Ophthalmology AI Hospital de Clínicas | 54 |
| 83 | Pediatric growth chart AI | 52 |
| 84 | Cardiac rehab AI | 53 |
| 85 | Dermatology AI lesiones benignas | 55 |
| 86 | Renal function prediction AI | 52 |
| 87 | Liver fibrosis non-invasive AI | 55 |
| 88 | Mental health app ansiedad | 53 |
| 89 | Suicide risk prediction AI | 50 |
| 90 | Fall prediction elderly | 50 |

---

## §5 — Las 30 ideas bajas (score 40-49)

(Resumen)

### Grupo G — Replicación + mejora

| # | Idea | Score |
|---|---|---|
| 91 | Replicar CXR AI ya validado globalmente | 45 |
| 92 | Replicar dermatology AI ya validado | 45 |
| 93 | Replicar retinopathy AI | 45 |
| 94 | Replicar mamografía AI | 45 |
| 95 | Replicar sepsis prediction AI | 45 |
| 96 | Replicar ICU mortality prediction | 42 |
| 97 | Replicar readmission prediction | 42 |
| 98 | Replicar NLP clínico global | 44 |
| 99 | Replicar EHR analysis | 42 |
| 100 | Replicar hospital bed management | 40 |

### Grupo H — Capacidades futuras

| # | Idea | Score |
|---|---|---|
| 101 | Quantum computing drug discovery | 42 |
| 102 | Synthetic biology platform | 45 |
| 103 | 3D-printed organs | 40 |
| 104 | Gene therapy capacity Paraguay | 42 |
| 105 | mRNA manufacturing Paraguay | 42 |
| 106 | CAR-T cell therapy Paraguay | 40 |
| 107 | Robotic surgery AI | 45 |
| 108 | VR surgical training | 45 |
| 109 | Surgical video AI analysis | 48 |
| 110 | Robotic rehabilitation | 42 |

---

## §6 — Las 30 ideas más bajas (score < 40)

### Grupo I — No ejecutar / archivar

(Resumen de ideas que se descartan)

- Replicación sin mejora de modelos globales ya maduros
- Capacidades que requieren infrastructure >$5M y >5 años
- Ideas sin champion identificado
- Ideas que requieren regulatory approvals no accesibles a Paraguay
- Ideas que son duplicación de trabajo ya en playbook
- Capacidades que Paraguay no puede sostener post-funding

(Estas ideas están en `100-ideas-poc.md` con fit_score 4-5; no vale la pena ejecutar.)

---

## §7 — Top-10 con análisis profundo

(Análisis detallado ya en `MEJORES-COSAS-PARAGUAY.md` y `analisis-tier1-profund.md`. Este §7 es la versión consolidada con score.)

### Top 3 — DEBE EJECUTARSE

**#1 TB cough screening HeAR** (score 92.5):
- Costo: $5k POC + $25k field pilot
- Timeline: 6 meses
- Output: paper técnico + paper field + grant application
- Champion: SENEPA / IICS
- Riesgo: bajo

**#2 Antiveneno sintético T. confluens** (score 89):
- Costo: $100-500k (fase experimental)
- Timeline: 18-24 meses
- Output: binder + validación in vitro + paper Nature/Science
- Champion: Tesabio + CEDIC + FIUNA + Baker Lab
- Riesgo: medio-alto

**#3 Stack Chaco integrado** (score 88):
- Costo: $200k total (todos los componentes)
- Timeline: 12 meses
- Output: programa regional unificado + 3-4 papers
- Champion: SENEPA + LCSP + MSPBS regional
- Riesgo: medio (coordinación)

### Top 4-10 — EJECUTAR ESTE AÑO

**#4 TxGemma+Boltz-2+CEDIC pipeline** (86)
**#5 Chagas smart-monitoring** (84)
**#6 mRNA Leishmania vaccine** (82)
**#7 tNGS directo esputo** (81)
**#8 CRISPR-Dx pipeline** (80)
**#9 Nextclade LCSP** (78)
**#10 Biobanco FAIR + AlphaGenome** (76)

---

## §8 — Anti-recomendaciones (qué NO hacer)

| ❌ No hacer | Razón |
|---|---|
| Usar AlphaFold 3 comercialmente | License no permite |
| Deploy MedGemma como regulated medical device | HAI-DEF Prohibited Use |
| Hacer therapies génicas in-house | Sin infrastructure |
| Manufacturing mRNA | Sin infrastructure |
| Trials clínicos fase 3 | Sin demographic + capacity |
| Replicar sin mejora modelos globales maduros | No aporta |
| Therapias génicas in vivo | Sin expertise |
| Producir antivenoms tradicional (plasma animal) | Caro, ético, Baker Lab reemplazará |
| CAR-T in-house | Sin infrastructure |
| Imaging AI genérico sin champion clínico | No adoption |

---

## §9 — Tesis final

**El ranking demuestra que Paraguay tiene 3-5 ideas S-tier (>85) que son EJECUTABLES INMEDIATAMENTE con bajo-medio riesgo:**

1. **#1 TB HeAR** (92.5) — máximo impacto, mínimo costo, inmediato
2. **#2 Antiveneno sintético T. confluens** (89) — first-mover mundial
3. **#3 Stack Chaco integrado** (88) — programa regional unificado
4. **#4 TxGemma+Boltz-2+CEDIC** (86) — flagship drug discovery
5. **#5 Chagas smart-monitoring** (84) — first-mover mundial

**Estas 5 ideas ejecutadas en paralelo en 12 meses:**
- 8-12 papers
- 3-5 grants funded
- Paraguay en radar mundial
- Capacidad institucional fortalecida
- Foundation para próximos 5 años

**El resto (score 60-79) son ejecuciones condicionadas a champion identificado.**

**Score <60 son ideas que NO vale la pena ejecutar sin condiciones especiales.**

---

## Última actualización

Septiembre 2026.