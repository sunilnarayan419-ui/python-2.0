import pandas as pd 

# Data cleaning = the process of fixing/removing:
# incomplete , incorrect, or irrelevant data. 
# ~75% of work done with Pandas is data cleaning.

df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex_(Update.04.20).csv") 

# 1. Drop irrelevant colums 
df = df.drop(columns=["Legendary", "No"]) 

# 2. Handle missing data 

df = df.dropna(subset=["Type2"])
df = df.fillna({"Type2":"None"}) 

# 3. Fix incosistent values 

df["Type1"] = df["Type1"].replace({"Grass":"GRASS" , "Fire":"FIRE","Water":"WATER"}) 

# 4. Standrize text 

df["Name"] = df["Name"].str.lower() 

# 5. Fix data type 

df["Legendary"] = df["Legendary"].astype(bool) 

# 6. Remove duplicate values

df = df.drop_duplicates() 

print(df) 
print(df.to_string()) 