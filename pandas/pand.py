import pandas as pd

print(pd.__version__)

'''data = ([1, 2, 3, 4, 5])

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

series.loc['c']=8
print(series) #by location of index

print(series.iloc[2])#by loc of integer

print(series[series >= 3])#by condition'''

calories = {"Day 1":1750, "Day 2":2100, "Day 3":1700}

series = pd.Series(calories)

series.loc["Day 3"] += 500

print(series.loc["Day 3"])