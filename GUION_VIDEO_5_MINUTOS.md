# Guion para video - Trabajo Machine Learning Titanic

**Duración objetivo:** 4 minutos 45 segundos

**Formato:** MP4

**Presentan:** Javiera Retamal y Cesar Retamal

**Docente:** Franco Andres Mansilla

> La pauta establece un máximo de 12 minutos. Este guion se diseñó para no superar 5 minutos, considerando pausas breves y cambios de pantalla.

## Preparación antes de grabar

- Abrir el cuaderno `notebooks/trabajo_titanic.ipynb` con todas las celdas ejecutadas.
- Abrir el repositorio de GitHub en otra pestaña.
- Usar siete diapositivas o láminas con estos títulos exactos: **Portada**, **Introducción**, **Punto 1**, **Punto 2**, **Punto 3**, **Punto 4** y **Conclusión**.
- Mostrar el rostro de quien habla, si el formato de grabación lo permite.
- Hablar con calma, sin leer los nombres de todas las columnas ni cada línea del código.

---

## 0:00-0:20 - Portada

**En pantalla:** Título del trabajo, Universidad Mayor, asignatura, integrantes, docente y fecha.

**Cesar dice:**

> Hola. Somos Javiera Retamal y Cesar Retamal. En este video presentamos nuestro trabajo de la Unidad 1 de Machine Learning de la Universidad Mayor, desarrollado con el conjunto de datos Titanic. El docente de la asignatura es Franco Andres Mansilla.

## 0:20-0:50 - Introducción

**En pantalla:** Objetivo general y una imagen o vista breve de las primeras filas del dataset.

**Javiera dice:**

> El objetivo fue construir un pipeline reproducible para explorar, limpiar y separar los datos de pasajeros del Titanic, estudiando su relación con la supervivencia. El trabajo comprende la comparación de frameworks analíticos, la evaluación de la calidad de los datos, el tratamiento de valores faltantes y atípicos, y la creación de muestras de entrenamiento, validación y test sin fuga de información.

## 0:50-1:30 - Punto 1. Frameworks para aplicar analítica de datos

**En pantalla:** Tabla comparativa de CRISP-DM, KDD y SEMMA.

**Cesar dice:**

> Comparamos tres frameworks. CRISP-DM organiza el proyecto en comprensión del negocio, comprensión de los datos, preparación, modelamiento, evaluación y despliegue. Su limitación es que entrega una guía general, pero no define herramientas concretas. KDD se enfoca en descubrir conocimiento mediante selección, transformación, minería e interpretación, aunque desarrolla menos el contexto del negocio y el despliegue. SEMMA considera muestreo, exploración, modificación, modelamiento y evaluación, pero tampoco incorpora formalmente la comprensión del negocio. Seleccionamos CRISP-DM porque cubre el proyecto completo y permite volver a etapas anteriores cuando aparecen problemas en los datos.

## 1:30-2:40 - Punto 2. Calidad de los datos

**En pantalla:** Dimensiones, gráfico de valores faltantes y tabla de decisiones de limpieza.

**Javiera dice:**

> La base de desarrollo contiene 891 pasajeros y 12 variables. La variable objetivo es Survived, donde cero representa que el pasajero no sobrevivió y uno que sí sobrevivió. No encontramos filas completamente duplicadas. Los principales problemas de calidad fueron los valores faltantes en Age, Cabin y Embarked, además de valores elevados en Fare y en algunos recuentos familiares.
>
> Para Age y Fare usamos imputación por mediana, y para Embarked, imputación por moda. Como Cabin tiene una ausencia muy alta, no inventamos una cabina; creamos las variables HasCabin y Deck. Los valores altos de Fare pueden ser pasajes legítimos de primera clase, por lo que aplicamos una transformación logarítmica en vez de eliminarlos. También creamos FamilySize, IsAlone y Title. Todas las estadísticas de imputación y escalamiento se aprenden solamente con los datos de entrenamiento para evitar fuga de información.

## 2:40-3:50 - Punto 3. Entrenamiento, validación y test

**En pantalla:** Tabla de métodos, proporción 70/15/15 y métricas finales.

**Cesar dice:**

> Evaluamos tres alternativas. La división aleatoria simple es rápida, pero puede alterar la proporción de supervivientes. La división estratificada conserva esa proporción en cada muestra. La validación cruzada estratificada entrega una evaluación más estable, aunque requiere mayor procesamiento y no sustituye un test final independiente.
>
> Seleccionamos una división aleatoria estratificada de 70 por ciento para entrenamiento, 15 por ciento para validación y 15 por ciento para test, usando random state igual a 42. Así obtuvimos 623, 134 y 134 observaciones, respectivamente. Implementamos un pipeline con preprocesamiento y regresión logística. La exactitud fue 0,8881 en validación y 0,7910 en el test interno final. Además, la balanced accuracy promedio de la validación cruzada de cinco particiones fue 0,8096. La diferencia entre validación y test confirma la importancia de no depender de una sola partición.

## 3:50-4:15 - Punto 4. Repositorio de GitHub

**En pantalla:** Página principal del repositorio y carpetas `data`, `notebooks` y `outputs`.

**Javiera dice:**

> Todo el desarrollo se guardó en un repositorio público de GitHub. Incluye los datos originales, el cuaderno ejecutado, el archivo de predicciones, las dependencias y un README con instrucciones de reproducción. El código usa rutas relativas y mantiene el preprocesamiento unido al modelo mediante un pipeline.

**En pantalla:** Mostrar brevemente esta dirección:

`https://github.com/CesarRR33/TRABAJOS-MACHINE-LEARNING-UMAYOR`

## 4:15-4:45 - Conclusión

**En pantalla:** Tres conclusiones breves.

**Cesar dice:**

> En conclusión, la calidad de los datos y una separación correcta son fundamentales para obtener resultados confiables.

**Javiera dice:**

> CRISP-DM permitió organizar el trabajo de forma iterativa, mientras que el pipeline evitó fugas de información y facilitó la reproducibilidad. El modelo base obtuvo resultados razonables, pero el principal resultado es un proceso documentado, repetible y preparado para futuras mejoras. Muchas gracias.

---

## Control final de tiempo y entrega

- Ensayar una vez con cronómetro; la meta es terminar entre **4:35 y 4:50**.
- Si supera 5 minutos, reducir pausas y acortar la explicación de los frameworks; no eliminar ningún título obligatorio.
- Exportar o grabar en **MP4**.
- Revisar que el audio sea claro y que el código se pueda leer.
- Adjuntar directamente en Blackboard el MP4 y el cuaderno Python con el enlace de GitHub; la pauta indica que no debe entregarse un enlace del video alojado en la nube.

> **Pendiente:** la pauta señala que el grupo debe tener entre 3 y 5 integrantes. Antes de grabar, se debe incorporar al tercer integrante o confirmar la excepción con el docente. Si se agrega una tercera persona, puede presentar el Punto 2 o el Punto 4 sin modificar el contenido del guion.
