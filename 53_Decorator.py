# Decorator = A function that extends the behavior of another function 
# w/o modifing the base function 
# Pass the base function as an argument to the decorator

# @add_sprinkes
# get_ice_cream("Vanilla")  


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print(f"*You add sprinkles*")    
        func(*args, **kwargs)   
    return wrapper  

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print(f"*You add fudge*")    
        func(*args, **kwargs)
    return wrapper  

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here id your {flavor} ice cream")    

get_ice_cream("vanilla")     