# Python writing files (.txt , .json , .csv)

txt_data = "I like pizza!"

file_path = "output.txt"

try: 
     with open(file_path, "w") as file:
      file.write("\n" + txt_data)
     print(f"txt file '{file_path} waas created") 
     
except FileExistsError:
    print("That file already exists!")  
    
# Ex 1
employee = ["Sunil","aman","sadik"] 

file_path = "sunil.txt"
try: 
    with open(file_path , "w") as file: 
        for employee in employee:
            file.write(employee + " \n ")
        print(f"txt file'{file_path} was created")
except FileExistsError:
    print("That file already exists!")  
    
# Ex 2

import json

employeE = {
    "name" : "sunil",
    "age" : 23 , 
    "job" : "cook"
}

file_path = "sunil.json"

try: 
    with open(file_path , "w") as file:
        json.dump(employeE,file, indent=3)  
        print(f"json file '{file_path}' was created ")
except FileExistsError:
    print(f"That file already exists!")     
    
# Ex 3 

import csv

employees = [["Name ", "Age","Job"],
             ["sunil","23","ML Engineer"],
             ["aman","47","Army"]]  
file_path = "sunil.csv"

try: 
    with open(file_path,"w", newline=" ") as file: 
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print(f"That file already exists!")         
    