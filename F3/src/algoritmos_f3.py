"""
Módulo de Programación Orientada a Objetos
Proyecto MCDI500 - Fase 3
"""

import timeit


class AIJobAnalyzer:
    """
    Clase encargada de encapsular operaciones de análisis
    sobre el dataset AI Job Impact.
    """

    def __init__(self, dataframe):
        """
        Constructor.

        Parametros
        ----------
        dataframe : pandas.DataFrame
            Dataset cargado.
        """

        self.dataframe = dataframe

    def obtener_salarios(self, cantidad=500):
        """
        Obtiene una lista de salarios.
        """

        return (
            self.dataframe["salary_after_ai"]
            .dropna()
            .head(cantidad)
            .tolist()
        )

    def promedio_salario(self):

        return self.dataframe["salary_after_ai"].mean()

    def salario_maximo(self):

        return self.dataframe["salary_after_ai"].max()

    def salario_minimo(self):

        return self.dataframe["salary_after_ai"].min()

    def cantidad_registros(self):

        return len(self.dataframe)

    def ordenar_python(self, cantidad=500):

        datos = self.obtener_salarios(cantidad)

        return sorted(datos)

    def medir_sorted(self, cantidad=500, repeticiones=5):

        datos = self.obtener_salarios(cantidad)

        tiempo = timeit.timeit(

            lambda: sorted(datos),

            number=repeticiones

        )

        return tiempo