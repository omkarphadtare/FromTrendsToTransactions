import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import base64

# --- Config ---
st.set_page_config(page_title="🧠 Scenario Planner", layout="wide", initial_sidebar_state="expanded")

# --- Hide default elements ---
hide_default_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
"""
st.markdown(hide_default_style, unsafe_allow_html=True)

# --- Professional Styling to Match Home Page ---
def set_professional_styling():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            .stApp {
                font-family: 'Inter', sans-serif;
                background: linear-gradient(135deg, #f1f5f9 0%, #e2e8f0 100%);
            }

            /* Sidebar Styling */
            .stSidebar {
                background: linear-gradient(135deg, rgba(255,255,255,0.92) 0%, rgba(248,250,252,0.92) 100%);
                border-right: 1px solid rgba(226,232,240,0.8);
                backdrop-filter: blur(10px);
            }

            .stSidebar .stSelectbox > div > div {
                background: rgba(255,255,255,0.8);
                border: 1px solid rgba(226,232,240,0.8);
                border-radius: 8px;
            }

            .stSidebar .stSlider > div > div {
                background: rgba(255,255,255,0.8);
                border-radius: 8px;
            }

            /* Main content styling */
            .main-container {
                background: linear-gradient(135deg, rgba(255,255,255,0.92) 0%, rgba(248,250,252,0.92) 100%);
                padding: 2rem 3rem;
                border-radius: 20px;
                margin: 2vh auto;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
                border: 1px solid rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
            }

            /* Page title styling */
            .page-title {
                font-size: 2.5rem;
                font-weight: 700;
                background: linear-gradient(135deg, #1e293b 0%, #475569 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin-bottom: 1rem;
                line-height: 1.2;
            }

            .page-subtitle {
                font-size: 1.1rem;
                color: #64748b;
                text-align: center;
                margin-bottom: 2rem;
                line-height: 1.6;
            }

            /* Metrics styling */
            .metrics-container {
                display: flex;
                gap: 2rem;
                margin-bottom: 2rem;
                justify-content: center;
            }

            .metric-card {
                background: linear-gradient(135deg, rgba(255,255,255,0.88) 0%, rgba(249,250,251,0.88) 100%);
                padding: 1.5rem 2rem;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.08);
                border: 1px solid rgba(255,255,255,0.3);
                backdrop-filter: blur(8px);
                text-align: center;
                min-width: 200px;
                transition: all 0.3s ease;
            }

            .metric-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 15px 40px rgba(0,0,0,0.12);
            }

            .metric-value {
                font-size: 2rem;
                font-weight: 700;
                color: #1e293b;
                margin-bottom: 0.5rem;
            }

            .metric-label {
                font-size: 0.9rem;
                color: #64748b;
                font-weight: 500;
            }

            /* Chart container */
            .chart-container {
                background: linear-gradient(135deg, rgba(255,255,255,0.88) 0%, rgba(249,250,251,0.88) 100%);
                padding: 2rem;
                border-radius: 16px;
                box-shadow: 0 15px 40px rgba(0,0,0,0.08);
                border: 1px solid rgba(255,255,255,0.3);
                backdrop-filter: blur(8px);
                margin-bottom: 2rem;
            }

            .chart-title {
                font-size: 1.3rem;
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 0.5rem;
            }

            .chart-subtitle {
                font-size: 0.95rem;
                color: #64748b;
                margin-bottom: 1.5rem;
                line-height: 1.5;
            }

            /* Info box styling */
            .info-box {
                background: linear-gradient(135deg, rgba(59,130,246,0.1) 0%, rgba(147,197,253,0.1) 100%);
                border: 1px solid rgba(59,130,246,0.2);
                border-radius: 12px;
                padding: 1rem 1.5rem;
                margin: 1rem 0;
            }

            .info-box p {
                color: #1e40af;
                margin: 0;
                font-size: 0.9rem;
            }

            /* Footer styling */
            .footer {
                text-align: center;
                padding: 1.5rem;
                background: rgba(248,250,252,0.85);
                border-radius: 12px;
                margin-top: 2rem;
                border: 1px solid rgba(226,232,240,0.8);
            }

            .footer-content {
                font-size: 0.85rem;
                color: #64748b;
                font-style: italic;
            }

            /* Sidebar title styling */
            .sidebar-title {
                font-size: 1.5rem;
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 0.5rem;
            }

            .sidebar-subtitle {
                font-size: 0.9rem;
                color: #64748b;
                margin-bottom: 1.5rem;
                line-height: 1.4;
            }

            .sidebar-section {
                margin-bottom: 1.5rem;
            }

            .sidebar-section h3 {
                font-size: 1.1rem;
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 1rem;
            }

            /* Divider */
            .divider {
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(226,232,240,0.8), transparent);
                margin: 1.5rem 0;
                border: none;
            }

            /* Smooth scrolling */
            html {
                scroll-behavior: smooth;
            }
        </style>
    """, unsafe_allow_html=True)

