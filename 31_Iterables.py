# Iterables = An object/collection that can return its elements one at a time , 
#  allowing it to be iterated over in a loop 

numbers = [1,2,3,4,5,6,]
numbers = (1,2,3,4,5,6,)
# numbers = {1,2,3,4,5,6,}


for number in numbers:
    print(number)
    
for number in reversed(numbers):
    print(number)
    
# ex 1 
name = "sunil narayan"

for latter in name:
    print(latter)   
    
# ex 2 
my_dictionary = {"A":1,"B":2,"C":3}

for key in my_dictionary:
    print(my_dictionary)
for value in my_dictionary:
    print(my_dictionary)
for key, value in my_dictionary.items():
    print(f"{key} = {value}")   
    