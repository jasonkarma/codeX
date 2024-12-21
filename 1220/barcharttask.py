import matplotlib.pyplot as plt
import numpy as np


# Sample data
random_numbers = np.random.randint(1, 10, 5)
categories = ['A', 'B', 'C', 'D', 'E']
# Create a bar chart
plt.bar(categories, random_numbers, color='pink')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

# Display the chart
plt.show()

#seed 
np.random.seed(42)
random_numbers= np.random.rand(5)
categories= ['A', 'B', 'C', 'D', 'E']
plt.bar(categories, random_numbers, color='blue')

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example with seed')
plt.show()