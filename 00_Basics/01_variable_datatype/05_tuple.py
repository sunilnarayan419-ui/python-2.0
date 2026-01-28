# ================================
# TUPLE DATATYPE IN PYTHON
# ================================

# A tuple is:
# - Ordered
# - Immutable (cannot be changed)
# - Written using round brackets ()

"""
Tuples are ordered, immutable collections with limited methods
but full support for indexing and slicing.
"""


# --------------------------------
# Tuple initialization
# --------------------------------
my_tuple = (10, 23, 45, 67, 68)
print(my_tuple)


# ================================
# TUPLE METHODS
# ================================

print(my_tuple.count(23))
print(my_tuple.index(23))


# ================================
# TUPLE OPERATIONS
# ================================

a = (1, 2, 3)
b = (4, 5)


# --------------------------------
# Concatenation & repetition
# --------------------------------
print(a + b)
print(a * 4)


# --------------------------------
# Membership operators
# --------------------------------
print(2 in a)
print(23 not in a)


# --------------------------------
# Length
# --------------------------------
print(len(a))


# --------------------------------
# Indexing
# --------------------------------
print(a[0])
print(a[-2])


# --------------------------------
# Slicing
# --------------------------------
print(a[1:3])
print(a[:2])
print(a[1:])


# --------------------------------
# Looping through tuple
# --------------------------------
for item in a:
    print(item + 3)


# --------------------------------
# Tuple packing & unpacking
# --------------------------------
tup = 10, 20, 30
x, y, z = tup
print(x, y, z)


# --------------------------------
# Type conversion (tuple ↔ list)
# --------------------------------
temp_list = list(a)
print(tuple(temp_list))
