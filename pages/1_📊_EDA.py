import streamlit as st
import pandas as pd
from src.eda import (
    plot_heatmap,
    plot_gender_distribution,
    plot_location_distribution,
    plot_avg_app_usage_by_gender,
    plot_scatter
)

# Cargar los datos
@st.cache_data
def load_data():
    return pd.read_csv("data/dataset.csv")

# Configuración de la página
st.title("Análisis Exploratorio de Datos (EDA)")

# Cargar datos
df = load_data()

# Información básica del conjunto de datos
st.header("Aspectos Básicos del Conjunto de Datos")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Número de Filas", value=df.shape[0], help="Total de filas en el conjunto de datos")
    with col2:
        st.metric(label="Número de Columnas", value=df.shape[1], help="Total de columnas en el conjunto de datos")
    with col3:
        missing_values = df.isnull().sum().sum()
        st.metric(label="Valores Perdidos", value=missing_values, help="Cantidad total de valores nulos")

# Mostrar gráficos
st.header("Distribución de Variables")
st.subheader("Distribución por Género")
gender_fig = plot_gender_distribution(df)
st.plotly_chart(gender_fig)

st.subheader("Distribución por Ubicación")
location_fig = plot_location_distribution(df)
st.plotly_chart(location_fig)

st.subheader("Promedio de Uso Total de Aplicaciones por Género")
avg_usage_fig = plot_avg_app_usage_by_gender(df)
st.plotly_chart(avg_usage_fig)

st.header("Mapa de Calor de Correlaciones")
heatmap_fig = plot_heatmap(df)
st.plotly_chart(heatmap_fig)

# Gráfico de dispersión interactivo
st.header("Gráfico de Dispersión Interactivo")
x_column = st.selectbox("Selecciona la columna X:", df.columns)
y_column = st.selectbox("Selecciona la columna Y:", df.columns)

scatter_fig = plot_scatter(df, x_column, y_column)
st.plotly_chart(scatter_fig)
