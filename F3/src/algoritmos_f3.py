"""
MCDI500
Proyecto: AI Job Impact

Clase orientada a objetos para encapsular
el preprocesamiento del dataset.
"""

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
        Muestra información general del dataset.
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
        Devuelve la columna salary_after_ai.
        """

        return self.df["salary_after_ai"].tolist()

    def resumen(self):
        """
        Devuelve estadísticas descriptivas.
        """

        return self.df.describe()


class PreprocesadorAIJobAvanzado(PreprocesadorAIJob):
    """
    Clase que hereda de PreprocesadorAIJob e incorpora
    funcionalidades adicionales para el análisis del
    dataset AI Job Impact.
    """

    def __init__(self, ruta_csv):
        super().__init__(ruta_csv)

    def promedio_salario(self):
        """
        Calcula el salario promedio después de la adopción de IA.
        """

        return self.df["salary_after_ai"].mean()

    def salario_maximo(self):
        """
        Obtiene el salario máximo después de la adopción de IA.
        """

        return self.df["salary_after_ai"].max()

    def salario_minimo(self):
        """
        Obtiene el salario mínimo después de la adopción de IA.
        """

        return self.df["salary_after_ai"].min()

    def filtrar_por_riesgo(self, riesgo):
        """
        Filtra los registros según el nivel de riesgo de automatización.
        """

        return self.df[
            self.df["automation_risk"] == riesgo
        ]

    def filtrar_por_industria(self, industria):
        """
        Filtra los registros según la industria.
        """

        return self.df[
            self.df["industry"] == industria
        ]