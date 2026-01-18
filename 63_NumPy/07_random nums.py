import numpy as np 

rng = np.random.default_rng() 

print(rng.integers(low=1,high=100 , size=(3,2))) 

np.random.seed(seed=1) 

print(np.random.uniform(low=-1 , high=2 , size=(3,4)))  

array = np.array([1,2,3,4,5]) 
rng.shuffle(array) 
print(array) 

fruits = np.array(["apple" , "orange" , "banana" , "coconut" , "pineapple"]) 
fruits = rng.choice(fruits , size=(3,3)) 
print(fruits) 