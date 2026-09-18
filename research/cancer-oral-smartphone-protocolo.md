# Tamizaje de cáncer oral con smartphone — protocolo de ejecución

> **Qué es este archivo:** la idea #9 del catálogo odontológico (score 74.5, Tier A) llevada a protocolo de ejecución completo, siguiendo el formato de `top-5-detalle-completo.md`: epidemiología, arquitectura técnica, evidencia, fases con gates, presupuesto, equipo, ética, riesgos, outputs.
>
> **Audiencia:** quien ejecutaría este proyecto. Escrito como si se arrancara mañana.
>
> **Última actualización:** septiembre 2026.

---

## Índice

- §1 — Resumen ejecutivo
- §2 — El problema: el cáncer oral y Paraguay
- §3 — La solución: qué es exactamente
- §4 — Evidencia global (lo que ya funciona)
- §5 — Arquitectura técnica completa
- §6 — Fases con gates de decisión
- §7 — Presupuesto línea por línea
- §8 — Equipo, socios y champions
- §9 — Ética y marco regulatorio
- §10 — Riesgos y mitigaciones
- §11 — Outputs y valor de largo plazo
- §12 — Por qué score 74.5 y no más alto

---

## §1 — Resumen ejecutivo

Un promotor de salud o agente comunitario abre la boca de una persona de 50 años que fuma y toma mate muy caliente, toma 5-8 fotos estandarizadas con un teléfono de $200, y en 10 segundos una app de IA corriendo en el teléfono (sin internet) estima si hay lesiones sospechosas de cáncer oral o de trastornos potencialmente malignos (OPMD). Los casos sospechosos se derivan con prioridad al especialista, con las fotos adjuntas para teleconsultas.

El cáncer oral es uno de los pocos cánceres con **lesiones precursoras visibles años antes** (leucoplasias, queilitis actínica, líquen) y con un salto brutal de supervivencia cuando se detecta localizado: **86.3% a 5 años localizado vs 40.4% diseminado** (SEER). Paraguay tiene todos los factores de riesgo: tabaco, alcohol, y la costumbre cultural de tomar mate muy caliente (clasificado por IARC como carcinógeno 2A por lesión térmica — estudios del Cono Sur con datos paraguayos). Aun así, no existe ningún programa nacional de tamizaje de cáncer oral: hoy la detección depende de que el paciente llegue tarde a consulta.

El proyecto adapta un blueprint ya validado en India (app DiagnOCe: AUC 0.867, kappa 0.88 con especialistas), con datasets públicos de 12,000+ imágenes de lesiones orales. Costo del POC: **<$15,000**. Piloto de campo completo: **~$50,000**. Timeline: 4 meses a validación, 9-12 meses a piloto publicado.

---

## §2 — El problema: el cáncer oral y Paraguay

### 2.1 La enfermedad

El cáncer de labio y cavidad oral (mayoritariamente carcinoma epidermoide, OSCC) causa ~390,000 casos y ~188,000 muertes al año mundialmente (GLOBOCAN 2022), con incidencia en aumento sostenido desde 1990 (GBD 2021). Es un cáncer de pobreza y de factores de riesgo conductuales:

- **Tabaco** (todas las formas)
- **Alcohol** (efecto multiplicativo con tabaco)
- **Betel/areca** (Asia — no relevante en PY)
- **Radiación UV** (labio — trabajo rural al sol)
- **Lesión térmica crónica** por bebidas muy calientes (IARC 2A)

### 2.2 El factor paraguayo: el mate muy caliente

Este punto es lo que hace el proyecto específicamente paraguayo y no una réplica genérica:

- **IARC clasificó en 2016 las bebidas muy calientes (>65°C) como carcinógeno grupo 2A** — la evidencia viene exactamente del Cono Sur.
- El estudio pivot: **Rolón et al. 2000** (5 estudios caso-control, 830 casos / 1,779 controles en áreas de alto riesgo de Sudamérica, **incluyendo Paraguay**): mate muy caliente y consumo >1 L/día asociados significativamente a cáncer esofágico tras ajustar por tabaco y alcohol.
- **Castellsagué et al.** — "Hot and cold mate drinking and esophageal cancer in Paraguay" (estudio específicamente paraguayo).
- Revisiones de OPS/Rev Panam Salud Publica 2009: "el rol del mate caliente en elevar el riesgo de cáncer de esófago, laringe y **cavidad oral** parece estar soportado por varios estudios epidemiológicos".
- Estudios ESCCAPE (IARC, Malawi/Tanzania 2024): "muy caliente" vs "caliente" = riesgo 1.92x — la temperatura, no la hierba, es el mecanismo (lesión térmica crónica de la mucosa).

