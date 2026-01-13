# Class methods = Allow operations related to the class itself
# Take (Cls) as the first parameter , which represents the class itself. 
# Instance method = Best for operation on instances of the class (objects)
# Static methods  = Best for utility function that do not need access to class data
# Class method = Best for class-level data or require access to the class itself.

class StUdent:
     
    count = 0
    total_gpa = 0
    def __init__(self , name , gpa):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1 
        Student.total_gpa += 1
    
    # INSTANCE METHOD    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of student : {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else: 
            return f"Average gpa : {cls.total_gpa/cls.count:.2f}"   
 
 # ELEMENTS   
Student1 = StUdent("sunil",5.6)
Student2 = StUdent("aman", 3.4)
Student3 = StUdent("sadik" , 6.7)

# TESTING   
print(StUdent.get_count()) 
print(StUdent.get_average_gpa()) 

# SAME BY AI 
class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return "Average GPA: 0"
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


# ELEMENTS
Student1 = Student("Sunil", 5.6)
Student2 = Student("Aman", 3.4)
Student3 = Student("Sadik", 6.7)

# TESTING
print(Student.get_count())
print(Student.get_average_gpa())
     