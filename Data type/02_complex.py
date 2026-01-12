# complex type 

real = float(input(f"Enter your real part : "))
imag = float(input(f"Enter your imaginary part : "))

complex_num = complex(real, imag)

print(f"Your real number: {real}, your imaginary number: {imag}")
print(f"Your complex number: {complex_num}")

# Some regular methods 
# 1. real
# Returns the real part of the complex number.

complex_num = 3 + 4j
print(complex_num.real) 

# 2. imag
# Returns the imaginary part  

complex_num = 3 + 5j
print(complex_num.imag) 

# 3. conjugate()
# Returns the complex conjugate. 

complex_num = 8 + 2j
print(complex_num.conjugate()) 

# NOT a method but used a lot 
# 1. complex

z = 3 + 4j
abs(z) # T get megnitude 
complex(2,4) # To create complex num

# 2. cmath 

import cmath

real = float(input(f"Enter your real num's real part : ")) 
img = float(input(f"Enter your num's immagnary part : ")) 

complex_num = complex(real , img)
print(complex_num) 

print(cmath.phase(complex_num)) # Angle (radians)  
print(cmath.polar(complex_num))  # (r , theta)
print(cmath.rect(3,45))  # convert polar to complex num 
print(cmath.sqrt(complex_num))

