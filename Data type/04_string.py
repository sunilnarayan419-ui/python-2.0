# string type 

name = str(input(f"Enter your name : ")) 
email = str(input(f"Enter your email :"))

print(f"Your name is : {name}") 
print(f"Your email is : {email}") 

# Some Regular methods 
# 1. Case Conversion Methods (VERY common)
# A. upper()  To convert in uppercase

name = input("Enter your name : ").upper()
fav_food = input("Enter your food's name : ").upper()

print(f"Your name is : {name}")
print(f"Your fav food is : {fav_food}")

# B. lower()  To convert in lowercase

name = input("Enter your name : ").lower() 
fav_food = input("Enter your food's name : ").lower() 

print(f"Your name is : {name}")
print(f"Your fav food is : {fav_food}")

# C. title() To capitalizes first letter of each word

name = input("Enter your name : ").title()
fav_food = input("Enter your food's name : ").title() 

print(f"Your name is : {name}")
print(f"Your fav food is : {fav_food}") 

# D. capitalize() Capitalizes first character

name = input("Enter your name : ").capitalize() 
fav_food = input("Enter your food's name : ").capitalize() 

print(f"Your name is : {name}")
print(f"Your fav food is : {fav_food}")

# E. swapcase() Swaps upper ↔ lower

name = input("Enter your name : ").swapcase() 
fav_food = input("Enter your food's name : ").swapcase() 

print(f"Your name is : {name}")
print(f"Your fav food is : {fav_food}")

# 2. Whitespace & Cleanup Methods
# A. strip() Remove both sides

student_name = str(input(f"Enter your name : ")).strip()
college_name = str(input(f"Enter your college's name : ")).strip() 

print(f"Your name is : {student_name}") 
print(f"Your college name is : {college_name}") 

# B. lstrip() Remove left side 

student_name = str(input(f"Enter your name : ")).lstrip() 
college_name = str(input(f"Enter your college's name : ")).lstrip() 

print(f"Your name is : {student_name}") 
print(f"Your college name is : {college_name}") 

# C. rstrip() Remove right side
student_name = str(input(f"Enter your name : ")).rstrip() 
college_name = str(input(f"Enter your college's name : ")).rstrip() 

print(f"Your name is : {student_name}") 
print(f"Your college name is : {college_name}") 

# 3. Search & Check Methods

name = 'sunil narayan' 

print(name.find("s")) # Index or -1
print(name.index('n'))  # Index or error
print(name.startswith("sunil")) # True/False
print(name.endswith("n")) # True/False
print(name.count("s")) # Occurrence count  

# 4. Validation/Checking Methods 

print("sunilnarayan".isalpha())  # Only letters 
print("123".isdigit()) # only digits
print("Sunilnarayan419".isalnum()) # Letters + digits 
print("Sunil Narayan".isspace()) # Only space 
print("Sunilnarayan".islower()) # All lowercase 
print("Sunilnarayan".isupper()) # All uppercase 
print("Sunil Narayan".istitle()) # Title case 

# 5. Replace and Modify 

text = "I am a student" 

print(text.replace("student","professional"))  # Replace text 

# translate() ; Advance replace

table = str.maketrans({'s': 'S', 't': 'T'})
result = text.translate(table) 
print(result) 

# 6. Split & Join

fruit_list = "mango,banana,orange,apple"

fruit = fruit_list.split(",")
fruit_right = fruit_list.rsplit(",", 1)

print(fruit)
print(fruit_right)

fruit_list = ("mango", "banana", "orange", "apple")

fruit = ", ".join(fruit_list)
print(fruit)


# 7. Formatting Methods

name = "Sunil Narayan"  
age = 20
random_num = 23455.5667654567

print(f"Your name is : {name}") 
print(f"Your name is :{name} and your {age}'s old") 
print(f"Your random num is : {random_num:.3f}")  

# 8. Alignment & Padding 

text = "Sunil Narayan"

# # center()
print(text.center(12))    # center align (spaces added on both sides)
print(text.center(12, '*'))  # center align with custom character

# # ljust()
print(text.ljust(12))    # left align
print(text.ljust(12, '-'))  # left align with custom character

# # rjust()
print(text.rjust(12))     # right align
print(text.rjust(12, '.'))  # right align with custom character

# # zfill()
num = "42"
print(num.zfill(6))  # pad with zeros

# 9. Encoding/Decoding 

text = "Sunil Narayan"

# convert string to bytes (default is UTF-8)
encoded_text = text.encode()

print(text)
print(encoded_text)
print(type(encoded_text))




