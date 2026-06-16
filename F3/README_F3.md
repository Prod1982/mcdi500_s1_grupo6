Fase 3 – Avance Semana 2
Impacto de la Inteligencia Artificial en el empleo, la productividad y la capacitación laboral

Este directorio contiene el avance correspondiente a la Fase 3 – Semana 2 del proyecto transversal de la asignatura MCDI500. El objetivo principal es implementar y evaluar algoritmos estructurados y recursivos en Python sobre el conjunto de datos procesado en la Fase 2, incorporando mediciones básicas de complejidad temporal, principios de programación orientada a objetos y criterios de eficiencia algorítmica.

1) Contenido
notebook_f3.ipynb (o el nombre real del notebook): notebook principal con el desarrollo del avance.
src/: scripts auxiliares y clases implementadas para el procesamiento y análisis del dataset.
results/: resultados y archivos generados durante las pruebas de complejidad temporal.

3) Funcionalidades implementadas
Carga del dataset procesado obtenido en la Fase 2.
Exploración, validación y limpieza básica de los datos.
Implementación del algoritmo estructurado insertion_sort.
Implementación del algoritmo recursivo merge_sort.
Comparación de desempeño con la función optimizada sorted() de Python.
Medición de tiempos de ejecución utilizando timeit.
Registro de resultados de complejidad en archivo de texto.
Implementación de la clase PreprocesadorAIJob para encapsular el preprocesamiento del dataset.
Implementación de la clase PreprocesadorAIJobAvanzado, utilizando herencia para incorporar funcionalidades adicionales de análisis.
Obtención de estadísticas descriptivas y filtrado de información mediante métodos orientados a objetos.
Generación de un gráfico tipo boxplot para comparar la distribución de los salarios antes y después de la adopción de inteligencia artificial.

4) Dependencias

El proyecto utiliza Python 3.x y las siguientes bibliotecas:

pandas
numpy
matplotlib
pathlib
timeit
tracemalloc

Las dependencias completas se encuentran disponibles en el archivo requirements.txt del repositorio.

4) Ejecución

Para ejecutar correctamente el proyecto se recomienda seguir los siguientes pasos:

Clonar el repositorio GitHub.
Instalar las dependencias especificadas en requirements.txt.
Abrir el notebook correspondiente mediante Jupyter Notebook o JupyterLab.
Ejecutar todas las celdas en orden secuencial para reproducir completamente el flujo de trabajo, las mediciones de complejidad y los resultados obtenidos.

5) Proyección

Como trabajo futuro, se contempla continuar fortaleciendo la modularidad del proyecto mediante la incorporación de nuevas clases y funcionalidades orientadas al análisis de datos, ampliar las métricas de evaluación de eficiencia algorítmica y mantener una arquitectura reproducible y escalable que facilite el desarrollo de las siguientes fases del proyecto.
