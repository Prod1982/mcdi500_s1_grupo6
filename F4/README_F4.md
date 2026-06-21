# Fase 4 — Visualización, validación y comunicación de resultados

## Proyecto

**Impacto de la inteligencia artificial en el empleo, la productividad y la capacitación laboral**

Curso: **MCD1500 — Programación para la Ciencia de Datos**  
Institución: **Universidad Andrés Bello (UNAB)**  
Docente: **Dr. Omar Salinas Silva**

---

## Objetivo de la Fase 4

La Fase 4 corresponde al cierre integrador del proyecto. Su propósito es consolidar los avances desarrollados en las fases anteriores, validar técnicamente el flujo de trabajo, construir visualizaciones analíticas y comunicar hallazgos relevantes de manera clara, reproducible y profesional.

Esta fase integra:

- el dataset limpio generado en Fase 2;
- el núcleo algorítmico desarrollado en Fase 3;
- la arquitectura modular y orientada a objetos;
- las mediciones de eficiencia temporal;
- las visualizaciones y evidencias finales de comunicación de resultados.

---

## Dataset utilizado

El dataset base utilizado corresponde al archivo limpio generado durante la Fase 2:

```text
data/processed/ai_job_impact_clean.csv

F4/
├── notebooks/
│   └── F4_visualizacion_validacion_cierre.ipynb
│
├── src/
│   ├── visualizaciones_f4.py
│   ├── validacion_f4.py
│   └── documentacion_f4.py
│
├── results/
│   ├── figura_1_salario_por_adopcion_ia.png
│   ├── figura_2_productividad_por_riesgo.png
│   ├── figura_3_correlaciones_laborales.png
│   ├── resumen_hallazgos_f4.txt
│   ├── metricas_validacion_f4.txt
│   └── documentacion_arquitectura_f4.txt
│
└── README_F4.md

## Descripción de la estructura de la Fase 4

La estructura de la Fase 4 fue organizada para separar claramente el notebook ejecutable, los módulos de apoyo, los resultados generados y la documentación técnica de cierre. Esta organización permite mantener trazabilidad entre el código desarrollado, las visualizaciones producidas y los archivos utilizados como evidencia en el informe final del proyecto.

La carpeta `notebooks` contiene el archivo principal de trabajo de la fase: `F4_visualizacion_validacion_cierre.ipynb`. Este notebook integra la carga del dataset limpio, la validación técnica inicial, la construcción de visualizaciones analíticas, la interpretación de hallazgos y la exportación de resultados. Su función principal es actuar como evidencia ejecutable y reproducible del cierre técnico del proyecto.

La carpeta `src` está destinada a almacenar módulos reutilizables de apoyo. En esta fase se consideran tres archivos principales: `visualizaciones_f4.py`, `validacion_f4.py` y `documentacion_f4.py`. Aunque el desarrollo inicial se realiza desde el notebook, esta carpeta permite proyectar una arquitectura más modular, donde las funciones de visualización, validación y documentación puedan trasladarse progresivamente a scripts independientes, facilitando mantenimiento y reutilización.

La carpeta `results` almacena todos los productos generados durante la Fase 4. En ella se guardan las figuras exportadas en formato PNG, el resumen de hallazgos, las métricas de validación y la documentación arquitectónica. Esta separación permite conservar evidencia persistente del análisis y facilita la incorporación de estos resultados al informe técnico final y a la presentación profesional.

El archivo `README_F4.md` documenta el propósito de la fase, la estructura de carpetas, los archivos generados, la relación con las fases anteriores y las buenas prácticas aplicadas. Su objetivo es facilitar la comprensión del avance, apoyar la reproducibilidad del trabajo y servir como referencia para otros integrantes del equipo o evaluadores.

## Flujo de trabajo de la Fase 4

El flujo de trabajo seguido en esta fase se resume de la siguiente manera:

```text
Dataset limpio de Fase 2
        ↓
Carga en notebook F4
        ↓
Validación técnica del dataset
        ↓
Construcción de visualizaciones analíticas
        ↓
Exportación de figuras y archivos TXT
        ↓
Documentación arquitectónica
        ↓
Comunicación de hallazgos para informe y presentación final

## Evidencias generadas

Durante esta fase se generaron las siguientes evidencias:

| Archivo | Ubicación | Propósito |
|---|---|---|
| `F4_visualizacion_validacion_cierre.ipynb` | `F4/notebooks/` | Notebook ejecutable de validación, visualización y cierre. |
| `figura_1_salario_por_adopcion_ia.png` | `F4/results/` | Comparar salario posterior a IA según nivel de adopción. |
| `figura_2_productividad_por_riesgo.png` | `F4/results/` | Analizar cambio de productividad según riesgo de automatización. |
| `figura_3_correlaciones_laborales.png` | `F4/results/` | Visualizar correlaciones entre variables laborales numéricas. |
| `resumen_hallazgos_f4.txt` | `F4/results/` | Registrar interpretación preliminar de los principales hallazgos. |
| `metricas_validacion_f4.txt` | `F4/results/` | Registrar métricas técnicas de validación del dataset y resultados. |
| `documentacion_arquitectura_f4.txt` | `F4/results/` | Documentar entradas, proceso, salidas y trazabilidad de la fase. |