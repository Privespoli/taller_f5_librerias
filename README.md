# 📱 Pulso Digital · Taller de Streamlit

Demo del taller **«De los datos a la web: tu primera app con Streamlit»**.
Construimos paso a paso una app que explora una encuesta sobre hábitos tecnológicos y bienestar digital.

> ⚠️ **Los datos son sintéticos.** La encuesta se creó para el taller: sirve para aprender a construir la herramienta, no para sacar conclusiones sobre personas reales.

## Qué hay en este repositorio

| Archivo | Para qué sirve |
| --- | --- |
| `app_01_basica.py` | App básica: título, carga del CSV e indicadores |
| `app_02_grafico.py` | App con gráficos: añadimos un gráfico de barras |
| `app.py` | App completa: filtros, dos gráficos y tabla |
| `encuesta_bienestar_digital.csv` | 200 respuestas ficticias |
| `requirements.txt` | Librerías necesarias |
| `railway.json` · `.python-version` | Configuración para publicar la app en Railway |

### Columnas del CSV

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `id_respuesta` | número | Identificador de la respuesta |
| `grupo_edad` | categoría | 18-24, 25-34, 35-44, 45+ |
| `plataforma` | categoría | Plataforma que más usa: Instagram, TikTok, YouTube, WhatsApp, Otras |
| `actividad` | categoría | Uso principal: Aprender, Entretenimiento, Trabajo, Conectar con otras personas |
| `horas_pantalla` | decimal | Horas de pantalla al día |
| `horas_sueno` | decimal | Horas de sueño por noche |
| `bienestar` | entero 1-10 | Autovaloración del bienestar digital |

## Cómo ejecutarla en tu ordenador

Necesitas **Python 3.10 o superior** y un editor (por ejemplo, VS Code).

```bash
# 1. Entra en la carpeta
cd taller-streamlit-pulso-digital

# 2. Crea el entorno virtual
python -m venv .venv
```

Activa el entorno:

- **Windows (PowerShell):** `.\.venv\Scripts\Activate.ps1`
- **macOS / Linux:** `source .venv/bin/activate`

```bash
# 3. Instala las librerías
python -m pip install -r requirements.txt

# 4. Arranca la app (prueba también app_01_basica.py y app_02_grafico.py)
streamlit run app.py
```

Se abrirá en el navegador en `http://localhost:8501`. Para pararla: `Ctrl + C` en la terminal.

## Las ideas clave

1. **Interfaz:** `st.title`, `st.write`, `st.subheader` escriben en la página.
2. **Datos:** `pd.read_csv()` carga el CSV en un DataFrame (una fila = una respuesta, una columna = una variable).
3. **Interacción:** `st.sidebar.multiselect` crea filtros en la barra lateral.
4. **Cálculos:** `len()` cuenta, `.mean()` calcula medias, `.groupby()` agrupa.
5. **Visualización:** `st.metric`, `st.bar_chart`, `st.scatter_chart`, `st.dataframe`.

**Lo más importante:** cada vez que cambias un filtro, Streamlit vuelve a ejecutar el script de arriba abajo y todo se actualiza solo.

## Publicarla en internet (Railway)

Deberás subir todo el directorio del proyecto realizado a GitHub y hacer el repositorio público.

El repositorio ya trae la configuración. Resumen:

1. Entra en [railway.com](https://railway.com) con tu cuenta de GitHub.
2. **New Project → Deploy from GitHub repo** → elige este repositorio.
3. Cuando termine el despliegue: **Settings → Networking → Generate Domain**.
4. Abre la URL `https://….up.railway.app` y comparte tu app.

La guía detallada está en el repositorio del reto (`DESPLIEGUE_RAILWAY.md`).

## Para seguir aprendiendo

- [Documentación de Streamlit](https://docs.streamlit.io)
- [Galería de apps de Streamlit](https://streamlit.io/gallery)
- [Documentación de Railway](https://docs.railway.com)
- [Lovable](https://lovable.dev): prototipar interfaces describiéndolas en lenguaje natural
# taller_f5_librerias
