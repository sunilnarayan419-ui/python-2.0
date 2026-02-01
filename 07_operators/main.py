#  Arithmetic Operations 

try: 
    num_1 = float(input(f"Enter your first number : ")) 
    num_2 = float(input(f"Enter your second number : ")) 

except ValueError:
 print(f"Please enter valid numbers !") 
 exit() 
 

print(f"Choose Operation : ")
print(f"1. Addition (+)") 
print(f"2. Subtraction (-)") 
print(f"3. Multiplication (*)")  
print(f"4. Division (/)") 
print(f"5. Floor Division (//)") 
print(f"6. Modulus (%)") 
print(f"7. Power (**)") 

try:
    choice = int(input(f"Enter your choice(1-7) : ")) 
except ValueError:
 print(f"Please enter valid numbers !") 
 exit() 


if choice == 1:
     print(f"Addition = {num_1 + num_2}") 
elif choice == 2:
     print(f"Subtraction = {num_1 - num_2}") 
elif choice == 3:
     print(f"Multiplication = {num_1 * num_2}") 
elif choice == 4:
    if num_2 != 0:
      print(f"Division = {num_1 / num_2}") 
    else: 
        print(f"Error : Division by zero !") 
elif choice == 5:
    if num_2 != 0:
      print(f"Floor Division = {num_1 // num_2}") 
    else: 
        print(f"Error : Division by zero ! ")
elif choice == 6:
    if num_2 != 0:
      print(f"Modulus = {num_1 % num_2}") 
    else: 
       print(f"Error : Division by zero !")
elif choice == 7:
     print(f"Power = {num_1 ** num_2}") 
else: 
     print(f"Invalid choice !")         
        
# comparision operations 

try: 
    num_1 = float(input("Enter your first number : ")) 
    num_2 = float(input("Enter your second number : ")) 

except ValueError:
    print("Please enter valid numbers !") 
    exit() 


print("Choose Comparison Operation : ")
print("1. Equal to (==)") 
print("2. Not Equal to (!=)") 
print("3. Greater than (>)")  
print("4. Less than (<)") 
print("5. Greater than or Equal to (>=)") 
print("6. Less than or Equal to (<=)") 

try:
    choice = int(input("Enter your choice (1-6) : ")) 
except ValueError:
    print("Please enter a valid choice !") 
    exit() 


if choice == 1:
    print(f"{num_1} == {num_2} → {num_1 == num_2}") 

elif choice == 2:
    print(f"{num_1} != {num_2} → {num_1 != num_2}") 

elif choice == 3:
    print(f"{num_1} > {num_2} → {num_1 > num_2}") 

elif choice == 4:
    print(f"{num_1} < {num_2} → {num_1 < num_2}") 

elif choice == 5:
    print(f"{num_1} >= {num_2} → {num_1 >= num_2}") 

elif choice == 6:
    print(f"{num_1} <= {num_2} → {num_1 <= num_2}") 

else:
    print("Invalid choice !")


# Logical  operators 

try: 
    num_1 = float(input("Enter your first number : ")) 
    num_2 = float(input("Enter your second number : ")) 

except ValueError:
    print("Please enter valid numbers !") 
    exit() 


# Create boolean expressions
condition_1 = num_1 > 0
condition_2 = num_2 > 0


print("Choose Logical Operation : ")
print("1. AND (num_1 > 0 and num_2 > 0)") 
print("2. OR  (num_1 > 0 or num_2 > 0)") 
print("3. NOT (not (num_1 > 0))")  

try:
    choice = int(input("Enter your choice (1-3) : ")) 
except ValueError:
    print("Please enter a valid choice !") 
    exit() 


if choice == 1:
    print(f"{condition_1} and {condition_2} → {condition_1 and condition_2}") 

elif choice == 2:
    print(f"{condition_1} or {condition_2} → {condition_1 or condition_2}") 

elif choice == 3:
    print(f"not ({condition_1}) → {not condition_1}") 

else:
    print("Invalid choice !")

# Assignment Operators 

try: 
    num_1 = float(input("Enter your first number : ")) 
    num_2 = float(input("Enter your second number : ")) 

except ValueError:
    print("Please enter valid numbers !") 
    exit() 


print("Choose Assignment Operation : ")
print("1. Assign (=)") 
print("2. Add and Assign (+=)") 
print("3. Subtract and Assign (-=)")  
print("4. Multiply and Assign (*=)") 
print("5. Divide and Assign (/=)") 
print("6. Floor Divide and Assign (//=)") 
print("7. Modulus and Assign (%=)") 
print("8. Power and Assign (**=)") 

try:
    choice = int(input("Enter your choice (1-8) : ")) 
except ValueError:
    print("Please enter a valid choice !") 
    exit() 


print(f"\nBefore Operation: num_1 = {num_1}")

if choice == 1:
    num_1 = num_2
    print(f"After (=): num_1 = {num_1}")

elif choice == 2:
    num_1 += num_2
    print(f"After (+=): num_1 = {num_1}")

elif choice == 3:
    num_1 -= num_2
    print(f"After (-=): num_1 = {num_1}")

elif choice == 4:
    num_1 *= num_2
    print(f"After (*=): num_1 = {num_1}")

elif choice == 5:
    if num_2 != 0:
        num_1 /= num_2
        print(f"After (/=): num_1 = {num_1}")
    else:
        print("Error: Division by zero!")

