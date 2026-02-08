import numpy as np 
from scipy.linalg import inv, det 
from scipy.linalg import solve 
from scipy.linalg import svd 

matrix = np.array([
    [2, 1],
    [3, 4]
])

inverse = inv(matrix) 
determinant = det(matrix) 

print("Inverse:\n", inverse) 
print("Determinant:", determinant)

# level 

A = np.array([
    [3, 1],
    [1, 2]
])

B = np.array([9, 8])
x = solve(A, B)

print("Solution:", x)

# level 

matrix = np.array([[3,1,1] , [-1,3,1]])

U,S,VT = svd(matrix) 

print("U matrix:\n", U) 
print("Singular Values:" , S) 
print("VT matrix:\n" , VT) 