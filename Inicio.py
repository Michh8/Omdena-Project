import streamlit as st
import os

# Configuración inicial
st.set_page_config(page_title="Proyecto de Predicción", layout="centered")

# Página de inicio
st.title("📱 Predicción de Género Basada en Uso de Aplicaciones")

st.markdown("""
## Bienvenido
Esta aplicación permite analizar un dataset sobre el uso de aplicaciones y 
realizar predicciones de género utilizando regresión logística.

Este proyecto incluye las siguientes páginas:
""")

# Sección de páginas con título y imágenes
col1, col2 = st.columns([2, 2])

with col1:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/exploration.png", width=250) 
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.subheader("EDA: Análisis exploratorio de datos")
    st.markdown("Examina los datos y descubre patrones interesantes. 🧐")

col3, col4 = st.columns([2, 2])

with col3:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    st.image("utils/idea.png", width=250)  
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.subheader("Hipótesis: Visualización de hipótesis propuestas")
    st.markdown("Evalúa diferentes hipótesis mediante gráficos interactivos. 📊")

col5, col6 = st.columns([2, 2])

with col5:
    st.markdown('<div class="column">', unsafe_allow_html=True)
    # Asegúrate de que la ruta esté bien escrita
    ruta_imagen = "utils/machinelearning.png"
    if os.path.exists(ruta_imagen):
        st.image(ruta_imagen, width=250)
    else:
        st.error(f"No se encontró el archivo en la ruta: {ruta_imagen}")  
    st.markdown('</div>', unsafe_allow_html=True)

with col6:
    st.subheader("Modelo: Predicciones con un modelo de árbol de decisiones")
    st.markdown("Genera predicciones y evalúa el desempeño del modelo. 🔮")

# Información del Dataset
st.markdown("---")
st.subheader("📋 Información del Dataset")

st.markdown("""
Este dataset proviene de un estudio sobre el uso de aplicaciones móviles y el comportamiento de los usuarios. Se utiliza para realizar predicciones sobre el género de los usuarios basándose en sus patrones de uso de aplicaciones.

### Características principales:
- **Filas**: 1000 muestras de datos.
- **Columnas**: 20 características relacionadas con el uso de aplicaciones, como la frecuencia de uso de diferentes aplicaciones, las horas activas, la duración de la sesión, entre otros.

### Columnas:
1. **User_ID**: Identificador único del usuario.
2. **App_Usage_Frequency**: Frecuencia de uso de aplicaciones en horas.
3. **Total_Apps_Used**: Número total de aplicaciones utilizadas por el usuario.
4. **Session_Duration**: Duración media de las sesiones en minutos.
5. **Activity_Level**: Nivel de actividad en la aplicación (alta, media, baja).
6. **Gender**: Género del usuario (masculino/femenino). Este es el objetivo de la predicción.

### Objetivo del Proyecto:
El objetivo principal de este proyecto es predecir el género de los usuarios utilizando técnicas de **regresión logística** basadas en sus patrones de uso de aplicaciones móviles. 

🔍 **Análisis de datos**: Antes de realizar las predicciones, se realiza un análisis exploratorio de los datos (EDA) para comprender los patrones y las relaciones entre las variables.

⚙️ **Modelo**: Se implementa un modelo de regresión logística para predecir el género de los usuarios basándose en sus características de uso de aplicaciones.
""")
