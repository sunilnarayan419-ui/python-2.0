# global variable 

name = "sunil narayan" 

def myfunc(): 
    print(f"My name is " + name) 
    
myfunc() 

# level 1

name = "sunil narayan" 

def myName():
    name = "Mohd. sadik" 
    print(f"my name is " + name) 
    
myName() 

print(f"My name is " + name) 

# level 2 

name = "sunil narayan" 

def Myname(): 
    global name 
    name = "mohd. sadik" 
    
myName() 

print(f"My name is " + name) 