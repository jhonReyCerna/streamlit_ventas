import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
import pandas as pd

# Page Config
st.set_page_config(page_title="Sales Predictor", layout="wide", initial_sidebar_state="collapsed")

# Modern Bright Custom Styling
st.markdown("""
<style>
    .main {
        background: #f0f2f6;
        color: #1f2937;
        padding: 2rem;
    }
    .dashboard-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid;
    }
    .prediction-card {
        border-left-color: #10B981;
        background: linear-gradient(to right, #f0fff4, white);
    }
    .history-card {
        border-left-color: #6366F1;
        background: linear-gradient(to right, #eef2ff, white);
    }
    .settings-card {
        border-left-color: #F59E0B;
        background: linear-gradient(to right, #fef3c7, white);
    }
    .graph-card {
        border-left-color: #3B82F6;
        background: linear-gradient(to right, #eff6ff, white);
    }
    h1 {
        color: #1f2937 !important;
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        margin: 2rem 0 !important;
    }
    h2 {
        color: #374151 !important;
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        margin-bottom: 1rem !important;
    }
    .stMetric {
        background: white !important;
        padding: 1rem !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
    }
    .stMetric label {
        color: #4B5563 !important;
        font-weight: 500 !important;
    }
    .stMetric > div {
        color: #1f2937 !important;
    }
    .css-1qg05tj {
        color: #1f2937 !important;
    }
    .stSelectbox label {
        color: #4B5563 !important;
    }
    .plot-container {
        background: white !important;
        border-radius: 10px !important;
        padding: 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1>📊 Dashboard de Predicción de Ventas</h1>", unsafe_allow_html=True)

# Data preparation (same as before)
meses = np.array([[10], [11]])
ventas = np.array([480, 520])
modelo = LinearRegression()
modelo.fit(meses, ventas)
prediccion_diciembre = modelo.predict(np.array([[12]]))[0]

# Datos de ventas por categoría
categorias = {
    'Electrónicos': {
        'Octubre': 50,
        'Noviembre': 55
    },
    'Televisores': {
        'Octubre': 45,
        'Noviembre': 50
    },
    'Computadoras y Laptops': {
        'Octubre': 40,
        'Noviembre': 45
    },
    'Cámaras y Fotografía': {
        'Octubre': 65,
        'Noviembre': 70.32    # 65 + 4.2%
    },
    'Videojuegos y Consolas': {
        'Octubre': 30,
        'Noviembre': 35
    }
}

# Datos de productos más vendidos
productos_top = {
    'Octubre': [
        {'Producto': 'iPhone 13', 'Unidades': 15, 'Ingresos': 15000},
        {'Producto': 'Samsung TV 55"', 'Unidades': 12, 'Ingresos': 9600},
        {'Producto': 'PlayStation 5', 'Unidades': 10, 'Ingresos': 5000},
        {'Producto': 'MacBook Air', 'Unidades': 8, 'Ingresos': 8800},
        {'Producto': 'Xiaomi Mi 11', 'Unidades': 7, 'Ingresos': 3500},
        {'Producto': 'Samsung Galaxy S21', 'Unidades': 6, 'Ingresos': 5400},
        {'Producto': 'Nintendo Switch', 'Unidades': 5, 'Ingresos': 1500},
        {'Producto': 'Sony WH-1000XM4', 'Unidades': 4, 'Ingresos': 1200},
        {'Producto': 'Xbox Series X', 'Unidades': 3, 'Ingresos': 1500},
        {'Producto': 'Dell XPS 13', 'Unidades': 2, 'Ingresos': 2400}
    ],
    'Noviembre': [
        {'Producto': 'iPhone 13', 'Unidades': 18, 'Ingresos': 18000},
        {'Producto': 'Samsung TV 55"', 'Unidades': 14, 'Ingresos': 11200},
        {'Producto': 'iPad Pro', 'Unidades': 12, 'Ingresos': 9600},
        {'Producto': 'MacBook Air', 'Unidades': 10, 'Ingresos': 11000},
        {'Producto': 'Google Pixel 6', 'Unidades': 8, 'Ingresos': 5600},
        {'Producto': 'LG OLED TV 65"', 'Unidades': 7, 'Ingresos': 14000},
        {'Producto': 'Nintendo Switch', 'Unidades': 6, 'Ingresos': 1800},
        {'Producto': 'Bose QuietComfort', 'Unidades': 5, 'Ingresos': 1500},
        {'Producto': 'Xbox Series X', 'Unidades': 4, 'Ingresos': 2000},
        {'Producto': 'Lenovo ThinkPad X1', 'Unidades': 3, 'Ingresos': 4500}
    ]
}

# Layout
col1, col2 = st.columns([1, 2])

with col1:
    # Prediction Card
    st.markdown("<div class='dashboard-card prediction-card'>", unsafe_allow_html=True)
    st.markdown("<h2>💫 Predicción de Ventas</h2>", unsafe_allow_html=True)
    st.metric(
        label="Ventas Esperadas Diciembre",
        value=f"${prediccion_diciembre:,.2f}",
        delta=f"{((prediccion_diciembre-ventas[-1])/ventas[-1]*100):.1f}%"
    )
    st.markdown("</div>", unsafe_allow_html=True)

    # Historical Data
    st.markdown("<div class='dashboard-card history-card'>", unsafe_allow_html=True)
    st.markdown("<h2>📈 Datos Históricos</h2>", unsafe_allow_html=True)
    col1_hist, col2_hist = st.columns(2)
    with col1_hist:
        st.metric("Octubre", f"${ventas[0]:,.0f}")
    with col2_hist:
        st.metric("Noviembre", f"${ventas[1]:,.0f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Model Settings Card
    st.markdown("<div class='dashboard-card settings-card'>", unsafe_allow_html=True)
    st.markdown("<h2>⚙️ Ajustes del Modelo</h2>", unsafe_allow_html=True)
    nuevo_mes = st.select_slider(
        'Mes a predecir',
        options=list(range(1,13)),
        value=12,
        format_func=lambda x: ['Enero','Febrero','Marzo','Abril','Mayo','Junio',
                             'Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre'][x-1]
    )
    nueva_prediccion = modelo.predict(np.array([[nuevo_mes]]))[0]
    st.metric("Nueva Predicción", f"${nueva_prediccion:,.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # Enhanced Graph
    st.markdown("<div class='dashboard-card graph-card'>", unsafe_allow_html=True)
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=[10, 11],
        y=ventas,
        mode='lines+markers',
        name='Histórico',
        line=dict(color='#3B82F6', width=3),
        marker=dict(size=10)
    ))
    
    fig.add_trace(go.Scatter(
        x=[11, 12],
        y=[ventas[-1], prediccion_diciembre],
        mode='lines+markers',
        name='Predicción',
        line=dict(color='#10B981', width=3, dash='dot'),
        marker=dict(size=10)
    ))

    fig.update_layout(
        title='Tendencia de Ventas',
        paper_bgcolor='rgba(255,255,255,0)',
        plot_bgcolor='rgba(247,250,252,0.8)',
        font=dict(color='#1f2937', size=12),
        height=400,
        xaxis=dict(
            title='Mes',
            ticktext=['Octubre', 'Noviembre', 'Diciembre'],
            tickvals=[10, 11, 12],
            gridcolor='rgba(160,174,192,0.2)'
        ),
        yaxis=dict(
            title='Ventas ($)',
            gridcolor='rgba(160,174,192,0.2)'
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Category Statistics
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<h2>📊 Métricas por Categoría</h2>", unsafe_allow_html=True)
    cat_cols = st.columns(len(categorias))
    for i, (categoria, datos) in enumerate(categorias.items()):
        with cat_cols[i]:
            variacion = ((datos['Noviembre'] - datos['Octubre']) / datos['Octubre'] * 100)
            st.metric(
                label=categoria,
                value=f"${datos['Noviembre']:,}",
                delta=f"{variacion:.1f}%"
            )
    st.markdown("</div>", unsafe_allow_html=True)

# Metrics Section
st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
metric_cols = st.columns(3)
with metric_cols[0]:
    st.metric("Retorno de Inversión", "+25%", "1.2%")
with metric_cols[1]:
    st.metric("Conversión", "3.4%", "0.8%")
with metric_cols[2]:
    st.metric("Satisfaction", "94%", "2.3%")
st.markdown("</div>", unsafe_allow_html=True)

# Tabla de productos más vendidos
st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
st.markdown("<h2>🏆 Top 10 Productos Más Vendidos</h2>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["Octubre", "Noviembre"])

with tab1:
    df_octubre = pd.DataFrame(productos_top['Octubre'])
    df_octubre.index = range(1, len(df_octubre) + 1)  # Índice desde 1
    st.table(df_octubre.style.format({
        'Ingresos': '${:,.0f}',
        'Unidades': '{:,.0f}'
    }))

with tab2:
    df_noviembre = pd.DataFrame(productos_top['Noviembre'])
    df_noviembre.index = range(1, len(df_noviembre) + 1)  # Índice desde 1
    st.table(df_noviembre.style.format({
        'Ingresos': '${:,.0f}',
        'Unidades': '{:,.0f}'
    }))
st.markdown("</div>", unsafe_allow_html=True)
