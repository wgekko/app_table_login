import streamlit as st
import sqlite3
import pyotp
import qrcode
import bcrypt
import time
from io import BytesIO
import os
import streamlit.components.v1 as components

# ==========================================
# 1. CONFIGURACIÓN E INICIALIZACIÓN
# ==========================================
# Esto SIEMPRE debe ser la primera línea de código de Streamlit
st.set_page_config(page_title="Login Seguro 2FA", page_icon=":material/shield_lock:", layout="centered")

def sentinel_v7():
    video_sources = [
        "https://mattcannon.games/codepen/glitches/cam1.mp4",
        "https://mattcannon.games/codepen/glitches/cam2.mp4",
        "https://mattcannon.games/codepen/glitches/cam3.mp4",
        "https://mattcannon.games/codepen/glitches/cam4.mp4",
        "https://mattcannon.games/codepen/glitches/cam5.mp4",
        "https://mattcannon.games/codepen/glitches/cam6.mp4"
    ]
    
    locations = ["MAIN ENTRANCE", "RECEPTION", "HALLWAY", "SERVER ROOM", "PARKING", "LOBBY"]

    html_code = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
        <style>
            :root {{
                --primary-bg: #0e0e12;
                --accent-blue: #2196f3;
                --error: #f44336;
                --text: #e0e0e0;
                --terminal-green: #4af626;
            }}

            body {{
                margin: 0; padding: 0;
                background-color: transparent;
                font-family: 'Share Tech Mono', monospace;
                color: var(--text);
                display: flex;
                justify-content: center;
                overflow: hidden;
            }}

            .security-system {{
                width: 98vw;
                max-width: 1200px;
                display: flex;
                flex-direction: column;
                gap: 8px;
                padding: 10px;
                background: var(--primary-bg);
                border: 1px solid #1a1a1f;
            }}

            .system-header {{
                display: flex;
                justify-content: space-between;
                border-bottom: 1px solid var(--accent-blue);
                padding-bottom: 5px;
            }}

            .glitch-text {{
                font-size: 20px;
                font-weight: bold;
                color: var(--accent-blue);
                letter-spacing: 2px;
            }}

            .camera-grid {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 8px;
            }}

            .camera-feed {{
                background: #000;
                border: 1px solid rgba(255,255,255,0.1);
                position: relative;
                display: flex;
                flex-direction: column;
                cursor: pointer;
            }}

            .camera-header, .camera-footer {{
                background: rgba(0, 0, 0, 0.8);
                padding: 3px 8px;
                font-size: 9px;
                display: flex;
                justify-content: space-between;
                z-index: 10;
            }}

            /* AJUSTE DE PROPORCIÓN 5/8 (Más bajo y compacto) */
            .camera-content {{
                position: relative;
                height: 100px; 
                overflow: hidden;
            }}

            video {{
                width: 100%; height: 100%;
                object-fit: cover;
                filter: grayscale(1) contrast(1.2);
                transition: filter 0.5s ease;
            }}

            video.color-mode {{
                filter: grayscale(0) contrast(1) brightness(1.1);
            }}

            .camera-feed.fullscreen {{
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                z-index: 9999;
            }}
            .camera-feed.fullscreen .camera-content {{ height: 100vh; }}

            .control-panel {{
                display: grid;
                grid-template-columns: 1fr auto;
                gap: 10px;
            }}

            .log-terminal {{
                background: rgba(0,0,0,0.9);
                border: 1px solid rgba(33, 150, 243, 0.2);
                height: 70px; /* Reducido para mantener la proporción */
                padding: 8px;
                font-size: 9px;
                color: var(--terminal-green);
                overflow-y: hidden;
                position: relative;
                line-height: 1.1;
            }}

            .controls-group {{
                display: flex;
                flex-direction: column;
                gap: 4px;
            }}

            .control-btn {{
                background-color: var(--accent-blue);
                color: #000;
                border: none;
                border-radius: 2px;
                padding: 6px 12px;
                font-family: inherit;
                font-size: 10px;
                font-weight: bold;
                cursor: pointer;
                text-transform: uppercase;
                width: 120px;
                text-align: center;
            }}

            .scan-line {{
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background: linear-gradient(to bottom, transparent 50%, rgba(0,0,0,0.1) 50%);
                background-size: 100% 2px;
                pointer-events: none;
                z-index: 5;
            }}
        </style>
    </head>
    <body>

    <div class="security-system">
        <header class="system-header">
            <div>
                <div class="glitch-text">SENTINEL</div>
                <div style="font-size:8px; opacity:0.6">PROPORTIONAL VIEW 5:8 // ONLINE</div>
            </div>
            <div style="text-align: right; font-size: 10px;">
                <span style="color:var(--error)">THREAT: LOW</span><br>
                <span>TIME: <span id="clock">00:00:00</span></span>
            </div>
        </header>

        <div class="camera-grid">
            {"".join([f'''
            <div class="camera-feed" onclick="toggleZoom(this)">
                <div class="camera-header">
                    <span>CAM_0{i+1}</span>
                    <span style="color:{'#4caf50' if i in [2,4] else 'var(--error)'}">● {'OFFLINE' if i in [2,4] else 'LIVE'}</span>
                </div>
                <div class="camera-content">
                    <video src="{video_sources[i]}" muted loop autoplay playsinline></video>
                    <div class="scan-line"></div>
                </div>
                <div class="camera-footer">{locations[i]}</div>
            </div>
            ''' for i in range(6)])}
        </div>

        <div class="control-panel">
            <div class="log-terminal" id="log-box"></div>
            <div class="controls-group">
                <button class="control-btn" onclick="toggleColorAll()">Color Mode</button>
                <button class="control-btn" onclick="location.reload()">Reset</button>
            </div>
        </div>
    </div>

    <script>
        setInterval(() => {{
            document.getElementById('clock').innerText = new Date().toLocaleTimeString();
        }}, 1000);

        let isColor = false;
        function toggleColorAll() {{
            isColor = !isColor;
            document.querySelectorAll('video').forEach(v => v.classList.toggle('color-mode', isColor));
        }}

        function toggleZoom(el) {{
            if (!el.classList.contains('fullscreen')) {{
                el.classList.add('fullscreen');
                gsap.from(el, {{ duration: 0.3, scale: 0.9, opacity: 0 }});
            }} else {{
                gsap.to(el, {{ duration: 0.2, opacity: 0, onComplete: () => {{
                    el.classList.remove('fullscreen');
                    gsap.set(el, {{ opacity: 1 }});
                }}}});
            }}
        }}

        const logBox = document.getElementById('log-box');
        const phrases = ["PKT_RECV", "0x" + Math.random().toString(16).slice(2,6).toUpperCase(), "PORT_SCAN", "AUTH_GRNT", "CORE_SYNC", "NET_ACTIVE"];

        function addRandomLog() {{
            const time = new Date().toLocaleTimeString().split(' ')[0];
            const msg = phrases[Math.floor(Math.random() * phrases.length)];
            const newLog = document.createElement('div');
            newLog.innerHTML = `> [${{time}}] ${{msg}}`;
            logBox.prepend(newLog);
            if (logBox.children.length > 8) logBox.removeChild(logBox.lastChild);
            setTimeout(addRandomLog, Math.random() * 300 + 100);
        }}
        addRandomLog();
    </script>
    </body>
    </html>
    """
    # Altura del componente reducida para que los cálculos aparezcan justo debajo
    components.html(html_code, height=440)


sentinel_v7()

st.markdown("""
    <style>
    h1 { color: #FFD700 !important; font-weight: 700 !important; font-size: 2.8rem !important; margin-bottom: 0.5rem !important; }
    h2, h3 { color: #E1AD01 !important; font-weight: 600 !important; margin-top: 1rem !important; }
    code { color: #F4A261 !important; background-color: #112B3C !important; font-family: 'Courier New', monospace !important; padding: 0.2rem 0.4rem !important; border-radius: 4px !important; }
    [data-testid="stMetricValue"] { color: #D4A017 !important; }
    [data-testid="stMetricLabel"] { color: #E0E1DD !important; }
    </style>
    """, unsafe_allow_html=True)

# Inicializar estados de sesión compartidos para toda la app
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""

# ==========================================
# NUEVO: OCULTAR EL MENÚ LATERAL SI NO HAY SESIÓN
# ==========================================
if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )    

# ==========================================
# 2. LÓGICA DE BASE DE DATOS (COMPARTIDA)
# ==========================================
def init_db():
    DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT,
            totp_secret TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT password_hash, totp_secret FROM users WHERE username = ?', (username,))
    data = c.fetchone()
    conn.close()
    return data

def create_user(username, password, totp_secret):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        c.execute('INSERT INTO users (username, password_hash, totp_secret) VALUES (?, ?, ?)', 
                (username, password_hash, totp_secret))
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False
    conn.close()
    return success

# Ejecutar inicialización al arrancar
init_db()

def get_system_stats():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    # Contamos el total de usuarios registrados
    c.execute('SELECT COUNT(*) FROM users')
    total_users = c.fetchone()[0]
    conn.close()
    return total_users


# ==========================================
# 3. BARRA LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.subheader(":material/key: Panel de Control")
    st.divider()
    if st.session_state.logged_in:
        st.success(f"Sesión activa: {st.session_state.username}")
        if st.button("Cerrar Sesión", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.rerun()
    else:
        st.info("Debe iniciar sesión para acceder al Dashboard.")
        with st.expander("Información del Sistema"):
            st.write("Sistema unificado utilizando SQLite, Bcrypt y PyOTP.")

# ==========================================
# 4. INTERFAZ PRINCIPAL (RUTEO)
# ==========================================
# CASO A: USUARIO YA ESTÁ AUTENTICADO (Ve el Dashboard)

if st.session_state.logged_in:
    # Obtenemos los datos reales
    total_registrados = get_system_stats()
    hora_entrada = st.session_state.get('login_time', "N/A")
    st.subheader(f"Bienvenido, {st.session_state.username}")
    st.title(f"Bienvenido, {st.session_state.username}")
    st.markdown(f"**Sesión iniciada a las:** `{hora_entrada}`")
    
    st.divider()
    
    st.subheader("Estado Global del Sistema")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Mostramos el total de usuarios en la DB
        st.metric("Usuarios en DB", total_registrados, delta="Sincronizado")
    
    with col2:
        # Un indicador de salud de la conexión
        db_status = "Online" if os.path.exists("users.db") else "Error"
        st.metric("Base de Datos", db_status, delta="SQLite3")
        
    with col3:
        # Nivel de seguridad basado en la sesión activa
        st.metric("Seguridad 2FA", "ACTIVA", delta="Protegido", delta_color="normal")

    st.info("Utiliza el menú lateral para navegar a las herramientas de análisis o cerrar la sesión.")
    
    #st.success("Acceso concedido. Estás en el área protegida.")
    #st.markdown("---")
    
    # st.subheader("Visualización de Datos Críticos")
    # st.info("Aquí puedes integrar tus modelos de Machine Learning, Dashboards de Finanzas o reportes operativos.")
    
    # col1, col2 = st.columns(2)
    # with col1:
    #     st.metric("Estado del Servidor", "Activo", delta="100%")
    # with col2:
    #     st.metric("Nivel de Seguridad", "Máximo", delta="TOTP Activo")

# CASO B: USUARIO NO AUTENTICADO (Ve las opciones de Login en Expanders)
else:
    st.subheader("Portal de Acceso Protegido")
    st.write("Selecciona la interfaz de inicio de sesión de tu preferencia:")

    # ---------------------------------------------------------
    # EXPANDER 1: LOGIN ESTÁNDAR (El código de tu login.py original)
    # ---------------------------------------------------------
    with st.expander(":material/login: Versión 1: Interfaz Google Authenticator", expanded=False):
        tab1_v1, tab2_v1 = st.tabs([":material/start: Iniciar Sesión", ":material/add_ad: Crear Cuenta"])
        
        with tab1_v1:
            with st.form("login_form_v1"):
                # NOTA: Usamos key="..." para que no choque con la versión 2
                login_user_1 = st.text_input("Usuario", key="user_v1")
                login_pass_1 = st.text_input("Contraseña", type="password", key="pass_v1")
                login_totp_1 = st.text_input("Segundo factor (6 dígitos)", max_chars=6, key="totp_v1")
                submit_login_1 = st.form_submit_button("Acceder")
                
                if submit_login_1:
                    if login_user_1 and login_pass_1 and login_totp_1:
                        user_data = get_user_data(login_user_1)
                        if user_data:
                            stored_hash, totp_secret = user_data
                            if bcrypt.checkpw(login_pass_1.encode('utf-8'), stored_hash.encode('utf-8')):
                                totp = pyotp.TOTP(totp_secret)
                                if totp.verify(login_totp_1, valid_window=1):    
                                    st.session_state.logged_in = True
                                    st.session_state.username = login_user_1
                                    st.session_state.login_time = time.strftime("%H:%M:%S")
                                    st.switch_page("pages/analytics.py")
                                    #st.rerun()
                                else:
                                    st.error("Código 2FA inválido.")
                            else:
                                st.error("Credenciales inválidas.")
                        else:
                            st.error("Credenciales inválidas.")
                    else:
                        st.warning("Completa todos los campos.")
                        
        with tab2_v1:
            with st.form("register_form_v1"):
                reg_user_1 = st.text_input("Usuario", key="reg_user_v1")
                reg_pass_1 = st.text_input("Contraseña Segura", type="password", key="reg_pass_v1")
                submit_register_1 = st.form_submit_button("Registrar Cuenta")
                
                if submit_register_1:
                    if reg_user_1 and reg_pass_1:
                        totp_secret = pyotp.random_base32()
                        if create_user(reg_user_1, reg_pass_1, totp_secret):
                            st.success("Cuenta creada exitosamente.")
                            totp = pyotp.TOTP(totp_secret)
                            provisioning_uri = totp.provisioning_uri(name=reg_user_1, issuer_name="App Segura")
                            
                            st.info("Escanea este QR con tu App Authenticator:")
                            qr = qrcode.make(provisioning_uri)
                            buf = BytesIO()
                            qr.save(buf)
                            st.image(buf.getvalue(), width=200)
                            st.write("O ingresa manualmente este código secreto:")
                            st.code(totp_secret)
                        else:
                            st.error("El usuario ya existe.")
                    else:
                        st.warning("Completa todos los campos.")

    # ---------------------------------------------------------
    # EXPANDER 2: LOGIN AVANZADO (El código de tu login2.py original)
    # ---------------------------------------------------------
    with st.expander(":material/login: Versión 2: Interfaz con Generador Interno de Tokens", expanded=False):
        tab1_v2, tab2_v2, tab3_v2 = st.tabs([":material/start: Iniciar Sesión", ":material/add_ad: Crear Cuenta", ":material/contextual_token: Generador de Tokens"])

        with tab1_v2:
            with st.form("login_form_v2"):
                login_user_2 = st.text_input("Usuario", key="user_v2")
                login_pass_2 = st.text_input("Contraseña", type="password", key="pass_v2")
                login_totp_2 = st.text_input("Código de 6 dígitos", max_chars=6, key="totp_v2")
                submit_login_2 = st.form_submit_button("Entrar")
                
                if submit_login_2:
                    if login_user_2 and login_pass_2 and login_totp_2:
                        user_data = get_user_data(login_user_2)
                        if user_data:
                            stored_hash, totp_secret = user_data
                            if bcrypt.checkpw(login_pass_2.encode('utf-8'), stored_hash.encode('utf-8')):
                                totp = pyotp.TOTP(totp_secret)
                                if totp.verify(login_totp_2, valid_window=1):
                                    st.session_state.logged_in = True
                                    st.session_state.username = login_user_2
                                    st.session_state.login_time = time.strftime("%H:%M:%S")
                                    st.switch_page("pages/analytics.py")
                                    #st.rerun()
                                else:
                                    st.error("Código 2FA incorrecto o expirado.")
                            else:
                                st.error("Contraseña incorrecta.")
                        else:
                            st.error("El usuario no existe.")
                    else:
                        st.warning("Completa todos los campos.")

        with tab2_v2:
            with st.form("register_form_v2"):
                reg_user_2 = st.text_input("Nombre de Usuario", key="reg_user_v2")
                reg_pass_2 = st.text_input("Nueva Contraseña", type="password", key="reg_pass_v2")
                submit_register_2 = st.form_submit_button("Generar Cuenta y Secreto")
                
                if submit_register_2:
                    if reg_user_2 and reg_pass_2:
                        totp_secret = pyotp.random_base32()
                        if create_user(reg_user_2, reg_pass_2, totp_secret):
                            st.success("Cuenta creada.")
                            st.write("Tu Secreto (GUÁRDALO BIEN):")
                            st.code(totp_secret)
                        else:
                            st.error("El usuario ya está registrado.")
                    else:
                        st.warning("Completa todos los campos.")

        with tab3_v2:
            st.subheader("Mi Generador Interno de Tokens")
            st.write("Usa esta herramienta si no tienes el celular a mano. Pega tu código secreto.")
            
            my_secret = st.text_input("Ingresa tu Secreto Base32", type="password", key="auth_tool_v2")
            
            if my_secret:
                try:
                    totp_gen = pyotp.TOTP(my_secret)
                    token = totp_gen.now()
                    segundos_restantes = 30 - (int(time.time()) % 30)
                    
                    st.markdown(f"### Código Actual: `{token}`")
                    st.progress(segundos_restantes / 30)
                    st.write(f"Válido por {segundos_restantes} segundos más.")
                    
                    if st.button("Actualizar Código", key="btn_update_v2"):
                        st.rerun()
                except Exception:
                    st.error("Secreto inválido. Asegúrate de que sea el código Base32.")


                    