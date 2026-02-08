import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5] 
y = [2, 3, 4, 5, 7]   

plt.plot(x, y, label="line plot", color="blue", marker="o") 
plt.title("line plot") 
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.legend() 
plt.show()

# level 

categories = ["x" , "y" , "z" , "w"] 
values = [4,7,1,8] 

plt.bar(categories , values , color="green") 
plt.title("bar plot") 
plt.xlabel("categories") 
plt.ylabel("values") 
plt.show() 

# level 

x = [5,7,8,7,2,17,2,9]
y = [99,86,87,100,86,103,87 , 89] 
plt.scatter(x,y,color="pink") 
plt.title("Scatter plot") 
plt.xlabel("x-axis") 
plt.ylabel("y-axis") 
plt.show() 