# Trabajo de Machine Learning - Titanic

Proyecto académico de la asignatura Machine Learning de la Universidad Mayor. Utiliza el conjunto **Titanic - Machine Learning from Disaster** para desarrollar un flujo reproducible de exploración, preparación, entrenamiento, optimización y evaluación de modelos de clasificación.

## Integrantes

- Javiera Retamal
- Cesar Retamal

**Docente:** Franco Andres Mansilla  
**Fecha de inicio:** 24-08-2026

## Contenido de la Unidad 1

El cuaderno incluye:

- Comparación de CRISP-DM, KDD y SEMMA.
- Exploración y descripción de los datos.
- Identificación de duplicados, faltantes y posibles atípicos.
- Tratamiento reproducible de variables numéricas y categóricas.
- Ingeniería de características (`FamilySize`, `IsAlone`, `HasCabin`, `Deck` y `Title`).
- Comparación de métodos de separación.
- División estratificada 70/15/15.
- Pipeline con `ColumnTransformer` y regresión logística.
- Validación cruzada estratificada.
- Evaluación en un test interno no utilizado durante el desarrollo.
- Generación opcional de un archivo de predicciones compatible con Kaggle.

## Contenido de la Unidad 2

- Regresión logística con penalización L1, L2 y Elastic Net.
- Random Forest, XGBoost y red neuronal MLP.
- Accuracy, Precision, Recall, F1, ROC-AUC y KS.
- Comparación entre entrenamiento y validación.
- Diagnóstico de sobreajuste.
- Optimización mediante Grid Search y Randomized Search.
- Validación cruzada estratificada de cinco folds.
- Selección e interpretación del modelo final.
- Evaluación única sobre un test interno reservado.
- Generación de predicciones compatibles con Kaggle.

## Estructura

```text
trabajo_machine_learning_titanic/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
├── notebooks/
│   ├── trabajo_titanic.ipynb
│   └── trabajo_titanic_unidad2.ipynb
├── outputs/
│   ├── submission_titanic.csv
│   ├── titanic_submission_unidad2.csv
│   ├── resumen_resultados_unidad2.csv
│   └── modelo_final_logistica_l2_unidad2.joblib
├── .gitignore
├── README.md
└── requirements.txt
```

## Instalación

Se recomienda Python 3.10 o superior. Desde la raíz del proyecto:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

En Linux o macOS:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecución

```bash
jupyter notebook notebooks/trabajo_titanic_unidad2.ipynb
```

Luego debe seleccionarse **Kernel > Restart & Run All**. El cuaderno detecta si se ejecuta desde la raíz del proyecto o desde la carpeta `notebooks`.

## Resultados principales de la Unidad 1

- Entrenamiento: 623 observaciones (69,92 %).
- Validación: 134 observaciones (15,04 %).
- Test interno: 134 observaciones (15,04 %).
- Balanced accuracy promedio en validación cruzada: 0,8096.
- Accuracy de validación: 0,8881.
- Accuracy del test interno final: 0,7910.

La diferencia entre validación y test muestra por qué no debe evaluarse un procedimiento utilizando solamente una partición y por qué conviene complementar con validación cruzada.

## Resultados principales de la Unidad 2

- Modelo final: Regresión Logística L2 con `C=0.1`.
- AUC promedio en validación cruzada: 0,8716.
- AUC de validación externa: 0,9170.
- AUC del test interno final: 0,8169.
- Accuracy del test interno final: 0,7612.
- F1 del test interno final: 0,6800.

El test interno se utilizó una sola vez después de fijar el modelo, los hiperparámetros, la métrica principal y el umbral de clasificación.

## Reproducibilidad

- Los CSV originales no se modifican.
- Las transformaciones dependientes de los datos se ajustan solamente con la muestra de entrenamiento de cada evaluación.
- El parámetro `random_state=42` permite reproducir las separaciones.
- `Pipeline` y `ColumnTransformer` mantienen unidos el preprocesamiento y el modelo.
- La búsqueda de hiperparámetros ajusta el preprocesamiento dentro de cada fold.
- Los archivos derivados se guardan en `outputs`.
- `requirements.txt` registra las dependencias necesarias.

## Fuente de datos

Kaggle: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
