# mcdi500\_s1\_grupo6

\# MCDI500 - Grupo 6



\## Proyecto



Proyecto de Ciencia de Datos desarrollado para la asignatura MCDI500, orientado al análisis del impacto de la Inteligencia Artificial en el empleo, la productividad y la capacitación laboral mediante técnicas de procesamiento, análisis de datos y diseño algorítmico en Python.

Integrantes



\## Integrantes



\- Pablo Rodriguez

\- Luiskar Espinoza





\## Herramientas



\- Python

\- JupyterLab

\- Git

\- GitHub

\- Pandas

\- NumPy


\- Matplotlib

\- Seaborn


\## Estructura


mcdi500_s1_grupo6/
├── data/
│   ├── raw/
│   └── processed/
├── F3/
│   ├── notebooks/
│   ├── src/
│   └── results/
├── F4/
│   ├── notebooks/
│   ├── src/
│   └── results/
├── docs/
├── requirements.txt
└── README.md

## Fase 2 - Pipeline de datos

La Fase 2 desarrolla el proceso de obtención, exploración, limpieza, transformación y validación del dataset AI Job Impact, preparando una versión consistente para las etapas posteriores del proyecto.

### Notebook principal

El notebook de esta fase se encuentra en:

```text
notebooks/F2_pipeline_datos.ipynb
```

## Fase 3 - Algoritmos y medición de complejidad

La Fase 3 implementa algoritmos estructurados y recursivos en Python sobre el conjunto de datos AI Job Impact, incorporando principios de programación orientada a objetos, mediciones de complejidad temporal y análisis comparativos de desempeño.

## Fase 4 - Visualización, validación y comunicación de resultados

La Fase 4 consolida el cierre integrador del proyecto mediante la construcción de visualizaciones analíticas, validación técnica del dataset, documentación arquitectónica y comunicación de hallazgos relevantes sobre el impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral.


### Notebook principal

El notebook de esta fase se encuentra en:

```text
F4/notebooks/F4_visualizacion_validacion_cierre.ipynb
```

### Contenido desarrollado

- Validación estructural del dataset limpio generado en la Fase 2.
- Construcción de visualizaciones analíticas utilizando Matplotlib y Seaborn.
- Generación de boxplots, histogramas, gráficos de barras, gráficos de dispersión y gráficos tipo violin.
- Análisis de correlaciones entre variables laborales relevantes.
- Exportación automática de figuras en formato PNG.
- Generación de métricas de validación técnica y reporte integrado.
- Documentación arquitectónica y trazabilidad metodológica entre las distintas fases del proyecto.
- Elaboración de un resumen de hallazgos para apoyar la interpretación de resultados y fortalecer el storytelling del análisis.
### Notebook principal

El notebook de esta fase se encuentra en:

```text
notebooks/F3_algoritmos_complejidad.ipynb
```

### Contenido desarrollado

- Carga del dataset y exploración inicial de la información.
- Limpieza básica y transformación de columnas numéricas.
- Validación posterior al procesamiento de los datos.
- Implementación del algoritmo estructurado insertion_sort.
- Implementación del algoritmo recursivo merge_sort.
- Implementación de la función auxiliar combinar_listas.
- Comparación de desempeño con la función optimizada sorted() de Python.
- Medición de tiempos de ejecución mediante timeit.
- Implementación de la clase PreprocesadorAIJob para encapsular el procesamiento del dataset.
- Implementación de la clase PreprocesadorAIJobAvanzado, utilizando herencia y sobrescritura de métodos para demostrar polimorfismo.
- Obtención de estadísticas descriptivas y filtrado de información mediante programación orientada a objetos.
- Generación de un gráfico tipo boxplot para analizar la distribución de salarios.
- Generación de un gráfico comparativo de tiempos de ejecución entre insertion_sort, merge_sort y sorted().
- Documentación técnica y análisis básico de eficiencia algorítmica.
- Dependencias principales

### Dependencias principales

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- JupyterLab
- timeit
- pathlib

## Resumen del proyecto

El proyecto integra técnicas de ciencia de datos desarrolladas progresivamente a lo largo de cuatro fases. Inicialmente se definió la problemática y la estructura reproducible del trabajo, posteriormente se realizó el procesamiento y validación del conjunto de datos, se implementaron algoritmos estructurados y recursivos junto con principios de programación orientada a objetos y mediciones de complejidad, y finalmente se desarrollaron visualizaciones y documentación técnica que permiten comunicar los principales hallazgos de manera clara y reproducible.

El resultado es un proyecto modular, documentado y versionado mediante Git y GitHub, orientado al análisis del impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral.