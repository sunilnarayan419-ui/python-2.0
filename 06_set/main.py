# set 

a = {1 ,2 ,3 ,4 ,5} 
b = {4 ,6 ,7 ,8 ,9} 

# operations on sets 

print(a.intersection(b)) 
print(a.union(b)) 
print(a.difference(b)) 
print(a.symmetric_difference(b)) 
print(a.issubset(b)) 
print(a.issuperset(b)) 
print(a.isdisjoint({2,3})) 

print({2,3,4} in a) 
print({2,6,7,8} not in a) 

print(a.add(19)) 
print(a.discard(8)) 
print(a.remove(2)) 
print(a.update({3,4}))  
 
# get the unique element of a list 

restaurants = ["McDonald's" , "Burger King" , "Kavita's Kitchen" , "Papu Malayi Wala"] 
unique_restaurants = list(restaurants)
unique_restaurants = set(restaurants) 
unique_restaurants = list(set(restaurants))
print(unique_restaurants) 

# set to sets 

d = {frozenset({1,2}) , frozenset({3,4})} 
print(d) 

# set operations using methods and builtins 

s = {1 ,2 ,3 ,4 ,5} 
n = {6 ,7 ,8 ,9 ,0} 

print(s.intersection(n)) 
print(s.union(n)) 
print(s.difference(n)) 
print(s.symmetric_difference(n)) 
print(s.issubset(n))
print(s.issuperset(n))
print(s.isdisjoint(n))
print(s.remove(4)) 

# testing membership 
print((1)in s) 
print((4) not in n) 

# length 

print(len(s)) 

# Sets vs multisets 

setA = {"a" , "v" , "m" , "f" , "o"}
setA = {"b" , "u" , "g" , "k" , "r"} 
print(set(["s" , "u" , "p"]))  

# level 
from collections import Counter 
counter_a = Counter(["a" , "b" ,"c"]) 
a = Counter({"a" : 3, "b" : 5 , "c" : 9})
print(a) 