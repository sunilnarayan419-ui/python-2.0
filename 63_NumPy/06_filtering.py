import numpy as np 

# Filtering = Refers to the process of selecting elements 
# from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]]) 

teenagers = ages[ages < 18] 
print(teenagers) 

adults = ages[(ages >= 18) & (ages < 605)] 
print(adults) 

seniors = ages[ages >= 65] 
print(seniors) 

even = ages[ages % 2 == 0] 
print(even) 

odd = ages[ages % 2 != 0] 
print(odd) 

adults = np.where(ages >= 18 , ages, 0) 
print(adults) 