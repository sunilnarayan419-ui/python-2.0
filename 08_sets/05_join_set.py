# join sets 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"} 

new_set = my_set.union(my_set1) 
print(new_set) 


# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"} 

new_set = my_set | my_set1 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  
my_set2 = {"guj" , "uk" ,"bihar" , "up" , "ap" , "telangana" , "mp"} 

new_set = my_set.union(my_set1 , my_set2) 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set | my_set1 | my_set2 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = ( "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar") 

new_set = my_set.union(my_set1) 
print(new_set) 

""" note: the | operators only allows you to join sets with set not with other type""" 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

my_set.update(my_set1) 
print(my_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

my_set.update(my_set1) 
print(my_set) 


# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set.intersection(my_set1) 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set & my_set1 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"} 

my_set.difference_update(my_set1) 
print(my_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"} 

new_set = my_set.difference(my_set1) 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set - my_set1 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

my_set.difference_update(my_set1) 

print(my_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set.symmetric_difference(my_set1) 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

new_set = my_set ^ my_set1 
print(new_set) 

# level 

my_set = { "sunil" , "sadik" , "aman" , "adersh" , "adarsh" , "manish"}  
my_set1 = { "suresh" , "sadik ji " , "aman yadav" , "adersh chouhan" , "adarsh sing " , "manish kumar"}  

my_set.symmetric_difference_update(my_set1) 
print(my_set) 