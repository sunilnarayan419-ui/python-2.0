# *args = allows you to pass multiple non-key arguments
# **kwags = allows you to pass multiple keyword-arguments
# *unpacking operator

def add(a ,b):
    return a + b

print(add(1,2)) 


# ex 1 
def display_name(*args):
    for arg in args:
        print(arg , end=" ")
    display_name("Mr","sunil","narayan") 

# ex 2
def print_address(**kwargs):
    print(type(kwargs))
    
print_address(street="sunil",city="vadodara",state="gujarat" ) 

# ex 3 
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")           
        
    
shipping_label("Mr", "sunil","narayan",
               country="INDIA",
               state="Gujarat",
               dist="vadodara",
               city= "vadodara",
               area= "karelibag",
               )