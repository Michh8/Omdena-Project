import streamlit as st
from src.hipotesis import analizar_hipotesis

st.title("💡 Análisis de Hipótesis")

st.write(
    """
    Analizamos si las hipótesis planteadas en el proyecto se cumplen 
    con los datos proporcionados.
    """
)

# Seleccionar hipótesis
hipotesis = st.selectbox(
    "Selecciona la hipótesis a analizar:",
    [
        "Hipótesis 1: Los hombres tienen un mayor promedio de horas de uso total de aplicaciones que las mujeres.",
        "Hipótesis 2: La ubicación influye en el número promedio de aplicaciones utilizadas por los usuarios.",
        "Hipótesis 3: Las personas más jóvenes (18-30 años) pasan más tiempo en redes sociales.",
        "Hipótesis 4: Usuarios con mayor uso de apps de productividad tienen menos horas en juegos.",
        "Hipótesis 5: El género puede predecirse con base en el uso de aplicaciones."
    ]
)

resultado = analizar_hipotesis(hipotesis)