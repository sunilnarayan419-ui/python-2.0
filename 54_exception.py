# Exception = An event that interrupts the flow of a program
# (ZeroDivisionError, TypeError, ValueError)
# 1. try , 2. except , 3. finally 

try:
    number = float(input("Enter a number: "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero.")

except ValueError:
    print("Please enter a valid number.")

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Do some cleanup here")


