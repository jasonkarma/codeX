import pandas as pd

df=pd.read_csv('titanic.csv')
print(df.head())

#clean the data
if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].mean())
print("Missing values handled successfully.")
#analyze the data 
#count passengers by gender
gender_counts = df['Sex'].value_counts()
print(gender_counts)

#claculate survival rate by gender and passenger class
gender_class_counts = df.groupby(['Sex', 'Pclass'])['Survived'].value_counts()
print(gender_class_counts)

#visualize the data
import matplotlib.pyplot as plt

#plot survival rate by gender and passenger class
gender_class_counts.plot(kind='bar', stacked=True)
plt.xlabel('Gender and Passenger Class')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Gender and Passenger Class')
plt.show()


