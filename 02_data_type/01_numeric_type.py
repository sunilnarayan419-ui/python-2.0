# Integer type 

num1 = int(input(f"Enter your frist num : ")) 
num2 = int(input(f"Enter your second num : ")) 

print(f"your frist num is {num1}") 
print(f"your second num is {num2}") 

# float type 

num1 = float(input(f"Enter your frist num : ")) 
num2 = float(input(f"Enter your second num : ")) 

print(f"your frist num is {num1}") 
print(f"your second num is {num2}") 


# complex type 

num1 = complex(input(f"Enter your frist num : ")) 
num2 = complex(input(f"Enter your second num : ")) 

print(f"your frist num is {num1}") 
print(f"your second num is {num2}") 

# Type casting 

x = 1 
y = 3.4 
z = 3 + 5j

print(type(x)) 
print(type(z)) 
print(type(y)) 

a = float(x) 
b = int(y) 
c = complex(x) 

print(type(a)) 
print(type(b)) 
print(type(c)) 

# range  

x = 8

for i in range(1 ,11): 
    print(f" {x} x {i} = {x*i}") 

# random number 

import random 

x = random.randrange(0 ,200 ,2)  

print(x) 
    
    