# ================================
# FROZENSET DATATYPE IN PYTHON
# ================================

# A frozenset is:
# - Unordered
# - Immutable (cannot be changed)
# - Stores unique elements
# - Immutable version of set

"""
A frozenset is an immutable set
that supports all set operations but no modification.
"""


# --------------------------------
# Frozenset initialization
# --------------------------------
fs = frozenset([1, 2, 3, 4, 5])
print(fs)


# ================================
# FROZENSET METHODS
# ================================

a = frozenset([3, 4, 5, 6, 7])
b = frozenset([5, 6, 4, 3, 7])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print({1, 3}.issubset(a))
print(a.issuperset({1, 4}))
print(a.copy())


# ================================
# FROZENSET OPERATIONS
# ================================

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)


# --------------------------------
# Membership
# --------------------------------
print(3 in a)


# --------------------------------
# Length
# --------------------------------
print(len(b))


# --------------------------------
# Looping through frozenset
# --------------------------------
for item in a:
    print(item * 2)
