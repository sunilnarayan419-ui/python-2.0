# ================================
# SET DATATYPE IN PYTHON
# ================================

# A set is:
# - Unordered
# - Mutable
# - Stores unique elements only
# - Written using curly braces {}

# Important Set Rules:
# - No duplicate elements
# - No indexing or slicing
# - Elements must be immutable
# - Sets are unordered


# --------------------------------
# Set initialization
# --------------------------------
my_set = {2, 3, 4, 5, 7, 8}
print(my_set)


# ================================
# SET METHODS
# ================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Adding elements
a.add(5)
a.update([78, 56])

# Removing elements
a.remove(4)
a.discard(90)
a.pop()

# Copying set
new_a = a.copy()
print(new_a)

print(a)


# ================================
# SET OPERATIONS
# ================================

# Union
print(a | b)
print(a.union(b))

# Intersection
print(a & b)
print(a.intersection(b))

# Difference
print(a - b)
print(a.difference(b))

# Symmetric Difference
print(a ^ b)
print(a.symmetric_difference(b))


# --------------------------------
# Membership
# --------------------------------
print(3 in a)


# --------------------------------
# Length
# --------------------------------
print(len(a))


# --------------------------------
# Looping through set
# --------------------------------
for item in a:
    print(item * 3)


# --------------------------------
# Subset & Superset
# --------------------------------
print({1, 2}.issubset(a))
print(a.issuperset({1, 2}))


# --------------------------------
# Clearing set (keep at the end)
# --------------------------------
a.clear()
print(a)
