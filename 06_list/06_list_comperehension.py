# List comprehension 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"] 
new_list = [] 

for x in my_list: 
    if "a" in x: 
        new_list.append(x) 
        
print(new_list) 

# level 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"]  
new_list = [x for x in my_list if "a" in x] 
print(new_list) 

# level 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"]  
new_list = [x for x in my_list if x!= "sunil"] 
print(new_list) 

# level 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"]  
new_list = [ x for x in my_list] 
print(new_list) 

# level 

my_list = [1,2,3,4,5]  
new_list = [ x for x in range(10)] 
print(new_list) 

# level 

my_list = [1,2,3,4,5]  
new_list = [ x for x in range(10) if x < 5]  
print(new_list) 

# level 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"] 
new_list = [x.title() for x in my_list] 
print(new_list) 

# level 

my_list = ["sunil" , "aman" , "sadik" , "adarsh" , "adersh" , "manish"] 
new_list = [ 'Hello' for x in my_list] 
print(new_list) 

# level 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"]
new_list = ["sunil" if x == "suneel" else x for x in my_list]
print(new_list)
 
