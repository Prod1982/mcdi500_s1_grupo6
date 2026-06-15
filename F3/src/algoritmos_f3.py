"""
MCDI500
Proyecto: AI Job Impact

Clase orientada a objetos para encapsular
el preprocesamiento del dataset.
"""

from pathlib import Path

import pandas as pd


class PreprocesadorAIJob:
    """
    Clase encargada de administrar el dataset
    del proyecto AI Job Impact.
    """

    def __init__(self, ruta_csv):

        self.ruta = ruta_csv

        self.df = None

    def cargar(self):

        """
        Carga el dataset desde un archivo CSV.
        """

        self.df = pd.read_csv(self.ruta)

        print(
            f"Dataset cargado correctamente: "
            f"{self.df.shape[0]} filas y "
            f"{self.df.shape[1]} columnas."
        )

        return self.df

    def explorar(self):

        """
        Muestra información general.
        """

        print("\nPrimeros registros:")

        print(self.df.head())

        print("\nInformación:")

        print(self.df.info())

        print("\nValores nulos:")

        print(self.df.isnull().sum())

    def limpiar(self):

        """
        Elimina filas con valores nulos.
        """

        antes = len(self.df)

        self.df = self.df.dropna()

        despues = len(self.df)

        print(
            f"Se eliminaron "
            f"{antes - despues} registros con nulos."
        )

        return self.df

    def validar(self):

        """
        Comprueba que no existan valores nulos.
        """

        nulos = self.df.isnull().sum().sum()

        if nulos == 0:

            print("Validación correcta.")

        else:

            print(f"Existen {nulos} valores nulos.")

        return nulos == 0

    def obtener_salarios(self):

        """
        Devuelve la columna Salary_After_AI.
        """

        return self.df["Salary_After_AI"].tolist()

    def resumen(self):

        """
        Devuelve estadísticas descriptivas.
        """

        return self.df.describe()