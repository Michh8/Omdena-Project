import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import StandardScaler
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
        # Cargar datos
        data = load_data(ruta)
        
        # Preprocesamiento
        data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
        
        # Filtrar valores atípicos extremos (percentiles 1 y 99)
        for col in ['Age', 'Total_App_Usage_Hours', 'Daily_Screen_Time_Hours', 
                    'Number_of_Apps_Used', 'Social_Media_Usage_Hours', 
                    'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']:
            low, high = data[col].quantile([0.01, 0.99])
            data = data[(data[col] >= low) & (data[col] <= high)]
        
        X = data[['Age', 'Total_App_Usage_Hours', 'Daily_Screen_Time_Hours',
                  'Number_of_Apps_Used', 'Social_Media_Usage_Hours',
                  'Productivity_App_Usage_Hours', 'Gaming_App_Usage_Hours']]
        y = data['Gender']

        # Normalización
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # División de datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Entrenar modelo con regularización L2
        model = LogisticRegression(penalty='l2', C=1.0, random_state=42)
        model.fit(X_train, y_train)

        # Predicción y métricas
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='binary')
        precision = precision_score(y_test, y_pred, average='binary')
        recall = recall_score(y_test, y_pred, average='binary')

        # Mostrar métricas
        st.title("Métricas del Modelo Entrenado")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Accuracy", f"{accuracy:.2f}")
        col2.metric("F1 Score", f"{f1:.2f}")
        col3.metric("Precisión", f"{precision:.2f}")
        col4.metric("Recall", f"{recall:.2f}")

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
