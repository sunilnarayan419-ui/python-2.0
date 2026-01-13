# Python reading files(.txt,.json , .csv)   


file_path = "sunil.txt"

try:
 with open(file_path, "r") as file:
    content = file.read()
    print(content) 
except FileExistsError:
    print(f"That file was not found")   
except PermissionError:
    print(f"You do not have permission to read that file")
    
# Ex 1

import json

file_path = "sunil.json"

try:
 with open(file_path, "r") as file:
    content = json.load(file)   
    print(content["value"]) 
except FileExistsError:
    print(f"That file was not found")   
except PermissionError:
    print(f"You do not have permission to read that file")
    
# Ex 2

import csv

file_path = "sunil.csv"

try:
 with open(file_path, "r") as file:
    content = csv.reader(file) 
    for line in content:  
     print(line[1])  
except FileExistsError:
    print(f"That file was not found")   
except PermissionError:
    print(f"You do not have permission to read that file")