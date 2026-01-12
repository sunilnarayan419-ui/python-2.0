# Boolean Type

is_student = True  

print(f"You are a {'student' if is_student else 'professional'}")

if is_student:
    print("You are a student!")
else:
    print("You are NOT a student.")

# Some regular methods 
# 1. __bool__()
# Returns the Boolean value of an object. 

x = True
print(x.__bool__()) 

# 2. __str__()
# Converts Boolean to string.

x = True
y = False 
print(str(x)) 
print(str(y)) 
 
# 3. __int__()
# Converts Boolean to integer.

x = True
y = False 
print(int(x)) 
print(int(y))
