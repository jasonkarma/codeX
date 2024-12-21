import matplotlib.pyplot as plt

# Region data
regions = ["North", "South", "East", "West"]
sales = [200, 150, 300, 400]

plt.figure(figsize=(10,8))
# Create separate figures for each region
for i, region in enumerate(regions):
    plt.subplot(2, 2, i + 1)
    plt.bar([region], [sales[i]], color="blue")
    plt.title(f"Sales in {region} Region")
    plt.xlabel("Region")
    plt.ylabel("Sales")
    
plt.tight_layout()
plt.show()

# Example: Accuracy and loss of 2 models
epochs = range(1, 11)
model1_acc = [0.7, 0.75, 0.8, 0.85, 0.88, 0.9, 0.91, 0.92, 0.93, 0.94]
model2_acc = [0.6, 0.65, 0.7, 0.78, 0.83, 0.85, 0.87, 0.88, 0.89, 0.9]

# Model 1 plot
plt.figure(figsize=(6, 4))
plt.plot(epochs, model1_acc, label="Model 1 Accuracy", color="blue")
plt.title("Model 1 Performance")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Model 2 plot
plt.figure(figsize=(6, 4))
plt.plot(epochs, model2_acc, label="Model 2 Accuracy", color="green")
plt.title("Model 2 Performance")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# Slide 1 - Simple Bar Chart
plt.figure(figsize=(8, 4))
plt.bar(["A", "B", "C"], [10, 20, 15], color="blue")
plt.title("Bar Chart Example")
plt.show()
