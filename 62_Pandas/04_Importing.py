import pandas as pd

df = pd.read_csv(r"C:\Users\HOME\Downloads\pokedex_(Update.04.20).csv" , index_col="Name")
print(df) 
print(df.to_string()) 

# SELECTION BY COLUMN 

print(df["Name"].to_string) 
print(df[["Name", "Height","Weight"]].to_string()) 

# SELECTION BY ROW/S
print(df.loc[0]) 
print(df)   
print(df.loc["Chaarizard"])
print(df.loc["Chaarizard"] , ["Height" , "Weight"]) 
print(df.loc["Chaarizard" : "Blastoise" , ["Height" , "Weight"]]) 
print(df.iloc[0:11:2 , 0:3])  

# 

pokemon = input("Enter a Pokemon name : ") 

try: 
    print(df.loc[pokemon]) 
except KeyError: 
    print(f"{pokemon} is not found") 