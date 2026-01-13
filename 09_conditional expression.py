# conditional expession = A one-line shoutcut for the if-else statement (ternary operator)
# print or assign one of two value based on a condition
# X if condition else Y 


# num = 34

# print("Positive"if num> 0 else "Negative")
# result = "EVEN" if num % 2 == 0  else "ODD"
# max_num = a if a > b else b 
# min_num = a  if a < b else a 


# print(result) 

# for age 
age = int(input("Enter your age: "))

if age < 18:
    print("You are a Child.")
elif age < 60:
    print("You are an Adult.")
else:
    print("You are Old.")


# for temperature
temperature = float(input("Enter the temperature in °C: "))

if temperature < 20:
    print("The weather is Cold.")
elif temperature < 30:
    print("The weather is Warm.")
else:
    print("The weather is Hot.")
