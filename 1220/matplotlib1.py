import matplotlib.pyplot as plt
#Creating a Simple Line Plot
#Sample data
x=[1,2,3,4,5]
y=[2,3,5,7,11]

#Create the plot
plt.plot(x,y)

#Add labels and title
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#Display the plot
plt.show()

#Creating a Scatter Plot
#Sample data
x=[5,7,8,7,2,17,2,9,4,11]
y=[99,86,87,88,100,86,103,87,94,78]

#Create the scatter plot
plt.scatter(x,y)

#Add labels and title
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()

#Line plot with customizations
plt.plot(x,y, color="red", linestyle='--', marker='o', linewidth=2, markersize=8)
#Add title and labels
plt.title("Customized Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()