import pandas as pd

df = pd.read_csv('data.csv')

#display the DataFrame
print("DataFrame loaded from CSV:")
print(df)

#display specific columns
print("\nName Column:")
print(df['Name'])

#summary statistics
print("\nSummary Statistics:")
print(df.describe())