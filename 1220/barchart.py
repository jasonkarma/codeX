import matplotlib.pyplot as plt

#Data
categories = ['A', 'B', 'C', 'D']
values=[5,7,3,8]

#Create the bar chart
plt.bar(categories,values, color='blue')

#Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')

#Display the chart
plt.show()

#Customizing Bar Charts
# Horizontal bar chart with customizations
plt.barh(categories, values, color='green', edgecolor='black', height=0.5)
plt.title("Horizontal Bar Chart Example")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()

#Histograms
#Sample data
data=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

#Create the histogram
plt.hist(data, bins=5, color='purple', edgecolor='black')

#Add labels and title
plt.xlabel('Data Values')
plt.title('Histogram Example')
plt.ylabel('Frequency')

#Display the histogram
plt.show()
