# Boolean 

x = 23 
y = 45 

if y > x: 
    print(f"y is greater than x") 
else: 
    print(f"y is less than x") 
    
# level 

print(bool("sunil")) 
print(bool(23)) 

# level 

x = "sunil" 
y = 12 

print(bool(x)) 
print(bool(y)) 

# level 

print(bool(False)) 
print(bool(None)) 
print(bool(0)) 
print(bool("")) 
print(bool(())) 
print(bool([])) 
print(bool({})) 

# level 

class myclass(): 
    def __len__(self): 
        return 0 
    
myobj = myclass() 
print(bool(myobj)) 

# func can return a boolean 

def myFunction(): 
    return True 
print(myFunction()) 

# level 

def Student(): 
    return True 

if Student(): 
    print("YES!") 
else: 
    print("NO!") 

# level 

x = 400 
print(isinstance(x , int)) 