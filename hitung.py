import streamlit as st

# Input number and units
X = st.number_input("Masukkan angka")
sx = st.text_input("Satuan", "C")
st.write(f"Anda memasukkan: {X} {sx}")
sy = st.text_input("Dikonversi ke", "C")

# Initialize variable for conversion result
y = 0

# Conversion logic
if sx == 'C':  # Input in Celsius
    if sy == 'C':
        y = X  # Celsius to Celsius (no change)
    elif sy == 'F':
        y = (X * 9/5) + 32  # Celsius to Fahrenheit
    elif sy == 'K':
        y = X + 273.15  # Celsius to Kelvin
    else:
        st.write("Satuan tujuan tidak dikenal")

elif sx == 'F':  # Input in Fahrenheit
    if sy == 'C':
        y = (X - 32) * 5/9  # Fahrenheit to Celsius
    elif sy == 'F':
        y = X  # Fahrenheit to Fahrenheit (no change)
    elif sy == 'K':
        y = (X - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    else:
        st.write("Satuan tujuan tidak dikenal")

elif sx == 'K':  # Input in Kelvin
    if sy == 'C':
        y = X - 273.15  # Kelvin to Celsius
    elif sy == 'F':
        y = (X - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
    elif sy == 'K':
        y = X  # Kelvin to Kelvin (no change)
    else:
        st.write("Satuan tujuan tidak dikenal")

else:
    st.write("Satuan input tidak dikenal")

# Output result
st.write(f"{X} {sx} = {y} {sy}")
