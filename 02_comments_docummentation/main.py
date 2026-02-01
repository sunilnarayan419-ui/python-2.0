# ================================
# COMMENTS AND DOCUMENTATION
# ================================

class Employee:
    """
    This class stores information about an employee.
    
    Attributes:
    1. name
    2. age
    3. salary
    4. position
    5. experience
    """

    def __init__(self, name, age, salary, position, experience):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position
        self.experience = experience

    def greet(self):
        print(f"Employee Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary}")
        print(f"Position / Job Role: {self.position}")
        print(f"Experience: {self.experience} years")


# --------------------------------
# Program execution
# --------------------------------
try:
    while True:
        name = input("Enter your name: ").title()
        age = int(input("Enter your age: "))
        salary = int(input("Enter your salary: "))
        position = input("Enter your job role / position: ").title()
        experience = int(input("Enter your work experience: "))

        employee = Employee(name, age, salary, position, experience)
        employee.greet()

        break

except ValueError:
    print("Please enter valid numeric values!!")
except Exception:
    print("Something went wrong!!")
