# nested loop = A loop within another loop ( outer , inner)
# outer loop:
#      inner loop:

x = 23.2
y = 34.5
while x > 0:
    while y > 0:
        print(f"do something ")
        
for x in range(3):
    for y in range(9):
        print(f"do something")
        
while x > 0:
    for y in range (9):
        print(f"do something ")
        

for x in range (3):
    while y > 0:
        print(f"do something") 

# example 
for x in range (1 , 10):
    print(x, end=" ")
    
for x in range (3):
    for y in range (1 , 10):
     print(y, end=" ") 
     print()
     
# example
rows = int(input(f"Enter the # of rows : "))
columns = int(input(f"Enter the # of columns : "))
symbol = input(f"Enter a symbol to use :")

for x in range(rows):
    for y in range(columns):
        print(symbol , end=" ")
    print()   

# countdown timer 
import time

hours = int(input("Enter hours   : "))
minutes = int(input("Enter minutes : "))
seconds = int(input("Enter seconds : "))

# Validation
if hours < 0 or minutes >= 60 or seconds >= 60:
    print("❌ Invalid time format")
else:
    print("\n⏳ Countdown Started...\n")

    for h in range(hours, -1, -1):

        # If it's the first hour, start from entered minutes
        if h == hours:
            m_start = minutes
        else:
            m_start = 59

        for m in range(m_start, -1, -1):

            # If it's first hour & first minute, start from entered seconds
            if h == hours and m == m_start:
                s_start = seconds
            else:
                s_start = 59

            for s in range(s_start, -1, -1):
                print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")
                time.sleep(1)

    print("\n⏰ Timer Finished Successfully!")


