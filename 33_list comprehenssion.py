# List comprehension = A concise way to list in Python 
# compact and easier to read then traditional loops
# [ expression for value in iterable if condition]

doubles = []

for x in range(1,10):
    doubles.append(x*2)
    


doubles = [x*2 for x in range(1, 11)]

triples = [y*3 for y in range(1 , 23)]

sqr = [ z*z for z in range(1,34)] 

# 
print(doubles)
print(triples)  
print(sqr)

fruits = ["apple","banana","orange","coconut"]
fruits = [ fruits.index for fruit in fruits]
print(fruits) 

# 

numbers = [ 1 , -2 , 3, -4 , 5, -6]
positive_num = [ num for num in numbers if num >= 0]
negative_num = [ num for num in numbers if num < 0]
even_num = [ num for num in numbers if num /2 == 0]
odd_num = [ num for num in numbers if num /2 == 1]

print(positive_num)
print(negative_num)
print(even_num)
print(odd_num)

# 
grades = [ 85,98 ,34,23,56,78,90,30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
