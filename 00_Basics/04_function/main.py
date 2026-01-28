# What is a Function in Python?
# A function is a block of reusable code that:
# Performs a specific task
# Runs only when it is called
# Helps avoid code repetition
# Makes programs clean & organized

def student_info(name, age, college):
    print("Name:", name)
    print("Age:", age)
    print("College:", college)


try:
    while True:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        college = input("Enter your college name: ")

        student_info(name, age, college)

        break   

except ValueError:
    print("Age must be a number!")
except Exception:
    print("Something went wrong!!")
