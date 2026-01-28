# ================================
# INTEGER DATATYPE IN PYTHON
# ================================


# --------------------------------
# Taking integer input
# --------------------------------
num = int(input("Enter some num: "))
print(num)


# --------------------------------
# Integer initialization
# --------------------------------
number = 2345


# --------------------------------
# Regular integer methods
# --------------------------------
print(number.bit_length())
print(number.to_bytes(2, byteorder="big"))
print(int.from_bytes(b'\x00\n', byteorder="big"))
print(number.as_integer_ratio())


# ================================
# INTEGER OPERATIONS
# ================================

a = 23
b = 45


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
print(int("123"))
print(int(12.3))


# --------------------------------
# Comparison operators
# --------------------------------
print(a == b)
print(a > b)
print(a < b)
print(a != b)


# --------------------------------
# Built-in functions with integers
# --------------------------------
print(abs(-3))
print(pow(2, 5))
print(round(34.5678))
print(min(1, 3, 6, 8, 0))
print(max(1, 3, 6, 8, 0))


# --------------------------------
# Looping using integers
# --------------------------------
for i in range(5):
    print(i + 1)
