# while loop = execute some WHILE some condition remains true

name = input("Enter your name : ")

if name == " ":
    print("You did not enter your name yet ")
else: 
    print(f"Hello {name}")



while name == " ":
    print("You did not enter your name ")
name = input(f"Enter your name : ")
    
print(f"Hello {name}")

# ex 1 
age = int(input(f"Enter your age : "))

while age < 0:
    print("Age can't be negative")
    age = int(input(f"Enter your age : "))
print(f"You are {age} years old.") 


 # ex 2 
food = input(f"Enter a food you like ( q to quit ): ")

while not food == "q":
    print(f"You like {food}")
    food = input(f"Enter another food you like (q to quit ): ")
print("bye bro ")

# ex 3 
while True:
    try:
        num = int(input("Enter a # between 1 - 10: "))
        if 1 <= num <= 10:
            break
        else:
            print(f"{num} is not valid")
    except ValueError:
        print("Please enter a number only")

print(f"Your number is {num}")
