# input() = A function that prompts the user to enter data 
#  Returns the entered data as a string.

# indentity
# name = str(input(f"Enter your name sir :"))
# age = int(input(f" Sir please enter your age : "))
# city = str(input(f"Your city sir : "))
# age = age + 2
# print( f" hello {name}")
# print(f"HAPPY GAY DAY SIR ")
# print(f" You are {age} year old.")
# print(f" You belongs to  {city}")

# ex 1
# Rectangle area calc
# l = float(input(f"Enter the length : "))
# w = float(input(f"Enter width : "))

# area = l*w

# print(f" The area is : {area} cm^2")

# ex 2

print(f"-----YOUR ORDER-----")

item = str(input(f"What would you like to buy : "))
price = float(input(f"What is the price : "))
quantity = int(input(f"How many items would you like : "))
total = price*quantity

print(f"You have bought {quantity} {item}/s")
print( f"Your total is ${total}")

print(f"----THANK YOU SIR-----")