import pandas as pd

data = {
       "Name": ["Alice", "Bob", "Charlie", "David"],
       "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3", "Employee 4"])

#add a new column to the DataFrame

df["City"] = ["New York", "Los Angeles", "Chicago", "Houston"]
df["job"] = ["Engineer", "Doctor", "Artist", "Lawyer"]


#add a new rows to the DataFrame
new_rows = pd.DataFrame([{"Name": "Eve", "Age": 28, "City": "San Francisco", "job": "Designer"},
                         {"Name": "Frank", "Age": 32, "City": "Seattle", "job": "Manager"}], 
                       index=["Employee 5", "Employee 6"],
                       
                       )

df = pd.concat([df, new_rows])

print(df)  
