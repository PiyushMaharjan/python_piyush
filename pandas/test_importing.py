import pandas as pd

df =pd.read_json("employee_data.json", orient="records")

print(df)