# Typecasting = The process of converting a value of one data type to another 
# ( string , integer , float , boolean ) 
# Explicit vs Implicit 

# Explicit

name = "sunil" 
age = 20 
gpa = 6.0
student = True 

print(type(name))
print(type(age)) 
print(type(gpa)) 
print(type(student)) 

age = float(age) 
print(type(age)) 
print(age) 

gpa = int(gpa) 
print(gpa) 

student = str(student) 
print(student) 
print(type(student))  

age = bool(age) 
print(age) 

name = bool(name) 
print(name) 

# Implicit 

x = 2
y = 2.0

x = x/2

print(x) 