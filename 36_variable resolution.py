# variable scope : where a variable is visible and accessible.
# scope resolution = ( LEGB) local -> Enclosed -> Global ->Build-in

def func1():
    a = 1
    print(a)
def func2():
    b =2 
    print(b)
    
func1()
func2()


def happy_birthday(name , age):
    print(f"Happy birthday dear {name}")
    print(f"You are {age} years old")
    
def main():
    name = "Sunil"
    age = 21
    happy_birthday(name, age)
    main()
    
    
from math import e 

def func3():
    print(e)
    
