# Trabajo de Machine Learning - Titanic

Proyecto académico de la asignatura Machine Learning de la Universidad Mayor. El objetivo es construir un pipeline reproducible para explorar, limpiar y separar el conjunto de datos **Titanic - Machine Learning from Disaster**.

## Integrantes

- Javiera Retamal
- Cesar Retamal

**Docente:** Franco Andres Mansilla  
**Fecha:** 24-08-2026



## Contenido

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

## Estructura

```text
trabajo_machine_learning_titanic/
├── data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
├── notebooks/
│   └── trabajo_titanic.ipynb
├── outputs/
│   └── submission_titanic.csv
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
jupyter notebook notebooks/trabajo_titanic.ipynb
```

Luego debe seleccionarse **Kernel > Restart & Run All**. El cuaderno usa rutas relativas y debe ejecutarse desde su ubicación dentro de `notebooks/`.

## Resultados principales

- Entrenamiento: 623 observaciones (69,92 %).
- Validación: 134 observaciones (15,04 %).
- Test interno: 134 observaciones (15,04 %).
- Balanced accuracy promedio en validación cruzada: 0,8096.
- Accuracy de validación: 0,8881.
- Accuracy del test interno final: 0,7910.

La diferencia entre validación y test muestra por qué no debe evaluarse un procedimiento utilizando solamente una partición y por qué conviene complementar con validación cruzada.

## Reproducibilidad

- Los CSV originales no se modifican.
- Las transformaciones dependientes de los datos se ajustan solamente con la muestra de entrenamiento de cada evaluación.
- El parámetro `random_state=42` permite reproducir las separaciones.
- `Pipeline` y `ColumnTransformer` mantienen unidos el preprocesamiento y el modelo.
- `requirements.txt` registra las dependencias necesarias.

## Fuente de datos

Kaggle: [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)

