"""
visualizaciones_f4.py

Módulo de visualizaciones analíticas para la Fase 4 del proyecto:
"Impacto de la inteligencia artificial en el empleo, la productividad
y la capacitación laboral".

Este archivo centraliza funciones reutilizables para generar gráficos
interpretables y exportarlos como evidencia reproducible en F4/results.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def graficar_salario_por_adopcion(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un boxplot del salario posterior a IA según nivel de adopción.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    df.boxplot(
        column="salary_after_ai",
        by="ai_adoption_level",
        ax=ax
    )

    ax.set_title("Salario posterior a IA según nivel de adopción")
    ax.set_xlabel("Nivel de adopción de IA")
    ax.set_ylabel("Salario posterior a IA")
    fig.suptitle("")

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


def graficar_productividad_por_riesgo(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un boxplot del cambio de productividad según riesgo de automatización.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    df.boxplot(
        column="productivity_change_%",
        by="automation_risk",
        ax=ax
    )

    ax.set_title("Cambio de productividad según riesgo de automatización")
    ax.set_xlabel("Riesgo de automatización")
    ax.set_ylabel("Cambio de productividad (%)")
    fig.suptitle("")

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


def graficar_correlaciones_laborales(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un mapa de calor de correlaciones entre variables laborales numéricas.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    columnas_correlacion = [
        "age",
        "years_experience",
        "salary_before_ai",
        "salary_after_ai",
        "work_hours_per_week",
        "job_satisfaction",
        "productivity_change_%"
    ]

    corr = df[columnas_correlacion].corr()

    fig, ax = plt.subplots(figsize=(9, 7))
    im = ax.imshow(corr)

    ax.set_xticks(range(len(columnas_correlacion)))
    ax.set_yticks(range(len(columnas_correlacion)))
    ax.set_xticklabels(columnas_correlacion, rotation=45, ha="right")
    ax.set_yticklabels(columnas_correlacion)

    for i in range(len(columnas_correlacion)):
        for j in range(len(columnas_correlacion)):
            ax.text(
                j,
                i,
                f"{corr.iloc[i, j]:.2f}",
                ha="center",
                va="center"
            )

    ax.set_title("Correlaciones entre variables laborales numéricas")
    fig.colorbar(im, ax=ax)

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


def graficar_distribucion_salario_after_ai(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un histograma del salario posterior a IA.

    Esta visualización permite analizar la distribución general de la variable
    salary_after_ai, observando concentración, dispersión y posibles asimetrías.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    ax.hist(
        df["salary_after_ai"],
        bins=30,
        edgecolor="black"
    )

    ax.axvline(
        df["salary_after_ai"].median(),
        linestyle="--",
        label=f"Mediana: {df['salary_after_ai'].median():.2f}"
    )

    ax.set_title("Distribución del salario posterior a IA")
    ax.set_xlabel("Salario posterior a IA")
    ax.set_ylabel("Frecuencia")
    ax.legend()

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


def graficar_promedio_salario_por_adopcion(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un gráfico de barras con el salario promedio posterior a IA
    según nivel de adopción de inteligencia artificial.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    promedio = (
        df.groupby("ai_adoption_level")["salary_after_ai"]
        .mean()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        promedio.index.astype(str),
        promedio.values
    )

    for i, valor in enumerate(promedio.values):
        ax.text(
            i,
            valor,
            f"{valor:.0f}",
            ha="center",
            va="bottom"
        )

    ax.set_title("Salario promedio posterior a IA por nivel de adopción")
    ax.set_xlabel("Nivel de adopción de IA")
    ax.set_ylabel("Salario promedio posterior a IA")

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida


def graficar_salario_antes_vs_despues_por_riesgo(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un gráfico de dispersión entre salario antes y después de IA,
    coloreando conceptualmente por riesgo de automatización.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """
    fig, ax = plt.subplots(figsize=(8, 5))

    riesgos = df["automation_risk"].astype(str).unique()

    for riesgo in riesgos:
        datos = df[df["automation_risk"].astype(str) == riesgo]

        ax.scatter(
            datos["salary_before_ai"],
            datos["salary_after_ai"],
            alpha=0.5,
            label=riesgo
        )

    ax.set_title("Salario antes vs. después de IA según riesgo de automatización")
    ax.set_xlabel("Salario antes de IA")
    ax.set_ylabel("Salario después de IA")
    ax.legend(title="Riesgo de automatización")

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(ruta_salida, dpi=300, bbox_inches="tight")
    plt.close(fig)

    return ruta_salida
    
def graficar_violin_salario_por_adopcion(
    df: pd.DataFrame,
    ruta_salida: Path
) -> Path:
    """
    Genera un gráfico tipo violin utilizando Seaborn para mostrar
    la distribución del salario posterior a IA según el nivel de adopción.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset limpio del proyecto.
    ruta_salida : Path
        Ruta donde se guardará la figura PNG.

    Returns
    -------
    Path
        Ruta del archivo generado.
    """

    fig, ax = plt.subplots(figsize=(9, 6))

    sns.violinplot(
        data=df,
        x="ai_adoption_level",
        y="salary_after_ai",
        inner="box",
        ax=ax
    )

    ax.set_title(
        "Distribución del salario posterior según nivel de adopción de IA"
    )
    ax.set_xlabel("Nivel de adopción de IA")
    ax.set_ylabel("Salario posterior a IA")

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    plt.savefig(
        ruta_salida,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close(fig)

    return ruta_salida
    