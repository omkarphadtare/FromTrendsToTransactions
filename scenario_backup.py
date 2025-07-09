import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Config ---
st.set_page_config(page_title="🧠 Scenario Planner", layout="wide")

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
st.sidebar.title("🧪 Scenario Planner")
st.sidebar.markdown("Use filters below to simulate forecasted demand changes.")

city_display = st.sidebar.selectbox("Select City", list(city_map.values()))
product_display = st.sidebar.selectbox("Select Product", list(product_map.values()))

# Convert back to raw keys
city = [k for k, v in city_map.items() if v == city_display][0]
product = [k for k, v in product_map.items() if v == product_display][0]

st.sidebar.markdown("---")
st.sidebar.subheader("Simulation Inputs")
price_change = st.sidebar.slider("Price Change (%)", -50, 50, 0)
inventory_change = st.sidebar.slider("Inventory Level (%)", 50, 150, 100)

# --- Filter Forecast & Sales ---
filtered_forecast = forecast_df[(forecast_df["city"] == city) & (forecast_df["product"] == product)].copy()
filtered_sales = sales_df[
    (sales_df["City"].str.lower() == city.lower()) &
    (sales_df["Product"].str.lower() == product.replace("_", " "))
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

# --- Metrics ---
col1, col2 = st.columns(2)
col1.metric("📈 Original Forecast (Total)", int(forecast_weekly["yhat"].sum()))
col2.metric("🧪 Simulated Forecast (Total)", int(forecast_weekly["Simulated_yhat"].sum()))

# --- Headings ---
st.markdown(f"#### 📊 {product_display} | {city_display} | Weekly Sales Forecast")
st.markdown("Comparing **Last Year (Jul–Sep 2024)** and **Forecast (Jul–Sep 2025)** in a continuous timeline.")

# --- Chart ---
fig, ax = plt.subplots(figsize=(14, 6), dpi=120)

# Plot past sales if available
if not sales_weekly.empty:
    ax.plot(
        sales_weekly["Label"], sales_weekly["Quantity"],
        label="Last Year's Sales", color="#8c8c8c", linestyle=":", linewidth=2
    )
else:
    st.info("ℹ️ No past sales data available for this product-city combination during Jul–Sep 2024.")

# Plot forecasts
ax.plot(
    forecast_weekly["Label"], forecast_weekly["yhat"],
    label="Forecast", color="#1f77b4", linewidth=2.5
)
ax.plot(
    forecast_weekly["Label"], forecast_weekly["Simulated_yhat"],
    label="Simulated", color="#2ca02c", linestyle="--", linewidth=2.5
)

# Style
ax.set_title(f"{product_display} | {city_display} | Simulated vs Forecasted Sales", fontsize=16, weight='bold')
ax.set_xlabel("Weeks", fontsize=12)
ax.set_ylabel("Units Sold", fontsize=12)
ax.tick_params(axis='x', rotation=45)
ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left", fontsize=11)
fig.tight_layout()

st.pyplot(fig)

# --- Footer ---
st.markdown("---")
st.caption("Simulations reflect directional changes based on price and inventory. Use insights to inform strategic planning.")