# if else statement 

"""if-else allows Python programs to make decisions 
by executing code based on conditions."""

name = "sunil narayan" 
s_name = input("Enter your name: ").strip

if name != s_name: 
    print(f"Please enter a valid name !!") 
else: 
    print(f"Your name match !!") 

# Ex 

while True:
    try:
        age = int(input("Enter your age: "))

        if age >= 90:
            print("You are a senior citizen!!")
        elif age >= 25:
            print("You are an adult!!")
        elif age >= 18:
            print("You can apply for a visa!!")
        else:
            print("You are a child yet!!")

        break   

    except ValueError:
        print("Please enter numeric values only.")
    except Exception:
        print("Something went wrong!!")
 