import streamlit as st
from src.model import entrenar_modelo, predecir

st.title("🤖 Entrenamiento y Predicción")

st.write(
    """
 ¿Qué es la Regresión Logística?
    La regresión logística es un algoritmo de aprendizaje supervisado que se utiliza para 
    resolver problemas de clasificación binaria. En este caso, se usa para predecir el género 
    (Masculino o Femenino) en función de las características del uso de aplicaciones.

    ¿Por qué se escogió este modelo?
    Este modelo es sencillo de implementar, eficiente y ofrece una interpretación directa 
    de las relaciones entre las variables predictoras y la variable objetivo.

   Mejoras implementadas
    -Normalización de características**: Para mejorar la estabilidad numérica y el rendimiento.
    -Filtrado de valores atípicos**: Para evitar que puntos extremos distorsionen el modelo.
    -Regularización**: Se utilizó regularización L2 para evitar el sobreajuste.
    1. Carga de datos:

Carga el conjunto de datos desde un archivo CSV.

Se asegura de mapear los géneros a valores numéricos (Male = 0, Female = 1).

2. Filtrado de valores atípicos:

Elimina valores extremos en las variables predictoras usando percentiles 1 y 99.

3. Normalización:

Usa StandardScaler para transformar las variables a una escala estándar (media 0, desviación estándar 1).

4. División del conjunto de datos:

Divide los datos en conjuntos de entrenamiento (80%) y prueba (20%).

5. Entrenamiento del modelo:

Ajusta un modelo de regresión logística con regularización .

6. Cálculo de métricas:

Se evalúa el modelo en el conjunto de prueba y se calculan las métricas principales:

Accuracy: Proporción de predicciones correctas.

F1 Score: Promedio armónico de precisión y recall.

Precisión (Precision): Fracción de predicciones positivas correctas.

Recall: Proporción de verdaderos positivos capturados.


7. Almacenamiento del modelo:

Guarda el modelo entrenado en un archivo pkl para su uso posterior.

Sección de predicción (predecir)

Carga el modelo previamente entrenado.

Recibe datos introducidos por el usuario y realiza una predicción.

    """
    
)

# Entrenar modelo
if st.button("Entrenar modelo"):
    accuracy, training_score, testing_score = entrenar_modelo("data/dataset.csv")
    st.write(f"Training Score: {training_score:.2f}")
    st.write(f"Testing Score: {testing_score:.2f}")
    st.write(f"Accuracy: {accuracy:.2f}")

# Predicción
st.subheader("Realiza una predicción")
edad = st.number_input("Edad:", min_value=0, max_value=100, value=30)
uso_total = st.number_input("Horas de uso total:", min_value=0.0, max_value=24.0, value=5.0)
pantalla = st.number_input("Horas de pantalla diaria:", min_value=0.0, max_value=24.0, value=5.0)
apps = st.number_input("Número de apps usadas:", min_value=0, max_value=100, value=10)
redes = st.number_input("Horas en redes sociales:", min_value=0.0, max_value=24.0, value=3.0)
productividad = st.number_input("Horas en apps de productividad:", min_value=0.0, max_value=24.0, value=2.0)
juegos = st.number_input("Horas en apps de juegos:", min_value=0.0, max_value=24.0, value=1.0)

if st.button("Predecir género"):
    prediccion = predecir([edad, uso_total, pantalla, apps, redes, productividad, juegos])
    st.write("Género Predicho:", "Masculino" if prediccion == 0 else "Femenino")

    
st.write(
    """
    ### Interpretación de las métricas

Resultados del modelo:

Accuracy (0.50):

El modelo predice correctamente el 50% de los casos en el conjunto de prueba.

Este valor indica un desempeño igual al azar para un problema de clasificación binaria con clases balanceadas.


F1 Score (0.42):

Muestra un balance entre precisión y recall, especialmente útil si hay clases desbalanceadas.

El valor bajo indica que ni precisión ni recall son particularmente buenos.

Precisión (0.46):

De todas las predicciones positivas (predijo Female), solo el 46% eran correctas.

Una precisión baja sugiere que el modelo tiene muchos falsos positivos.

Recall (0.38):

De todas las instancias de la clase Female, el modelo identificó correctamente solo el 38%.

Un recall bajo indica que el modelo tiene problemas para detectar la clase positiva.






Conclusión sobre el modelo:

El modelo no tiene un buen desempeño, posiblemente debido a:

Falta de características relevantes: Las variables predictoras podrían no ser suficientes para capturar la complejidad del problema.

Desbalance en los datos: Si hay más ejemplos de una clase que de otra, el modelo puede estar sesgado.

Modelo básico: La regresión logística puede no ser suficientemente compleja para este problema.


### Mejoras sugeridas:
1. Recolectar más datos y asegurarse de que las clases estén balanceadas.

2. Probar modelos más complejos como árboles de decisión o redes neuronales.

3. Agregar nuevas características relevantes que puedan mejorar la discriminación entre clases.

    """
    
)
