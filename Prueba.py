import streamlit as st

st.title("¡Streamlit funciona!")
url = st.text_input("Pega una URL aquí")

if url:
    st.success(f"URL recibida: {url}")