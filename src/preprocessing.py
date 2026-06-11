"""
Módulo de preprocesamiento para la Fase 2 del proyecto MCDI500.

Contiene funciones para cargar, explorar, limpiar, transformar,
validar y exportar el dataset AI Job Impact.
"""

from pathlib import Path
import pandas as pd


def cargar_datos(ruta_archivo):
    """
    Carga un archivo CSV y retorna un DataFrame.
    """
    ruta = Path(ruta_archivo)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    return pd.read_csv(ruta)


def explorar_datos(df):
    """
    Genera un resumen inicial del dataset.
    """
    resumen = {
        "filas": df.shape[0],
        "columnas": df.shape[1],
        "duplicados": int(df.duplicated().sum()),
        "valores_nulos_totales": int(df.isna().sum().sum())
    }

    return resumen


def normalizar_columnas(df):
    """
    Normaliza los nombres de columnas:
    minúsculas, sin espacios y con guion bajo.
    """
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def limpiar_datos(df):
    """
    Limpia el dataset eliminando duplicados y normalizando columnas.
    """
    df = df.copy()
    df = normalizar_columnas(df)
    df = df.drop_duplicates()
    return df


def transformar_datos(df):
    """
    Aplica transformaciones básicas al dataset.
    """
    df = df.copy()

    for columna in df.columns:
        if df[columna].dtype == "object":
            df[columna] = df[columna].astype(str).str.strip()

    return df


def validar_datos(df):
    """
    Valida condiciones básicas del dataset procesado.
    """
    validaciones = {
        "dataset_no_vacio": not df.empty,
        "duplicados": int(df.duplicated().sum()),
        "valores_nulos_totales": int(df.isna().sum().sum()),
        "filas": df.shape[0],
        "columnas": df.shape[1]
    }

    if df.empty:
        raise ValueError("El dataset está vacío.")

    return validaciones


def exportar_resultados(df, ruta_salida):
    """
    Exporta el DataFrame procesado a un archivo CSV.
    """
    ruta = Path(ruta_salida)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(ruta, index=False)
    return ruta