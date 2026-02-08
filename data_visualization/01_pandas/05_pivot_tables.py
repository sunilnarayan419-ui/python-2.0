import pandas as pd 

data = {
    'city': ['New York' , 'los angeles' , 'vadodara' ,'hyderabad' , 'indore'] , 
    'Month':['jan' , 'feb' , 'jan' , 'feb' , 'may'],
    'sales': [200,300,450,600,550]
    
} 

df = pd.DataFrame(data) 
pivot_table = df.pivot_table(values='sales' , index='city' , columns='Month' , aggfunc='sum',fill_value=0) 
print(pivot_table) 

# level 

data = { 
        'Gender': ['Male' , 'Female' ,'Male' , 'Female' ,'Female' ] , 
        'Purchased':['Yes' , 'No', 'Yes' , 'No' ,'Yes']
        } 

df = pd.DataFrame(data) 
cross_tab = pd.crosstab(df['Gender'] , df['Purchased']) 
print(cross_tab) 