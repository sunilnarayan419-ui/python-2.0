# Static method = A method that belong to a class rather than any object from that class (instance ) 
# Usually used for general utility functions 
# Static methods = Best for utility function that do not need access to class data  

class EmplOyee : 
    def __init__(self , name , position ):
        self.name = name 
        self.position = position 
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position( position):
        valid_positions = [ "Manager","Cashier","Cook","Janitor"]
        return position in valid_positions  
  
employee1 = EmplOyee("sunil","Manager") 
employee2 = EmplOyee("aman", "Cashier")
employee3 = EmplOyee("sadik","Cook")    
  
  
  
    
print(EmplOyee.is_valid_position("Cook")) 
print(employee1.get_info())   
print(employee2.get_info())   
print(employee3.get_info())  

#  SAME PROGRAM BY AI 

class Employee:
    valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
    
    def __init__(self, name, position):
        if not Employee.is_valid_position(position):
            raise ValueError(f"Invalid position: {position}")
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        return position in Employee.valid_positions
 