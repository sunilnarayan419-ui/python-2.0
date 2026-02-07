import numpy as np 

# array1 = np.array([1,2,3,4]) 
# array2 = np.array([5,6,7,8]) 

# matrix1 = array1.reshape(2,2)
# matrix2 = array2.reshape(2,2)

# vertical_stack = np.vstack((matrix1 , matrix2)) 
# horizontal_stack= np.hstack((matrix1 , matrix2)) 

# print(vertical_stack) 
# print(horizontal_stack) 

# level 

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result = np.dot(matrix_a, matrix_b)

A = np.array([[2, 1], [1, 3]])
b = np.array([8, 18])

x = np.linalg.solve(A, b)

print("Matrix multiplication result:\n", result)
print("\nSolution to Ax = b:\n", x) 