elif choice == 6:
    if num_2 != 0:
        num_1 //= num_2
        print(f"After (//=): num_1 = {num_1}")
    else:
        print("Error: Division by zero!")

elif choice == 7:
    if num_2 != 0:
        num_1 %= num_2
        print(f"After (%=): num_1 = {num_1}")
    else:
        print("Error: Division by zero!")

elif choice == 8:
    num_1 **= num_2
    print(f"After (**=): num_1 = {num_1}")

else:
    print("Invalid choice !")


# Bitwise operators 

try: 
    num_1 = int(input("Enter your first integer : ")) 
    num_2 = int(input("Enter your second integer : ")) 

except ValueError:
    print("Please enter valid integers !") 
    exit() 


print("Choose Bitwise Operation : ")
print("1. AND (&)") 
print("2. OR (|)") 
print("3. XOR (^)")  
print("4. NOT (~) [applies to first number]") 
print("5. Left Shift (<<)") 
print("6. Right Shift (>>)") 

try:
    choice = int(input("Enter your choice (1-6) : ")) 
except ValueError:
    print("Please enter a valid choice !") 
    exit() 


if choice == 1:
    print(f"{num_1} & {num_2} = {num_1 & num_2}")

elif choice == 2:
    print(f"{num_1} | {num_2} = {num_1 | num_2}")

elif choice == 3:
    print(f"{num_1} ^ {num_2} = {num_1 ^ num_2}")

elif choice == 4:
    print(f"~{num_1} = {~num_1}")

elif choice == 5:
    print(f"{num_1} << {num_2} = {num_1 << num_2}")

elif choice == 6:
    print(f"{num_1} >> {num_2} = {num_1 >> num_2}")

else:
    print("Invalid choice !")


# Membership operators 

try:
    elements = input(
        "Enter elements separated by spaces (e.g. 10 20 30 apple): "
    ).strip().split()

    value = input("Enter the value to check membership: ").strip()

except Exception:
    print("Invalid input!")
    exit()


print("Choose Membership Operation : ")
print("1. IN (value in collection)")
print("2. NOT IN (value not in collection)")

try:
    choice = int(input("Enter your choice (1-2) : "))
except ValueError:
    print("Please enter a valid choice !")
    exit()


print(f"\nCollection: {elements}")
print(f"Value: {value}")

if choice == 1:
    print(f"{value} in collection → {value in elements}")

elif choice == 2:
    print(f"{value} not in collection → {value not in elements}")

else:
    print("Invalid choice !")

# Identity Operators 

try:
    value_1 = input("Enter first value : ").strip()
    value_2 = input("Enter second value : ").strip()

except Exception:
    print("Invalid input!")
    exit()


# Create objects (lists used to clearly show identity behavior)
obj_1 = [value_1]
obj_2 = [value_2]

print("\nChoose Identity Operation : ")
print("1. IS (obj_1 is obj_2)")
print("2. IS NOT (obj_1 is not obj_2)")
print("3. Same Reference (obj_1 is obj_3)")

try:
    choice = int(input("Enter your choice (1-3) : "))
except ValueError:
    print("Please enter a valid choice!")
    exit()


if choice == 1:
    print(f"obj_1 is obj_2 → {obj_1 is obj_2}")

elif choice == 2:
    print(f"obj_1 is not obj_2 → {obj_1 is not obj_2}")

elif choice == 3:
    obj_3 = obj_1
    print(f"obj_1 is obj_3 → {obj_1 is obj_3}")

else:
    print("Invalid choice!")


# Conditional Operators 

try:
    num_1 = float(input("Enter your first number : "))
    num_2 = float(input("Enter your second number : "))

except ValueError:
    print("Please enter valid numbers!")
    exit()


print("Choose Conditional Operation : ")
print("1. Greater Number")
print("2. Smaller Number")
print("3. Check Even / Odd (first number)")
print("4. Check Positive / Negative (first number)")

try:
    choice = int(input("Enter your choice (1-4) : "))
except ValueError:
    print("Please enter a valid choice!")
    exit()


if choice == 1:
    result = num_1 if num_1 > num_2 else num_2
    print(f"Greater number = {result}")

elif choice == 2:
    result = num_1 if num_1 < num_2 else num_2
    print(f"Smaller number = {result}")

elif choice == 3:
    result = "Even" if int(num_1) % 2 == 0 else "Odd"
    print(f"{int(num_1)} is {result}")

elif choice == 4:
    result = "Positive" if num_1 >= 0 else "Negative"
    print(f"{num_1} is {result}")

else:
    print("Invalid choice!")


# Special Operators 

try:
    num = int(input("Enter a number : "))
except ValueError:
    print("Please enter a valid number!")
    exit()


print("Choose Special Operator : ")
print("1. Lambda (square of a number)")
print("2. Walrus Operator (:=)")
print("3. Yield (generator example)")

try:
    choice = int(input("Enter your choice (1-3) : "))
except ValueError:
    print("Please enter a valid choice!")
    exit()


if choice == 1:
    square = lambda x: x * x
    print(f"Square of {num} = {square(num)}")

elif choice == 2:
    # Walrus operator assigns and checks in one step
    if (n := num) > 10:
        print(f"{n} is greater than 10")
    else:
        print(f"{n} is less than or equal to 10")

elif choice == 3:
    def number_generator(n):
        for i in range(1, n + 1):
            yield i

    print("Generated numbers:")
    for value in number_generator(num):
        print(value, end=" ")

else:
    print("Invalid choice!")


