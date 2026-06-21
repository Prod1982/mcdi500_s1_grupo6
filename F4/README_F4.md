# Fase 4 — Visualización, validación y comunicación de resultados

## Proyecto

**Impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral**

Curso: **MCD1500 — Programación para la Ciencia de Datos**  
Institución: **Universidad Andrés Bello (UNAB)**  
Docente: **Dr. Omar Salinas Silva**

---

## Objetivo de la Fase 4

La Fase 4 corresponde al cierre integrador del proyecto. Su propósito es consolidar los avances desarrollados en las fases anteriores, validar técnicamente el flujo de trabajo, construir visualizaciones analíticas y comunicar hallazgos relevantes de manera clara, reproducible y profesional.

Esta fase integra:

- el dataset limpio generado en Fase 2;
- el núcleo algorítmico desarrollado en Fase 3;
- la arquitectura modular y orientada a objetos;
- las mediciones de eficiencia temporal;
- las visualizaciones y evidencias finales de comunicación de resultados.

---

## Dataset utilizado

El dataset base utilizado corresponde al archivo limpio generado durante la Fase 2:

```text
data/processed/ai_job_impact_clean.csv

F4/
├── notebooks/
│   └── F4_visualizacion_validacion_cierre.ipynb
│
├── src/
│   ├── visualizaciones_f4.py
│   ├── validacion_f4.py
│   └── documentacion_f4.py
│
├── results/
│   ├── figura_1_salario_por_adopcion_ia.png
│   ├── figura_2_productividad_por_riesgo.png
│   ├── figura_3_correlaciones_laborales.png
│   ├── resumen_hallazgos_f4.txt
│   ├── metricas_validacion_f4.txt
│   └── documentacion_arquitectura_f4.txt
│
└── README_F4.md

## Descripción de la estructura de la Fase 4

La estructura de la Fase 4 fue organizada para separar claramente el notebook ejecutable, los módulos de apoyo, los resultados generados y la documentación técnica de cierre. Esta organización permite mantener trazabilidad entre el código desarrollado, las visualizaciones producidas y los archivos utilizados como evidencia en el informe final del proyecto.

La carpeta `notebooks` contiene el archivo principal de trabajo de la fase: `F4_visualizacion_validacion_cierre.ipynb`. Este notebook integra la carga del dataset limpio, la validación técnica inicial, la construcción de visualizaciones analíticas, la interpretación de hallazgos y la exportación de resultados. Su función principal es actuar como evidencia ejecutable y reproducible del cierre técnico del proyecto.

La carpeta `src` está destinada a almacenar módulos reutilizables de apoyo. En esta fase se consideran tres archivos principales: `visualizaciones_f4.py`, `validacion_f4.py` y `documentacion_f4.py`. Aunque el desarrollo inicial se realiza desde el notebook, esta carpeta permite proyectar una arquitectura más modular, donde las funciones de visualización, validación y documentación puedan trasladarse progresivamente a scripts independientes, facilitando mantenimiento y reutilización.

La carpeta `results` almacena todos los productos generados durante la Fase 4. En ella se guardan las figuras exportadas en formato PNG, el resumen de hallazgos, las métricas de validación y la documentación arquitectónica. Esta separación permite conservar evidencia persistente del análisis y facilita la incorporación de estos resultados al informe técnico final y a la presentación profesional.

El archivo `README_F4.md` documenta el propósito de la fase, la estructura de carpetas, los archivos generados, la relación con las fases anteriores y las buenas prácticas aplicadas. Su objetivo es facilitar la comprensión del avance, apoyar la reproducibilidad del trabajo y servir como referencia para otros integrantes del equipo o evaluadores.

## Flujo de trabajo de la Fase 4

El flujo de trabajo seguido en esta fase se resume de la siguiente manera:

```text
Dataset limpio de Fase 2
        ↓
Carga en notebook F4
        ↓
Validación técnica del dataset
        ↓
Construcción de visualizaciones analíticas
        ↓
Exportación de figuras y archivos TXT
        ↓
Documentación arquitectónica
        ↓
Comunicación de hallazgos para informe y presentación final

## Visualizaciones generadas

Durante la Fase 4 se generaron siete visualizaciones principales orientadas a comunicar hallazgos relevantes sobre salario, productividad, adopción de inteligencia artificial y riesgo de automatización.

Estas visualizaciones permiten transformar los resultados técnicos en evidencia interpretable para el informe final y la presentación profesional del proyecto. Cada figura responde a una pregunta analítica específica y queda almacenada como archivo PNG dentro de la carpeta `F4/results`.

Adicionalmente, se incorporó una visualización desarrollada con la biblioteca Seaborn para enriquecer el análisis exploratorio y fortalecer la comunicación de los resultados mediante una representación más detallada de la distribución de los datos.

### Figura 1 — Salario posterior a IA según nivel de adopción

**Archivo:** `F4/results/figura_1_salario_por_adopcion_ia.png`

**Propósito:** comparar la distribución del salario posterior a la adopción de inteligencia artificial según el nivel de adopción de IA. Esta visualización permite observar diferencias en mediana, dispersión y posibles valores atípicos entre categorías de adopción tecnológica.