**Implicación operacional**: en Paraguay el mate no es un hábito — es la condición basal. La exposición térmica crónica de la mucosa oral + tabaco + alcohol + trabajo rural al sol (labio) configura un perfil de riesgo donde el OPMD y el OSCC temprano son razonablemente prevalentes en adultos >40. La prevalencia global de OPMD es **4.67%** (meta-análisis 2025, 108 estudios) y en **Sudamérica/Caribe es ~5.4%, con leucoplasia y queilitis actínica dominando** — queilitis actínica es la firma de exposición solar rural, exactamente el perfil chaqueño y campesino.

### 2.3 La ventana de detección y por qué se pierde

- La progresión es: mucosa normal → OPMD (leucoplasia/eritroplasia/queilitis actínica, visibles años) → OSCC temprano → OSCC avanzado.
- **Supervivencia 5 años: 86.3% localizado vs 40.4% a distancia** (SEER). Detectar en la fase visible-pre-maligna o temprana es la diferencia entre una biopsia menor y una cirugía maxilofacial mutilante + radioterapia.
- El tamizaje visual por inspección oral (OEV) está recomendado en poblaciones de riesgo en LMIC; el problema es que **requiere personal entrenado** y Paraguay tiene odontólogos concentrados en Asunción/Central y vacíos en el interior (solo 1.4% de la fuerza laboral dental mundial está en países de ingreso bajo).
- Resultado: el sistema paraguayo detecta mayoritariamente casos sintomáticos tardíos. No existe registro sistemático de OPMD ni programa de tamizaje.

**La brecha exacta**: hay una ventana clínica de años (lesiones visibles) y nadie mirando sistemáticamente la boca de los paraguayos de riesgo.

---

## §3 — La solución: qué es exactamente

### 3.1 El flujo en el campo

1. **Captura**: un promotor de salud (no odontólogo, no médico) usa una app en un smartphone estándar.
2. **Protocolo estandarizado de 5-8 fotos**: comisuras, mucosa yugal bilateral, paladar duro/blando, dorso y cara ventral de lengua, suelo de boca, reborde alveolar, labio (exterior para queilitis actínica). Flash fijo, distancia ~10 cm con guía en pantalla, dos retractores de plástico ($2 el par).
3. **Inferencia on-device** (offline): el modelo corre en el teléfono (TFLite cuantizado) y marca en las fotos las regiones sospechosas + nivel de riesgo (verde/amarillo/rojo).
4. **Salida**: (a) recomendación de derivación con prioridad; (b) registro automático del caso; (c) cuando hay conectividad, sync al dashboard central.
5. **Circuito de confirmación**: los casos amarillos/rojos van a teleconsulta con especialista de FOUNA (fotos + anamnesis breve estructurada) → decisión de biopsia → biopsia en FOUNA/INCAN → histopatología como gold standard.

### 3.2 Qué NO es

- No es un dispositivo de diagnóstico autónomo: es un **tamizador + priorizador de derivación**. El diagnóstico lo da el especialista con biopsia.
- No reemplaza al odontólogo: **habilita cobertura donde no hay nadie** mirando bocas.

---

## §4 — Evidencia global (lo que ya funciona)

### 4.1 El blueprint directo: DiagnOCe (India, 2025)

- App construida con MIT App Inventor (herramienta no-code) + clasificador de imágenes.
- Estudio transversal en entorno de atención primaria india: **AUC 0.867, sensibilidad ~71%, especificidad alta, F1 86.4%, kappa interobservador 0.88**.
- Conclusión de los autores: herramienta factible para tamizaje en entornos de recursos limitados por trabajadores de salud no especializados.
- **Lección clave para Paraguay**: no hicieron una red neuronal exótica — hicieron una app simple con un clasificador competente y la validaron en el circuito real de derivación. Ese es el estándar a igualar/mejorar.

