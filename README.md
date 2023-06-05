#HABI Interview

# Introducción:
En este proyecto, se aborda el desafío de clasificar la viabilidad y selección de un usuario utilizando datos relacionados con diferentes variables. El objetivo es construir un modelo predictivo que pueda determinar estas variables. Se han realizado una serie de pasos previos, como limpieza de datos, análisis exploratorio y preparación de los datos, así como la selección y entrenamiento de diferentes modelos utilizando técnicas de validación cruzada y ajuste de hiperparámetros.

## Tabla de contenidos:
* Comprensión del negocio
* Comprensión de los datos
* Preparación de los datos
* Modelado
* Evaluación
* Despliegue

### 1) Comprensión del negocio:
El objetivo de este proyecto es clasificar la viabilidad y selección de un usuario en función de los datos disponibles.

### 2) Comprensión de los datos:
Durante la comprensión de los datos, se identificaron valores nulos, duplicados e inconsistencias en los registros de los usuarios. Además, se observó un desbalance en las variables objetivo. Estas observaciones permitieron diseñar un plan de trabajo para abordar estas problemáticas en las etapas posteriores del proyecto.

Además, se realizó una descripción de las variables en base a supuestos, con el fin de comprender su significado y su relevancia en el contexto del problema. Esta información fue utilizada para guiar el proceso de limpieza, análisis y modelado de los datos.

### 3) Preparación de los datos:
Durante la etapa de preparación de los datos, se llevaron a cabo diversas tareas para garantizar la calidad y la integridad de los datos. Estas tareas incluyeron:

* Eliminación de registros con valores nulos o duplicados para asegurar la consistencia de los datos.
* Manejo de los valores faltantes mediante técnicas de imputación o reemplazo para evitar la pérdida de información.
* Transformación de variables categóricas utilizando one-hot encoding, lo cual permite representar las categorías como variables binarias.
* Eliminación de valores atípicos (outliers) que podrían afectar negativamente el desempeño del modelo.

### 4) Modelado:
En esta etapa, se explorarán y entrenarán diferentes modelos de machine learning para predecir la viabilidad y selección de un usuario. Se probarán modelos como XGBClassifier, LogisticRegression, SVC y MLPClassifier. Se utilizarán técnicas de validación cruzada y ajuste de hiperparámetros para obtener los mejores resultados posibles.

### 5) Evaluación:
La evaluación de los modelos es esencial para determinar su rendimiento y seleccionar el mejor modelo para su implementación. Se utilizarán métricas como f1-score, roc curve y precision-recall curve para evaluar la capacidad de los modelos para clasificar correctamente la viabilidad y selección de los usuarios.

### 6) Despliegue:
En esta etapa, se llevará a cabo el despliegue de los modelos seleccionados en una API utilizando la biblioteca FastAPI. Los modelos entrenados se guardarán en archivos pickle y se cargarán en la API para realizar predicciones. 


# Instrucciones
Este README proporciona una descripción general de las diferentes etapas del proyecto y su enfoque en la clasificación de viabilidad y selección de usuarios. Cada sección se explorará en detalle en los notebooks correspondientes.

* 1) cleaning_eda: Limpieza de datos y EDA
   * 2.a) is_selected_prediction: Modelado y Clasificacion de la variable `is_selected`
   * 2.b) viability_prediction: Modelado y Clasificacion de la variable `viability`
