import pandas as pd

data = {
    "Date": ["2024-12-01", "2024-12-01", "2024-12-02", "2024-12-02"],
    "Category": ["Electronics", "Furniture", "Electronics", "Furniture"],
    "Sales": [1000, 200, 1500, 300],
    "Region": ["North", "South", "North", "South"]
}
df = pd.DataFrame(data)

# Create a pivot table
pivot = df.pivot_table(
    values="Sales", index="Category", columns="Region", aggfunc="sum", fill_value=0
)
print("\nPivot Table:")
print(pivot)