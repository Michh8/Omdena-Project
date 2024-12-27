import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from imblearn.over_sampling import SMOTE

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
        
        label_encoder = LabelEncoder()
        y_h1 = label_encoder.fit_transform(data['Gender'])
        X_h1 = data[['Total_App_Usage_Hours']]
        
        X_train, X_test, y_train, y_test = train_test_split(X_h1, y_h1, test_size=0.2, random_state=42)
        model_h1 = LogisticRegression()
        model_h1.fit(X_train, y_train)
        y_pred_h1 = model_h1.predict(X_test)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Matriz de Confusión")
            fig_cm, ax_cm = plt.subplots()
            cm = confusion_matrix(y_test, y_pred_h1)
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=label_encoder.classes_, 
                       yticklabels=label_encoder.classes_, ax=ax_cm)
            ax_cm.set_xlabel("Predicción")
            ax_cm.set_ylabel("Real")
            st.pyplot(fig_cm)
        
        with col2:
            st.write("Curva ROC")
            fig_roc, ax_roc = plt.subplots()
            y_prob_h1 = model_h1.predict_proba(X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test, y_prob_h1)
            roc_auc = auc(fpr, tpr)
            ax_roc.plot(fpr, tpr, color='darkorange', lw=2, 
                       label=f'ROC (AUC = {roc_auc:.2f})')
            ax_roc.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            ax_roc.set_xlabel("Tasa de Falsos Positivos")
            ax_roc.set_ylabel("Tasa de Verdaderos Positivos")
            ax_roc.legend(loc="lower right")
            st.pyplot(fig_roc)
        
        st.write("### Métricas del Modelo")
        st.write(f"Score de Entrenamiento: {model_h1.score(X_train, y_train):.2f}")
        st.write(f"Score de Prueba: {model_h1.score(X_test, y_test):.2f}")
        st.write("### Reporte de Clasificación")
        st.text(classification_report(y_test, y_pred_h1))
        
    elif "Hipótesis 2" in hipotesis:
        # Hipótesis 2: Apps por ubicación
        st.subheader("Análisis de número de aplicaciones por ubicación")
        
        X_h2 = data[['Number_of_Apps_Used']]
        y_h2 = data['Gender']
        
        X_train, X_test, y_train, y_test = train_test_split(X_h2, y_h2, test_size=0.2, random_state=42)
        model_h2 = LogisticRegression()
        model_h2.fit(X_train, y_train)
        y_pred_h2 = model_h2.predict(X_test)
        
        fig_dist = plt.figure(figsize=(10, 6))
        sns.boxplot(x='Gender', y='Number_of_Apps_Used', data=data)
        plt.title("Distribución de Apps por Género")
        st.pyplot(fig_dist)
        
        st.write("### Métricas del Modelo")
        st.write(f"Score de Entrenamiento: {model_h2.score(X_train, y_train):.2f}")
        st.write(f"Score de Prueba: {model_h2.score(X_test, y_test):.2f}")
        
    elif "Hipótesis 3" in hipotesis:
        # Hipótesis 3: Redes sociales por edad
        st.subheader("Análisis de uso de redes sociales por edad")
        
        data['Age_Group'] = pd.cut(data['Age'], bins=[18, 30, 40, 50, 60], 
                                  labels=["18-30", "31-40", "41-50", "51-60"])
        
        fig_box = plt.figure(figsize=(10, 6))
        sns.boxplot(x="Age_Group", y="Social_Media_Usage_Hours", data=data)
        plt.title("Horas en redes sociales por grupos de edad")
        st.pyplot(fig_box)
        
        X_h3 = data[['Social_Media_Usage_Hours']]
        y_h3 = pd.cut(data['Age'], bins=[0, 18, 35, 50, 100], labels=[0, 1, 2, 3])
        
        X_train, X_test, y_train, y_test = train_test_split(X_h3, y_h3, test_size=0.2, random_state=42)
        model_h3 = LogisticRegression(multi_class='multinomial', solver='lbfgs', max_iter=1000)
        model_h3.fit(X_train, y_train)
        y_pred_h3 = model_h3.predict(X_test)
        
        st.write("### Métricas del Modelo")
        st.write(f"Score de Entrenamiento: {model_h3.score(X_train, y_train):.2f}")
        st.write(f"Score de Prueba: {model_h3.score(X_test, y_test):.2f}")
        st.write("### Reporte de Clasificación")
        st.text(classification_report(y_test, y_pred_h3))
        
    elif "Hipótesis 4" in hipotesis:
        # Hipótesis 4: Productividad vs Juegos
        st.subheader("Análisis de relación entre apps de productividad y juegos")
        
        fig_scatter = plt.figure(figsize=(10, 6))
        sns.scatterplot(x="Productivity_App_Usage_Hours", 
                       y="Gaming_App_Usage_Hours", 
                       hue="Gender", 
                       data=data)
        plt.title("Relación entre uso de aplicaciones de productividad y juegos")
        st.pyplot(fig_scatter)
        
        data['Gaming_Binary'] = (data['Gaming_App_Usage_Hours'] > 0.1).astype(int)
        X_h4 = data[['Productivity_App_Usage_Hours']]
        y_h4 = data['Gaming_Binary']
        
        X_train, X_test, y_train, y_test = train_test_split(X_h4, y_h4, 
                                                           test_size=0.2, 
                                                           random_state=42, 
                                                           stratify=y_h4)
        
        smote = SMOTE(random_state=42)
        X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
        
        model_h4 = LogisticRegression()
        model_h4.fit(X_train_res, y_train_res)
        y_pred_h4 = model_h4.predict(X_test)
        
        st.write("### Métricas del Modelo")
        st.write(f"Score de Entrenamiento: {model_h4.score(X_train_res, y_train_res):.2f}")
        st.write(f"Score de Prueba: {model_h4.score(X_test, y_test):.2f}")
        st.write("### Reporte de Clasificación")
        st.text(classification_report(y_test, y_pred_h4))
        
    elif "Hipótesis 5" in hipotesis:
        # Hipótesis 5: Tiempo en pantalla por género
        st.subheader("Análisis de tiempo en pantalla por género")
        
        fig_box = plt.figure(figsize=(10, 6))
        sns.boxplot(x="Gender", y="Daily_Screen_Time_Hours", data=data)
        plt.title("Tiempo diario en pantalla por género")
        st.pyplot(fig_box)
        
        X_h5 = data[['Daily_Screen_Time_Hours']]
        y_h5 = data['Gender']
        
        X_train, X_test, y_train, y_test = train_test_split(X_h5, y_h5, test_size=0.2, random_state=42)
        model_h5 = LogisticRegression()
        model_h5.fit(X_train, y_train)
        y_pred_h5 = model_h5.predict(X_test)
        
        st.write("### Métricas del Modelo")
        st.write(f"Score de Entrenamiento: {model_h5.score(X_train, y_train):.2f}")
        st.write(f"Score de Prueba: {model_h5.score(X_test, y_test):.2f}")
        st.write("### Reporte de Clasificación")
        st.text(classification_report(y_test, y_pred_h5))