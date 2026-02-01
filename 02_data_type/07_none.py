class Person:
    @staticmethod
    def get_details(name=None, age=None, city=None):
        if name is None or age is None or city is None:
            return None   
        
        return {
            "name": name,
            "age": age,
            "city": city
        }


# Case 1: Missing data → returns None
result1 = Person.get_details()
print(result1)
print(type(result1))

# Case 2: Proper data → returns details
result2 = Person.get_details("sunil", 56, "hyderabad")
print(result2)
print(type(result2))
