
  ## Financial Analytics Dashboard with Secure 2FA 
Este proyecto es una aplicación web de alto rendimiento desarrollada con **Python** y **Streamlit**, diseñada para entornos que requieren un balance crítico entre la **seguridad de grado corporativo** y la **agregación de datos compleja**.
La aplicación integra un sistema de autenticación multifactor (MFA) con capacidades de analítica interactiva mediante tablas dinámicas (Pivot Tables).
"## Características Principales
"### Seguridad Avanzada (Core de Acceso)
**Autenticación de Doble Factor (2FA):** Implementación de protocolos TOTP (Time-based One-Time Password) compatibles con Google Authenticator y Microsoft Authenticator.
**Hashing de Alta Seguridad:** Las credenciales nunca se almacenan en texto plano; se utiliza la librería `bcrypt` para el cifrado de contraseñas.
**Gestión de Sesiones:** Control de estado persistente mediante `streamlit.session_state` para proteger rutas y datos sensibles.
**Aprovisionamiento vía QR:** Generación dinámica de códigos QR para una vinculación rápida del dispositivo móvil del usuario.
"### Análisis de Datos (Dashboard)
**Pivot Tables Interactivas:** Motor de análisis basado en pandas que permite a los usuarios reestructurar y explorar grandes datasets en tiempo real.
**Visualización Dinámica:** Interfaz optimizada para transformar datos transaccionales en información accionable para la toma de decisiones financieras.
**Exportación en Memoria:** Manejo eficiente de objetos binarios para evitar la saturación del almacenamiento local.
"## Stack Tecnológico
**Lenguaje:** Python 3.x
**Framework:** Streamlit
**Base de Datos:** SQLite3 (Persistencia de usuarios y semillas TOTP)
**Criptografía:** Bcrypt & PyOTP
**Procesamiento de Datos:** Pandas
**Entorno:** Optimizado para sistemas operativos Linux
para configurar los estilos, tipo de letras y background 
se debe crear una carpeta .streamlit y dentro de ella colocar un archivo 'config.toml'
1ra opcion: 
""
[server]
enableStaticServing = false
[[theme.fontFaces]]
family = "Inter"
url = "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap"
[theme]
primaryColor = "#FF8C00"
backgroundColor = "#0D1B2A"
secondaryBackgroundColor = "#1B263B"
textColor = "#FFA500"
linkColor = "#FFA500"
borderColor = "#CCCCCC"
showWidgetBorder = true
baseRadius = "0.5rem"
buttonRadius = "0.5rem"
font = "Inter"
headingFontWeights = [600, 500]
headingFontSizes = ["2.5rem", "1.8rem"]
codeFont = "Courier New"
codeFontSize = "0.75rem"
codeBackgroundColor = "#112B3C"
showSidebarBorder = false
chartCategoricalColors = [
  "#FF8C00",  # Orange oscuro
  "#FFA500",  # Naranja clásico
  "#FFD700",  # Mostaza / dorado
  "#E1C16E",  # Mostaza claro
  "#C8E25D",  # Lima suave
  "#A8D08D",  # Verde pastel
  "#7AC36A",  # Verde hoja
  "#4CAF50",  # Verde medio
  "#40C4FF",  # Celeste vibrante
  "#00B0F0",  # Celeste profesional
  "#3399FF",  # Celeste más oscuro
  "#1E88E5",  # Azul Francia
  "#1976D2",  # Azul fuerte
  "#1565C0",  # Azul oscuro
  "#0D47A1",   # Azul muy profundo
  "#FF8C00",
  "#FFA500",
  "#FFB347",
  "#FFD580",
  "#FFA07A",
  "#FF7F50",
  "#FF6F00",
  "#CC7000",
  "#FFC107",
  "#FFDD57",
  "#E67E22",
  "#D35400",
  "#F39C12",
  "#E67E22",
  "#F4A261"
]
[theme.sidebar]
backgroundColor = "#1E3A5F"
secondaryBackgroundColor = "#1B263B"
headingFontSizes = ["1.6rem", "1.4rem", "1.2rem"]
dataframeHeaderBackgroundColor = "#1A2A40"
""
2da opcion: 
"" 
[server]
enableStaticServing = false
[[theme.fontFaces]]
# Tamaños de encabezados aumentados para usuarios con visión limitada
headingFontWeights = [700, 600]
headingFontSizes = ["3.2rem", "2.4rem", "1.8rem"]
# Configuración de código (para fórmulas o logs)
codeFont = "Courier New"
codeFontSize = "0.85rem"
codeBackgroundColor = "#112B3C"
showSidebarBorder = false
# Paleta de colores para gráficos (Optimizado para daltonismo y contraste)
chartCategoricalColors = [
  "#FF8C00", # Naranja
  "#00B0F0", # Celeste
  "#4CAF50", # Verde
  "#FFD700", # Oro
  "#E67E22", # Zanahoria
  "#5DADE2", # Azul claro
  "#A569BD", # Púrpura
  "#EC7063"  # Coral
]

[theme.sidebar]
# Sidebar más oscuro para jerarquía visual
backgroundColor = "#08111D"
secondaryBackgroundColor = "#1B263B"
# Encabezados de sidebar grandes
headingFontSizes = ["1.8rem", "1.6rem", "1.4rem"]
# Cabeceras de tablas en el sidebar
dataframeHeaderBackgroundColor = "#1A2A40"
""

"## Instalación y Uso
1. **Clonar el repositorio:**
   bash
   git clone : https://github.com/wgekko/app_table_login.git

video demo 

https://github.com/user-attachments/assets/62fc2be9-ea8d-4474-985b-0712c9dc2f29





