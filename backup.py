import streamlit as st
import base64

# --- Page Configuration ---
st.set_page_config(
    page_title="Fashion Forecasting | AI-Powered Analytics",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Hide sidebar and default elements ---
hide_default_style = """
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stDeployButton {display: none;}
    </style>
"""
st.markdown(hide_default_style, unsafe_allow_html=True)


# --- Enhanced Background with Professional Styling ---
def set_professional_bg(img_path):
    with open(img_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

            .stApp {{
                background: none;
                font-family: 'Inter', sans-serif;
            }}

            .background {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                opacity: 0.15;
                z-index: -1;
            }}

            .hero-section {{
                background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(248,250,252,0.95) 100%);
                padding: 4rem 3rem 3rem 3rem;
                border-radius: 20px;
                max-width: 1000px;
                margin: 3vh auto 2vh auto;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
                border: 1px solid rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
            }}

            .services-grid {{
                background: linear-gradient(135deg, rgba(255,255,255,0.92) 0%, rgba(249,250,251,0.92) 100%);
                padding: 2.5rem 3rem;
                border-radius: 20px;
                max-width: 1000px;
                margin: 2vh auto;
                box-shadow: 0 15px 40px rgba(0,0,0,0.08);
                border: 1px solid rgba(255,255,255,0.3);
                backdrop-filter: blur(8px);
            }}

            .hero-title {{
                font-size: 3.2rem;
                font-weight: 700;
                background: linear-gradient(135deg, #1e293b 0%, #475569 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-align: center;
                margin-bottom: 0.5rem;
                line-height: 1.2;
            }}

            .hero-subtitle {{
                font-size: 1.4rem;
                color: #475569;
                text-align: center;
                margin-bottom: 2rem;
                font-weight: 500;
            }}

            .hero-description {{
                font-size: 1.1rem;
                color: #64748b;
                text-align: center;
                line-height: 1.6;
                max-width: 600px;
                margin: 0 auto 2rem auto;
            }}

            .service-card {{
                background: rgba(255,255,255,0.8);
                border: 1px solid rgba(226,232,240,0.8);
                border-radius: 16px;
                padding: 2rem;
                margin: 1.5rem 0;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }}

            .service-card:hover {{
                transform: translateY(-5px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.15);
                border-color: rgba(59,130,246,0.5);
            }}

            .service-card::before {{
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 4px;
                background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
                opacity: 0;
                transition: opacity 0.3s ease;
            }}

            .service-card:hover::before {{
                opacity: 1;
            }}

            .service-icon {{
                font-size: 2.5rem;
                margin-bottom: 1rem;
                display: block;
            }}

            .service-title {{
                font-size: 1.3rem;
                font-weight: 600;
                color: #1e293b;
                margin-bottom: 0.8rem;
            }}

            .service-description {{
                font-size: 0.95rem;
                color: #64748b;
                margin-bottom: 1.5rem;
                line-height: 1.5;
            }}

            .service-link {{
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                color: #3b82f6;
                text-decoration: none;
                font-weight: 500;
                font-size: 0.95rem;
                transition: all 0.3s ease;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                background: rgba(59,130,246,0.1);
                border: 1px solid rgba(59,130,246,0.2);
            }}

            .service-link:hover {{
                background: rgba(59,130,246,0.15);
                transform: translateX(5px);
                text-decoration: none;
                color: #2563eb;
            }}

            .cta-button {{
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);
                color: white;
                text-decoration: none;
                font-weight: 600;
                font-size: 1rem;
                padding: 1rem 2rem;
                border-radius: 12px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(59,130,246,0.4);
                border: none;
            }}

            .cta-button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(59,130,246,0.6);
                text-decoration: none;
                color: white;
            }}

            .footer {{
                text-align: center;
                padding: 2rem 3rem;
                background: rgba(248,250,252,0.9);
                border-radius: 15px;
                max-width: 1000px;
                margin: 2vh auto;
                border: 1px solid rgba(226,232,240,0.8);
            }}

            .footer-content {{
                font-size: 0.9rem;
                color: #64748b;
                line-height: 1.6;
            }}

            .footer-content a {{
                color: #3b82f6;
                text-decoration: none;
            }}

            .footer-content a:hover {{
                text-decoration: underline;
            }}

            .divider {{
                height: 1px;
                background: linear-gradient(90deg, transparent, rgba(226,232,240,0.8), transparent);
                margin: 2rem 0;
                border: none;
            }}

            .badge {{
                display: inline-block;
                background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: 500;
                margin-left: 0.5rem;
            }}
        </style>
        <div class="background"></div>
    """, unsafe_allow_html=True)


# Apply the professional background
set_professional_bg("data/bg_fashion.jpg")

# --- Hero Section ---
st.markdown('''
<div class="hero-section">
    <h1 class="hero-title">🛍️ From Trends to Transactions</h1>
    <p class="hero-subtitle">AI-Powered Fashion Retail Forecasting</p>
    <p class="hero-description">
        Transform your retail strategy with cutting-edge AI analytics. 
        Unlock actionable insights from past sales, market trends, and predictive models 
        to drive data-driven decisions and maximize profitability.
    </p>
    <div style="text-align: center; margin-top: 2rem;">
        <a href="#services" class="cta-button" style="margin-right: 1rem;">
            🚀 Explore Analytics
        </a>
        <a href="?page=Scenario_Planner" class="cta-button" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); box-shadow: 0 4px 15px rgba(16,185,129,0.4);">
            🧪 Launch Scenario Planner
        </a>
    </div>
</div>
''', unsafe_allow_html=True)

# --- Services Grid ---
st.markdown('<div class="services-grid" id="services">', unsafe_allow_html=True)

# Service Card 1
st.markdown('''
<div class="service-card">
    <span class="service-icon">📊</span>
    <h3 class="service-title">Descriptive Analytics</h3>
    <p class="service-description">
        Comprehensive analysis of historical sales data with interactive visualizations. 
        Identify patterns, seasonal trends, and performance metrics across product categories.
    </p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://your-link-1" target="_blank" class="service-link">
            📈 View Dashboard →
        </a>
        <span style="font-size: 0.85rem; color: #64748b; padding: 0.5rem;">
            <strong>Features:</strong> Sales Trends • Category Analysis • Performance KPIs
        </span>
    </div>
</div>
''', unsafe_allow_html=True)

# Service Card 2
st.markdown('''
<div class="service-card">
    <span class="service-icon">🌐</span>
    <h3 class="service-title">Market Intelligence</h3>
    <p class="service-description">
        Real-time market sentiment analysis combining Google Trends and Reddit discussions. 
        Stay ahead of emerging fashion trends and consumer preferences.
    </p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://your-link-2" target="_blank" class="service-link">
            🔍 Explore Trends →
        </a>
        <span style="font-size: 0.85rem; color: #64748b; padding: 0.5rem;">
            <strong>Sources:</strong> Google Trends • Reddit • Social Media
        </span>
    </div>
</div>
''', unsafe_allow_html=True)

# Service Card 3
st.markdown('''
<div class="service-card">
    <span class="service-icon">🧠</span>
    <h3 class="service-title">Predictive Forecasting</h3>
    <p class="service-description">
        Advanced machine learning models for demand forecasting and inventory optimization. 
        Reduce stockouts and overstock with precise demand predictions.
    </p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
        <a href="https://your-link-3" target="_blank" class="service-link">
            🤖 View Forecasts →
        </a>
        <span style="font-size: 0.85rem; color: #64748b; padding: 0.5rem;">
            <strong>Models:</strong> ARIMA • Prophet • Neural Networks
        </span>
    </div>
</div>
''', unsafe_allow_html=True)

# Service Card 4 - Interactive Scenario Planner
st.markdown('''
<div class="service-card" style="border: 2px solid rgba(16,185,129,0.3); background: linear-gradient(135deg, rgba(16,185,129,0.05) 0%, rgba(255,255,255,0.9) 100%);">
    <span class="service-icon">🧪</span>
    <h3 class="service-title">Scenario Planning <span class="badge">INTERACTIVE</span></h3>
    <p class="service-description">
        Dynamic scenario modeling tool for strategic planning. Test different market conditions, 
        pricing strategies, and promotional campaigns with real-time impact analysis.
    </p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap; align-items: center;">
''', unsafe_allow_html=True)

# Add Streamlit button for scenario planner
if st.button("🚀 Launch Scenario Planner", key="scenario_planner_btn",
             help="Click to access the interactive scenario planning tool"):
    st.switch_page("pages/Scenario_Planner.py")  # Adjust path as needed

st.markdown('''
        <span style="font-size: 0.85rem; color: #64748b; margin-left: 1rem;">
            <strong>Features:</strong> What-if Analysis • ROI Calculator • Risk Assessment
        </span>
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('''
<div class="footer">
    <div class="footer-content">
        <strong>Built by Group 22</strong> | Contributing to UN SDG 8 • 9 • 12<br>
        <em>Decent Work & Economic Growth • Industry Innovation • Responsible Consumption</em><br><br>
        📧 <a href="mailto:team22@fashion-ai.com">team22@fashion-ai.com</a> | 
        🔗 <a href="#" target="_blank">Documentation</a> | 
        📈 <a href="#" target="_blank">API Access</a>
    </div>
</div>
''', unsafe_allow_html=True)