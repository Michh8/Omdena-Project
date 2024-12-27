import streamlit as st
from src.model import entrenar_modelo, predecir

st.title("🤖 Entrenamiento y Predicción")

st.write(
    """
    Entrenamos un modelo de regresión logística para predecir el género
    basado en las características del uso de aplicaciones.
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
