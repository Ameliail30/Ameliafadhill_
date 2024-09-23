import streamlit as st

X = st.number_input("Masukkan angka ")
sx = st.text_input("Satuan", "C")
st.write("Anda memasukkan, x,' ', sx)
