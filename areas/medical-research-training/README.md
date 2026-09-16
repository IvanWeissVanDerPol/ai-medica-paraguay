# Área 8 — Capacitación en investigación clínica

Volver al [README principal](../README.md) · [mapa de actores](../docs/mapa-actor-instituciones.md) · [marco regulatorio](../docs/marco-regulatorio.md) · [AI stack ref](../docs/ai-stack-reference.md#§7-agentes-de-ia-para-ciencia) · [research findings](../docs/research-findings.md)

---

## Problema

Los residentes médicos paraguayos reciben solo un semestre de bioestadística en pregrado. El 78 % nunca cursó metodología de investigación posgrado. Solo el 24 % ha publicado nacionalmente, solo el 14 % internacionalmente. Sin embargo, el 70 % cree que la formación en investigación debe ser obligatoria y el 95 % que la investigación mejora atención al paciente. Hay talento y motivación; faltan tiempo protegido, mentores y herramientas.

## Capacidades locales

- **Facultad de Ciencias Médicas (UNA)** — 9.000 docentes, hospital escuela.
- **CONAREM** — 23 unidades formadoras, ~500 residentes.
- **IICS-UNA** — Maestrías y Doctorado en Ciencias Biomédicas, Maestría en Ingeniería Biomédica.
- **Hospital de Clínicas** — programa de residencia en Medicina Familiar con requisito de tesis.

## Herramientas de código abierto

- [Galaxy](https://galaxyproject.org) — interfaz web sin instalación para análisis bioinformático.
- [nf-core](https://github.com/nf-core) — pipelines reproducibles (Nextflow).
- [RMarkdown](https://rmarkdown.rstudio.com) / [Quarto](https://quarto.org) — informes reproducibles.
- [Bioconductor](https://bioconductor.org) — recursos R para biología.
- [Scikit-learn](https://scikit-learn.org) / [PyTorch](https://pytorch.org) — base para cursos introductorios de ML.
- [STATA / R / Python](https://www.r-project.org) — herramientas estadísticas estándar.

## Primer proyecto concreto

> Taller "Bioinformática y Análisis Clínico con Galaxy" para 30 residentes del Hospital de Clínicas, en alianza con IICS y la red SoIBio/AB3C. Programa: 5 sesiones, enseñar Galaxy + RMarkdown + lectura crítica. Materiales abiertos en español. Acreditar como curso de educación médica continua.

Entregables:
- Materiales del curso en repo abierto (en español).
- Pre/post test de conocimientos.
- Acreditación ante CONAREM como EMC.
- Tutoría posterior para los proyectos de tesis de los residentes.
- Paper sobre la experiencia + lecciones aprendidas.

## Vacíos de información

- ¿Qué cursos de educación médica continua existen ya?
- ¿Quién sería el champion en CONAREM?
- ¿Hay financiamiento específico para este tipo de capacitación?
- ¿Quién de IICS o FCM-UNA podría co-impartir el taller?
- ¿Qué hace falta para acreditar como EMC?
- ¿Hay precedentes de cursos SoIBio/AB3C en Paraguay?

## Próximo paso inmediato

Mapeo de champions en CONAREM + IICS. Verificar si existe ya un programa de bioestadística para residentes.

## Notas regulatorias

- No aplica directamente la Ley 7593/2025 (no toca datos de pacientes directamente).
- Política Nacional de Ética en Investigación en Salud (2024) puede tener requisitos de capacitación obligatoria para investigadores — verificar.

## Riesgos

- **Adopción**: si los residentes no ven beneficio inmediato, no vendrán. Diseño debe resolver un problema concreto (la tesis obligatoria, por ejemplo).
- **Sostenibilidad**: si depende de un instructor externo, muere cuando se va. Diseño debe crear capacidad local.
- **Acceso a datos**: los talleres son más valiosos si usan datos reales (anonimizados) de IICS. Requiere coordinación con DPIA.

## Conexión con otras áreas

Esta área es **multiplicadora**: cada taller entrena usuarios reales para los proyectos 1 (vigilancia genómica), 3 (LLM clínicos), 4 (patología digital), 5 (AMR), 6 (salud mental). Invertir aquí rinde en todas las demás.