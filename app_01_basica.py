# ------------------------------------------------------------
# Pulso Digital · Paso 1 de 3: título, datos e indicadores
# Ejecutar:  streamlit run app_01_basica.py
# ------------------------------------------------------------
import pandas as pd
import streamlit as st
#Pestaña del navegador.
st.set_page_config(page_title="Pulso Digital", page_icon="📱", layout="wide")

# 1. Presentación
st.title("📱 Pulso Digital")
st.write("Explora los hábitos tecnológicos y el bienestar digital de una comunidad ficticia.")

# 2. Carga de datos: una fila = una respuesta, una columna = una variable
df = pd.read_csv("encuesta_bienestar_digital.csv")

st.subheader("Así son nuestros datos")
st.dataframe(df.head(10))

# 3. Indicadores
st.subheader("Resumen")
col1, col2, col3 = st.columns(3)
col1.metric("Respuestas", len(df))
col2.metric("Pantalla media", f"{df['horas_pantalla'].mean():.1f} h/día")
col3.metric("Bienestar medio", f"{df['bienestar'].mean():.1f}/10")
