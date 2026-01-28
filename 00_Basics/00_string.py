# ================================
# STRING DATATYPE IN PYTHON
# ================================


# --------------------------------
# Rules to write variable names
# --------------------------------
# Must start with a letter (a–z / A–Z) or underscore (_)
# Can contain letters, numbers, and underscores only
# Cannot contain spaces
# Cannot be a Python keyword
# Variable names are case-sensitive
# Use meaningful names (best practice)
# Use snake_case (Python style)


# --------------------------------
# Taking user input (string)
# --------------------------------
student_name = str(input("Enter your name : "))


# --------------------------------
# String initialization
# --------------------------------
name = "sunil narayan"


# --------------------------------
# Basic string output
# --------------------------------
print(f"your name is {student_name}")


# --------------------------------
# Common string methods (case)
# --------------------------------
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.format())
print(name.title())
print(name.swapcase())


# --------------------------------
# Whitespace removing methods
# --------------------------------
print(name.strip())
print(name.lstrip())
print(name.rstrip())


# --------------------------------
# Searching & counting methods
# --------------------------------
print(name.find("u"))
print(name.index("sunil"))
print(name.count("n"))


# --------------------------------
# Replace method
# --------------------------------
print(name.replace("sunil", "aman"))


# --------------------------------
# String checking methods (Boolean)
# --------------------------------
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())


# --------------------------------
# Startswith / Endswith
# --------------------------------
print(name.startswith("s"))
print(name.endswith("n"))


# --------------------------------
# Split & Join
# --------------------------------
print(name.split())
print(" , ".join(["sunil", "narayan"]))


# --------------------------------
# Length of string
# --------------------------------
print(len(name))


# ================================
# STRING OPERATIONS
# ================================

a = "sunil"
b = "narayan"

# Concatenation
c = a + " " + b
print(a + " " + b)

# Repetition
print(c * 3)


# --------------------------------
# Indexing
# --------------------------------
print(c[0])
print(c[-2])


# --------------------------------
# Slicing
# --------------------------------
print(c[0:3])
print(c[2:])
print(c[:3])


# --------------------------------
# Membership operators
# --------------------------------
print("sunil" in c)
print("python" in c)


# --------------------------------
# String comparison
# --------------------------------
print("c" == "a")
print("a" > "b")


# --------------------------------
# Looping through a string
# --------------------------------
for sun in "a":
    print(sun)


# --------------------------------
# Type conversion (int → string)
# --------------------------------
age = 20
g = "Age is " + str(age)
print(g)


# --------------------------------
# Escape characters
# --------------------------------
print("hello\nworld")
