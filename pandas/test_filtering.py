import pandas as pd

df = pd.read_csv("employee_data.csv")

age_employees = df[df['Age'] >= 30]
job_employees = df[df['Job'] == 'Engineer']
name_employees = df[(df['Name'] == 'Alice')|
                    (df['Name'] == 'Bob')]
id_employees = df[(df['EmployeeID'] == 'E002') & 
                  (df['EmployeeID'] == 'E004')]


print(age_employees)
print(job_employees)
print(name_employees)
print(id_employees)