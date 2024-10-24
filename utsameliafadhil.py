import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import random

# Set page title and layout with wide mode
st.set_page_config(page_title="UTS Fisika Komputasi Awan", layout="wide", page_icon="🌸")

# Custom CSS for enhanced styling
st.markdown(
    """
    <style>
    body {
        background-color: #f7f3e9;
        color: #444;
    }
    h1 {
        font-size: 3rem;
        color: #d97d54;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0;
    }
    h3, h4 {
        text-align: center;
        color: #c06c84;
    }
    .reportview-container .main footer {
        visibility: hidden;
    }
    .stButton>button {
        background-color: #c06c84;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        width: 100%;
        padding: 10px;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton>button:hover {
        background-color: #d97d54;
        transform: scale(1.05);
    }
    .caption {
        font-size: 14px;
        color: #555;
        text-align: center;
        margin-top: 20px;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1>UTS Fisika Komputasi Awan</h1>", unsafe_allow_html=True)
st.markdown("<h3>Amelia Fadhil Nurlaila</h3>", unsafe_allow_html=True)
st.markdown("<h4>210322607210</h4>", unsafe_allow_html=True)

circle = Circle((0, 0), 1, color='#6a0572', fill=False, linewidth=3, linestyle='-', alpha=0.3)
x = []
y = []
color = []
size = []
x.append(0)
y.append(0)
color.append((0.8, 0.4, 0.8))
size.append(500)

if st.button("Data ✨"):
    for i in range(111):
        x0 = 2 * (random.random() - 0.5)
        y0 = 2 * (random.random() - 0.5)
        if (x0 ** 2 + y0 ** 2) > 1.:
            y0 = np.sqrt(1 - x0 ** 2) if y0 > 0 else -np.sqrt(1 - x0 ** 2)

        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713 * random.random())


fig, ax = plt.subplots(figsize=(10, 10))
ax.add_patch(circle)

for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='purple', linestyle='--', alpha=0.2)

scatter = ax.scatter(x, y, c=color, s=size, alpha=0.8, edgecolor='#5a5a5a')

# Set labels and title
ax.set_ylabel("Y-axis", fontsize=16, color='#8e44ad')
ax.set_xlabel("X-axis", fontsize=16, color='#8e44ad')
ax.set_title('Data acak yang berubah ketika tombol ditekan 🌸', fontsize=15, color='#d97d54')

# Customize ticks and grid
ax.tick_params(axis='y', labelsize=12, colors='#6a0572')
ax.tick_params(axis='x', labelsize=12, colors='#6a0572')
ax.grid(True, linestyle='-.', alpha=0.7)

# Set limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Display the plot in Streamlit
st.pyplot(fig)

# Add caption below the plot
st.markdown('<div class="caption">Lingkaran dengan warna pastel dan ukuran acak. Data berubah setiap kali tombol ditekan 🌸</div>', unsafe_allow_html=True)
