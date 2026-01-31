# variable scope and binding 

# nonlocal variable example

def counter():
    num = 0

    def incrementer():
        nonlocal num
        num += 1
        return num

    return incrementer


# example usage
c = counter()

print(c())  
print(c())  
print(c())  


# Global variable

x = "Hi"

# Reading a global variable

def read_x():
    print(x)

read_x()

# Trying to read an undefined variable (will fail)

# def read_y_fail():
    # print(y)   # y is not defined globally

# read_y_fail()   # ❌ Uncommenting this will raise NameError

# Local variable inside function

def read_y():
    y = "Yes"     # local variable
    print(y)

read_y()

# Local variable inside unreachable block

def read_x_local_fail():
    if False:
        x = "Hey"   # local variable (never executed)

    print(x)       # refers to GLOBAL x

read_x_local_fail()

# Level 

x = "hi" 

def change_local_x(): 
    x = "Bye" 
    print(x) 
change_local_x() 
print(x) 

# level 

x = "sunil" 

def change_global_x(): 
    global x 
    x = "sadik" 
    print(x) 
    
change_global_x() 
print(x) 

# TO summarize: 
""" 
1. If you've found global x, then x is a global variable. 
2. if you've found nonlocal x, then x belongs to an enclosing function ,and is neither local nor global.
3. if you've found x = 5 or for x in range(4) or some other binding , then x is a local variable.
4. otherwise x belongs to some enclosing scope (function scope , global scope , or builtins) 
""" 

# local variable 

def foo(): 
    if True: 
        a = 5 
    print(a) 
    
b = 3 
def bar(): 
    b = 5 
print(b) 


# THE del COMMAND 

# del with class attributes
class Student:
    """This class demonstrates the del command"""

    name = "Sunil Narayan"
    age = 21
    college = "University of Hyderabad"


# Access class attributes
print(Student.name)
print(Student.age)
print(Student.college)

# Delete class attributes
del Student.name
del Student.age
del Student.college

# Uncommenting below lines will raise AttributeError
# print(Student.name)
# print(Student.age)
# print(Student.college)

# del with list (slice deletion)

x = [0, 1, 2, 3, 4]

del x[1:2]
print(x)

# FUNCTIONS SKIP CLASS SCOPE WHEN LOOKING UP NAMES

# Global variable
a = "global"


class Fred:
    # Class variable
    a = "class"

    # Generator expression
    # Looks for 'a' → does NOT see class scope → uses GLOBAL 'a'
    b = (a for i in range(10))

    # List comprehension
    # Has its own scope → skips class scope → uses GLOBAL 'a'
    c = [a for i in range(10)]

    # Simple assignment in class body
    # This DOES see class scope
    d = a

    # Lambda function
    # Name lookup happens when function is CALLED → uses GLOBAL 'a'
    e = lambda: a

    # Lambda with default argument
    # Default args are evaluated at definition time → captures CLASS 'a'
    f = lambda a=a: a

    # Static method
    # Behaves like a normal function → skips class scope → uses GLOBAL 'a'
    @staticmethod
    def g():
        return a


# --------------------------------------------
# Outputs
# --------------------------------------------
print(Fred.a)        # class
print(next(Fred.b))  # global
print(Fred.c[0])     # global
print(Fred.d)        # class
# print(Fred.e())      # global
# print(Fred.f())      # class
print(Fred.g())      # global

# Function within Function (Nested functions + nonlocal)

def func1():
    foo = 10   # enclosing variable

    def func2():
        nonlocal foo

        def func3():
            nonlocal foo
            print("Before:", foo)
            foo = 20
            print("After :", foo)

        func3()

    func2()
    print("Final :", foo)


func1()


# Binding Occurrence 

x = 34

for i in range(1, 11):
    print(f"{x} x {i} = {x * i}")
