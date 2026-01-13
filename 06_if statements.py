# if some code only IF some condition is True
# Else do something else 

age = int(input(f"Enter your age : "))

if age >= 18:
    print(f"You are now signed up!")
elif age < 0:
    print(f"You haven't been born yet")
elif age >= 100:
    print(f"You are too old to sign up")
else: 
    print(f"You mujst be 18+ to sign up")

# ex 1 
response = input("Would you like food ? (Y/N):  ")

if response == "Y":
    print(f"Have some food !")
else: 
    print(f"No food for you!")    

# ex 2
name = str(input(f"Enter your name : "))

if name == " ":
    print(f" You did not type in your name !")
else:
    print(f"Hello {name}")

# ex 3 
for_sale = True

if for_sale:
    print(f"This item is for sale")
else: 
    print(f"This item is NOT for sale ")
    
for_sale = False

if for_sale:
    print(f"This item is for sale")
else: 
    print(f"This item is NOT for sale ")

# ex 4 
online = True

if online:
    print(f"The user is online")
else:
    print(f"The user is offline") 
    
online = False

if online:
    print(f"The user is online")
else:
    print(f"The user is offline")