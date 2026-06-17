"""
MCDI500
Proyecto: AI Job Impact

Módulo de algoritmos y clases auxiliares
utilizados en la Fase 3.
"""

import pandas as pd


def insertion_sort(lista):
    """
    Ordena una lista utilizando el algoritmo
    Insertion Sort.

    Parámetros
    ----------
    lista : list

    Retorna
    -------
    list
        Lista ordenada.
    """

    lista = lista.copy()

    for i in range(1, len(lista)):

        clave = lista[i]

        j = i - 1

        while j >= 0 and lista[j] > clave:

            lista[j + 1] = lista[j]

            j -= 1

        lista[j + 1] = clave

    return lista


def combinar_listas(izquierda, derecha):
    """
    Combina dos listas ordenadas en una
    única lista ordenada.
    """

    resultado = []

    i = 0
    j = 0

    while (
        i < len(izquierda)
        and j < len(derecha)
    ):

        if izquierda[i] <= derecha[j]:

            resultado.append(
                izquierda[i]
            )

            i += 1

        else:

            resultado.append(
                derecha[j]
            )

            j += 1

    resultado.extend(
        izquierda[i:]
    )

    resultado.extend(
        derecha[j:]
    )

    return resultado


def merge_sort(lista):
    """
    Implementación recursiva del algoritmo
    Merge Sort.
    """

    if len(lista) <= 1:

        return lista

    mitad = len(lista) // 2

    izquierda = merge_sort(
        lista[:mitad]
    )

    derecha = merge_sort(
        lista[mitad:]
    )

    return combinar_listas(
        izquierda,
        derecha
    )

class PreprocesadorAIJob:
    """
    Clase encargada de administrar el dataset
    AI Job Impact.
    """

    def __init__(self, ruta_csv):

        self._ruta = ruta_csv

        self._df = None

    @property
    def ruta(self):
        """
        Devuelve la ruta del dataset.
        """

        return self._ruta

    @property
    def df(self):
        """
        Devuelve el DataFrame cargado.
        """

        return self._df

    def cargar(self):
        """
        Carga el dataset desde un archivo CSV.
        """

        self._df = pd.read_csv(
            self._ruta
        )
        self._df.columns = (
            self._df.columns
            .str.lower()
        )

        print(
            f"Dataset cargado correctamente: "
            f"{self._df.shape[0]} filas y "
            f"{self._df.shape[1]} columnas."
        )

        return self._df

    def explorar(self):
        """
        Muestra información general.
        """

        print("\nPrimeros registros:")

        print(
            self._df.head()
        )

        print("\nInformación:")

        print(
            self._df.info()
        )

        print("\nValores nulos:")

        print(
            self._df.isnull().sum()
        )

    def limpiar(self):
        """
        Elimina registros con valores nulos.
        """

        antes = len(self._df)

        self._df = (
            self._df.dropna()
        )

        despues = len(
            self._df
        )

        print(
            f"Se eliminaron "
            f"{antes - despues} registros."
        )

        return self._df

    def transformar(self):
     """
     Realiza una transformación básica
     sobre columnas numéricas.
     """

     columnas_numericas = [
        "salary_before_ai",
        "salary_after_ai",
        "age",
        "years_experience",
        "work_hours_per_week",
        "job_satisfaction"
     ]

     for columna in columnas_numericas:

        if columna in self._df.columns:

            self._df[columna] = (
                pd.to_numeric(
                    self._df[columna],
                    errors="coerce"
                )
            )


     self._df = self._df.dropna()

     return self._df

    def validar(self):
        """
        Comprueba la existencia
        de valores nulos.
        """

        nulos = (
            self._df
            .isnull()
            .sum()
            .sum()
        )

        if nulos == 0:

            print(
                "Validación correcta."
            )

        else:

            print(
                f"Existen {nulos} valores nulos."
            )

        return nulos == 0

    def obtener_salarios(self):
        """
        Devuelve salary_after_ai.
        """

        return (
            self._df[
                "salary_after_ai"
            ]
            .tolist()
        )

    def resumen(self):
        """
        Devuelve estadísticas descriptivas.
        """

        return (
            self._df.describe()
        )

class PreprocesadorAIJobAvanzado(PreprocesadorAIJob):
    """
    Clase que hereda de PreprocesadorAIJob e incorpora
    funcionalidades adicionales para el análisis del
    dataset AI Job Impact.
    """

    def __init__(self, ruta_csv):

        super().__init__(ruta_csv)

    def resumen(self):
        """
        Sobrescribe el método resumen de la clase base
        para demostrar polimorfismo.
        """

        print("\n=== Resumen avanzado del dataset ===\n")

        return super().resumen()

    def promedio_salario(self):
        """
        Calcula el salario promedio después de la IA.
        """

        return self._df["salary_after_ai"].mean()

    def salario_maximo(self):
        """
        Obtiene el salario máximo.
        """

        return self._df["salary_after_ai"].max()

    def salario_minimo(self):
        """
        Obtiene el salario mínimo.
        """

        return self._df["salary_after_ai"].min()

    def filtrar_por_riesgo(self, riesgo):
        """
        Filtra registros según el nivel
        de riesgo de automatización.
        """

        return self._df[
            self._df["automation_risk"] == riesgo
        ]

    def filtrar_por_industria(self, industria):
        """
        Filtra registros según la industria.
        """

        return self._df[
            self._df["industry"] == industria
        ]