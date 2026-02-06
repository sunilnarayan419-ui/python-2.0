# set methods 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}   

my_set.add("rahul") 
print(my_set) 
print(my_set.clear()) 
print(my_set.copy()) 
print(my_set.difference(my_set1)) 
print(my_set.difference_update(my_set1))
print(my_set.discard("aman")) 
print(my_set.intersection(my_set1)) 
print(my_set.intersection_update(my_set1)) 
print(my_set.isdisjoint(my_set1)) 
print(my_set.issubset(my_set1))
print(my_set1.issuperset(my_set)) 
print(my_set > my_set1) 
print(my_set >= my_set1) 
print(my_set.pop()) 
print(my_set.remove("sadik")) 
print(my_set.symmetric_difference(my_set1)) 
print(my_set.symmetric_difference_update(my_set1)) 
print(my_set.union(my_set1)) 
print(my_set.update(my_set1)) 
