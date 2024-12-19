import numpy as np
import matplotlib.pyplot as plt

# Generate normal distributions with different scales
data_small_scale = np.random.normal(loc=0, scale=1, size=1000)  # Scale = 1
data_large_scale = np.random.normal(loc=0, scale=3, size=1000)  # Scale = 3

# Plot
plt.hist(data_small_scale, bins=30, alpha=0.7, label='Scale = 1', density=True)
plt.hist(data_large_scale, bins=30, alpha=0.7, label='Scale = 3', density=True)
plt.legend()
plt.title("Effect of Scale on Normal Distribution")
plt.show()
