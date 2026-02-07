# numpy 

import numpy as np 

# data creating 

list_data = [1,2,3,4,5] 
arry_data = np.array(list_data) 

print("list:", list_data) 
print("Numpy Arry:" , arry_data) 

# other method 

start = 1000
stop = 10000 
step = 2 

arry_arange = np.arange(start , stop , step) 
print("Arry created with np.arrange:", arry_arange) 
