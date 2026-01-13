friends = 0
friends = friends + 1 
friends = friends-2
friends+= 1
friends = friends*3
friends = friends/2
friends = friends**2
friends**= 2
remainder = friends % 3
friends/=2

print(friends)  

# next round

x = 3.14
y = 4
z = 5

result = round(x)
result = abs(y)
result = pow(4,3)
result = max(x , y , z)
result = min(x, y, z)
print(result)

# next round
import math 

x =45

print(math.pi)
print(math.e)
result = math.sqrt(x)
result = math.ceil(x)
result = math.floor(x)
print(result)


# ex 1
# circumfrence of a circle

import math
r = float(input(f"Enter the radius od a circle : "))
c = 2*math.pi*r

print(f"The circumjfrence is : {round(c,2)} cm") 

# ex 2
# area of a circle
import math
r = float(input(f"Enter the radius of a circle : "))
a = math.pi*pow(r,2)

print(f"The area of the circle is : {round(a,2)} cm^2")

# ex 3
# hyponeteous

import math

a = float(input(f"Enter side A : "))
b = float(input(f"Enter side B : "))

c = math.sqrt(pow(a,2) + pow(b , 2))

print(f"Side C = {c}")