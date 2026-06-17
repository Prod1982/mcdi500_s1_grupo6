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

La Fase 3 implementa algoritmos estructurados y recursivos en Python sobre el conjunto de datos AI Job Impact, incorporando principios de programación orientada a objetos, mediciones de complejidad temporal y análisis comparativos de desempeño.

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
- JupyterLab
- timeit
- pathlib