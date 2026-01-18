import numpy as np 

# Broadcasting allows NumPy to perform operation on arrays 
# with different shapes by virtually expanding dimesions
# so they match the larger arry's shape 

# The dimensions have the same size 
# or 
# one of the dimensions has a size of 1  


array1 = np.array([[1,2,3,4]]) 

array1 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])  
array2 = np.array([[1] , [2] ,[3] , [4]]) 

print(array1.shape) 
print(array2.shape) 

print(array1 * array2) 

# Ex 

array1 = np.array([1,2,3,4,5,6,7,8,9,10]) 
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]) 

print(array1.shape) 
print(array2.shape) 

print(array1 * array2) 