# =========================================================
# PORSCHE CLASSIC PRICE PREDICTOR — MAGAZINE STYLE
# =========================================================

import streamlit as st
import joblib
import pandas as pd
import numpy as np
import base64

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Porsche Classic Price Predictor",
    page_icon="🏁",
    layout="centered"
)

# ---------------------------------------------------------
# MAGAZINE-STYLE CSS
# ---------------------------------------------------------
st.markdown("""
    <style>
        body {
            background-color: white;
            color: black;
            font-family: Helvetica, Arial, sans-serif;
        }
        .block-container {
            padding-top: 0rem;
            max-width: 900px;
        }

        /* HERO IMAGE SECTION */
        .hero-section {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: white;
            margin: 0;
            padding: 0;
        }
        .hero-section img {
            width: 90%;
            max-width: 1600px;
            height: auto;
        }

        /* TITLES */
        h1 {
            font-size: 72px;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0.2em;
            letter-spacing: -1px;
            color: #111;
            line-height: 1.1;
        }
        h2 {
            font-size: 20px;
            font-weight: 400;
            text-align: center;
            margin-bottom: 1.5em;
            color: #444;
        }
        .author {
            text-align: center;
            font-size: 18px;
            color: #555;
            margin-bottom: 3em;
        }

        /* DESCRIPTION */
        .description {
            text-align: justify;
            color: #222;
            line-height: 1.6;
            margin-bottom: 2.5em;
            font-size: 16px;
        }

        /* PRICE RESULT */
        .price-box {
            border-top: 2px solid #000;
            border-bottom: 2px solid #000;
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            padding: 1rem;
            margin-top: 2.5em;
            color: #111;
        }

        /* FOOTER */
        .footer {
            text-align: center;
            color: #555;
            margin-top: 3em;
            font-size: 14px;
        }

        /* BUTTON STYLE */
        .stButton>button {
            background-color: black;
            color: white;
            border-radius: 0;
            border: none;
            font-weight: bold;
            width: 100%;
            height: 3em;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #600000;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# MODEL LOAD
# ---------------------------------------------------------
model = joblib.load('pipeline_catboost.pkl')

# ---------------------------------------------------------
# HERO IMAGE (FULL SCREEN)
# ---------------------------------------------------------

# Ruta exacta del archivo SVG
svg_path = "porsche_burgundy_simple.svg"

# Lee el SVG y conviértelo a base64
with open(svg_path, "r") as f:
    svg_data = f.read()
b64 = base64.b64encode(svg_data.encode()).decode()

# Inserta el SVG embebido en HTML
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; margin: 2em 0;">
        <img src="data:image/svg+xml;base64,{b64}" style="width:100%; max-width:1400px; height:auto;" />
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown("<h1>How to predict the price<br>of a Porsche.</h1>", unsafe_allow_html=True)
st.markdown("<h2>When precision meets timeless design.</h2>", unsafe_allow_html=True)
st.markdown("<div class='author'>Antonio Sánchez Salamanca</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# DESCRIPTION
# ---------------------------------------------------------
st.markdown("""
<div class="description">
I’m Antonio Sánchez, a final year student of Mathematical Engineering at CUNEF University and a lifelong car enthusiast. 
I created this project as a way to apply analytical thinking to something I genuinely enjoy — estimating the market 
price of my dream car. It reflects how I approach challenges: with curiosity, precision, and the drive to turn ideas 
into measurable results.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="description">
Since 1948, Porsche has built more than cars — it has built icons of engineering and balance. 
This project follows that same philosophy, using analytical thinking and real-world data 
to estimate the market value of classic Porsche models through a <b>CatBoost regression model</b>.
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# FORM
# ---------------------------------------------------------
st.markdown("---")
st.subheader("Enter your Porsche specifications:")

col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year of Manufacture", min_value=1950, max_value=2025, value=1985)
    mileage_km = st.number_input("Mileage (km)", min_value=0, max_value=500000, value=100000)
    power_hp = st.number_input("Power (HP)", min_value=50, max_value=600, value=250)
    cylinder_capacity = st.number_input("Engine Capacity (cc)", min_value=0, max_value=7000, value=3200)

with col2:
    matching_numbers = st.selectbox("Matching Numbers (original engine)", ["Yes", "No"])
    drive = st.selectbox("Drive Type", ["Rear", "Front", "Other"])
    transmission = st.selectbox("Transmission", ["Manual", "PDK", "Automatic"])

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
input_data = pd.DataFrame([{
    'year': year,
    'mileage_km': mileage_km,
    'power_hp': power_hp,
    'cylinder_capacity': cylinder_capacity,
    'specs_raw.Matching numbers:': 1 if matching_numbers == "Yes" else 0,
    'specs_raw.Drive:_Rear drive': 1 if drive == "Rear" else 0,
    'transmission_Manual': 1 if transmission == "Manual" else 0,
    'transmission_PDK': 1 if transmission == "PDK" else 0
}])

if st.button("Predict Price"):
    pred = model.predict(input_data)[0]
    st.markdown(f"<div class='price-box'>Estimated Market Value: €{pred:,.0f}</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("<div class='footer'>Developed by <b>Antonio Sánchez Salamanca</b> · CatBoost ML · Streamlit 2025 · Data from Elferspot.com </div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>For any questions about the procedure or code, you can contact me at antonio.sanchez.sal@outlook.es</div>", unsafe_allow_html=True)
st.markdown("<div class='footer'>You can view my full CV at the link below:</div>", unsafe_allow_html=True)
'''
with open("cv_antonio_sanchez.pdf", "rb") as pdf_file:
    pdf_bytes = pdf_file.read()


st.download_button(
    label="Download my CV",
    data=pdf_bytes,
    file_name="Antonio_Sanchez_CV.pdf",
    mime="application/pdf"
)
'''