import streamlit as st
import base64

def get_base64_image(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

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
                opacity: 0.35;
                z-index: -1;
            }}

            .hero-section {{
                background: linear-gradient(135deg, rgba(255,255,255,0.92) 0%, rgba(248,250,252,0.92) 100%);
                padding: 4rem 3rem 3rem 3rem;
                border-radius: 20px;
                max-width: 1000px;
                margin: 3vh auto 2vh auto;
                box-shadow: 0 20px 60px rgba(0,0,0,0.1);
                border: 1px solid rgba(255,255,255,0.2);
                backdrop-filter: blur(10px);
            }}

            .services-grid {{
                background: linear-gradient(135deg, rgba(255,255,255,0.88) 0%, rgba(249,250,251,0.88) 100%);
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
                background: rgba(255,255,255,0.75);
                border: 1px solid rgba(226,232,240,0.8);
                border-radius: 16px;
                padding: 2rem;
                margin: 1.5rem auto;
                max-width: 1500px;
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
                cursor: pointer;
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
                background: rgba(248,250,252,0.85);
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

            /* Custom styling for button to match service-link */
            .stButton > button {{
                display: inline-flex !important;
                align-items: center !important;
                gap: 0.5rem !important;
                color: #3b82f6 !important;
                text-decoration: none !important;
                font-weight: 500 !important;
                font-size: 0.95rem !important;
                transition: all 0.3s ease !important;
                padding: 0.75rem 1.5rem !important;
                border-radius: 8px !important;
                background: rgba(59,130,246,0.1) !important;
                border: 1px solid rgba(59,130,246,0.2) !important;
                cursor: pointer !important;
                width: auto !important;
                min-height: auto !important;
            }}

            .stButton > button:hover {{
                background: rgba(59,130,246,0.15) !important;
                transform: translateX(5px) !important;
                color: #2563eb !important;
            }}

            .stButton > button:focus {{
                outline: none !important;
                box-shadow: 0 0 0 2px rgba(59,130,246,0.2) !important;
            }}

            /* Specific styling for card 4 button alignment */
            .card4-button-container {{
                display: flex !important;
                align-items: center !important;
                gap: 1rem !important;
                flex-wrap: wrap !important;
                margin-top: 0 !important;
            }}

            .card4-button-container .stButton {{
                margin: 0 !important;
            }}

            .card4-features {{
                display: flex !important;
                align-items: center !important;
                font-size: 0.85rem !important;
                color: #64748b !important;
                margin: 0 !important;
            }}

            /* Smooth scrolling */
            html {{
                scroll-behavior: smooth;
            }}
        </style>
        <div class="background"></div>

        <script>
            function scrollToServices() {{
                const servicesSection = document.getElementById('services');
                if (servicesSection) {{
                    servicesSection.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }}
        </script>
    """, unsafe_allow_html=True)


# Apply the professional background
set_professional_bg("data/bg_fashion.jpg")

# --- Hero Section ---
st.markdown('''
<div class="hero-section">
<div style="height: 4px; width: 60px; background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899); margin: 0 auto 1.5rem auto; border-radius: 8px;"></div>
    <h1 style="
    font-size: 3.2rem;
    font-weight: 700;
    text-align: center;
    line-height: 1.2;
    background: linear-gradient(90deg, #3b82f6, #8b5cf6, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    color: transparent;
    ">
        🛍️ From Trends to Transactions
    </h1>
    <p class="hero-subtitle">AI-Powered Fashion Retail Forecasting</p>
    <p style="text-align: center; font-size: 1.1rem; color: #64748b; line-height: 1.6; max-width: 600px; margin: 0 auto 2rem auto;">
        Transform your retail strategy with cutting-edge AI analytics. 
        Unlock actionable insights from past sales, market trends, and predictive models 
        to drive data-driven decisions and maximize profitability.
    </p>
    <div style="text-align: center; margin-top: 2rem;">
        <a href="#services" class="cta-button" style="margin-right: 1rem;color: white;">
            Explore Analytics
        </a>
        <a href="#scenario-planner" class="cta-button" style="margin-right: 1rem;color: white;">
            Launch Scenario Planner
        </a>
    </div>
</div>
''', unsafe_allow_html=True)

# Add anchor for services section
st.markdown('<div id="services"></div>', unsafe_allow_html=True)

img_base64 = get_base64_image("data/img1.jpeg")
img1_base64 = get_base64_image("data/market.png")
img2_base64 = get_base64_image("data/predictive.png")
img3_base64 = get_base64_image("data/scenario.png")

# Service Card 1
st.markdown(f'''
<div class="service-card" style="display: flex; justify-content: space-between; align-items: center; gap: 2rem;">
    <div style="flex: 1;">
        <span class="service-icon">📊</span>
        <h3 class="service-title">Performance Overview</h3>
        <p class="service-description">
            Comprehensive analysis of historical sales data with interactive visualizations. 
            Identify patterns, seasonal trends, and performance metrics across product categories.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="https://app.powerbi.com/reportEmbed?reportId=5f3802bd-611a-46db-bdaa-286fc27b15c8&autoAuth=true&ctid=46fe5ca5-866f-4e42-92e9-ed8786245545" target="_blank" class="service-link">
                📈 View Dashboard →
            </a>
            <span style="font-size: 0.95rem; color: #64748b; padding: 0.5rem;">
                <strong>Features: </strong> Sales Trends • Category Analysis • Performance KPIs
            </span>
        </div>
    </div>
    <div style="flex: 0 0 200px;">
        <img src="data:image/jpeg;base64,{img_base64}" alt="Descriptive Analytics" style="width: 100%; border-radius: 12px;">
    </div>
</div>
''', unsafe_allow_html=True)

# Service Card 2
st.markdown(f'''
<div class="service-card" style="display: flex; justify-content: space-between; align-items: center; gap: 2rem;">
    <div style="flex: 1;">
        <span class="service-icon">🌐</span>
        <h3 class="service-title">Current Market Insights</h3>
        <p class="service-description">
            Decode fashion signals from Google Trends and Reddit conversations. 
            Stay ahead of emerging fashion trends and consumer preferences.
        </p>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
            <a href="https://app.powerbi.com/reportEmbed?reportId=7f1ad401-3538-4acf-9c4d-bd230c6865f5&autoAuth=true&ctid=46fe5ca5-866f-4e42-92e9-ed8786245545" target="_blank" class="service-link">
                🔍 Explore Trends →
            </a>
            <span style="font-size: 0.95rem; color: #64748b; padding: 0.5rem;">
                <strong>Sources:</strong> Google Trends • Reddit
            </span>
        </div>
    </div>
    <div style="flex: 0 0 200px;">
        <img src="data:image/jpeg;base64,{img1_base64}" alt="Market Insights" style="width: 100%; border-radius: 12px;">
    </div>
</div>
''', unsafe_allow_html=True)

# Service Card 3
st.markdown(f'''
<div class="service-card" style="display: flex; justify-content: space-between; align-items: center; gap: 2rem;">
    <div style="flex: 1;">
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
            <span style="font-size: 0.95rem; color: #64748b; padding: 0.5rem;">
                <strong>Models:</strong> XGBoost
            </span>
        </div>
    </div>
    <div style="flex: 0 0 200px;">
        <img src="data:image/jpeg;base64,{img2_base64}" alt="Predictive Forecasting" style="width: 100%; border-radius: 12px;">
    </div>
</div>
''', unsafe_allow_html=True)

# Anchor to scroll target
st.markdown('<a name="scenario-planner"></a>', unsafe_allow_html=True)

# --- Full-card button style for Scenario Planner ---
card4_style = """
    <style>
        .clickable-card-btn > button {
            width: 100%;
            height: 100%;
            padding: 0;
            border: none;
            background: none;
        }
        .clickable-card-inner {
            border: 2px solid rgba(16,185,129,0.3);
            background: linear-gradient(135deg, rgba(16,185,129,0.05) 0%, rgba(255,255,255,0.9) 100%);
            padding: 2rem;
            border-radius: 16px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        .clickable-card-inner:hover {
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            transform: translateY(-4px);
        }
        .clickable-card-inner .service-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: block;
        }
        .clickable-card-inner .service-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: #1e293b;
            margin-bottom: 0.8rem;
        }
        .clickable-card-inner .badge {
            background: linear-gradient(135deg, #10b981 0%, #059669 100%);
            color: white;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
            margin-left: 0.5rem;
        }
        .clickable-card-inner .service-description {
            font-size: 0.95rem;
            color: #64748b;
            margin-bottom: 1rem;
            line-height: 1.5;
        }
        .clickable-card-inner .card4-features {
            font-size: 0.85rem;
            color: #64748b;
        }
    </style>
"""

st.markdown(card4_style, unsafe_allow_html=True)

# --- Scenario Planner Card (clickable simulation) ---
st.markdown(f"""
<div class="service-card" style="display: flex; justify-content: space-between; align-items: center; gap: 2rem; border: 2px solid rgba(16,185,129,0.3); background: linear-gradient(135deg, rgba(16,185,129,0.05) 0%, rgba(255,255,255,0.9) 100%);">
    <div style="flex: 1;">
        <span class="service-icon">🧪</span>
        <h3 class="service-title">Scenario Planning <span class="badge">INTERACTIVE</span></h3>
        <p class="service-description">
            Dynamic scenario modeling tool for strategic planning. Test different market conditions and
            pricing strategies for impact analysis.
        </p>
        <span style="font-size: 0.95rem; color: #64748b; padding: 0.5rem;">
                <strong>Features: </strong> What-if Analysis • Risk Assessment
        </span>
    </div>
    <div style="flex: 0 0 200px;">
        <img src="data:image/jpeg;base64,{img3_base64}" alt="Scenario Planning" style="width: 100%; border-radius: 12px;">
    </div>
</div>
""", unsafe_allow_html=True)

# Place the button just below the card
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
with col3:
    launch = st.button("🚀 Launch Scenario Planner →", key="scenario_planner_button")


if launch:
    st.switch_page("pages/Scenario_Planner.py")

# --- Footer ---
st.markdown('''
<div class="footer">
    <div class="footer-content">
        <strong>Smarter decisions</strong> | Contributing to UN SDG 8 • 9 • 12<br>
        <em>Decent Work & Economic Growth • Industry Innovation • Responsible Consumption</em><br><br>
         | 📧 <a href="124109697@umail.ucc.ie">Contact Us</a> | 
    </div>
</div>
''', unsafe_allow_html=True)