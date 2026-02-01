# ================================
# FLOAT DATATYPE IN PYTHON
# ================================


# --------------------------------
# Taking float input
# --------------------------------
num = float(input("Enter a number: "))
print(num)


# --------------------------------
# Float initialization
# --------------------------------
num = 23.56


# --------------------------------
# Regular float methods
# --------------------------------
print(num.as_integer_ratio())
print(num.is_integer())
print(num.hex())
print(float.fromhex(num.hex()))


# ================================
# FLOAT OPERATIONS
# ================================

a = 23.45
b = 78.56


# --------------------------------
# Arithmetic operations
# --------------------------------
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


# --------------------------------
# Type conversion
# --------------------------------
print(float(23))
print(float("12.34"))


# --------------------------------
# Comparison operators
# --------------------------------
print(a == b)
print(a > b)
print(a < b)
print(a != b)


# --------------------------------
# Built-in functions with float
# --------------------------------
print(abs(-10.5))
print(round(12.5678, 2))
print(pow(2.5, 2))
print(min(1.2, 3.4, 0.5))
print(max(1.2, 3.4, 0.5))


# --------------------------------
# Looping using float values
# --------------------------------
for i in range(7):
    print(i * 23.45)
