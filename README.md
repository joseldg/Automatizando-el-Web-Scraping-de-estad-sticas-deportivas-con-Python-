# 📊 HTML Table Processor to Pandas

Una solución robusta y profesional en Python para extraer datos tabulares de sitios web complejos (como FanGraphs, Baseball-Reference o portales de noticias financieras) y convertirlos automáticamente en DataFrames de **Pandas**.

Esta herramienta está diseñada para manejar las dificultades comunes del web scraping, como XPaths dinámicos, encabezados complejos y la necesidad de limpiar datos crudos al instante.

## ✨ Características Principales

- **🛡️ Evasión de Bloqueos:** Configurado con headers de navegador real para evitar errores de tipo `403 Forbidden`.
- **🧩 XPaths Dinámicos:** Permite inyectar el nombre de la clase de la tabla para localizar datos en estructuras HTML cambiantes.
- **📈 Integración Directa con Pandas:** Convierte filas y celdas HTML en un DataFrame estructurado en un solo paso.
- **🧹 Post-procesamiento Inteligente:** Soporta el mapeo de columnas y el parseo de tipos de datos (fechas, porcentajes, números) mediante funciones auxiliares.
- **🔗 Soporte Multi-fuente:** Capacidad para extraer datos desde una URL activa, un archivo HTML local o un objeto de `lxml`.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Requests:** Para la gestión de peticiones HTTP.
- **LXML:** Para el parseo ultra rápido de documentos HTML/XML.
- **Pandas:** Para la manipulación y análisis de los datos extraídos.

## 🚀 Instalación y Uso

1. **Clona este repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/html-table-processor-python.git](https://github.com/TU_USUARIO/html-table-processor-python.git)
