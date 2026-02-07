import pandas as pd 

data = pd.DataFrame({'Name': ['sunil' , 'sadik' , 'aman'] , 
                     'Age': [30,60,90] , 
                     'Score': [45,60,00]
}) 

selected_columns = data[['Name' , 'Score']] 

print("Selected Columns:\n" , selected_columns) 

# level 

data = pd.DataFrame({'Name': ['sunil' , 'sadik' , 'aman'] , 
                     'Age': [30,60,90] , 
                     'Score': [45,60,00]
}) 

row_by_label = data.loc[1] 
row_by_position = data.iloc[2] 

print(row_by_label) 
print(row_by_position) 

# level 

data = pd.DataFrame({'Name': ['sunil' , 'sadik' , 'aman'] , 
                     'Age': [30,60,90] , 
                     'Score': [45,60,00]
}) 

filtered_data = data[data['Score'] >85 ] 

print("Filtered Data:\n" , filtered_data) 