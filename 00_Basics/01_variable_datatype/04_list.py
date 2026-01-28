# ================================
# LIST DATATYPE IN PYTHON
# ================================


# --------------------------------
# List initialization
# --------------------------------
my_list = [10, 20, 30, 40, 50]
print(my_list)


# ================================
# REGULAR LIST METHODS
# ================================

# Add elements
my_list.append(90)
my_list.insert(2, 300)
my_list.extend([23, 45, 34])

# Remove elements
my_list.remove(30)
my_list.pop(2)

# Searching & counting
print(my_list.index(10))
print(my_list.count(20))

# Sorting & reversing
my_list.sort()
my_list.sort(reverse=True)
my_list.reverse()

# Copying list
new_list = my_list.copy()
print(new_list)
print(my_list)

# Clearing list (keep this at the end)
my_list.clear()
print(my_list)


# ================================
# LIST OPERATIONS
# ================================

a = [3, 5, 6, 7]
b = [7, 9]


# --------------------------------
# Concatenation & repetition
# --------------------------------
print(a + b)
print(a * 4)


# --------------------------------
# Membership operators
# --------------------------------
print(3 in a)
print(23 not in b)


# --------------------------------
# Length
# --------------------------------
print(len(a))


# --------------------------------
# Indexing
# --------------------------------
print(a[3])
print(a[-3])


# --------------------------------
# Slicing
# --------------------------------
print(a[1:3])
print(a[:2])
print(a[1:])


# --------------------------------
# Updating list (mutability)
# --------------------------------
a[1] = 1008
print(a)


# --------------------------------
# Looping through list
# --------------------------------
for item in a:
    print(item * 5)
