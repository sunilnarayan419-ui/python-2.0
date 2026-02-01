class Student:
    def __init__(self, name, age, college, city):
        self.name = name
        self.age = age
        self.college = college
        self.city = city

    def greet(self):
        print(f"Hello, my name is {self.name}")
        print(f"I am {self.age} years old.")
        print(f"My college's name is {self.college}.")
        print(f"I am from {self.city}.")


try:
    while True:
        name = input("Enter your name: ").title()
        age = int(input("Enter your age:  ")) 
        college = input("Enter your college name: ").title()
        city = input("Enter your city name: ").title()

        # creating object
        student = Student(name, age, college, city)

        # calling method
        student.greet()

        break

except ValueError:
    print("Age must be a number!")
except Exception:
    print("Something went wrong!!")
