# Membership operator = used to whether a value or variable is found in a sequence 
# ( string , list , tuple , set  or dictionary)
# 1. in , 2. not in 

word = "APPLE"

letter = input("Guess a letter in the secret word : ")

if letter in word:
    print(f"There is a {letter}")
else: 
    print(f"{letter} waas not found") 
    
name = "SUNIL"

latter = input("Guess a latter in the secret word : ")

if latter not in name:
    print(f"{latter} was not found in the name")
else: 
    print(f"{latter} was found in the name")
    
    
students = {"sunil","aman","sadik"} 

student = input("Enter the name of a student : ")

if student in students:
    print(f"{student} is a student")
else: 
    print(f"{student} was not found")
    
grades = {"SUNIL":"A",
          "SADIK":"B",
          "AMAN":"C"}

student = input("Enter the name of a student : ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")    
else: 
    print(f"{student} was not found")
    
email = "Sunil@gamil.com"

if "@" in email and "." in email:
    print(f"Valid email")
else: 
    print(f"Invalid email") 