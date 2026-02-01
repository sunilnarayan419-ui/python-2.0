# ================================
# DICTIONARY DATATYPE IN PYTHON
# ================================

"""
A dictionary stores data in key–value pairs, is mutable,
and is used for fast lookup.
"""


# --------------------------------
# Dictionary initialization
# --------------------------------
student = {
    "name": "sunil",
    "age": 20,
    "city": "Hyderabad",
    "college": "UOH"
}

print(student)


# ================================
# DICTIONARY METHODS
# ================================

# Accessing keys, values, items
print(student.keys())
print(student.values())
print(student.items())

# Safe access
print(student.get("marks"))

# Updating / adding data
student.update({"marks": 96, "fav": "food"})

# Removing elements
student.pop("city")
student.popitem()   # removes last inserted item

# Copying dictionary
new_student = student.copy()
print(new_student)

# setdefault (adds if key not present)
student.setdefault("country", "India")
print(student)


# ================================
# DICTIONARY OPERATIONS
# ================================

# Adding new key
student["gender"] = "Male"

# Deleting key
del student["age"]

print(student)


# --------------------------------
# Membership (checks keys only)
# --------------------------------
print("name" in student)


# --------------------------------
# Length
# --------------------------------
print(len(student))


# --------------------------------
# Accessing values
# --------------------------------
print(student.get("city"))   # safe (returns None)


# ================================
# LOOPING THROUGH DICTIONARY
# ================================

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key–Value pairs
for key, value in student.items():
    print(key * 2, value)


# Nested dictionary 

student = {
    "name": "Sunil",
    "details": {
        "age": 20,
        "course": "Python"
    }
}

print(student["details"]["course"])
