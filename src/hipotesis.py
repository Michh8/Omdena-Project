import pandas as pd
import plotly.express as px
import streamlit as st

# Función para cargar datos
def cargar_datos(ruta="data/dataset.csv"):
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        st.error("Error: No se encontró el archivo de datos.")
        return None

# Función principal para analizar hipótesis
def analizar_hipotesis(hipotesis):
    df = cargar_datos()
    if df is None:
        return

    if hipotesis == "Hipótesis 1: Los hombres tienen un mayor promedio de horas de uso total de aplicaciones que las mujeres.":
        st.subheader(hipotesis)
        avg_usage = df.groupby('Gender')['Total_App_Usage_Hours'].mean()
        fig = px.bar(
            avg_usage,
            x=avg_usage.index,
            y=avg_usage.values,
            labels={'x': 'Género', 'y': 'Promedio de Uso (Horas)'},
            color=avg_usage.values,
            color_continuous_scale='Viridis',
            title="Promedio de Horas de Uso Total de Aplicaciones por Género"
        )
        st.plotly_chart(fig)

        promedio_hombres = avg_usage.get('Male', 0)
        promedio_mujeres = avg_usage.get('Female', 0)
        st.write(f"Promedio general de hombres: {promedio_hombres:.2f} horas.")
        st.write(f"Promedio general de mujeres: {promedio_mujeres:.2f} horas.")

        if promedio_hombres > promedio_mujeres:
            st.success("Conclusión: La hipótesis se respalda.")
        else:
            st.error("Conclusión: La hipótesis no se respalda.")

    elif hipotesis == "Hipótesis 2: La ubicación influye en el número promedio de aplicaciones utilizadas por los usuarios.":
        st.subheader(hipotesis)
        if 'Location' in df.columns:
            avg_apps = df.groupby('Location')['Number_of_Apps_Used'].mean()
            fig = px.bar(
                avg_apps,
                x=avg_apps.index,
                y=avg_apps.values,
                labels={'x': 'Ubicación', 'y': 'Promedio de Aplicaciones Utilizadas'},
                color=avg_apps.values,
                color_continuous_scale='Viridis',
                title="Número Promedio de Aplicaciones Utilizadas por Ubicación"
            )
            st.plotly_chart(fig)
            st.write(avg_apps)

            if avg_apps.max() - avg_apps.min() > 2:
                st.success("Conclusión: La hipótesis se respalda.")
            else:
                st.error("Conclusión: La hipótesis no se respalda.")
        else:
            st.error("Error: La columna 'Location' no está disponible.")

    elif hipotesis == "Hipótesis 3: Las personas más jóvenes (18-30 años) pasan más tiempo en redes sociales.":
        st.subheader(hipotesis)
        df['Age_Group'] = pd.cut(
            df['Age'], bins=[18, 30, 40, 50, 60],
            labels=["18-30", "31-40", "41-50", "51-60"]
        )
        avg_social_media = df.groupby('Age_Group')['Social_Media_Usage_Hours'].mean()
        fig = px.bar(
            avg_social_media,
            x=avg_social_media.index,
            y=avg_social_media.values,
            labels={'x': 'Grupo de Edad', 'y': 'Horas Promedio en Redes Sociales'},
            color=avg_social_media.values,
            color_continuous_scale='Viridis',
            title="Horas Promedio en Redes Sociales por Grupo de Edad"
        )
        st.plotly_chart(fig)

        promedio_18_30 = avg_social_media["18-30"]
        otros_promedios = avg_social_media.drop("18-30").mean()
        if promedio_18_30 > otros_promedios:
            st.success("Conclusión: La hipótesis se respalda.")
        else:
            st.error("Conclusión: La hipótesis no se respalda.")

    elif hipotesis == "Hipótesis 4: Usuarios con mayor uso de apps de productividad tienen menos horas en juegos.":
        st.subheader(hipotesis)
        fig = px.scatter(
            df,
            x="Productivity_App_Usage_Hours",
            y="Gaming_App_Usage_Hours",
            color="Gender",
            labels={
                "Productivity_App_Usage_Hours": "Horas en Productividad",
                "Gaming_App_Usage_Hours": "Horas en Juegos",
                "Gender": "Género"
            },
            title="Relación entre Uso de Apps de Productividad y Juegos"
        )
        st.plotly_chart(fig)

        correlation = df['Productivity_App_Usage_Hours'].corr(df['Gaming_App_Usage_Hours'])
        st.write(f"Correlación entre uso de apps de productividad y juegos: {correlation:.2f}")
        if correlation < 0:
            st.success("Conclusión: La hipótesis se respalda.")
        else:
            st.error("Conclusión: La hipótesis no se respalda.")

    elif hipotesis == "Hipótesis 5: El género puede predecirse con base en el uso de aplicaciones.":
        st.subheader(hipotesis)
        features = ['Total_App_Usage_Hours', 'Social_Media_Usage_Hours', 'Gaming_App_Usage_Hours']
        avg_features_by_gender = df.groupby('Gender')[features].mean()
        st.write(avg_features_by_gender)

        if avg_features_by_gender.std().sum() > 0:
            st.success("Conclusión: La hipótesis se respalda.")
        else:
            st.error("Conclusión: La hipótesis no se respalda.")
