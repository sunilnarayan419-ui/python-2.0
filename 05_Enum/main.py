# Enum 

# Creating an enum 

from enum import Enum 

class Colour(Enum): 
    red = 1 
    green = 2 
    blue = 3 
    
print(Colour.red) 
print(Colour(1)) 
print(Colour["red"]) 

# Iteration

from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

# iterate over enum members
colors = [c for c in Color]
print(colors)

