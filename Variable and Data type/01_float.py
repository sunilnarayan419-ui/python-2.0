# float type 

float_1 = float(input(f"Please enter your frist float : "))
float_2 = float(input(f"Please enter your second float  : "))  

print(f"Your frist float is {float_1} and your second float is {float_2}") 

# Some importance methods 
# Returns the float as a ratio of two integers.

# 1. as_integer_ratio

x  = 0.78
print(x.as_integer_ratio()) 

# 2. is_integer()
# Checks if the float value is mathematically an integer.

a = 4.0
b = 3.4

print(a.is_integer())
print(b.is_integer()) 

# 3. hex() 
# Return hexadecimal representation of a float 

c = 2.3 
print(c.hex())  

# 4. fromhex() 
# Create a float from a hexadecimal string.

d  = float.fromhex('0x1.c000000000000p+1')
print(d) 

