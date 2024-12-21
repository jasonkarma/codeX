import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Scatter plot of total_bill vs tip
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex", size="size")

plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

# Distribution of total_bill
sns.histplot(data=tips, x="total_bill", kde=True, color="blue")

plt.title("Histogram with KDE: Total Bill")
plt.show()

# Box plot of total_bill by day
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")

plt.title("Box Plot: Total Bill by Day and Sex")
plt.show()

# Pair plot of numeric columns
sns.pairplot(tips, hue="sex", diag_kind="kde")

plt.title("Pair Plot of Tips Dataset")
plt.show()
