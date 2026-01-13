# Python file detector  

import os 

file_path = "python/54_exception.py"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exist")
    
    if os.path.isfile(file_path):
        print(f"That  is a file")
elif os.path.isdir(file_path):
    print(f"That is a directory ")  
else: 
    print(f"That location doesn't exist")    