# python calculator
operator = input(f"Enter an operator ( - + * / ): ")
num_1 = float(input(f"Enter the 1st number : "))
num_2 = float(input(f"Enter the 2st number : "))

if operator == " + ":
    result = num_1 + num_2 
    print(result)
elif operator == " - ":
    result = num_1 - num_2
    print(result)
elif operator == " * ":
    result = num_1 * num_2
    print(result)
elif operator == " / ":
    result = num_1 / num_2
    print(result)   
    print()

# ex 1
weigth = float(input(f"Enter your weigth : "))
unit = input(f"kilogram or pound ? ( K or L): ")

if unit == "K":
    weight = weigth*2.205
    unit = "L"
elif unit == "L":
    weight = weigth /2.205
    unit = "kg"
else: 
    print(f"Your weigth is : {weigth} {unit}")
print(f"Your weigth is : {weigth} {unit}") 

# ex 3
print("Temperature Unit Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"Temperature in Fahrenheit: {f:.2f} °F")

elif choice == 2:
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"Temperature in Celsius: {c:.2f} °C")

elif choice == 3:
    c = float(input("Enter temperature in Celsius: "))
    k = c + 273.15
    print(f"Temperature in Kelvin: {k:.2f} K")

elif choice == 4:
    k = float(input("Enter temperature in Kelvin: "))
    c = k - 273.15
    print(f"Temperature in Celsius: {c:.2f} °C")

else:
    print("Invalid choice! Please select between 1 and 4.")
