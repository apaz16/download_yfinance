##   Primero --->  cd '/Users/alejandropaz/Desktop/UP/9° Semestre/Ing Financiera'
###  Segundo ---> "/opt/anaconda3/bin/python" -m streamlit run download_yfinance.py
############################# ----------- ##############
### Created by apaz

import streamlit as st
import yfinance as yf
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Precios Yfinance",
    page_icon="📈",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center;'>Descarga de Datos con Yahoo Finance 📈</h1>",
    unsafe_allow_html=True
)

# Generación de la variable
Ticker_1 = st.text_input("Ingresa el Ticker del Instrumento Financiero", "AAPL")

# Extraer la información de Yahoo Finance
Ticker = yf.Ticker(Ticker_1)
Text_Period = st.text_input("Periodo deseado", "1y")
Text_Granularity = st.text_input("Granularidad deseada:", "1d")
DH = Ticker.history(Text_Period, interval = Text_Granularity)

Info = Ticker.get_info()
Info = pd.DataFrame([Info])
Name = Info["longname"]

st.write(f"Tabla de Precios de {Name}")
st.dataframe(DH, use_container_width = True, height = 300)

output = BytesIO()

DH.index = DH.index.tz_localize(None)

with pd.ExcelWriter(output, engine="openpyxl") as writer:
    DH.to_excel(writer, sheet_name=Ticker_1)

st.download_button(
    "Descargar archivo Excel",
    data=output.getvalue(),
    file_name=f"Precios {Ticker_1}.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