### 4.2 Datasets públicos disponibles (no hay que recolectar nada para el POC)

| Dataset | Contenido | Acceso |
|---|---|---|
| **Egipto BDJ 2025** | **9,201 fotos intraorales** (4,405 normales / 2,314 bajo riesgo / 2,482 alto riesgo) anotadas por especialistas en LabelMe | Zenodo 14571990 (bajo acuerdo de citación, CC BY-NC-ND) |
| **Sri Lanka 2024** | **3,000 fotos** de 714 pacientes: sano/benigno/OPMD/cáncer + metadatos (edad, sexo, tabaco, alcohol) en COCO | Zenodo 10664056 (previa solicitud) |
| **HuggingFace mucosal** | 1,348 imágenes: normal/OLK/OLP/OSF/cáncer | HF: HRruiH/Dataset-of-oral-mucosal-diseases |
| NDB-UFES (Brasil) | Histopatología + datos de pacientes (leucoplasia, cáncer) | Data in Brief 2023 |

**Total: ~13,500 imágenes clínicas públicas.** Con eso se entrena un clasificador competente sin tocar un solo paciente paraguayo — los pacientes paraguayos entran solo en la fase de validación.

### 4.3 Revisiones sistemáticas del área

- **Review 23 estudios 2015-2024** (smartphone imaging + mHealth para OPMD/cáncer oral): factible y efectivo en community y clinical settings, con dual-modality autofluorescence y mobile cytology como complementos.
- **Systematic review 40 estudios / 136,257 participantes** en poblaciones rurales/low-resource: OEV, azul de toluidina, autofluorescencia, quimioluminiscencia, mHealth apps y AI — todas las estrategias son complementarias; las apps con IA son las que escalan.
- **Frontiers Oral Health 2026** (multimodal AI para prevención de precisión): el movimiento es de screening remoto → predicción multimodal de riesgo; Paraguay puede entrar directo en la generación actual.

---

## §5 — Arquitectura técnica completa

### 5.1 El modelo

**Tarea**: clasificación de regiones en fotos intraorales → {normal, bajo riesgo (aftas, fibromas, mucoceles...), alto riesgo/OPMD (leucoplasia, eritroplasia, líquen, queilitis actínica), sospecha de cáncer}.

**Enfoque** (por orden de complejidad creciente, cada nivel es un fallback del anterior):

1. **Nivel 1 — Fine-tuning de modelo de fundación**: partir de un ViT/DINOv2/EVA preentrenado y fine-tunearlo en los ~13,500 imágenes públicas en 3 clases (normal / bajo riesgo / alto riesgo+cáncer). En una T4 de Colab son horas, no días. Este es el baseline a superar.
2. **Nivel 2 — Detección + clasificación**: YOLOv8-seg o RT-DETR entrenado para segmentar la lesión (los datasets traen anotaciones de contorno) → localización + clasificación. Mejor UX (marca dónde está la lesión) y mejor audibilidad clínica.
3. **Nivel 3 — Multimodalidad**: foto + anamnesis estructurada (edad, tabaco, alcohol, mate muy caliente y/o c/día, exposición solar) → modelo tabular+imagen. Esto replica el razonamiento clínico real y probablemente suma puntos de AUC. (El dataset de Sri Lanka trae los metadatos de riesgo — está diseñado para esto.)

**Métrica objetivo**: superar AUC 0.87 de DiagnOCe en validación local paraguaya; sensibilidad para lesiones de alto riesgo ≥0.85 (en tamizaje oncológico la sensibilidad manda — un falso negativo cuesta una vida, un falso positivo cuesta una teleconsulta).

**Cuantización y deployment**: export a TFLite INT8 → corre offline en teléfonos Android de gama baja (los mismos que usa SENEPA en campo). Sin nube, sin datos personales saliendo del dispositivo salvo consentimiento de sync.

### 5.2 La app

