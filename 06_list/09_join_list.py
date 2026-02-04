# join list 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"] 
my_list1 = ["narayan" , "yadav", "mohd" , "chouhan" , "sing" , "ji"] 

new_list = my_list + my_list1 
print(new_list) 

# level 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"] 
my_list1 = ["narayan" , "yadav", "mohd" , "chouhan" , "sing" , "ji"] 

for x in my_list1: 
    my_list1.append(x) 
    
print(my_list1) 

# level 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"] 
my_list1 = ["narayan" , "yadav", "mohd" , "chouhan" , "sing" , "ji"]  

my_list.extend(my_list1) 
print(my_list) 



