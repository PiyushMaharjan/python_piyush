import pandas as pd

df = pd.read_json("employee_data.json")

print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.median(numeric_only=True))
print(df.std(numeric_only=True))

grouped = df.groupby('Job')
print(grouped.mean(numeric_only=True))