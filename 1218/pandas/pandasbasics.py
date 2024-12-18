import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Here is the DataFrame:")
print(df)

#Accessing specific columns
print("\nNames Column:")
print(df["Name"])

#Basic information about the DataFrame
print("\nDataFrame Information:")
print(df.info())