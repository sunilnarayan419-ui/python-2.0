import pandas as pd 

# df1 = pd.DataFrame({'ID' : [1,2,3] , 
#                     'Name': ['olivia' , 'sadik' , 'aman' ,]}) 

# df2 = pd.DataFrame({'ID' : [2,3,4] , 'Score' : [92,87 ,96]}) 

# merged_df = pd.merge(df1 , df2 , on='ID') 
# print(merged_df)  

# level 

import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['olivia', 'sadik', 'aman']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Score': [92, 87, 96]
})

df3 = pd.DataFrame({
    'ID': [5, 6],
    'Name': ['David', 'Eve']
})

df1.set_index(keys='ID', inplace=True)
df2.set_index(keys='ID', inplace=True)

joined_df = df1.join(df2, how='inner')

concat_df = pd.concat(
    objs=[df1.reset_index(), df3],
    ignore_index=True
)

print(concat_df)
print(joined_df)
