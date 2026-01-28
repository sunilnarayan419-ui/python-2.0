# ================================
# COMPLEX DATATYPE IN PYTHON
# ================================


# --------------------------------
# Taking complex number input
# --------------------------------
num = complex(input("Enter num : "))
print(num)


# --------------------------------
# Complex number initialization
# --------------------------------
z = 3 + 4j


# --------------------------------
# Regular complex attributes & methods
# --------------------------------
print(z.real)
print(z.imag)
print(z.conjugate())
print(abs(z))


# ================================
# COMPLEX NUMBER OPERATIONS
# ================================

a = 2 + 4j
b = 3 + 9j


# --------------------------------
# Arithmetic operations
# --------------------------------
print(a + b)
print(a - b)
print(a * b)
print(a / b)


# --------------------------------
# Type conversion to complex
# --------------------------------
print(complex(3, 2))
print(complex("4+9j"))


# --------------------------------
# Comparison
# --------------------------------
print(a == b)


# --------------------------------
# Using cmath module
# --------------------------------
import cmath

print(cmath.sqrt(-1))
print(cmath.phase(a))
print(cmath.polar(a))
