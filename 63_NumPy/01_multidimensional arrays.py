import numpy as np 

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','P'],['Q','R','S']],
                  [['T','U','V'],['X','Y','Z'],['1','2','3']]])  

print(array.ndim) 
print(array.shape) 
print(array[0][0][0])  
print(array[2,2,2]) 

word = array[0,0,0] + array[2,0,0] + array[2,0,0] 
print(word) 