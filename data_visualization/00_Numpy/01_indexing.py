import numpy as np 

# Indexing 

arry_2d = np.array([[1,2,3] , [4,5,6] ,[7,8,9]]) 

element = arry_2d[1,2]

print(arry_2d) 
print("element at row 1 , column 2:" , element) 



subarry = arry_2d[0:2 , 1:3] 

print(arry_2d) 
print("Sliced subarray:\n" , subarry) 

# reshaping 

import numpy as np

array_1d = np.array([1, 2, 3, 4, 5, 6])

array_reshaped = array_1d.reshape(2, 3)

print(array_1d)
print("Reshaped 2D Array:\n", array_reshaped)

