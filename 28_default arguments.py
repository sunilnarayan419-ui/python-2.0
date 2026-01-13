# deefault arguments = A default value for certain parameters
# default is used when that argument is omitted 
# make your functions more flexible , reduce # of arguments 
# 1. positional , 2. default , 3. keyword , 4. arbitrary 

# default statements
def price_as(list_price, discount=0, tax=0.7):
    return list_price * (1 - discount) * (1 + tax)
 
print(price_as)
# Positional arguments
price = price_as(500, 0, 0.5)

print(price)

# default statement
def net_price(list_price , discount=0 , tax=0.5):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500)) 


# ex 1
import time

def co(start, end):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE")

# Function call
co(1, 5)


def count( end , start=0):
    for x in range( start , end+1 ):
        print(x)
        time.sleep(1)
    print("DONE")
    
count(0 , 10)