---

### Figura 2 — Cambio de productividad según riesgo de automatización

**Archivo:** `F4/results/figura_2_productividad_por_riesgo.png`

**Propósito:** explorar si los distintos niveles de riesgo de automatización presentan diferencias en el cambio de productividad reportado. Esta figura permite vincular el riesgo tecnológico con posibles variaciones en el desempeño laboral.

---

### Figura 3 — Correlaciones entre variables laborales numéricas

**Archivo:** `F4/results/figura_3_correlaciones_laborales.png`

**Propósito:** identificar asociaciones lineales entre variables como edad, experiencia, salario antes de IA, salario después de IA, horas de trabajo, satisfacción laboral y cambio de productividad. Esta visualización permite detectar relaciones relevantes entre variables laborales numéricas.

---

### Figura 4 — Distribución del salario posterior a IA

**Archivo:** `F4/results/figura_4_distribucion_salario_after_ai.png`

**Propósito:** analizar la distribución general de la variable `salary_after_ai`, identificando concentración, dispersión y posibles asimetrías en el salario posterior a la adopción de inteligencia artificial. Esta figura entrega una visión general antes de comparar grupos específicos.

---

### Figura 5 — Salario promedio posterior a IA por nivel de adopción

**Archivo:** `F4/results/figura_5_promedio_salario_por_adopcion.png`

**Propósito:** comparar de forma agregada el salario promedio posterior a IA entre los distintos niveles de adopción tecnológica. Esta visualización facilita una lectura directa de diferencias entre grupos y fortalece la comunicación de resultados.

---

### Figura 6 — Salario antes vs. después de IA según riesgo de automatización

**Archivo:** `F4/results/figura_6_salario_antes_vs_despues_por_riesgo.png`

**Propósito:** explorar la relación entre salario antes de IA y salario posterior a IA, incorporando el riesgo de automatización como dimensión interpretativa. Esta figura permite observar si existe una relación visual entre ambas variables salariales y si los niveles de riesgo muestran patrones diferenciados.

---

### Figura 7 — Distribución del salario posterior a IA por nivel de adopción mediante gráfico tipo violin (Seaborn)

**Archivo:** `F4/results/figura_7_violin_salario_por_adopcion.png`

**Propósito:** representar la distribución completa del salario posterior a la adopción de inteligencia artificial para cada nivel de adopción utilizando un gráfico tipo *violin plot* implementado con la biblioteca Seaborn. Esta visualización permite apreciar simultáneamente la densidad, dispersión y tendencia central de los datos, complementando el análisis realizado mediante boxplots tradicionales y fortaleciendo la interpretación de los resultados.

---

## Evidencias generadas

Durante esta fase se generaron las siguientes evidencias:

| Archivo | Ubicación | Propósito |
|---|---|---|
| `F4_visualizacion_validacion_cierre.ipynb` | `F4/notebooks/` | Notebook ejecutable de validación, visualización y cierre. |
| `figura_1_salario_por_adopcion_ia.png` | `F4/results/` | Comparar salario posterior a IA según nivel de adopción. |
| `figura_2_productividad_por_riesgo.png` | `F4/results/` | Analizar cambio de productividad según riesgo de automatización. |
| `figura_3_correlaciones_laborales.png` | `F4/results/` | Visualizar correlaciones entre variables laborales numéricas. |
| `figura_4_distribucion_salario_after_ai.png` | `F4/results/` | Analizar la distribución general del salario posterior a IA. |
| `figura_5_promedio_salario_por_adopcion.png` | `F4/results/` | Comparar salario promedio posterior a IA por nivel de adopción. |
| `figura_6_salario_antes_vs_despues_por_riesgo.png` | `F4/results/` | Explorar la relación entre salario antes y después de IA según riesgo de automatización. |
| `figura_7_violin_salario_por_adopcion.png` | `F4/results/` | Visualizar la distribución completa del salario posterior a IA por nivel de adopción mediante un gráfico tipo violin implementado con Seaborn. |
| `resumen_hallazgos_f4.txt` | `F4/results/` | Registrar interpretación preliminar de los principales hallazgos. |
| `metricas_validacion_f4.txt` | `F4/results/` | Registrar métricas técnicas de validación del dataset y resultados. |
| `documentacion_arquitectura_f4.txt` | `F4/results/` | Documentar entradas, proceso, salidas y trazabilidad de la fase. |
| `trazabilidad_fases_f4.txt` | `F4/results/` | Registrar la evolución metodológica y técnica desde Fase 1 hasta Fase 4. |
| `reporte_integrado_f4.txt` | `F4/results/` | Consolidar métricas, evidencias y síntesis metodológica del cierre de Fase 4. |

Estos archivos permiten mantener trazabilidad entre el notebook, las visualizaciones, las métricas técnicas, la documentación arquitectónica y la comunicación de hallazgos.

---

## Validación técnica

La validación técnica de Fase 4 incluye:

