# 📊 Dashboard Económico Argentina

Dashboard interactivo en tiempo real que muestra indicadores económicos clave de Argentina.

## 🚀 Características

- **Cotizaciones del Dólar**: Oficial, Blue, MEP y CCL en tiempo real
- **Brecha Cambiaria**: Análisis visual de las diferencias entre cotizaciones
- **Inflación**: Gráficos de evolución mensual
- **Riesgo País**: Indicadores de confianza económica
- **Actualización Automática**: Datos refrescados cada 5 minutos

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **Streamlit**: Framework para dashboards interactivos
- **Plotly**: Visualizaciones interactivas
- **Pandas**: Procesamiento de datos
- **DolarAPI**: API pública para cotizaciones

## 📦 Instalación Local

### Requisitos Previos
- Python 3.10 o superior
- pip

### Pasos

1. **Clona el repositorio**
```bash
git clone https://github.com/tu-usuario/economic-dashboard-arg.git
cd economic-dashboard-arg
```

2. **Crea un entorno virtual** (recomendado)
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecuta la aplicación**
```bash
streamlit run economic_dashboard.py
```

5. **Abre tu navegador**
La app se abrirá automáticamente en `http://localhost:8501`

## 🌐 Deploy en Streamlit Cloud (GRATIS)

1. **Sube tu código a GitHub**
   - Crea un repositorio en GitHub
   - Sube los archivos: `economic_dashboard.py` y `requirements.txt`

2. **Deploy en Streamlit Cloud**
   - Ve a [share.streamlit.io](https://share.streamlit.io)
   - Conecta tu cuenta de GitHub
   - Selecciona tu repositorio
   - Click en "Deploy"
   - ¡Listo! Tu app estará en línea en minutos

3. **URL Pública**
   Tu dashboard estará disponible en: `https://tu-usuario-economic-dashboard.streamlit.app`

## 📁 Estructura del Proyecto

```
economic-dashboard-arg/
├── economic_dashboard.py    # Aplicación principal
├── requirements.txt         # Dependencias
└── README.md               # Esta documentación
```

## 🔄 Actualización de Datos

- **Cotizaciones**: Se actualizan cada 5 minutos mediante cache
- **Inflación**: Datos mensuales (en producción se conectaría a API del INDEC)
- **Riesgo País**: Actualización en tiempo real

## 🎨 Personalización

### Cambiar Colores
Edita las secciones de `marker_color` en el código:
```python
marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
```

### Agregar Nuevos Indicadores
Crea nuevas funciones siguiendo el patrón:
```python
@st.cache_data(ttl=300)
def get_nuevo_indicador():
    # Tu lógica aquí
    return data
```

### Modificar Frecuencia de Actualización
Cambia el parámetro `ttl` (en segundos):
```python
@st.cache_data(ttl=300)  # 300 segundos = 5 minutos
```

## 📊 APIs Utilizadas

- **DolarAPI**: https://dolarapi.com
  - Endpoint: `https://dolarapi.com/v1/dolares`
  - Libre y gratuita, no requiere API key

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Mejoras Futuras

- [ ] Integración con API oficial del INDEC para inflación
- [ ] Datos históricos con mayor profundidad
- [ ] Predicciones usando modelos de ML
- [ ] Comparación con otros países de la región
- [ ] Alertas por email/Telegram
- [ ] Exportación de datos a Excel/PDF
- [ ] Modo oscuro/claro

## ⚠️ Disclaimer

Este dashboard es solo para fines informativos y educativos. Los datos mostrados son referenciales y no constituyen asesoramiento financiero. Para decisiones de inversión, consulte fuentes oficiales y profesionales habilitados.

## 📄 Licencia

MIT License - Libre para uso personal y comercial

## 👤 Autor

**Bautista Verna**
- LinkedIn: Bautista Verna(www.linkedin.com/in/bautista-verna)
- GitHub: BautistaVerna(https://github.com/BautistaVerna)
- Email: bautiverna@gmail.com

---

⭐ Si este proyecto te resultó útil, dale una estrella en GitHub!

**Hecho con ❤️ en Argentina usando Python y Streamlit**
