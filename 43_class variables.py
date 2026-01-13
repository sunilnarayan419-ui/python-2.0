# class variables = Shared among all instance of a class
# Defined outside the constructor
# Allow you to share data among all objects created from that class

class student :
    
    class_year = 2025
    num_students = 0 
    
    def __init__(self,name , age) :
        self.name = name 
        self.age = age
        student.num_students += 1
        
student1 = student("sunil narayan",23)
student2 = student("aman yadav",34) 

print(student1.name)
print(student2.name)   
print(student1.class_year)
print(student2.class_year)   

print(student.num_students) 
print(f"My graduting class of {student.class_year} has {student.num_students} students")
print(student1.name)
print(student2.name)  
