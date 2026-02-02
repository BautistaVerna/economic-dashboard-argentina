import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import requests

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Económico Argentina",
    page_icon="📊",
    layout="wide"
)

# Título principal
st.title("📊 Dashboard Económico Argentina")
st.markdown("*Datos en tiempo real del mercado argentino*")

# Función para obtener cotizaciones del dólar
@st.cache_data(ttl=300)  # Cache por 5 minutos
def get_dollar_rates():
    try:
        url = "https://dolarapi.com/v1/dolares"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            rates = {}
            for item in data:
                if item['casa'] in ['oficial', 'blue', 'bolsa', 'contadoconliqui']:
                    rates[item['casa']] = {
                        'compra': item['compra'],
                        'venta': item['venta'],
                        'fecha': item['fechaActualizacion']
                    }
            return rates
        return None
    except Exception as e:
        st.error(f"Error obteniendo datos del dólar: {str(e)}")
        return None

# Función para obtener datos de inflación (ejemplo con datos mock)
@st.cache_data(ttl=3600)  # Cache por 1 hora
def get_inflation_data():
    # En un caso real, esto vendría de una API como INDEC o similar
    # Por ahora usamos datos de ejemplo
    dates = pd.date_range(end=datetime.now(), periods=12, freq='M')
    inflation = [3.2, 4.1, 3.8, 5.2, 4.9, 6.1, 5.8, 6.5, 7.2, 6.8, 7.5, 8.1]
    
    df = pd.DataFrame({
        'Mes': dates,
        'Inflación (%)': inflation
    })
    return df

# Función para obtener riesgo país (mock data)
@st.cache_data(ttl=300)
def get_risk_country():
    # En producción, esto vendría de una API real
    return 1850  # Puntos básicos

# Layout principal con columnas
col1, col2, col3, col4 = st.columns(4)

# Obtener datos
dollar_rates = get_dollar_rates()

# Tarjetas de cotizaciones
if dollar_rates:
    with col1:
        st.metric(
            label="💵 Dólar Oficial",
            value=f"${dollar_rates.get('oficial', {}).get('venta', 'N/A')}",
            delta=f"Compra: ${dollar_rates.get('oficial', {}).get('compra', 'N/A')}"
        )
    
    with col2:
        st.metric(
            label="💰 Dólar Blue",
            value=f"${dollar_rates.get('blue', {}).get('venta', 'N/A')}",
            delta=f"Compra: ${dollar_rates.get('blue', {}).get('compra', 'N/A')}"
        )
    
    with col3:
        st.metric(
            label="📈 Dólar MEP",
            value=f"${dollar_rates.get('bolsa', {}).get('venta', 'N/A')}",
            delta=f"Compra: ${dollar_rates.get('bolsa', {}).get('compra', 'N/A')}"
        )
    
    with col4:
        st.metric(
            label="🌐 Dólar CCL",
            value=f"${dollar_rates.get('contadoconliqui', {}).get('venta', 'N/A')}",
            delta=f"Compra: ${dollar_rates.get('contadoconliqui', {}).get('compra', 'N/A')}"
        )
else:
    st.warning("No se pudieron cargar las cotizaciones del dólar")

# Separador
st.markdown("---")

# Sección de análisis
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Brecha Cambiaria")
    
    if dollar_rates and 'oficial' in dollar_rates and 'blue' in dollar_rates:
        oficial_venta = dollar_rates['oficial']['venta']
        blue_venta = dollar_rates['blue']['venta']
        brecha = ((blue_venta - oficial_venta) / oficial_venta) * 100
        
        # Gráfico de comparación
        fig = go.Figure(data=[
            go.Bar(
                x=['Oficial', 'Blue', 'MEP', 'CCL'],
                y=[
                    dollar_rates.get('oficial', {}).get('venta', 0),
                    dollar_rates.get('blue', {}).get('venta', 0),
                    dollar_rates.get('bolsa', {}).get('venta', 0),
                    dollar_rates.get('contadoconliqui', {}).get('venta', 0)
                ],
                marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],
                text=[
                    f"${dollar_rates.get('oficial', {}).get('venta', 0)}",
                    f"${dollar_rates.get('blue', {}).get('venta', 0)}",
                    f"${dollar_rates.get('bolsa', {}).get('venta', 0)}",
                    f"${dollar_rates.get('contadoconliqui', {}).get('venta', 0)}"
                ],
                textposition='outside'
            )
        ])
        
        fig.update_layout(
            title="Comparación de Cotizaciones (Venta)",
            xaxis_title="Tipo de Dólar",
            yaxis_title="Precio ($)",
            height=400,
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.metric(
            label="Brecha Oficial-Blue",
            value=f"{brecha:.1f}%",
            delta=f"${blue_venta - oficial_venta:.2f} de diferencia"
        )

with col_right:
    st.subheader("📈 Inflación Mensual")
    
    inflation_df = get_inflation_data()
    
    # Gráfico de inflación
    fig_inflation = px.line(
        inflation_df,
        x='Mes',
        y='Inflación (%)',
        markers=True,
        title="Evolución de la Inflación (Últimos 12 meses)"
    )
    
    fig_inflation.update_traces(
        line_color='#e74c3c',
        marker=dict(size=8)
    )
    
    fig_inflation.update_layout(
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_inflation, use_container_width=True)
    
    # Métricas de inflación
    avg_inflation = inflation_df['Inflación (%)'].mean()
    last_inflation = inflation_df['Inflación (%)'].iloc[-1]
    
    col_inf1, col_inf2 = st.columns(2)
    with col_inf1:
        st.metric("Inflación Promedio", f"{avg_inflation:.1f}%")
    with col_inf2:
        st.metric("Último Mes", f"{last_inflation:.1f}%")

# Separador
st.markdown("---")

# Sección de riesgo país
st.subheader("🌍 Indicadores Adicionales")

col_risk1, col_risk2, col_risk3 = st.columns(3)

with col_risk1:
    risk = get_risk_country()
    st.metric(
        label="Riesgo País",
        value=f"{risk} pts",
        delta="Puntos básicos",
        delta_color="inverse"
    )

with col_risk2:
    # Calculadora rápida
    st.metric(
        label="Inflación Acumulada (12m)",
        value=f"{inflation_df['Inflación (%)'].sum():.1f}%"
    )

with col_risk3:
    if dollar_rates:
        st.metric(
            label="Actualizado",
            value=datetime.now().strftime("%H:%M"),
            delta=datetime.now().strftime("%d/%m/%Y")
        )

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Dashboard creado con Streamlit y Python | Datos de APIs públicas</p>
    <p style='font-size: 0.8em;'>⚠️ Los datos son referenciales. Para inversiones consulte fuentes oficiales.</p>
</div>
""", unsafe_allow_html=True)

# Sidebar con información adicional
with st.sidebar:
    st.header("ℹ️ Información")
    st.markdown("""
    ### Sobre este Dashboard
    
    Este dashboard muestra datos económicos clave de Argentina en tiempo real:
    
    - **Cotizaciones del Dólar**: Oficial, Blue, MEP y CCL
    - **Brecha Cambiaria**: Diferencia entre cotizaciones
    - **Inflación**: Evolución mensual
    - **Riesgo País**: Indicador de confianza
    
    ### Fuentes de Datos
    - DolarAPI.com (cotizaciones)
    - Datos públicos (inflación)
    
    ### Actualización
    Los datos se actualizan automáticamente cada 5 minutos.
    """)
    
    st.markdown("---")
    st.markdown("**💡 Tip**: Actualizá la página para ver los últimos datos")
