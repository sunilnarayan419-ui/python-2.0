import pandas as pd 

data = {'A': [1,2,3] , 'B': [4,5,6]} 
df = pd.DataFrame(data) 

df['Sum'] = df.apply(lambda row : row['A'] + row['B']  , axis=1) 
print(df) 

# level 

data = {'A': [1,2,3] , 'B': [4,5,6]} 
df = pd.DataFrame(data) 

df['A_squared'] = df['A'].map(lambda x: x**2) 
print(df) 

# level 

data = {'A': [1,2,3] , 'B': [4,5,6]} 
df = pd.DataFrame(data) 

df['A_plus_B'] = df.apply(lambda row: row['A']  + row['B'] , axis=1) 
df['A_plus_10'] = df['A'].map(lambda x: x + 10) 
print(df) 

