import numpy as np 
import random as rd 

random_integers = np.random.randint(1,100,size=(3,3)) 

random_floats = np.random.randint(1, 100 , size=(3,3)) 

print(random_integers) 
print(random_floats) 

# level 

tosses = np.random.choice(["Heads" , "Tails"] , size=100) 

heads_count = np.sum(tosses == "Heads") 
tails_count = np.sum(tosses== "Tails") 

print(tosses) 
print(heads_count) 
print(tails_count) 