- Android nativo o Flutter, offline-first, en español + guaraní.
- Guía de captura en pantalla (contorno de boca, distancia, luz) — la calidad de captura es la mitad del rendimiento.
- Flujo de 3 pantallas: datos mínimos (edad/sexo/factores) → captura guiada → resultado con semáforo + foto marcada.
- Sync diferido + dashboard central (los mismos componentes que el stack Chaco ya define — sinergia directa con la idea #8/#10 odontológicas y el stack TB).

### 5.3 El circuito de confirmación (esto es lo que convierte fotos en salud pública)

```
Promotor (app offline)
   │ fotos + semáforo
   ▼
Teleconsulta FOUNA (especialista ve fotos + anamnesis)
   │ triage especializado
   ▼
Biopsia FOUNA / INCAN ──► histopatología (gold standard)
   │                              │
   ▼                              ▼
Tratamiento temprano        Datos de validación → paper
```

---

## §6 — Fases con gates de decisión

**Fase 0 — Setup (semana 1, $0)**: solicitar acceso a los datasets (Zenodo, acuerdo de citación), definir entorno.

**Fase 1 — Entrenamiento (semanas 2-8, $0-2,000)**: Nivel 1 y 2 sobre datos públicos. Métricas internas cross-dataset (entrenar en Egipto+Sri Lanka, testear en HF).
*Gate 1 (semana 8): AUC ≥0.85 interno y sensibilidad alto-riesgo ≥0.80 → continuar. Si no → iterar (Nivel 3 multimodal, más datos).* 

**Fase 2 — Validación retrospectiva local (meses 3-4, $5,000-8,000)**: 300-500 fotos de pacientes FOUNA ya diagnosticados (con consentimiento, anotadas por 2 especialistas, kappa interobservador reportado) — sin intervención sobre pacientes nuevos, solo archivo.
*Gate 2: AUC local ≥0.80 y sensibilidad alto-riesgo ≥0.75 → el modelo generaliza a mucosa/fotografía paraguaya. Si hay caída fuerte → fine-tuning con las fotos locales y re-test.*

**Fase 3 — Piloto de campo (meses 5-9, $30,000-40,000)**:
- Sitio: 2 distritos (1 urbano-periférico + 1 rural) con circuito de derivación definido hacia FOUNA/teleconsulta.
- Población objetivo: adultos 40+ con ≥1 factor de riesgo (tabaco/alcohol/mate muy caliente/exposición solar) — tamizaje oportunista en centros de salud + campañas.
- n=1,000-1,500 tamizados. Todos con captura de fotos; los semáforos amarillo/rojo a teleconsulta; biopsia según criterio especialista.
- Endpoints primarios: rendimiento diagnóstico vs histopatología (sensibilidad/especificidad/PPV/NPV para alto riesgo+cáncer), tasa de derivación completa, tiempo desde tamizaje hasta resultado.
- Endpoints secundarios: aceptabilidad (promotores y pacientes), costo por caso detectado.
*Gate 3: sensibilidad campo ≥0.75 para alto riesgo+cáncer con especificidad ≥0.60, y ≥80% de derivaciones completadas → escala. Si no → publicar lecciones y ajustar protocolo de captura (la causa más común de fallo).*

**Fase 4 — Escala y sostenibilidad (meses 10-24)**: integración al circuito DSBD/FOUNA + Hospital Odontológico; registro nacional de OPMD (hoy inexistente — primer dataset epidemiológico paraguayo de OPMD); policy brief MSPBS.

---

## §7 — Presupuesto línea por línea

### Fases 0-2 (validación técnica y retrospectiva)

| Ítem | $ |
|---|---|
| Compute (Colab Pro / créditos) | 1,500 |
| Storage y herramientas | 500 |
| Estipendio anotación 2 especialistas FOUNA (300-500 fotos) | 3,000 |
| Coordinación técnica (parcial FTE) | 3,000 |
| **Subtotal** | **~8,000** |

### Fase 3 (piloto de campo)

| Ítem | $ |
|---|---|
| 8 smartphones gama media (~$220) | 1,800 |
| Desarrollo/pulido de app + dashboard | 6,000 |
| 4 promotores × 5 meses (estipendio parcial) | 6,000 |
| Retractores, espejos, kits de captura (×500) | 1,500 |
| Teleconsulta: horas especialista FOUNA | 4,000 |
| Biopsias + histopatología ( subsidio ~150 biopsias × $40) | 6,000 |
| Logística, transporte, campañas | 4,000 |
| IRB, consentimientos bilingües, materiales | 2,000 |
| M&E y análisis de datos | 3,000 |
| Contingencia 20% | 7,000 |
| **Subtotal** | **~41,000** |

**Total proyecto completo: ~$49,000.** POC solo (Fases 0-2): **<$15,000**.

---

## §8 — Equipo, socios y champions

**Equipo mínimo**:
- 1 ML engineer (FIUNA/Politécnica — mismo perfil que los otros proyectos)
- 1 odontólogo especialista en medicina oral (FOUNA) — el champion clínico
- 1 patólogo (FOUNA/INCAN) para histopatología
- 4 promotores de salud (campo)
- 1 coordinador de campo

**Champion institucional**: **Cátedra de Medicina Oral / Patología de FOUNA**. FOUNA es "Alma Mater de la Odontología Paraguaya" (80+ años), tiene servicio clínico con flujo de pacientes, cultura de investigación (publican en SciELO/revistas regionales), y está construyendo el Hospital Odontológico KOICA 2026-2031 — este proyecto puede nacer como proyecto semilla del hospital nuevo.

**Socios complementarios**: INCAN (biopsias avanzadas/oncología), DSBD-MSPBS (programa), cooperación coreana KOICA (línea presupuestaria del hospital), y el circuito de teleconsulta puede montarse sobre la experiencia de teledentología WhatsApp chilena (idea #3).

**Champion profile**: docente de medicina oral FOUNA 35-50 años con interés en OPMD/cáncer oral (buscable en autores de publicaciones SciELO paraguayas sobre lesiones de mucosa — la literatura local existe y es activa).

---

## §9 — Ética y marco regulatorio

- **IRB**: Comité de Ética FOUNA/UNA. Fase 2 con datos retrospectivos anonimizados; Fase 3 con consentimiento informado (bilingüe donde corresponda).
- **Uso y responsabilidad**: la app informa/deriva, no diagnostica. Disclaimer explícito. El resultado no se usa para decisiones clínicas autónomas — el especialista decide.
- **Ley 7593/2025** (vigencia nov 2027): anonimización en captura (edad/sexo/factores, sin identificadores en el modelo), DPIA antes del deploy a escala, datos en jurisdicción paraguaya.
- **Comunidades indígenas**: si el piloto toca poblaciones indígenas (dado el perfil chaqueño de exposición solar), aplica consulta comunitaria previa y gobernanza CARE de las imágenes (las fotos de lesiones pueden ser identificables — tratarlas como datos sensibles).
- **Equidad**: el tamizaje es gratuito para el tamizado; el circuito de biopsia necesita subsidio para no crear una ruta de derivación sin destino.

---

## §10 — Riesgos y mitigaciones

| # | Riesgo | Prob. | Mitigación |
|---|---|---|---|
| 1 | Calidad de fotos de campo degrada el modelo (iluminación, encuadre) | Alta | Protocolo de captura guiado en la app (la mitad del proyecto); augmentations de campo en entrenamiento; Gate 2 con fotos locales reales |
| 2 | Falsos negativos en lesiones tempranas (leucoplasias finas) | Media | Priorizar sensibilidad en el punto de corte; doble lector (IA + teleconsulta); reportar por subtipo de lesión |
| 3 | Derivaciones que no llegan a biopsia (pérdida en el circuito) | Alta | Teleconsulta como filtro con cita directa; subsidio de biopsia; tracking en dashboard (endpoint explícito) |
| 4 | PPV bajo → muchas biopsias innecesarias | Media | Telederm... teleconsulta especializada antes de biopsia (el filtro humano de 2 niveles es la defensa); reportar PPV por umbral |
| 5 | No surge champion en FOUNA | Media | Outreach a cátedras de medicina oral + INCAN como alternativa; co-autoría como incentivo |
|  Gates de corte | — | Kill criteria explícitos por fase (§6) — fallo barato y temprano |
| 6 | Sobrediagnóstico de OPMD que nunca progresaría | Media | Registro con seguimiento (sub-producto valioso: historia natural paraguaya de OPMD, hoy desconocida) |

---

## §11 — Outputs y valor de largo plazo

**A los 4 meses**: clasificador validado + app + paper de validación (enviable a BDJ/Open Dentistry Journal/JOralRes — revistas donde FOUNA ya publica).

**A los 9-12 meses**: piloto publicado (1-2 papers): rendimiento diagnóstico + costo por caso detectado + circuito de derivación — el argumento para MSPBS.

**Activos de largo plazo**:
1. **Primer registro/dataset paraguayo de OPMD y cáncer oral temprano** — hoy no existe ningún dato nacional. Valor epidemiológico enorme y único.
2. Infraestructura de tamizaje con smartphone reutilizable para las otras ideas (caries #2, fluorosis #12, anemia gingival #14 — la misma app puede alojar múltiples modelos: "la app de la boca paraguaya").
3. Historia natural local de OPMD (sub-producto del seguimiento).
4. Alineación perfecta con el Hospital Odontológico FOUNA-KOICA: llega funcionando justo cuando el hospital se inaugura.

**Primicia potencial**: primer programa nacional de tamizaje de cáncer oral asistido por IA en una población de consumo de mate — un correlato epidemiológico que no existe en ningún otro lugar del mundo. El eje "mate muy caliente + lesión térmica + detección temprana" es un ángulo de investigación publicable por sí mismo y culturalmente específico de esta región.

---

## §12 — Por qué score 74.5 y no más alto

Desglose: A=7 (carga menor que caries/TB pero con mortalidad alta y evitable), B=8 (blueprint DiagnOCe + 13,500 imágenes públicas), C=8 (<$15k POC), D=7 (4 meses a validación), E=7 (riesgo de campo medio), F=8 (primicia regional con ángulo mate), G=7 (replicable a lesiones de mucosa en general).

No es S-tier porque: (a) la incidencia de cáncer oral es un orden de magnitud menor que la prevalencia de caries — el número absoluto de vidas por año es menor que el de caries/TB; (b) el PPV esperable de cualquier tamizaje de cáncer poco prevalente es bajo y exige un circuito de confirmación sólido (ese es el verdadero costo organizacional); (c) depende de champion clínico (FOUNA) para el circuito de biopsia — sin él, el tamizaje no cierra el ciclo.

**Pero es el proyecto con la mejor relación mortalidad-evitable / costo de todo el catálogo odontológico**: cada caso detectado en fase localizada es una vida con ~86% de supervivencia en vez de ~40%, y el proyecto completo cuesta menos de $50k.

---

## Fuentes principales

- DiagnOCe app study — J Indian Acad Oral Med Radiol 2025 (AUC 0.867, kappa 0.88)
- Smartphone imaging oral cancer review (23 estudios 2015-2024) — researcher.life discovery
- Rural/low-resource screening systematic review (40 estudios, 136,257 participantes) — U. Saskatchewan
- Dataset Egipto 9,201 imágenes — Ayman et al., Br Dent J 2025 + Zenodo 14571990
- Dataset Sri Lanka 3,000 imágenes — Oral Oncology 2024;106946 + Zenodo 10664056
- HuggingFace oral mucosal 1,348 imágenes — HRruiH
- OPMD prevalencia global 4.67% / Sudamérica ~5.4% — J Oral Pathol Med 2025 (jop.70146)
- Leucoplasia global 3.41%, transformación maligna 3.5-9.8% — BMC Oral Health 2023
- Supervivencia 86.3% vs 40.4% — Frontiers Oral Health 2026 (SEER)
- Mate muy caliente + cáncer esofágico/oral — Rolón/Castellsagué et al. IJC 2000 (830 casos/1,779 controles, incluye Paraguay); Rev Panam Salud Publica 2009;25(6)
- IARC bebidas muy calientes grupo 2A — IARC Monographs
- ESCCAPE thermal index — IARC 2024
- Burden oral cancer GBD 2021 — PMC11775039

## Última actualización

Septiembre 2026.