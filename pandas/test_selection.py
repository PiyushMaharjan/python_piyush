import pandas as pd

df = pd.read_csv("employee_data.csv", index_col="Name")

'''#selection by columns
print(df[['Name', 'Salary']].to_string()) '''

#selection by rows

'''print(df.loc['Eve'])'''

'''print(df.loc["Alice": "Eve", ["Age", "City"]])'''

employee = input("Enter employee name: ")

try:
    print(df.loc[employee])
except KeyError:
    print(f"'{employee}' not found.")
