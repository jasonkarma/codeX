import pandas as pd

df = pd.read_csv('sales.csv')

#1. Explore the dataset
print("Dataset Overview:")
print(df.head())  # Display the first 5 rows

#2. Calculate total sales and quantity by category
category_summary = df.groupby('Category')[['Sales', 'Quantity']].sum()
print("\nTotal Sales and Quantity by Category:")
print(category_summary)

#3.Filter data for the North region
north_data = df[df['Region'] == 'North']
print("\nSales Data for North Region:")
print(north_data)

#4. Sort the dataset by sales
sorted_data = df.sort_values('Sales', ascending=False)
print("\nData Sorted by Sales:")
print(sorted_data)

#5. Export the sorted data to a new CSV
sorted_data.to_csv('sorted_sales.csv', index=False)
print("\nSorted data exported to 'sorted_sales.csv'")