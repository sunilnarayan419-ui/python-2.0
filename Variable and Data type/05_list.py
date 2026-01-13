# List 
# Used to store multiple variables.
# ordered and changeable. Duplicates ok 

num = [ 1 ,2 ,3 ,4 ,5 ,6 ] 

# Some operations 

print(len(num)) 
print(max(num)) 
print(min(num)) 
print(sum(num)) 

# slicing methods

print(num[4])
print(num[0:3])
print(num[::])
print(num[:-1]) 

# Some regular methods 
# 1. append()
# Adds one element at the end.

num.append(7) 
print(num) 

# 2. extend()
# Adds multiple elements from another iterable.

num.extend([7,8 ,9 ,0]) 
print(num)  

# 3. insert()
# Inserts element at a specific index.

num.insert(1,100)
print(num) 

# 4. remove()
# Removes first occurrence of a value.

num.remove(6)  
print(num)  

# 5. pop()
# Removes & returns element by index (default: last).

num.pop(2) 
print(num) 


# 6. index()
# Returns index of first occurrence. 

print(num.index(3))

# 7. count()
# Counts how many times an element appears. 

print(num.count(1))

# 8. sort()
# Sorts list in place. 
 
num.sort(reverse=True) 
print(num)  

# 9. reverse()
# Reverses the list in place.

num.reverse() 
print(num) 

# 10. copy()
# Creates a shallow copy. 

new_num = num.copy()
print(new_num)  

# 11. clear()
# Removes all elements.

num.clear() 
print(num)