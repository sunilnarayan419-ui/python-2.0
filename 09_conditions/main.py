"""Examples of Python conditional statements

This file demonstrates:
- conditional expression (ternary)
- if, if-else, if-elif-else
- nested conditions
- logical operators (and/or)
- membership testing (in)
"""

# conditional expression
n = 10
num = "greater than 2" if n > 2 else "smaller than or equal to 2"
print("Conditional expression result:", num)


# Example 1: Simple if statement
age = 20
if age >= 18:
    print("You are an adult")


# Example 2: if-else statement
temperature = 15
if temperature > 20:
    print("It's warm")
else:
    print("It's cold")


# Example 3: if-elif-else statement
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")


# Example 4: Nested conditions
user_age = 25
has_license = True
if user_age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")


# Example 5: Conditional with logical operators
marks = 85
attendance = 90
if marks >= 80 and attendance >= 80:
    print("You pass with distinction")
elif marks >= 50 or attendance >= 50:
    print("You pass")
else:
    print("You fail")


# Example 6: Using 'in' operator
fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list")


# Boolean-logic examples
# Example 7: Basic boolean operators
is_admin = False
is_owner = True
if is_admin or is_owner:
    print("Access granted")
else:
    print("Access denied")


# Example 8: Combining with comparisons
age = 30
income = 40000
if age > 25 and income > 30000:
    print("Eligible for premium account")


# Example 9: Using 'not' and truthiness
items = []
if not items:
    print("No items found")


# Example 10: Short-circuit evaluation
def expensive_check():
    print("Running expensive check...")
    return True

# 'and' will not run expensive_check if first operand is False
flag = False
if flag and expensive_check():
    print("Both true")
else:
    print("Short-circuited or false")

# 'or' will not run expensive_check if first operand is True
flag2 = True
if flag2 or expensive_check():
    print("At least one true (short-circuit)")


# Example 11: Complex boolean expression
score = 82
attendance = 76
if (score >= 80 and attendance >= 75) or is_owner:
    print("Qualified")
