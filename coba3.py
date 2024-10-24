import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import random

# Set page title and layout
st.set_page_config(page_title="UTS Fisika Komputasi Awan", layout="centered")

# Header
st.markdown("<h1 style='text-align: center; color: #1f77b4;'>UTS Fisika Komputasi Awan</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #1f77b4;'>Amelia Fadhil Nurlaila</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #1f77b4;'>210322607210</h4>", unsafe_allow_html=True)

# Circle definition
circle = Circle((0, 0), 1, color='green', fill=False, linewidth=2, linestyle='-', alpha=0.2)

# Initialize data
x = []
y = []
color = []
size = []
x.append(0)
y.append(0)
color.append((0., 0.7, 0.))
size.append(371)

# Button interaction
if st.button("Generate Random Data"):
    for i in range(111):
        x0 = 2*(random.random() - .5)
        y0 = 2*(random.random() - .5)
        if (x0**2 + y0**2) > 1.:
            y0 = np.sqrt(1 - x0**2) if y0 > 0 else -np.sqrt(1 - x0**2)
        
        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))
        size.append(3713 * random.random())

# Create figure and plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.add_patch(circle)

# Plot lines from center
for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='red', linestyle='--', alpha=0.2)

# Scatter plot
ax.scatter(x, y, c=color, s=size, alpha=0.6, edgecolor='black')

# Set labels and title
ax.set_ylabel("Y-axis", fontsize=14, color='blue')
ax.set_xlabel("X-axis", fontsize=14, color='blue')
ax.set_title('Randomly Generated Data Inside a Circle', fontsize=16, color='purple')

# Customize ticks and grid
ax.tick_params(axis='y', labelsize=12, colors='purple')
ax.tick_params(axis='x', labelsize=12, colors='purple')
ax.grid(True, linestyle='-.', alpha=0.7)

# Set limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])

# Display the plot in Streamlit
st.pyplot(fig)

# Add caption below the plot
st.caption("Points are generated randomly and constrained within a circle of radius 1. Each point has a random size and color.")
