import numpy as np 

array1 = np.array([1,2,3,4]) 
array2 = np.array([5,6,7,8,]) 

sum_array = array1 + array2 
product_array = array1 * array2 

print(array1) 
print(array2) 

print("Element - wise sum : " , sum_array) 
print("Element - wise product :" , product_array) 

# level 

array = np.array([[2,3,6] , [8,2,9] , [7,9,1]]) 

array_sum = np.sum(array) 
array_mean = np.mean(array) 
array_max = np.max(array) 

print(array) 
print(array_sum) 
print(array_mean) 
print(array_max) 