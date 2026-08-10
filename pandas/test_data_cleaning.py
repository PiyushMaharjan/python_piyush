import pandas as pd

df = pd.read_csv("employee_data.csv")

#drop the column
df = df.drop(columns=['Job'], axis=1)

#handle missing data
df = df.dropna(subset=['Age', 'City'])
df = df.fillna({'City': 'panga'})

#fix inconsistent data
df['City'] = df['City'].replace({"panga": "Panga"})

#standardize data formats
df['Salary'] = df['Salary'].replace('[\$,]', '', regex=True).astype

#fix data types
df['Age'] = df['Age'].astype(int)
df['Salary'] = df['Salary'].astype(float)
print(df)