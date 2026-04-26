import streamlit as st
import pandas as pd
from streamlit_pivot import st_pivot_table
from animacion.animacion import render_animation 
import sqlite3
import os

# Configuración inicial de la página web de Streamlit
# Define el título de la pestaña del navegador y usa todo el ancho de la pantalla (layout="wide")
st.set_page_config(page_title="Análisis con Pivot Table", layout="wide")

# Validar que el usuario haya pasado por el login
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Debes iniciar sesión para acceder a esta página.")
    st.switch_page("main.py") # Cambia "main.py" por el nombre exacto de tu archivo de login

# A partir de aquí va el código protegida
# Botón para cerrar sesión desde la app
if st.sidebar.button(":material/logout: Cerrar Sesión"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("main.py")

# --- FUNCIÓN DE RESET ---
def reset_parametros():
    """
    Limpia el estado de la aplicación.
    
    Itera sobre todas las variables almacenadas en la sesión de Streamlit (st.session_state)
    y elimina aquellas que comiencen con el prefijo "pt_" (parámetros del pivot table).
    Esto devuelve la barra lateral y la tabla a sus valores por defecto.
    """
    for key in list(st.session_state.keys()):
        if key.startswith("pt_"):
            del st.session_state[key]

render_animation()

st.markdown("""
    <style>
    h1 { color: #FFD700 !important; font-weight: 700 !important; font-size: 2.8rem !important; margin-bottom: 0.5rem !important; }
    h2, h3 { color: #E1AD01 !important; font-weight: 600 !important; margin-top: 1rem !important; }
    code { color: #F4A261 !important; background-color: #112B3C !important; font-family: 'Courier New', monospace !important; padding: 0.2rem 0.4rem !important; border-radius: 4px !important; }
    [data-testid="stMetricValue"] { color: #D4A017 !important; }
    [data-testid="stMetricLabel"] { color: #E0E1DD !important; }
    </style>
    """, unsafe_allow_html=True)

st.divider()
# --- HEADER INFORMATIVO DISCRETO ---
def get_system_stats():
    # Asegúrate de que la ruta a la DB sea correcta desde la carpeta /pages
    db_path = os.path.join(os.path.dirname(__file__), "..", "users.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    total = c.fetchone()[0]
    conn.close()
    return total

total_registrados = get_system_stats()

# Creamos dos columnas: una ancha para el título y una pequeña para las métricas
col_titulo, col_stats = st.columns([3, 1])


with col_titulo:
    #st.info(f"Dashboard análisis de datos ")
    st.info(f"Análisis activo para: **{st.session_state.username.upper()}**")

with col_stats:
    # Inyectamos CSS para que las métricas se vean pequeñas y alineadas a la derecha
    st.markdown(f"""
        <div style="
            text-align: right; 
            padding: 10px; 
            border-radius: 5px; 
            background-color: rgba(17, 43, 60, 0.5);
            border: 1px solid #1a1a1f;
            line-height: 1.2;
        ">
            <span style="color: #E1AD01; font-size: 0.7rem; font-weight: bold; text-transform: uppercase;">Estado del Sistema</span><br>
            <span style="color: #e0e0e0; font-size: 0.8rem;">👥 Usuarios: <b>{total_registrados}</b></span><br>
            <span style="color: #4af626; font-size: 0.8rem;">🔒 2FA: <b>Activo</b></span><br>
            <span style="color: #2196f3; font-size: 0.8rem;">🗄️ DB: <b>Online</b></span>
        </div>
    """, unsafe_allow_html=True)

st.divider()

st.subheader(":blue[:material/pivot_table_chart:] Análisis de datos con :blue-background[Pivot Table]")
st.subheader(f"Usuario logueado : {st.session_state.username}")
st.info("Contenido confidencial cargado correctamente.")
st.markdown("""
1. **Controlado por Sidebar**: Modifica el estado del componente forzando parámetros desde Streamlit.
2. **Pivot Libre**: Muestra el componente en su estado natural (Auto-Detect), permitiéndote arrastrar, soltar, filtrar y usar los menús internos de la tabla directamente en la interfaz.
""")

#-------------------------------------------------------------------------------------
# --- FUNCIÓN OPTIMIZADA CON CACHÉ ---
@st.cache_data(show_spinner="Procesando archivo...")
def load_data(file):
    """
    Carga el archivo y realiza las extracciones básicas.
    Streamlit guardará el resultado en memoria y no volverá a leer el archivo
    a menos que el archivo cambie.
    """
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    
    # Extraer columnas aquí también ayuda al rendimiento
    columnas = df.columns.tolist()
    num_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    return df, columnas, num_cols

# ----------------- BARRA LATERAL (SIDEBAR) -----------------
st.sidebar.subheader("1. Cargar Datos")
# Widget para subir archivos. Acepta formatos de texto (CSV) y hojas de cálculo (Excel).
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV o Excel", type=["csv", "xlsx", "xls"])

if uploaded_file:
    try:
        # --- TRANSFORMACIONES Y LECTURA DE DATOS CON PANDAS --- 
        # LLAMADA A LA FUNCIÓN CACHEADA
        df, columnas, num_cols = load_data(uploaded_file)       
        # 1. Lectura del archivo: Dependiendo de la extensión, usamos una función distinta de pandas.
        if uploaded_file.name.endswith('.csv'):
            # pd.read_csv convierte un archivo de texto separado por comas en un DataFrame (tabla bidimensional).
            df = pd.read_csv(uploaded_file)
        else:
            # pd.read_excel convierte un archivo de Excel en un DataFrame.
            df = pd.read_excel(uploaded_file)
            
        # 2. Extracción de nombres de columnas
        # df.columns devuelve los nombres de las columnas. .tolist() los convierte en una lista estándar de Python.
        columnas = df.columns.tolist()
        
        # 3. Filtrado por tipo de dato (Transformación clave)
        # select_dtypes(include=['number']) filtra el DataFrame dejando solo las columnas numéricas (int, float).
        # Esto es vital porque operaciones como promedios o escalas de color solo tienen sentido con números.
        num_cols = df.select_dtypes(include=['number']).columns.tolist()

        # Botón para ejecutar la función de reseteo definida arriba
        st.sidebar.button(":material/display_settings: Resetear Sidebar", on_click=reset_parametros, type="primary", width='stretch')
        st.sidebar.divider()

        # ----------------- OPCIONES DEL PIVOT TABLE -----------------
        st.sidebar.subheader("2. Dimensiones y Métricas (Solo para Tab 1)")
        
        # Selectores múltiples para decidir qué datos van en filas, columnas y qué se va a calcular.
        rows = st.sidebar.multiselect("Filas (rows)", options=columnas, key="pt_rows")
        columns = st.sidebar.multiselect("Columnas (columns)", options=columnas, key="pt_columns")
        values = st.sidebar.multiselect("Valores (values)", options=columnas, key="pt_values")
        
        # ----------------- PARÁMETROS DE COMPORTAMIENTO -----------------
        st.sidebar.subheader("3. Parámetros Avanzados")
        
        # Selector de la función de agregación matemática (suma, promedio, conteo, etc.)
        aggregation = st.sidebar.selectbox("Agregación (aggregation)", 
            options=["sum", "avg", "count", "min", "max", "median", "first", "last"], key="pt_agg")
        
        # Opciones booleanas (True/False) representadas con casillas de verificación (checkboxes)
        show_totals = st.sidebar.checkbox("Mostrar Totales Generales (show_totals)", value=True, key="pt_totals")
        show_subtotals = st.sidebar.checkbox("Habilitar Subtotales (Requerido para agrupar/colapsar)", value=True, key="pt_subtotals")
        sticky_headers = st.sidebar.checkbox("Fijar encabezados (sticky_headers)", value=True, key="pt_sticky")
        
        # ----------------- FORMATO CONDICIONAL -----------------
        st.sidebar.subheader("4. :material/format_list_bulleted_add: Formato Condicional")
        st.sidebar.caption("Selecciona qué columnas numéricas aplicarán para cada formato.")
        
        # -- A. DATA BARS (Barras horizontales dentro de la celda según su valor) --
        st.sidebar.subheader("A. Data Bars (Barras de relleno)")
        # Nota: Aquí usamos la lista 'num_cols' que filtramos previamente con pandas
        db_cols = st.sidebar.multiselect("Columnas para Data Bars", options=num_cols, key="pt_db_cols")
        if db_cols:
            db_color = st.sidebar.color_picker("Color de barra", value="#1976d2", key="pt_db_color")

        # -- B. COLOR SCALE (Mapa de calor) --
        st.sidebar.subheader("B. Color Scale (Escala de color)")
        cs_cols = st.sidebar.multiselect("Columnas para Color Scale", options=num_cols, key="pt_cs_cols")
        if cs_cols:
            col1, col2 = st.sidebar.columns(2)
            cs_min = col1.color_picker("Color Min", value="#1b2e1b", key="pt_cs_min")
            cs_max = col2.color_picker("Color Max", value="#4caf50", key="pt_cs_max")

        # -- C. THRESHOLD (Cambio de color si supera o es menor a un valor umbral) --
        st.sidebar.subheader("C. Threshold (Umbral)")
        th_cols = st.sidebar.multiselect("Columnas para Threshold", options=num_cols, key="pt_th_cols")
        if th_cols:
            # Diccionario para mapear símbolos matemáticos con los operadores que entiende la librería
            op_map = {
                "> (Mayor que)": "gt",
                "< (Menor que)": "lt",
                "= (Igual a)": "eq",
                ">= (Mayor o igual)": "gte",
                "<= (Menor o igual)": "lte"
            }
            th_op_label = st.sidebar.selectbox("Condición", options=list(op_map.keys()), index=0, key="pt_th_op")
            th_val = st.sidebar.number_input("Valor límite", value=1000.0, key="pt_th_val")
            th_bg = st.sidebar.color_picker("Color de fondo de celda", value="#1565c0", key="pt_th_bg")
            th_bold = st.sidebar.checkbox("Texto en Negrita", value=True, key="pt_th_bold")

        # ----------------- INTERACCIÓN Y TAMAÑO -----------------
        st.sidebar.subheader("5. Interacción")
        interactive = st.sidebar.checkbox("Modo interactivo (interactive)", value=True, key="pt_interactive")
        locked = st.sidebar.checkbox("Bloquear configuración (locked)", value=False, key="pt_locked")
        enable_drilldown = st.sidebar.checkbox("Habilitar detalle al clic (drilldown)", value=True, key="pt_drill")
        
        max_height = st.sidebar.number_input("Altura máxima (max_height)", min_value=200, max_value=1500, value=500, step=50, key="pt_height")

        # ----------------- RENDERIZAR VISTAS EN PESTAÑAS -----------------
        st.divider()
        
        # Crear los dos Tabs (pestañas) para organizar la vista principal
        tab_controlado, tab_libre = st.tabs([":material/pivot_table_chart: Pivot Controlado por Sidebar", ":material/crop_free: Pivot Libre (Interacción Natural)"])

        # ==========================================
        # TAB 1: PIVOT CONTROLADO POR SIDEBAR
        # ==========================================
        with tab_controlado:
            st.subheader("Modo Parametrizado")
            st.info("La vista de este pivot se sobreescribe cada vez que cambias algo en la barra lateral.")
            
            # Construir un diccionario con los argumentos base configurados en la barra lateral
            pivot_kwargs = {
                "key": "pivot_dinamico",
                "aggregation": aggregation,
                "show_totals": show_totals,
                "show_subtotals": show_subtotals,
                "interactive": interactive,
                "locked": locked,
                "sticky_headers": sticky_headers,
                "enable_drilldown": enable_drilldown,
                "max_height": int(max_height)
            }
            
            # Agregar dinámicamente las dimensiones solo si el usuario seleccionó alguna
            if rows: pivot_kwargs["rows"] = rows
            if columns: pivot_kwargs["columns"] = columns
            if values: pivot_kwargs["values"] = values

            # Compilar lista de Formato Condicional basada en las selecciones
            cf_list =[]
            if db_cols: cf_list.append({"type": "data_bars", "apply_to": db_cols, "color": db_color, "fill": "gradient"})
            if cs_cols: cf_list.append({"type": "color_scale", "apply_to": cs_cols, "min_color": cs_min, "max_color": cs_max})
            if th_cols: cf_list.append({"type": "threshold", "apply_to": th_cols, "conditions":[{"operator": op_map[th_op_label], "value": th_val, "background": th_bg, "bold": th_bold}]})

            # Si hay formatos condicionales, los añadimos a los argumentos
            if cf_list:
                pivot_kwargs["conditional_formatting"] = cf_list

            # Llamada al componente final pasando el DataFrame (procesado por pandas) y desempaquetando los argumentos (**)
            st_pivot_table(df, **pivot_kwargs)

        # ==========================================
        # TAB 2: PIVOT LIBRE (AUTO-DETECT)
        # ==========================================
        with tab_libre:
            st.subheader("Modo Interacción Natural (UI)")
            st.info("""
            Este componente se carga "limpio". **Usa la propia interfaz de la tabla**:
            * Haz clic en **'Rows / Columns / Values'** dentro del componente para arrastrar las columnas.
            * Usa la **tuerca (⚙)** arriba a la derecha para exportar o cambiar densidades.
            * Haz clic en los **embudos** para filtrar datos.
            * Esta pestaña ignora los parámetros del menú izquierdo.
            """)
            
            # Llamada al componente SIN parámetros adicionales (solo el Dataframe y una key única).
            # Importante: Streamlit requiere un 'key' distinto para evitar conflictos cuando se usa el mismo componente varias veces.
            st_pivot_table(df, key="pivot_libre")

    except Exception as e:
        # Manejo de errores: Si el archivo está corrupto o hay un error, se muestra en pantalla amigablemente.
        st.error(f"Error al procesar el archivo o mostrar el Pivot Table: {e}")
else:
    # Mensaje por defecto cuando no se ha subido ningún archivo aún.
    st.info(":material/data_object: Por favor, carga un archivo CSV o Excel en la barra lateral izquierda para comenzar.")