# Apply the professional styling
set_professional_styling()

# --- Load Data ---
@st.cache_data
def load_data():
    forecast_df = pd.read_excel("data/xgb_forecast_july2025_90days_fully_varied.xlsx")
    sales_df = pd.read_csv("data/sales_data.csv")
    forecast_df['ds'] = pd.to_datetime(forecast_df['ds'])
    sales_df['Date'] = pd.to_datetime(sales_df['Date'], errors='coerce')
    return forecast_df, sales_df

forecast_df, sales_df = load_data()

# --- Dropdown Label Maps ---
city_map = {c: c.replace("_", " ").title() for c in forecast_df['city'].unique()}
product_map = {p: p.replace("_", " ").title() for p in forecast_df['product'].unique()}

# --- Sidebar ---
st.sidebar.markdown('<div class="sidebar-title">🧪 Scenario Planner</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Use filters below to simulate forecasted demand changes.</div>', unsafe_allow_html=True)

city_display = st.sidebar.selectbox("Select City", list(city_map.values()))
product_display = st.sidebar.selectbox("Select Product", list(product_map.values()))

# Convert back to raw keys
city = [k for k, v in city_map.items() if v == city_display][0]
product = [k for k, v in product_map.items() if v == product_display][0]

st.sidebar.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-section"><h3>Simulation Inputs</h3></div>', unsafe_allow_html=True)
price_change = st.sidebar.slider("Price Change (%)", -50, 50, 0)
inventory_change = st.sidebar.slider("Inventory Level (%)", 50, 150, 100)

# --- Filter Forecast & Sales ---
filtered_forecast = forecast_df[(forecast_df["city"] == city) & (forecast_df["product"] == product)].copy()

filtered_sales = sales_df[
    (sales_df["City"].str.strip().str.lower() == city.strip().lower()) &
    (sales_df["Product"].str.strip().str.lower() == product.replace("_", " ").strip().lower())
].copy()

# --- Simulated Forecast ---
price_elasticity = 0.6
price_effect = 1 - (price_change / 100 * price_elasticity)
inventory_effect = inventory_change / 100
filtered_forecast["Simulated_yhat"] = filtered_forecast["yhat"] * price_effect * inventory_effect

# --- Weekly Aggregation ---
forecast_weekly = filtered_forecast.resample("W-Mon", on="ds").sum().reset_index()
forecast_weekly["Label"] = [f"Week {i+1}" for i in range(len(forecast_weekly))]

# --- Past Sales (Jul–Sep last year) ---
forecast_start = filtered_forecast["ds"].min()
forecast_months = filtered_forecast["ds"].dt.month.unique()

sales_last_year = filtered_sales[filtered_sales["Date"] >= (forecast_start - pd.DateOffset(days=365))]
sales_same_months = sales_last_year[sales_last_year["Date"].dt.month.isin(forecast_months)]
sales_weekly = sales_same_months.resample("W-Mon", on="Date").agg({"Quantity": "sum"}).reset_index()
sales_weekly["Label"] = [f"Week {i+1}" for i in range(len(sales_weekly))]

