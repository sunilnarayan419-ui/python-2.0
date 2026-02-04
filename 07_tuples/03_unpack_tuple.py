# Unpack tuple 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish")

student1, student2, student3, student4, student5, student6 = my_tuple

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)
print(student6)

# level 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish") 
( student, *student1) = my_tuple
print(student) 
print(student1) 

# level 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish") 
(student , *uoh , student1) = my_tuple 

print(student) 
print(uoh) 
print(student1) 


   