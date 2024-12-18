import pandas as pd 
import numpy as np

#Sample dataset with missing values
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, np.nan, 35],
    "City": ["New York", "Los Angeles", None, "Chicago"]
}
df = pd.DataFrame(data)

#Detect missing values
print("Detect missing values:")
print(df.isnull())

#Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)

print("\nAfter filling missing values:")
print(df)

#Drop rows with missing values (if any remain)
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:")
print(df_dropped)