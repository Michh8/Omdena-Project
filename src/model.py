import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import pickle

@st.cache_data
def load_data(ruta):
    """Cargar y mostrar vista previa de los datos"""
    data = pd.read_csv(ruta)
    st.write("Vista previa del conjunto de datos cargado desde el archivo local:")
    st.dataframe(data.head())
    return data

def entrenar_modelo(ruta):
    try:
        # Cargar y mostrar datos usando la función cacheada
        data = load_data(ruta)
        
        # Preparar datos
        data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
        X = data[['Age', 'Total_App_Usage_Hours', 'Daily_Screen_Time_Hours',
                'Number_of_Apps_Used', 'Social_Media_Usage_Hours',
                'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']]
        y = data['Gender']
        
        # División de datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Entrenar modelo
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Calcular métricas
        y_pred = model.predict(X_test)
        
        # Calcular todas las métricas
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='binary')
        precision = precision_score(y_test, y_pred, average='binary')
        recall = recall_score(y_test, y_pred, average='binary')

        # Mostrar métricas usando st.metric en columnas
        st.title("Métricas del Modelo Entrenado")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{accuracy:.2f}", border=True)
        col2.metric("F1 Score", f"{f1:.2f}", border=True)
        col3.metric("Precisión", f"{precision:.2f}", border=True)
        col4.metric("Recall", f"{recall:.2f}", border=True)

        # Guardar modelo
        with open("models/logistic_regression_model.pkl", "wb") as f:
            pickle.dump(model, f)
        
        return accuracy, model.score(X_train, y_train), model.score(X_test, y_test)

    except FileNotFoundError:
        st.error(f"El archivo {ruta} no se encontró. Verifica que exista en el folder especificado.")
        return None, None, None
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo de entrenamiento: {e}")
        return None, None, None

def predecir(datos):
    try:
        with open("models/logistic_regression_model.pkl", "rb") as f:
            model = pickle.load(f)
        return model.predict([datos])[0]
    except Exception as e:
        st.error(f"Error durante la predicción: {e}")
        return None