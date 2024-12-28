import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analizar_hipotesis(hipotesis):
    # Cargar datos
    try:
        data = pd.read_csv("data/dataset.csv")  # Ajusta la ruta
    except:
        st.error("Por favor, asegúrate de tener el archivo de datos en la ruta correcta")
        return

    if "Hipótesis 1" in hipotesis:
        # Hipótesis 1: Uso por género
        st.subheader("Análisis de uso de aplicaciones por género")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Distribución del tiempo de uso por género")
            fig, ax = plt.subplots()
            sns.boxplot(x='Gender', y='Total_App_Usage_Hours', data=data, ax=ax)
            ax.set_title("Tiempo de uso por género")
            st.pyplot(fig)

        with col2:
            st.write("Distribución de género")
            fig, ax = plt.subplots()
            data['Gender'].value_counts().plot(kind='bar', ax=ax)
            ax.set_title("Conteo de géneros")
            st.pyplot(fig)

        # Conclusión para Hipótesis 1
        st.markdown("### Conclusión Hipótesis 1")
        st.write("Basado en el gráfico de distribución del tiempo de uso por género, no parece haber una diferencia significativa entre hombres y mujeres en el promedio de horas totales de uso de aplicaciones. Esto sugiere que el género no es un factor determinante en el tiempo de uso total de aplicaciones.")

    elif "Hipótesis 2" in hipotesis:
        # Hipótesis 2: Apps por ubicación
        st.subheader("Análisis de número de aplicaciones por ubicación")

        if 'Location' in data.columns:  # Asegúrate de que 'Location' sea la columna de ubicación
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x='Location', y='Number_of_Apps_Used', data=data, ax=ax)
            ax.set_title("Distribución de Apps por Ubicación")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)

            # Conclusión para Hipótesis 2
            st.markdown("### Conclusión Hipótesis 2")
            st.write("En la gráfica de distribución del número de aplicaciones utilizadas por ubicación, las medianas y los rangos intercuartiles son bastante consistentes entre las ciudades evaluadas. Esto sugiere que la ubicación no influye significativamente en el número promedio de aplicaciones utilizadas.")
        else:
            st.error("La columna 'Location' no está disponible en el dataset. Por favor, verifica los datos.")

    elif "Hipótesis 3" in hipotesis:
        # Hipótesis 3: Redes sociales por edad
        st.subheader("Análisis de uso de redes sociales por edad")

        data['Age_Group'] = pd.cut(data['Age'], bins=[18, 30, 40, 50, 60], 
                                  labels=["18-30", "31-40", "41-50", "51-60"])

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x="Age_Group", y="Social_Media_Usage_Hours", data=data, ax=ax)
        ax.set_title("Horas en redes sociales por grupos de edad")
        st.pyplot(fig)

        # Conclusión para Hipótesis 3
        st.markdown("### Conclusión Hipótesis 3")
        st.write("El análisis muestra que los usuarios entre 18 y 30 años tienen una mediana ligeramente superior en comparación con otros grupos de edad. Esto apoya la hipótesis de que las personas más jóvenes tienden a pasar más tiempo en redes sociales.")

    elif "Hipótesis 4" in hipotesis:
        # Hipótesis 4: Productividad vs Juegos
        st.subheader("Análisis de relación entre apps de productividad y juegos")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x="Productivity_App_Usage_Hours", 
                       y="Gaming_App_Usage_Hours", 
                       hue="Gender", 
                       data=data, ax=ax)
        ax.set_title("Relación entre uso de aplicaciones de productividad y juegos")
        st.pyplot(fig)

    elif "Hipótesis 5" in hipotesis:
        # Hipótesis 5: Tiempo en pantalla por género
        st.subheader("Análisis de tiempo en pantalla por género")

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x="Gender", y="Daily_Screen_Time_Hours", data=data, ax=ax)
        ax.set_title("Tiempo diario en pantalla por género")
        st.pyplot(fig)
