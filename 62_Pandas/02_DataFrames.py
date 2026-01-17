import pandas as pd 

# DataFrame = A tabular data structure with rows AND columns . (2-D) 
# Similar to an Excel spreadsheet 

data = {"Name":["Spongebob","Patrick" , "Squiward"] , 
        "Age": [30,35,45]
        }

df = pd.DataFrame(data) 
df = pd.DataFrame(data , index=["Employee 1 " , "Employee 2 ", "Employee 3 "]) 
print(df) 
print(df.loc["Employee 1"]) 
print(df.iloc[2])  

# Add a new colomn

df["Job"]  =["Cook" , "N/A" , "Casier"] 
print(df) 

# Add a new rows

new_rows = pd.DataFrame([{"Name":"Sandy" , "Age":28 ,"Job": "Engineer "},
                         {"Name":"Eugene" , "Age":60 ,"Job": "Manager"}],
                        index=["Employee 4" , "Employee 5"]) 
df = pd.concat([df , new_rows]) 

print(df) 