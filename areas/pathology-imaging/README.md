# Área 4 — Patología digital e imágenes médicas

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§4-modelos-fundacionales-de-patología) · [research findings](../docs/research-findings.md) · [Google dedicado](../docs/google-deepmind-paraguay.md)

---

## Problema

Paraguay no tiene patología digital sistemática. INCAN procesa biopsias para cáncer (especialmente colorrectal por el trabajo publicado de MassARRAY OncoCarta) pero los slides son físicos, no digitalizados. Los modelos fundacionales de patología (UNI, CONCH, Virchow2, Path Foundation) podrían detectar y segmentar tumores con cero o poco entrenamiento adicional.

## Capacidades locales

- **INCAN** — perfil molecular del cáncer colorrectal paraguayo, parte del consorcio LEGACY (UE-LATAM) para cáncer gástrico.
- **City Cancer Challenge (C/Can)** — Asunción es una de las 4 primeras "learning cities" desde 2017.
- **Programa RACAM** (ASCO 2025) — navegación multicomponente.
- **Asociación regional** con Hospital Italiano de Buenos Aires (referente en IA clínica).

## Herramientas de código abierto

### Pathology foundation models

| Modelo | Top en | Licencia | Notas |
|---|---|---|---|
| [CONCH](https://github.com/mahmoodlab/CONCH) | Top general (Nature BME 2025) | Research use | Vision-language, Mahmood Lab. |
| [Virchow2](https://github.com/Paige-AI/virchow) | Cerca 2° general | Research use | Paige + Microsoft. ViT-H/632M. |
| [UNI2-h](https://github.com/mahmoodlab/UNI) | Mejor en low-data | Apache 2.0 | Mahmood Lab. |
| [H-optimus-0/1](https://github.com/bioptimus/h-optimus-0) | Staining shifts | Research use | Bioptimus, ViT-giant/1.1B. |
| [PathOrchestra](https://github.com/SLIIV/PathOrchestra) | Cross-task (112 tasks) | Research use | Shanghai AI Lab. |
| [KEEP](https://github.com/SLIIV/KEEP) | Knowledge-enhanced | Research use | Shanghai AI Lab + SJTU. |
| [TITAN](https://github.com/mahmoodlab/TITAN) | Slide-level | Research use | Construido sobre CONCH1.5. |
| [Midnight](https://github.com/SophontAI/Midnight) | Open reproduction | MIT | 12K WSIs TCGA, $1.6k. |
| [OpenMidnight](https://github.com/SophontAI/OpenMidnight) | Midnight totalmente abierta | MIT | Fully reproducible. |

### Segmentación

| Herramienta | Función | Licencia | Notas |
|---|---|---|---|
| [MedSAM](https://github.com/bowang-lab/MedSAM) | Segmentación universal médica | MIT | Funciona en CT/MRI/X-ray/ultrasonido. |

### Encoders visuales médicos de Google (HAI-DEF)

| Modelo | Función | Licencia |
|---|---|---|
| **[Path Foundation](https://developers.google.com/health-ai-developer-foundations)** | Embeddings histopathology | HAI-DEF |
| [CXR Foundation](https://developers.google.com/health-ai-developer-foundations/cxr-foundation) | Embeddings chest X-rays | HAI-DEF |
| [Derm Foundation](https://developers.google.com/health-ai-developer-foundations) | Embeddings dermatología | HAI-DEF |
| [MedSigLIP](https://developers.google.com/health-ai-developer-foundations/medsiglip/model-card) | SigLIP médico | Apache 2.0 |

## Primer proyecto concreto

> Escanear 1.000 slides de H&E retrospectivos del INCAN (con consentimiento + IRB + DPIA). Aplicar CONCH para detección zero-shot de tumor, MedSAM para segmentación. Validar contra lecturas de patólogos del INCAN.

**Variante con Path Foundation**: usar Path Foundation + MedSAM en lugar de CONCH.

Entregables:
- Paper de validación (métricas vs gold-standard).
- Dataset abierto (slides + anotaciones).
- Ruta clínica documentada para despliegue futuro.
- White paper para MSPBS sobre regulación de IA diagnóstica.

## Vacíos de información

- ¿Tiene INCAN un escáner de slides digital? ¿Cuál?
- ¿Qué cobertura tiene el archivo patológico histórico?
- ¿Cómo se gestiona el consentimiento para uso secundario de muestras históricas?
- ¿Hay patólogos con tiempo disponible para validación?
- ¿Cuál es el costo de escanear 1.000 slides?
- ¿La infraestructura eléctrica y de red del INCAN soporta el flujo?
- ¿Hay datos paraguayos para validar CXR Foundation (TB, neumonía)?
- ¿Hay datos paraguayos para Derm Foundation (teledermatología rural)?

## Próximo paso inmediato

Mapeo de champions en INCAN patología. LinkedIn, papers conjuntos, contacto a través de City Cancer Challenge.

**Recursos de arranque**:
- Curated index: [github.com/georg-wolflein/pathology-foundation-models](https://github.com/georg-wolflein/pathology-foundation-models)
- Alternative: [github.com/dibalokechanda/PFMs](https://github.com/dibalokechanda/PFMs)
- Google HAI-DEF models en [developers.google.com/health-ai-developer-foundations](https://developers.google.com/health-ai-developer-foundations)

## Notas regulatorias

- Datos de salud = sensibles (Ley 7593/2025).
- DPIA obligatoria.
- Si se usan bloques de parafina históricos, verificar consentimiento original + obtener ampliación o re-consentimiento.
- Coordinar con la Sociedad Paraguaya de Anatomía Patológica.
- **HAI-DEF Prohibited Use**: Path/CXR/Derm Foundation no pueden usarse como dispositivo médico regulado. Solo asistir al clínico.

## Riesgos

- Sin escáner digital en INCAN, el primer paso es comprar/alquilar uno (~$15–50k USD).
- Sin consentimiento ampliado, no se puede usar el archivo histórico para investigación.
- La validación con patólogos requiere tiempo protegido — un bien escaso.
- Distribución geográfica: Patólogos de INCAN en Capiatá, no en otros departamentos. Scalability limitada.