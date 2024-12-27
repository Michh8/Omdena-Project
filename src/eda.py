import pandas as pd
import plotly.express as px

def plot_heatmap(df):
    """Genera un heatmap de las correlaciones en el DataFrame."""
    # Seleccionar solo las columnas numéricas
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Calcular la matriz de correlación
    correlation_matrix = numeric_df.corr()
    
    # Crear el heatmap
    fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale='Viridis',
        labels=dict(color="Correlación"),
        title="Mapa de Calor de Correlaciones"
    )
    return fig

def plot_gender_distribution(df):
    """Genera un gráfico de barras mostrando la distribución por género."""
    gender_counts = df['Gender'].value_counts()
    fig = px.bar(
        gender_counts,
        x=gender_counts.index,
        y=gender_counts.values,
        labels={'x': 'Género', 'y': 'Cantidad'},
        color=gender_counts.values,
        color_continuous_scale='Viridis',
        title="Distribución por Género"
    )
    return fig

def plot_location_distribution(df):
    """Genera un gráfico de barras mostrando la distribución por ubicación."""
    location_counts = df['Location'].value_counts()
    fig = px.bar(
        location_counts,
        x=location_counts.index,
        y=location_counts.values,
        labels={'x': 'Ubicación', 'y': 'Cantidad'},
        color=location_counts.values,
        color_continuous_scale='Viridis',
        title="Distribución por Ubicación"
    )
    return fig

def plot_avg_app_usage_by_gender(df):
    """Gráfico de barras: Promedio de uso total de aplicaciones por género."""
    avg_usage = df.groupby('Gender', as_index=False)['Total_App_Usage_Hours'].mean()
    fig = px.bar(
        avg_usage,
        x='Gender',
        y='Total_App_Usage_Hours',
        labels={'Total_App_Usage_Hours': 'Promedio de Uso (horas)', 'Gender': 'Género'},
        color='Total_App_Usage_Hours',
        color_continuous_scale='Viridis',
        title="Promedio de Uso Total de Aplicaciones por Género"
    )
    return fig

def plot_scatter(df, x_column, y_column):
    """Genera un gráfico de dispersión basado en las selecciones del usuario."""
    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        color='Gender',
        labels={'x': x_column, 'y': y_column, 'color': 'Género'},
        title="Gráfico de Dispersión"
    )
    return fig