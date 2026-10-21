# ------------------------------------------------------------
# Pulso Digital · Paso 3 de 3: versión final con filtros
# Ejecutar:  streamlit run app.py
# ------------------------------------------------------------
#Trae las dos herramientas. pandas trabaja con los datos y Streamlit los convierte en página web.
import pandas as pd
import streamlit as st

#configura la pestaña del navegador, NO el contenido de la página:  título, icono y ancho de la página(sin esto,el contenido quedaría en una sola columna).
st.set_page_config(page_title="Pulso Digital", page_icon="📱", layout="wide")

#Bloque 1 · La función de carga con caché
# Guardamos los datos en caché: el CSV se lee una vez,
# aunque Streamlit vuelva a ejecutar el script en cada clic.
@st.cache_data
#decorador: le dice a Streamlit que guarde el resultado en caché (memoria temporal).

def cargar_datos():
    """
    definimos la función: bloque de código con nombre que se puede llamar después. Todavía no ejecuta nada.
    lee el archivo CSV. Una vez leído, lo guarda en "caché" (memoria temporal).
    """
    #Lee el CSV y lo convierte en un dataframe
    return pd.read_csv("encuesta_bienestar_digital.csv")


# 1. Bloque 2 · Presentación
#Título principal de la página 
st.title("📱 Pulso Digital")
#Escribe una frase introductoria
st.write("Explora los hábitos tecnológicos y el bienestar digital de una comunidad ficticia.")
#Subtítulo con información adicional
st.caption("Datos sintéticos creados para el taller: sirven para aprender, no para sacar conclusiones reales.")

#Bloque 3 · Carga de datos
# 2. Carga de datos function. Lee el CSV y lo convierte en un dataframe : df
df = cargar_datos()

# Bloque 4 · Filtros en la barra lateral
# 3. Filtros en la barra lateral
#coloca el elemento en la barra lateral izquierda en lugar de en la página principal. Funciona con casi todo: st.sidebar.write, st.sidebar.metric…
st.sidebar.header("Filtra las respuestas")
#Crea un desplegable con las edades
#multiselect: permite seleccionar varios valores.
edades = st.sidebar.multiselect(
    "Grupo de edad",
    #options=sorted(df["grupo_edad"].unique()) -> Obtiene valores únicos y los ordena
    options=sorted(df["grupo_edad"].unique()),
    #default=sorted(df["grupo_edad"].unique()) -> Hace que se seleccionen todos por defecto
    default=sorted(df["grupo_edad"].unique()),
)
#Otro desplegable con las plataformas principales
plataformas = st.sidebar.multiselect(
    "Plataforma principal",
    options=sorted(df["plataforma"].unique()),
    default=sorted(df["plataforma"].unique()),
)

#Bloque 5 · Aplicar los filtros
# 4. Aplicamos los filtros: nos quedamos con las filas que cumplen las dos condiciones
filtrado = df[
    #recorre las 200 filas y responde, para cada una, True o False: “¿su grupo de edad está en la lista elegida?”. El resultado es una columna de 200 True/False, llamada máscara.
    df["grupo_edad"].isin(edades)
    # y lo mismo para plataforma
    & df["plataforma"].isin(plataformas)
    #resultado se guarda en la variable nueva de filtrado
]

#Bloque 6 · Protección contra la selección vacía
# Si no queda ninguna fila, avisamos y paramos aquí: en caso de que se desmarquen todas las edades/opciones
if filtrado.empty:
    #mostrará aviso amarillo
    st.warning("No hay respuestas con estos filtros. Prueba a seleccionar más opciones.")
    #se detiene el script en este punto. 
    st.stop()

#Bloque 7 · Indicadores
# 5. Indicadores
#título de la sección.
st.subheader("Resumen")
#divide la fila en 3 columnas del mismo ancho y devuelte tres "huecos", que se guardan en col1,col2,col3
col1, col2, col3 = st.columns(3)
#coloca una tarjeta de indicador dentro de la columna 1. Recibe dos argumentos: etiqueta y el valor. len:cuenta las filas,es decir, el número de respuestas
col1.metric("Respuestas", len(filtrado))
#cadena de texto f-string. Calcula la media de esa columna: horas_pantalla . 1f: 1 décimal
col2.metric("Pantalla media", f"{filtrado['horas_pantalla'].mean():.1f} h/día")
col3.metric("Bienestar medio", f"{filtrado['bienestar'].mean():.1f}/10")

#Bloque 8 · Gráficos
# 6. Gráficos
#2 columnas
izquierda, derecha = st.columns(2)

with izquierda:
    st.subheader("Bienestar medio por plataformas")
    resumen = (
        filtrado.groupby("plataforma")["bienestar"]
        .mean()
        .sort_values(ascending=False)
    )
    st.bar_chart(resumen, sort=False)  # sort=False respeta nuestro orden (de mayor a menor)

with derecha:
    st.subheader("Horas de pantalla y bienestar")
    st.scatter_chart(filtrado, x="horas_pantalla", y="bienestar", color="grupo_edad")

#Bloque 9 · Tabla de detalle
# 7. Datos de detalle
with st.expander("Consultar las respuestas filtradas"):
    st.dataframe(filtrado, hide_index=True)
