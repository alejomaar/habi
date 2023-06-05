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

# 1) Comprensión del negocio:
El objetivo de este proyecto es clasificar la viabilidad y selección de un usuario en función de los datos disponibles.

# 2) Comprensión de los datos:
Antes de realizar cualquier análisis o modelado, es crucial comprender los datos disponibles. Esto implica explorar las variables, comprender su significado y relación con las variables objetivo, identificar posibles problemas de calidad de los datos y evaluar la distribución y la presencia de valores atípicos.

# 3) Preparación de los datos:
La preparación de los datos es una etapa importante en el proceso de modelado. Esto incluye la eliminación de registros con valores nulos o duplicados, el manejo de valores faltantes mediante imputación o eliminación, y la transformación de variables categóricas en representaciones numéricas adecuadas, como el one-hot encoding.

# 4) Modelado:
En esta etapa, se explorarán y entrenarán diferentes modelos de machine learning para predecir la viabilidad y selección de un usuario. Se probarán modelos como XGBClassifier, LogisticRegression, SVC y MLPClassifier. Se utilizarán técnicas de validación cruzada y ajuste de hiperparámetros para obtener los mejores resultados posibles.

# 5) Evaluación:
La evaluación de los modelos es esencial para determinar su rendimiento y seleccionar el mejor modelo para su implementación. Se utilizarán métricas como f1-score, roc curve y precision-recall curve para evaluar la capacidad de los modelos para clasificar correctamente la viabilidad y selección de los usuarios.

# 6) Despliegue:
En esta etapa, se llevará a cabo el despliegue de los modelos seleccionados en una API utilizando la biblioteca FastAPI. Los modelos entrenados se guardarán en archivos pickle y se cargarán en la API para realizar predicciones en tiempo real. La API proporcionará endpoints que aceptarán solicitudes de predicción y devolverán los resultados obtenidos a partir de los modelos cargados.

Este README proporciona una descripción general de las diferentes etapas del proyecto y su enfoque en la clasificación de viabilidad y selección de usuarios. Cada sección se explorará en detalle en los notebooks correspondientes.