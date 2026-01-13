# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reuseability and extensibility 
# class child(parent) / sub(super classes) 

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF!")


class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")    


# Objects
dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# Testing
print(mouse.name)
print(mouse.is_alive)

mouse.eat()
mouse.sleep()
