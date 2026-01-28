# ================================
# INDENTATION EXAMPLE IN PYTHON
# ================================

"""
Indentation means leading spaces (or tabs)
at the beginning of a line.
"""


# --------------------------------
# Class definition
# --------------------------------
class Student:
    def __init__(self, name, age, college, city, country):
        self.name = name
        self.age = age
        self.college = college
        self.city = city
        self.country = country

    def greet(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"College Name: {self.college}")
        print(f"City Name: {self.city}")
        print(f"Country Name: {self.country}")


# --------------------------------
# Program execution (OUTSIDE class)
# --------------------------------
try:
    while True:
        name = input("Enter your name: ").title()
        age = int(input("Enter your age: "))
        college = input("Enter your college name: ").title()
        city = input("Enter your city name: ").title()
        country = input("Enter your country name: ").title()

        student = Student(name, age, college, city, country)
        student.greet()

        break

except ValueError:
    print("Please enter a valid age!!")
except Exception:
    print("Something went wrong!!")

    
        
        
        
        