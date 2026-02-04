# sort list 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"]
my_list.sort() 
print(my_list)  

# level 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"] 
my_list.sort(reverse=True) 
print(my_list)  

# level 

def myFunc(n): 
    return abs(n - 50) 

my_list = [ 1 ,2 ,3 ,4 ,5 ,6] 
my_list.sort(key=myFunc) 
print(my_list) 

# level 

my_list = ["sunil", "aman", "Sadik", "adarsh", "adersh", "manish"]  
my_list.sort() 
print(my_list) 

# level 

my_list = ["Sunil", "Aman", "Sadik", "Adarsh", "Adersh", "Manish"] 
my_list.sort(key=str.lower) 
print(my_list) 

# level 

my_list = ["sunil", "aman", "sadik", "adarsh", "adersh", "manish"]  
my_list.reverse() 
print(my_list) 
