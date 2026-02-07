import pandas as pd 
import numpy as np  

# data = pd.DataFrame({ 
#                     'Name': ['sunil' , 'sadik' , 'aman'  , 'narayan'],
#                     'Age': [20,np.nan , np.nan , 30] , 
#                     'Score': [85 , 90 , np.nan ,95] 
# }) 

# data['Age'].fillna(data['Age'].mean() , inplace=True) 
# data['Score'].fillna(data['Score'].mean(), inplace=True) 

# print(data) 

# level 

# data = pd.DataFrame({'Name': ['Sunil' , 'sadik' , 'aman ' , 'narayan'],
#                      'Age' :[25,30,35,40], 
#                      'Score': [85 ,90 , 85 , 95] 
# }) 

# data.drop_duplicates(inplace=True) 

# print(data) 

# level 

from scipy.stats import zscore

data = pd.DataFrame({
    'Name': ['lucy', 'noah', 'oliver', 'ruby', 'sophia'],
    'Age': [25, 30, 35, 40, 90],
    'Score': [85, 90, 80, 150, 95]
})

# calculate z-scores from actual columns
data['Z_Age'] = zscore(data['Age'])
data['Z_Score'] = zscore(data['Score'])

# filter rows without outliers
cleaned_data = data[
    (data['Z_Age'].abs() <= 3) &
    (data['Z_Score'].abs() <= 3)
]

print("Data after removing outliers:\n",  
      cleaned_data[['Name', 'Age', 'Score']])

