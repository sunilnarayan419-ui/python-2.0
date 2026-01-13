# @property = Decorator used to define a method as a property (It can be accessed like an attribute)
# Benefit : Add additional logic when read,write,or delete attributes
# Give you getter , setter, and deleter method 

class Rectange:
    def __init__(self,width,height):
        self._width = width 
        self._height = height
    @property   
    def width(self):
        return f"{self._width:.2f} cm"
    
    @property
    def height(self):
        return f"{self._height:.2f} cm"
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else: 
            print(f"Width must be greater than zero")
    
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else: 
            print(f"Height must be greater than zero")  
            
    @width.deleter
    def width(self):
        del self._width
        print(f"Width has been deleted")
        
    @height.deleter
    def height(self):
        del self._height
        print(f"Height has been deleted")   

#ELEMENTS    
rectangle = Rectange(5,3)

# TESTING
print(rectangle._width)
print(rectangle._height)
