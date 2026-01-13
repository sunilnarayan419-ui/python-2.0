
# Compound Interest Calculator

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("\n--- Result ---")
print(f"Principal Amount : ${principal}")
print(f"Rate of Interest : {rate}%")
print(f"Time Period      : {time} years")
print(f"Total Amount     : ${amount:.2f}")
print(f"Compound Interest: ${compound_interest:.2f}")

# ex 1

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

while principal <= 0:
    principal = float(input(f"Enter the principal amount : "))
    if principal <= 0 :
        print(f"Enter can't be less than or equal to zero ")

while rate <= 0:
    rate = float(input(f"Enter the intrest rate : "))
    if rate <= 0:
        print(f"Intrest rate can't be less than or equal to zero ")
        
        
while time <= 0:
    time  = float(input(f"Enter the time in years : "))
    if time  <= 0:
        print(f"Time  can't be less than or equal to zero ") 
        
        
total = principal *pow((1 + rate/100), time)
print(f"Balance after {time} year/s :   ${total:.2f}")
        
print(principal)
print(rate) 
print(time)        
