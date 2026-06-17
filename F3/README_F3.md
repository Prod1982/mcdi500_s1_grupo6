Fase 3 – Avance Semana 2
Impacto de la Inteligencia Artificial en el empleo, la productividad y la capacitación laboral

Este directorio contiene el avance correspondiente a la Fase 3 – Semana 2 del proyecto transversal de la asignatura MCDI500. El objetivo principal es implementar y evaluar algoritmos estructurados y recursivos en Python sobre el conjunto de datos AI Job Impact, incorporando mediciones de complejidad temporal, principios de programación orientada a objetos y criterios básicos de eficiencia algorítmica.

1. Contenido
notebook_f3.ipynb (o el nombre correspondiente): notebook principal con el desarrollo de la Fase 3.
src/: módulo algoritmos_f3.py que contiene los algoritmos implementados y las clases orientadas a objetos utilizadas durante el desarrollo.
results/: archivos generados durante las mediciones de complejidad temporal y resultados obtenidos.
2. Funcionalidades implementadas
Carga del dataset AI Job Impact desde el archivo de datos de entrada.
Exploración inicial del conjunto de datos.
Limpieza básica mediante eliminación de registros con valores nulos.
Transformación de columnas numéricas utilizando pandas.to_numeric().
Validación posterior al proceso de limpieza y transformación.
Implementación del algoritmo estructurado insertion_sort.
Implementación del algoritmo recursivo merge_sort.
Implementación de la función auxiliar combinar_listas.
Comparación de desempeño con la función optimizada sorted() de Python.
Medición de tiempos de ejecución utilizando timeit.
Registro de resultados de complejidad temporal en archivo de texto.
Implementación de la clase PreprocesadorAIJob para encapsular el procesamiento del dataset.
Implementación de la clase PreprocesadorAIJobAvanzado, aplicando herencia y sobrescritura de métodos para demostrar polimorfismo.
Obtención de estadísticas descriptivas, cálculo de indicadores y filtrado de información mediante programación orientada a objetos.
Generación de un gráfico boxplot para visualizar la distribución de salarios.
Generación de un gráfico comparativo de tiempos de ejecución entre insertion_sort, merge_sort y sorted().
3. Dependencias

El proyecto utiliza Python 3.x y las siguientes bibliotecas principales:

pandas
numpy
matplotlib
pathlib
timeit
tracemalloc

Las dependencias completas se encuentran especificadas en el archivo requirements.txt del repositorio.

4. Ejecución

Para ejecutar correctamente el proyecto se recomienda seguir los siguientes pasos:

Clonar el repositorio GitHub.
Instalar las dependencias especificadas en requirements.txt.
Abrir el notebook correspondiente utilizando Jupyter Notebook o JupyterLab.
Ejecutar las celdas en orden secuencial para reproducir completamente el flujo de trabajo, las transformaciones realizadas, las mediciones de complejidad temporal y los resultados obtenidos.

5. Proyección

Como trabajo futuro se contempla ampliar las funcionalidades orientadas al análisis de datos mediante nuevas clases y métodos, incorporar mediciones adicionales de eficiencia temporal y espacial sobre distintos tamaños de entrada, fortalecer la modularidad del proyecto y mantener una arquitectura reproducible y escalable para las siguientes fases del desarrollo.