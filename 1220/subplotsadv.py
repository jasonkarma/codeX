import matplotlib.pyplot as plt
import numpy as np

# Sample data
#Subplots: Arranging multiple plots together.
#Create grids of plots (2x2, 3x1, etc.).
#Customize spacing, titles, and axes.

# Data for multiple plots
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 5)

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot in each subplot
axes[0, 0].plot(x, y1, label="sin(x)", color="blue")
axes[0, 0].set_title("Sine Wave")
axes[0, 0].legend()

axes[0, 1].plot(x, y2, label="cos(x)", color="green")
axes[0, 1].set_title("Cosine Wave")
axes[0, 1].legend()

axes[1, 0].plot(x, y3, label="tan(x)", color="red")
axes[1, 0].set_title("Tangent Wave")
axes[1, 0].legend()

axes[1, 1].plot(x, y4, label="exp(x/5)", color="purple")
axes[1, 1].set_title("Exponential Growth")
axes[1, 1].legend()

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()