- verificación de dimensiones del dataset;
- confirmación de ausencia de valores nulos;
- confirmación de ausencia de registros duplicados;
- validación de existencia de la variable `salary_after_ai`;
- comprobación de generación de visualizaciones;
- exportación de métricas a `metricas_validacion_f4.txt`;
- verificación de archivos documentales y visuales generados en `F4/results`.

El archivo asociado a esta validación es `F4/results/metricas_validacion_f4.txt`.

Esta evidencia permite comprobar que el dataset utilizado mantiene consistencia estructural y que los productos principales de la fase fueron generados correctamente.

---

## Documentación arquitectónica

La documentación arquitectónica se registra en `F4/results/documentacion_arquitectura_f4.txt`.

Esta documentación describe:

- objetivo de la fase;
- entradas del pipeline;
- proceso desarrollado;
- salidas generadas;
- relación entre Fase 2, Fase 3 y Fase 4;
- criterios de trazabilidad;
- buenas prácticas aplicadas.

La documentación arquitectónica permite explicar cómo se conectan los componentes del repositorio y cómo se mantiene la reproducibilidad del análisis.

---

## Trazabilidad metodológica F1-F4

La Fase 4 incorpora una evidencia específica de trazabilidad metodológica mediante el archivo `F4/results/trazabilidad_fases_f4.txt`.

Este archivo resume la evolución técnica del proyecto desde la Fase 1 hasta la Fase 4, identificando los principales avances, evidencias y mejoras aplicadas en cada etapa.

| Fase | Avance técnico | Evidencia | Mejora aplicada |
|---|---|---|---|
| Fase 1 | Definición del problema, objetivos y estructura inicial | `F1_Definicion.ipynb` | Organización inicial del proyecto y documentación reproducible |
| Fase 2 | Limpieza, transformación y validación del dataset | `data/processed/ai_job_impact_clean.csv` | Dataset limpio sin nulos ni duplicados |
| Fase 3 | Algoritmos, complejidad temporal, POO y patrones de diseño | `F3/src/algoritmos_f3.py` | Modularización, Strategy/Factory, polimorfismo y medición de eficiencia |
| Fase 4 | Visualización, validación final y comunicación de resultados | `F4/notebooks/F4_visualizacion_validacion_cierre.ipynb` | Narrativa de datos, visualizaciones exportables y documentación arquitectónica |

---

## Reporte integrado de cierre

Además de las visualizaciones y archivos de validación, se generó un reporte integrado de cierre: `F4/results/reporte_integrado_f4.txt`.

Este reporte consolida métricas del dataset, validación de evidencias generadas y una síntesis metodológica de la Fase 4. Su función es servir como evidencia final de que el pipeline produce resultados verificables, documentados y reproducibles.

---

## Relación con fases anteriores

Fase 1 → Definición del problema y reproducibilidad inicial.  
Fase 2 → Limpieza, transformación y validación del dataset.  
Fase 3 → Algoritmos, complejidad temporal, POO y arquitectura modular.  
Fase 4 → Visualización, validación final, documentación y comunicación de resultados.

La Fase 4 no reemplaza el trabajo anterior, sino que lo integra y lo comunica. El dataset limpio proviene de Fase 2, el núcleo algorítmico y modular proviene de Fase 3, y las visualizaciones y documentos finales permiten cerrar el proyecto con evidencia técnica verificable.

---

## Buenas prácticas aplicadas

- Uso de rutas reproducibles mediante `pathlib`.
- Separación de carpetas por fase.
- Uso de notebook ejecutable.
- Exportación persistente de resultados.
- Validaciones con `assert`.
- Documentación narrativa en Markdown.
- Modularización progresiva en `F4/src`.
- Control de versiones mediante Git y GitHub.
- Trazabilidad entre código, resultados e informe final.

---

## Ejecución recomendada

Desde la raíz del repositorio:

`cd /c/Users/LuiskarEspinoza/Documents/Proyectos/mi_app/mcdi500_s1_grupo6`

Luego ejecutar:

`jupyter lab`

Abrir el notebook:

`F4/notebooks/F4_visualizacion_validacion_cierre.ipynb`

Ejecutar todas las celdas en orden.

---

## Estado de avance

La Fase 4 cuenta actualmente con:

- estructura de carpetas creada;
- notebook ejecutable;
- siete visualizaciones generadas, incluyendo una visualización adicional desarrollada con Seaborn;
- resumen de hallazgos;
- métricas de validación técnica;
- documentación arquitectónica;
- trazabilidad metodológica F1-F4;
- reporte integrado de cierre;
- módulos reutilizables en `F4/src`;
- control de versiones mediante GitHub.

---

## Conclusión

La Fase 4 consolida el cierre técnico del proyecto mediante visualizaciones, validación, documentación reproducible y comunicación de hallazgos. La incorporación de una visualización adicional desarrollada con Seaborn fortalece el análisis exploratorio y el storytelling del proyecto, permitiendo representar con mayor detalle la distribución de los salarios posteriores a la adopción de inteligencia artificial. En conjunto, esta etapa integra los resultados obtenidos en las fases anteriores y entrega evidencia técnica clara, verificable y reproducible sobre el impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral. Esta etapa permite vincular los resultados técnicos con la problemática central del proyecto: el impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral.
