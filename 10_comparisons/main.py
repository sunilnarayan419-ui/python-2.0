
"""Comparison examples

Includes:
- chained comparisons
- `is` vs `==`
- greater than / less than
- not equal (`!=`)
- equal (`==`)
- comparing objects using a class and custom `__eq__`
"""

print("--- Chained comparisons ---")
x = 3
print("1 < x < 5 ->", 1 < x < 5)  # True when both 1 < x and x < 5
print("0 <= x <= 3 ->", 0 <= x <= 3)

print("\n--- 'is' vs '==' ---")
a = 256
b = 256
print("a == b ->", a == b)    # value equality
print("a is b ->", a is b)    # identity (may be True for small ints due to interning)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 == list2 ->", list1 == list2)  # True, same contents
print("list1 is list2 ->", list1 is list2)  # False, different objects
print("list1 is list3 ->", list1 is list3)  # True, same object reference

none_var = None
print("none_var is None ->", none_var is None)  # preferred way to check for None
print("none_var == None ->", none_var == None)  # works but `is` is preferred

print("\n--- Greater than / Less than ---")
a = 10
b = 7
print("a > b ->", a > b)
print("a < b ->", a < b)
print("a >= 10 ->", a >= 10)
print("b <= 7 ->", b <= 7)

print("\n--- Not equal / Equal ---")
val1 = 5
val2 = 5
val3 = 6
print("val1 == val2 ->", val1 == val2)
print("val1 != val3 ->", val1 != val3)

print("\n--- Comparing objects using a class ---")
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f"Person({self.name!r}, {self.age})"

# default `==` compares identity unless __eq__ is defined
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = p1
print("p1 == p2 ->", p1 == p2)  # False by default
print("p1 is p2 ->", p1 is p2)  # False
print("p1 is p3 ->", p1 is p3)  # True

print("\nNow add __eq__ to compare by attributes")

class PersonEq:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __eq__(self, other):
		if not isinstance(other, PersonEq):
			return NotImplemented
		return (self.name, self.age) == (other.name, other.age)

	def __repr__(self):
		return f"PersonEq({self.name!r}, {self.age})"

pe1 = PersonEq("Bob", 25)
pe2 = PersonEq("Bob", 25)
pe3 = pe1
print("pe1 == pe2 ->", pe1 == pe2)  # True because __eq__ compares attributes
print("pe1 is pe2 ->", pe1 is pe2)  # Still False (different objects)
print("pe1 is pe3 ->", pe1 is pe3)  # True

