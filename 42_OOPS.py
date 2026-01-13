# Object = A " bundle" of related attributes (variable) and methods (functions)
# Ex. phone, cup , book 
# You need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")

    def describe(self):
        status = "for sale" if self.for_sale else "not for sale"
        print(f"{self.year} {self.color} {self.model} ({status})")


# Objects
car1 = Car("Mustang", 2025, "Red", False)
car2 = Car("Corvette", 2025, "Blue", True)
car3 = Car("Charger", 2026, "Yellow", True)

# Actions
car1.drive()
car2.drive()
car3.drive()

car1.stop()
car2.stop()
car3.stop()

car1.describe()
car2.describe()
car3.describe()

# Accessing attributes
print(car1.model, car1.year, car1.color, car1.for_sale)
print(car2.model, car2.year, car2.color, car2.for_sale)
print(car3.model, car3.year, car3.color, car3.for_sale)
