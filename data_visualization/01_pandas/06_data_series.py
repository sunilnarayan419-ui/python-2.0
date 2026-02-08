import pandas as pd 

data = { 
    'Date': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-04'],
    'Sales': [350, 560, 400, 670] 
} 

df = pd.DataFrame(data) 

df['Date'] = pd.to_datetime(df['Date']) 
df.set_index(keys='Date', inplace=True) 

print(df)

# level 

data = { 
    'Date': ['2024-12-01', '2024-12-02', '2024-12-03', '2024-12-04'],
    'Sales': [350, 560, 400, 670] 
} 

df = pd.DataFrame(data) 

weekly_sales = df['Sales'] 
print(weekly_sales) 
