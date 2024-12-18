import pandas as pd

sales_data = {
    "Product": ["Phone", "Laptop", "Tablet"],
    "Sales": [699, 1200, 399],
}
region_data = {
    "Product": ["Phone", "Laptop", "Tablet"],
    "Region": ["North", "South", "East"]
}

df_sales = pd.DataFrame(sales_data)
df_region = pd.DataFrame(region_data)

#Merge datasets on the "Product" column
merged_df = pd.merge(df_sales, df_region, on="Product")
print("Merged DataFrame:")
print(merged_df)
