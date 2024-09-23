import streamlit as st

# Input number and units
st.header("Kalkulator suhu")
X = st.number_input("Masukkan angka")
sx = st.selectbox("Dikonversi ke", ("C", "F", "K"), key='sx')
st.write(f"Anda memasukkan: {X} {sx}")
sy = st.selectbox("Dikonversi ke", ("C", "F", "K"), key='sy')
y = 0
# Conversion logic
if sx == 'C':  # Input in Celsius
    if sy == 'C':
        y = X  # Celsius to Celsius (no change)
    elif sy == 'F':
        y = (X * 9/5) + 32  # Celsius to Fahrenheit
    elif sy == 'K':
        y = X + 273.15  # Celsius to Kelvin
    elif sy == 'R':
        y = (X + 273.15) * 9/5 
    else:
        st.write("Satuan tujuan tidak dikenal")

elif sx == 'F':  # Input in Fahrenheit
    if sy == 'C':
        y = (X - 32) * 5/9  # Fahrenheit to Celsius
    elif sy == 'F':
        y = X  # Fahrenheit to Fahrenheit (no change)
    elif sy == 'K':
        y = (X - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    elif sy == 'R':
        y = X + 459.67  # Fahrenheit to Rankine
    else:
        st.write("Satuan tujuan tidak dikenal")

elif sx == 'K':  # Input in Kelvin
    if sy == 'C':
        y = X - 273.15  # Kelvin to Celsius
    elif sy == 'F':
        y = (X - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
    elif sy == 'K':
        y = X  # Kelvin to Kelvin (no change)
     elif sy == 'R':
        y = X * 9/5  # Kelvin to Rankine
    else:
        st.write("Satuan tujuan tidak dikenal")
        
elif sx == 'R':  # Input in Rankine
    if sy == 'C':
        y = (X - 491.67) * 5/9  # Rankine to Celsius
    elif sy == 'F':
        y = X - 459.67  # Rankine to Fahrenheit
    elif sy == 'K':
        y = X * 5/9  # Rankine to Kelvin
    elif sy == 'R':
        y = X  # Rankine to Rankine (no change)
    else:
        st.write
else:
    st.write("Satuan input tidak dikenal")

# Output result
st.write(f"{X} {sx} = {y} {sy}")
