# ================================
# BOOLEAN DATATYPE IN PYTHON
# ================================

# What is Boolean?
# - Only two values: True and False
# - Subclass of int (True == 1, False == 0)
# - Used in conditions, loops, comparisons

"""
Boolean represents truth values and is the backbone
of conditions, comparisons, and control flow in Python.
"""


# --------------------------------
# Boolean variable & condition
# --------------------------------
online = False

if online != False:
    print("Yes!! He is online.")
else:
    print("No!! He is not online.")


# ================================
# BOOLEAN METHODS (TYPE CONVERSION)
# ================================

print(str(True))
print(int(True))
print(int(False))


# ================================
# BOOLEAN OPERATIONS
# ================================

a = True
b = False


# --------------------------------
# Logical operators
# --------------------------------
print(a and b)
print(a or b)
print(not a)


# --------------------------------
# Comparison operators
# --------------------------------
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# --------------------------------
# Membership operators
# --------------------------------
print(2 in [1, 2, 3])
print("a" not in "cat")


# --------------------------------
# Identity operators
# --------------------------------
print(a is True)
print(b is False)
print(a is not b)


# ================================
# TYPE CONVERSION TO BOOLEAN
# ================================

print(bool(1))
print(bool(0))
print(bool(""))
print(bool("hello"))
print(bool([]))
print(bool([1, 2]))


# ================================
# BOOLEAN IN CONTROL FLOW
# ================================

# if-else
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# while loop
flag = True

while flag:
    print("Running once")
    flag = False


# ================================
# BOOLEAN AS INTEGER
# ================================

print(True + True)
