# series  = A pandas 1-dimensional labeled array that can hold any data type 
# Think of it like a single column in a spreadsheet (1-D) 

import pandas as pd 

data = [100.5 , 102.4 , 104.7] 
data = [True , False , True] 
data = ["A", "V","B","R"] 
data = [100 , 102 , 104 ,200 , 202] 

series = pd.Series(data , index=["a", "b","c","d","e"])  
series = pd.Series(data) 

print(series) 

series.loc["C"] = 200
print(series.loc["C"])  

print(series.iloc[1]) 

print(series[series < 200])


# for dics

calories = {"Day 1":1750,
            "Day 2":2100,
            "Day 3":1700}

series = pd.Series(calories) 
series.loc["Day 3"] += 600 
print(series) 
print(series.loc["Day 3"])  

print(series[series >= 2000]) 