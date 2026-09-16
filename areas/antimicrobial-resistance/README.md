# Área 5 — Resistencia antimicrobiana + screening TB respiratorio

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§14-google-deepmind--hai-def--catálogo-detallado) · [research findings](../docs/research-findings.md) · [Google dedicado](../docs/google-deepmind-paraguay.md)

---

## Problema

Paraguay no tiene un sistema nacional automatizado de vigilancia genómica de resistencia antimicrobiana. IICS opera una red desde 2007 para caracterización molecular de resistencia, con 17 años de datos acumulados pero sin capa de aprendizaje automático. La convocatoria 2026 FAPESP-CONACYT-CONICET está explícitamente dirigida a resistencia antimicrobiana en producción animal — Paraguay es exportador importante importante de carne.

**TB es endémico en Paraguay** (165k Chagas en Chaco, TBC persistente en comunidades indígenas chaqueñas; transmisión doméstica + VIH). Atención primaria rural no tiene acceso a chest X-ray. **HeAR** (Google) permite screening acústico de TB vía smartphone — extensión natural de este área.

## Capacidades locales

- **IICS-UNA** opera la Red Nacional de Resistencia Antibiótica desde 2007.
- **Hospital General de Barrio Obrero** — datos activos de TB IGRA-TB vs QFT-Plus (estudio 2025 publicado).
- **BioProsNat** — screening antimicrobiano experimental.
- **SENACSA** — Servicio Nacional de Calidad y Salud Animal, regula uso veterinario.
- **SENEPA** — Servicio Nacional de Erradicación del Paludismo, pero también epidemiología general.

## Herramientas de código abierto

### Genómica AMR

| Herramienta | Función | Patógeno |
|---|---|---|
| [Mykrobe](https://github.com/Mykrobe-tools/mykrobe) | Predicción de resistencia desde WGS | *M. tuberculosis*, *S. aureus* |
| [TBProfiler](https://github.com/jodyphelan/TBProfiler) | Genotipado + resistencia TB | *M. tuberculosis* |
| [AMRFinderPlus (NCBI)](https://github.com/ncbi/amr) | Genes de resistencia desde genomas bacterianos | General |
| [Staramr](https://github.com/phac-nml/staramr) | Predicción AMR desde WGS | General |
| [ResFinder](https://genomicepidemiology.org/services/) | Base de datos genes de resistencia | General |
| [ARIBA](https://github.com/sanger-pathogens/ariba) | Genes de resistencia desde reads | General |

### Audio-based screening (TB, COVID, COPD, asma)

| Herramienta | Función | Licencia | Notas |
|---|---|---|---|
| **[HeAR](https://huggingface.co/google/hear)** | Embeddings 512-d para clips de audio de 2s (tos, respiración, habla) | **HAI-DEF** | **⭐⭐⭐ Nuevo para Paraguay.** Linear probing SOTA en 33 health acoustic tasks. |
| [Whisper](https://github.com/openai/whisper) | ASR multilingüe | MIT | Para transcripts. |

### Patología digital + radiology (para casos con imaging)

| Herramienta | Función | Licencia |
|---|---|---|
| [CXR Foundation](https://developers.google.com/health-ai-developer-foundations/cxr-foundation) | Embeddings para chest X-rays | HAI-DEF |
| [Path Foundation](https://developers.google.com/health-ai-developer-foundations) | Embeddings histopathology | HAI-DEF |

## Primer proyecto concreto

### Opción A: AMR genómico (clásico)

> Aplicar Mykrobe + AMRFinderPlus sobre el archivo histórico de aislamientos del IICS. Entrenar un clasificador XGBoost sobre los 17 años de datos de la red. Construir un dashboard de vigilancia nacional. Aplicar a la convocatoria 2026 FAPESP-CONACYT-CONICET.

Entregables:
- Paper con perfil genómico de resistencia histórica del Paraguay.
- Pipeline reproducible abierto.
- Dashboard web de vigilancia.
- Propuesta formal a la convocatoria 2026 FAPESP-CONACYT-CONICET (fecha de cierre abril 2026 — verificar).

### Opción B: TB cough screening con HeAR (nuevo, alto impacto)

> Entrenar clasificador lineal (logistic regression / SVM) sobre embeddings HeAR para distinguir toses TB-positivas vs TB-negativas. Desplegar en smartphone para community health workers en Chaco.

**Pipeline**:
1. Cargar HeAR (HF: `google/hear`).
2. Usar datasets públicos para bootstrap (COUGHVID, SPRSound, ICBHI).
3. Si hay datos locales disponibles, fine-tune.
4. Entrenar clasificador lineal (binario TB / no-TB).
5. Evaluar en test set.
6. **Si funciona**: prototipo de app móvil.

Entregables:
- Modelo open weights + clasificador.
- Paper con resultados de validación.
- Demo de app móvil (puede ser React Native + backend Python).

## Vacíos de información

### Opción A (AMR)

- ¿Los datos están en WHONET o en un sistema propio?
- ¿Hay aislados secuenciados (WGS) disponibles?
- ¿Cuál es la capacidad de cómputo del IICS?
- ¿Cuál es la política del SENACSA sobre datos de uso veterinario?
- ¿Hay coinvestigadores brasileños o argentinos con trabajo previo en AMR animal con los que aliarnos?

### Opción B (HeAR TB)

- ¿Hay datos paraguayos de toses grabados?
- ¿Qué infraestructura hay en Hospital de Clínicas / SENEPA para capturar toses?
- ¿Hay datasets etiquetados TB vs no-TB en Paraguay?
- ¿Cuál es la cobertura de smartphones en el Chaco?
- ¿Cuál es la postura regulatoria del MSPBS para usar AI para triaje TB?

## Próximo paso inmediato

**Opción A**: contactar a **Dra. Rosa Guillén Fretes** (IICS Microbiología, PRONII II) — es la persona que lidera la red desde 2007. Una conversación inicial responde la mitad de las preguntas.

**Opción B**: contactar a **SENEPA** y al **Hospital General de Barrio Obrero** (TB research activo). Explorar acceso a datasets de toses y clínica de TB.

## Notas regulatorias

- Si los datos son a nivel paciente (no aislado): aplica Ley 7593/2025.
- Si son aislados con metadata epidemiológica: caso por caso.
- SENACSA regula el lado animal; requiere acuerdo específico.
- La convocatoria 2026 FAPESP-CONACYT-CONICET tiene requisitos administrativos — verificar elegibilidad institucional con CONACYT.
- Para Opción B: **HeAR no es dispositivo médico regulado** (HAI-DEF Prohibited Use). **Solo asistir al clínico**, no autonomous diagnosis. El deployer asume la responsabilidad regulatoria.