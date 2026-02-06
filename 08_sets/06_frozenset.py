# frozenset 
# immutable , unique , unodered , unchangeable 
# elements can not be added or removed 

my_frozenset = frozenset({ "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}) 
print(my_frozenset) 
print(type(my_frozenset)) 

# methods 

my_frozenset = frozenset({ "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}) 
my_frozenset1 = frozenset({ "sunil narayan" , "mohd sadik " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}) 

print(my_frozenset.copy())  
print(my_frozenset.difference()) 
print(my_frozenset.intersection()) 
print(my_frozenset.isdisjoint("sunil"))
print(my_frozenset.issubset("sunil")) 
print(my_frozenset.issuperset("sadik")) 
print(my_frozenset.symmetric_difference(my_frozenset)) 
print(my_frozenset.union(my_frozenset1))