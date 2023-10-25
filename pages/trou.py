import streamlit as st
import pandas


st.set_page_config(
    page_title="le trou!!",
    page_icon="🕳️",
    layout="wide"
)

uploaded_files = st.file_uploader("Déposez un fichier CSV")

if uploaded_files is not None:
    df = pandas.read_csv(uploaded_files)
    st.write(df)