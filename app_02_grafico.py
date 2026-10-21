# ------------------------------------------------------------
# Pulso Digital · Paso 2 de 3: añadimos un gráfico
# Ejecutar:  streamlit run app_02_grafico.py
# ------------------------------------------------------------
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Pulso Digital", page_icon="📱", layout="wide")

# 1. Presentación
st.title("📱 Pulso Digital")
st.write("Explora los hábitos tecnológicos y el bienestar digital de una comunidad ficticia.")

# 2. Carga de datos
df = pd.read_csv("encuesta_bienestar_digital.csv")

# 3. Indicadores
st.subheader("Resumen")
col1, col2, col3 = st.columns(3)
col1.metric("Respuestas", len(df))
col2.metric("Pantalla media", f"{df['horas_pantalla'].mean():.1f} h/día")
col3.metric("Bienestar medio", f"{df['bienestar'].mean():.1f}/10")

# 4. Gráfico: agrupamos por plataforma y calculamos la media de bienestar
st.subheader("Bienestar medio por plataforma")
resumen = (
    df.groupby("plataforma")["bienestar"]
    .mean()
    .sort_values(ascending=False)
)
st.bar_chart(resumen, sort=False)  # sort=False respeta nuestro orden (de mayor a menor)
