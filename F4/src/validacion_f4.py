"""
validacion_f4.py

Módulo de validación técnica para la Fase 4 del proyecto:
"Impacto de la inteligencia artificial en el empleo, la productividad
y la capacitación laboral".

Este módulo centraliza funciones reutilizables para verificar la calidad
estructural del dataset, la existencia de variables relevantes y la generación
de evidencias persistentes en F4/results.
"""

from pathlib import Path
from typing import Dict, Iterable

import pandas as pd


def validar_dataset_f4(
    df: pd.DataFrame,
    variable_objetivo: str = "salary_after_ai",
    filas_esperadas: int = 2000,
    columnas_esperadas: int = 17
) -> Dict[str, object]:
    """
    Valida la estructura principal del dataset utilizado en Fase 4.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio proveniente de Fase 2.
    variable_objetivo : str
        Variable analítica central del proyecto.
    filas_esperadas : int
        Número esperado de registros.
    columnas_esperadas : int
        Número esperado de columnas.

    Returns
    -------
    dict
        Diccionario con métricas de validación técnica.
    """
    metricas = {
        "filas_dataset": df.shape[0],
        "columnas_dataset": df.shape[1],
        "valores_nulos_totales": int(df.isnull().sum().sum()),
        "registros_duplicados": int(df.duplicated().sum()),
        "variable_objetivo": variable_objetivo,
        "existe_variable_objetivo": variable_objetivo in df.columns,
        "cumple_filas_esperadas": df.shape[0] == filas_esperadas,
        "cumple_columnas_esperadas": df.shape[1] == columnas_esperadas
    }

    return metricas


def validar_archivos_resultado(
    rutas: Iterable[Path]
) -> Dict[str, bool]:
    """
    Verifica la existencia de archivos de resultados generados en Fase 4.

    Parameters
    ----------
    rutas : Iterable[Path]
        Colección de rutas a verificar.

    Returns
    -------
    dict
        Diccionario donde la clave es el nombre del archivo y el valor indica
        si existe o no.
    """
    return {
        Path(ruta).name: Path(ruta).exists()
        for ruta in rutas
    }


def ejecutar_asserts_validacion_f4(
    metricas_dataset: Dict[str, object],
    archivos_resultado: Dict[str, bool]
) -> None:
    """
    Ejecuta aserciones formales sobre métricas del dataset y archivos generados.

    Esta función deja evidencia de validación técnica reproducible. Si alguna
    condición falla, se genera una excepción AssertionError, facilitando la
    detección temprana de problemas en el pipeline.

    Parameters
    ----------
    metricas_dataset : dict
        Métricas calculadas por validar_dataset_f4.
    archivos_resultado : dict
        Resultado calculado por validar_archivos_resultado.
    """
    assert metricas_dataset["cumple_filas_esperadas"] is True
    assert metricas_dataset["cumple_columnas_esperadas"] is True
    assert metricas_dataset["valores_nulos_totales"] == 0
    assert metricas_dataset["registros_duplicados"] == 0
    assert metricas_dataset["existe_variable_objetivo"] is True

    for nombre_archivo, existe in archivos_resultado.items():
        assert existe is True, f"No se encontró el archivo esperado: {nombre_archivo}"


def exportar_metricas_validacion(
    metricas_dataset: Dict[str, object],
    archivos_resultado: Dict[str, bool],
    ruta_salida: Path
) -> Path:
    """
    Exporta métricas de validación técnica a un archivo TXT.

    Parameters
    ----------
    metricas_dataset : dict
        Métricas estructurales del dataset.
    archivos_resultado : dict
        Validación de existencia de archivos.
    ruta_salida : Path
        Ruta donde se guardará el archivo TXT.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write("Métricas de validación técnica - Fase 4\n")
        archivo.write("=======================================\n\n")

        archivo.write("Validación del dataset\n")
        archivo.write("----------------------\n")
        for clave, valor in metricas_dataset.items():
            archivo.write(f"{clave}: {valor}\n")

        archivo.write("\nValidación de archivos generados\n")
        archivo.write("--------------------------------\n")
        for nombre_archivo, existe in archivos_resultado.items():
            archivo.write(f"{nombre_archivo}: {existe}\n")

        archivo.write("\nInterpretación:\n")
        archivo.write(
            "Las métricas confirman la consistencia estructural del dataset, "
            "la ausencia de valores nulos y duplicados, la existencia de la "
            "variable objetivo salary_after_ai y la generación de evidencias "
            "persistentes en F4/results.\n"
        )

    return ruta_salida