# --- Main Content ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Page title
st.markdown('<div style="height: 4px; width: 60px; background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899); margin: 0 auto 1.5rem auto; border-radius: 8px;"></div>', unsafe_allow_html=True)
st.markdown('<h1 class="page-title">🧠 Scenario Planning Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p class="page-subtitle">Dynamic scenario modeling for strategic planning and impact analysis</p>', unsafe_allow_html=True)

# --- Metrics ---
original_total = int(forecast_weekly["yhat"].sum())
simulated_total = int(forecast_weekly["Simulated_yhat"].sum())
change_percent = ((simulated_total - original_total) / original_total * 100) if original_total > 0 else 0

st.markdown(f'''
<div class="metrics-container">
    <div class="metric-card">
        <div class="metric-value">📈 {original_total:,}</div>
        <div class="metric-label">Original Forecast (Total)</div>
    </div>
    <div class="metric-card">
        <div class="metric-value">🧪 {simulated_total:,}</div>
        <div class="metric-label">Simulated Forecast (Total)</div>
    </div>
    <div class="metric-card">
        <div class="metric-value" style="color: {'#10b981' if change_percent >= 0 else '#ef4444'};">
            {'↗️' if change_percent >= 0 else '↘️'} {change_percent:+.1f}%
        </div>
        <div class="metric-label">Change from Original</div>
    </div>
</div>
''', unsafe_allow_html=True)

# --- Chart Container ---
st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.markdown(f'<h3 class="chart-title">📊 {product_display} | {city_display} | Weekly Sales Forecast</h3>', unsafe_allow_html=True)
st.markdown('<p class="chart-subtitle">Comparing <strong>Last Year (Jul–Sep 2024)</strong> and <strong>Forecast (Jul–Sep 2025)</strong> in a continuous timeline.</p>', unsafe_allow_html=True)

# Display info if no past sales data
if sales_weekly.empty:
    st.markdown('''
    <div class="info-box">
        <p>ℹ️ No past sales data available for this product-city combination during Jul–Sep 2024.</p>
    </div>
    ''', unsafe_allow_html=True)

# --- Chart ---
fig, ax = plt.subplots(figsize=(14, 6), dpi=120)

# Set style to match the professional theme
plt.style.use('default')
fig.patch.set_facecolor('white')
ax.set_facecolor('#fafafa')

# Plot past sales if available
if not sales_weekly.empty:
    ax.plot(
        sales_weekly["Label"], sales_weekly["Quantity"],
        label="Last Year's Sales", color="#8c8c8c", linestyle=":", linewidth=2.5, marker='o', markersize=4
    )

# Plot forecasts
ax.plot(
    forecast_weekly["Label"], forecast_weekly["yhat"],
    label="Original Forecast", color="#3b82f6", linewidth=3, marker='s', markersize=5
)
ax.plot(
    forecast_weekly["Label"], forecast_weekly["Simulated_yhat"],
    label="Simulated Forecast", color="#10b981", linestyle="--", linewidth=3, marker='^', markersize=5
)

# Style the chart to match the design
ax.set_title(f"{product_display} | {city_display} | Sales Forecast Comparison",
             fontsize=16, weight='bold', color='#1e293b', pad=20)
ax.set_xlabel("Weeks", fontsize=12, color='#475569', weight='500')
ax.set_ylabel("Units Sold", fontsize=12, color='#475569', weight='500')
ax.tick_params(axis='x', rotation=45, colors='#64748b')
ax.tick_params(axis='y', colors='#64748b')
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
ax.grid(True, linestyle="--", alpha=0.3, color='#cbd5e1')
ax.legend(loc="upper left", fontsize=11, frameon=True, fancybox=True, shadow=True)

# Style the spines
for spine in ax.spines.values():
    spine.set_color('#e2e8f0')
    spine.set_linewidth(1)

fig.tight_layout()
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)  # Close chart container

# --- Footer ---
st.markdown('''
<div class="footer">
    <div class="footer-content">
        Simulations reflect directional changes based on price and inventory adjustments. 
        Use these insights to inform strategic planning and decision-making processes.
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close main container