import pandas as pd 

# aggregate functionj = Reduce a set of values into a single summary value 
# Used to summarize and analyze data 
# Often used with the groupby() function 

df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex_(Update.04.20).csv") 

# Whole dataframe
print(df.mean(numeric_only=True)) 
print(df.sum(numeric_only=True)) 
print(df.min(numeric_only=True)) 
print(df.max(numeric_only=True)) 
print(df.count()) 

# Single column
print(df["Height"].mean()) 
print(df["Height"].sum()) 
print(df["Height"].min()) 
print(df["Height"].max()) 
print(df["Height"].count()) 

group = df.groupby("Type1") 

print(group["Height"].mean()) 
print(group["Height"].sum()) 
print(group["Height"].min()) 
print(group["Height"].count()) 