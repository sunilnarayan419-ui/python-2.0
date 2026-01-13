# Multiple inheritance = inherit from more than one parent class
# c(A,B)
# Multiple inheritance = inherit from a parent which inherits from another parent
# c(B) <- B(A) <-A 

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing from danger!")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting for food!")


class Rabbit(Prey):
    def eat(self):
        print(f"{self.name} is eating carrots 🥕")


class Hawk(Predator):
    def sleep(self):
        print(f"{self.name} is sleeping on a tree 🌳")


class Fish(Prey, Predator):
    def swim(self):
        print(f"{self.name} is swimming 🐟")

    def eat(self):
        print(f"{self.name} is eating plankton")


# -------------------------
# Objects
# -------------------------
rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

# -------------------------
# Testing
# -------------------------
print("\n--- Rabbit ---")
rabbit.eat()
rabbit.sleep()
rabbit.flee()

print("\n--- Hawk ---")
hawk.eat()
hawk.sleep()
hawk.hunt()

print("\n--- Fish ---")
fish.swim()
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()

print("\nMRO of Fish:")
print(Fish.mro())
