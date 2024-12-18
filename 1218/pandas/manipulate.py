import pandas as pd

df = pd.read_csv('data.csv')

#filter rows where age is greater than 30
filtered_df = df[df['Age'] > 30]
print("Filtered Data (Age > 30):")
print(filtered_df)

#Add a new column
df['Salary'] = [50000, 60000, 70000]
print("\nDataFrame with New Column (Salary):")
print(df)

#Sort the DataFrame by Age
sorted_df = df.sort_values('Age')
print("\nSorted DataFrame by Age:")
print(sorted_df)