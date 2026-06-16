# mcdi500\_s1\_grupo6

\# MCDI500 - Grupo 6



\## Proyecto



Proyecto de Ciencia de Datos desarrollado para la asignatura MCDI500, , orientado al análisis del impacto de la Inteligencia Artificial en el empleo, la productividad y la capacitación laboral mediante técnicas de procesamiento y análisis de datos en Python.

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


\## Estructura



\- data

\- notebooks

\- docs

\- results

## Fase 2 - Pipeline de datos

La Fase 2 desarrolla el proceso de obtención, exploración, limpieza, transformación y validación del dataset AI Job Impact, preparando una versión consistente para las etapas posteriores del proyecto.

### Notebook principal

El notebook de esta fase se encuentra en:

```text
notebooks/F2_pipeline_datos.ipynb
```

## Fase 3 - Algoritmos y medición de complejidad

La Fase 3 implementa algoritmos estructurados y recursivos sobre el dataset procesado en la Fase 2, incorporando mediciones básicas de complejidad temporal, principios de programación orientada a objetos y herramientas de análisis exploratorio.

### Notebook principal

El notebook de esta fase se encuentra en:

```text
notebooks/F3_algoritmos_complejidad.ipynb
```

### Contenido desarrollado

- Implementación del algoritmo estructurado insertion_sort.
- Implementación del algoritmo recursivo merge_sort.
- Comparación de desempeño con la función optimizada sorted() de Python.
- Medición de tiempos de ejecución mediante timeit.
- Implementación de la clase PreprocesadorAIJob para encapsular el preprocesamiento del dataset.
- Implementación de la clase PreprocesadorAIJobAvanzado utilizando herencia para ampliar las funcionalidades de análisis.
- Validación, limpieza y exploración de los datos mediante métodos orientados a objetos.
- Generación de un gráfico tipo boxplot para comparar la distribución de los salarios antes y después de la adopción de inteligencia artificial.
- Documentación técnica y análisis básico de eficiencia algorítmica.

### Dependencias principales

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- JupyterLab
- timeit
- pathlib