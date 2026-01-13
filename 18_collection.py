# collection = single " variable" used to store multiple values
# list = [] ordered and changeable . duplicates OK 
# set = {} unodered and immutable , but Add/Remove OK. NO duplicates
# tuple = () oredred and unchangeable . Duplicates OK.FASTER 


# list
fruits = ["apple" , "orange" , "banana" , "coconut "]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple " in fruits)
fruits[0] = "pineapple"
fruits.append("pineapple")
fruits.remove("apple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()
fruits.index("apple")
fruits.count("banana")

print(fruits[4])
print(fruits[0:3])
print(fruits[::])
print(fruits[:-1])

for x in fruits:
    print(fruits)
    
# set 

fruits = ["apple" , "orange" , "banana" , "coconut "]

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("apple " in fruits)
fruits.insert
fruits.remove("apple")

# tuple 
fruits = ("apple" , "orange" , "banana" , "coconut ")
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pineapple" in fruits)

fruits.__add__
fruits.__reduce__
fruits.__reversed__