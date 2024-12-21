import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Year': [2018, 2019, 2020, 2021, 2022],
        'Sales': [150, 200, 250, 300, 400]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot using pandas
df.plot(x='Year', y='Sales', kind='line', title='Yearly Sales', marker='o')

# Customize the axes
plt.xlabel("Year")
plt.ylabel("Sales (in 1000s)")
plt.grid()

# Show the plot
plt.show()

#Bar chart
# Sample data
data = {'Region': ['North', 'South', 'East', 'West'],
        'Sales': [200, 150, 300, 400]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a bar chart
df.plot(x='Region', y='Sales', kind='bar', title='Regional Sales', color='skyblue')

# Customize the axes
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid(axis='y')

# Show the plot
plt.show()


#Histogram
# Sample data
data = {'Age': [22, 25, 29, 34, 23, 27, 40, 30, 36, 28]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a histogram
df['Age'].plot(kind='hist', bins=5, title='Age Distribution', color='green', edgecolor='black')

# Customize the axes
plt.xlabel("Age")
plt.ylabel("Frequency")

# Show the plot
plt.show()

#Scatter plot
# Sample data
data = {'Hours_Studied': [1, 2, 3, 4, 5, 6, 7, 8],
        'Scores': [35, 50, 55, 60, 70, 75, 80, 90]}

# Create a DataFrame
df = pd.DataFrame(data)

# Plot a scatter plot
df.plot(x='Hours_Studied', y='Scores', kind='scatter', title='Study Time vs Scores', color='red')

# Customize the axes
plt.xlabel("Hours Studied")
plt.ylabel("Scores")

# Show the plot
plt.show()
