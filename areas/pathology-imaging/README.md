# Área 4 — Patología digital e imágenes médicas

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§4-modelos-fundacionales-de-patología) · [research findings](../docs/research-findings.md)

---

## Problema

Paraguay no tiene patología digital sistemática. INCAN procesa biopsias para cáncer (especialmente colorrectal, por el trabajo publicado de MassARRAY OncoCarta) pero los slides son físicos, no digitalizados. Los modelos fundacionales de patología (UNI, CONCH, Virchow2, Path Foundation) podrían detectar y segmentar tumores con cero o poco entrenamiento adicional.

## Capacidades locales

- **INCAN** — perfil molecular del cáncer colorrectal paraguayo, parte del consorcio LEGACY (UE-LATAM) para cáncer gástrico.
- **City Cancer Challenge (C/Can)** — Asunción es una de las 4 primeras "learning cities" desde 2017.
- **Programa RACAM** (ASCO 2025) — navegación de pacientes oncológicos.
- **Asociación regional** con Hospital Italiano de Buenos Aires (referente en IA clínica).

## Herramientas de código abierto

| Herramienta | Función | Benchmark 2025 | Licencia |
|---|---|---|---|
| [UNI](https://github.com/mahmoodlab/UNI) | Visión-only pathology FM | Top 3 | Apache 2.0 |
| [CONCH](https://github.com/mahmoodlab/CONCH) | Visión-lenguaje pathology FM | **Top 1** | Research use |
| [Virchow / Virchow2](https://github.com/Paige-AI/virchow) | Visión-only, ViT-H/632M params | Top 2 | Research use |
| [Path Foundation](https://developers.google.com/health-ai-developer-foundations) | Google | — | Apache 2.0 |
| [H-optimus-0](https://github.com/bioptimus/h-optimus-0) | Visión-only | Top 5 | Research use |
| [MedSAM](https://github.com/bowang-lab/MedSAM) | Segmentación universal médica | — | MIT |
| [BiomedCLIP](https://github.com/microsoft/BiomedCLIP) | Image-text retrieval médico | — | MIT |
| [MAIRA-2](https://huggingface.co/microsoft/maira-2) | Informes radiológicos | — | MSRLA |
| [CheXagent](https://github.com/Stanford-AIMI/CheXagent) | Chest X-ray FM | Top en clasificación | Research use |

## Primer proyecto concreto

> Escanear 1.000 slides de H&E retrospectivos del INCAN (con consentimiento + IRB + DPIA). Aplicar CONCH para detección zero-shot de tumor, MedSAM para segmentación. Validar contra lecturas de patólogos del INCAN.

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

## Próximo paso inmediato

Mapeo de champions en INCAN patología. LinkedIn, papers conjuntos, contacto a través de City Cancer Challenge.

## Notas regulatorias

- Datos de salud = sensibles (Ley 7593/2025).
- DPIA obligatoria.
- Si se usan bloques de parafina históricos, verificar consentimiento original + obtener ampliación o re-consentimiento.
- Coordinar con la Sociedad Paraguaya de Anatomía Patológica.

## Riesgos

- Sin escáner digital en INCAN, el primer paso es comprar/alquilar uno (~$15–50k USD).
- Sin consentimiento ampliado, no se puede usar el archivo histórico para investigación.
- La validación con patólogos requiere tiempo protegido — un bien escaso.