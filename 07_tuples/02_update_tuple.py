# Update tuple 

# since the tuple is unchangeable or immutable means you can not change , add , remove iteams once created. 
# but we can do in df way 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish") 

y = list(my_tuple)      
y[1] = "vijay"          
x = tuple(y)            
print(x)

# level 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish")

y = list(my_tuple)
y.append("ajay")        
x = tuple(y)
print(x)

# level 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish") 
y = ("musid",)

new_tuple = y + my_tuple
print(new_tuple)

# level 

my_tuple = ("sunil", "sadik", "aman", "adersh", "adarsh", "manish") 
y = list(my_tuple) 
y.remove("sunil") 
new_tuple = tuple(y) 
print(new_tuple) 







