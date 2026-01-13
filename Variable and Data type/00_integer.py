# intiger type 
# Int : Whole nums 

int_1 = int(input(f"Enter your frist number : ")) 
int_2 = int(input(f"Enter your second number : ")) 

print(f"Your frist number is {int_1} and your second number is {int_2}") 

# Some regular methods
 
# 1. bit_length() 
# Returns number of bits needed to represent the integer in binary (excluding sign).

a = 10 
print(a.bit_length()) 

# 2. to_bytes() 
# convert integer to bytes
b = 234
print(b.to_bytes(5, byteorder= 'big'))  

# 3. from_bytes() 
# Creates integer from bytes.

c = b'\x00\xff'
d = int.from_bytes(c, byteorder='big')
print(d)

# 4. bit_count() 
# Count number of 1 s in binary representation 

e = 13 
print(e.bit_count()) 

# 5. __ads__ 
# internal method for absolute value

f = -67
print(f.__abs__()) 

