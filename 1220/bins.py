import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randint(1, 101, 100)  # 100 random integers between 1 and 100

# Plot histograms with different bin sizes
plt.figure(figsize=(12, 6))

# Few bins
plt.subplot(1, 3, 1)
plt.hist(data, bins=5, color='blue', edgecolor='black')
plt.title("5 Bins")

# Moderate bins
plt.subplot(1, 3, 2)
plt.hist(data, bins=10, color='green', edgecolor='black')
plt.title("10 Bins")

# Many bins
plt.subplot(1, 3, 3)
plt.hist(data, bins=20, color='red', edgecolor='black')
plt.title("20 Bins")

# Show the plots
plt.tight_layout()
plt.show()
