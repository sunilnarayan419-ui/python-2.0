import matplotlib.pyplot as plt 
import numpy as np 

data = np.random.normal(loc=50 , scale=10, size=1000) 

plt.hist(data , bins=20, color="pink" , edgecolor="black" , alpha=0.8) 
plt.title("Histogram of data") 
plt.xlabel("value range") 
plt.ylabel("Frequency") 
plt.show() 

# level 

data1 = np.random.normal(loc=50, scale=10, size=100)
data2 = np.random.normal(loc=60, scale=15, size=100)
data3 = np.random.normal(loc=55, scale=5, size=100)

plt.boxplot(
    x=[data1, data2, data3],
    label=["Group 1", "Group 2", "Group 3"],
    patch_artist=True,
    boxprops=dict(facecolor="lightblue", color="pink")
)

plt.title("Boxplot of group") 
plt.xlabel("groups") 
plt.ylabel("values") 
plt.show()

# level 

categories = ["Categories A" , "Categories B" , "Categories C" , "Categories D"] 
values = [15,30,45,10] 

plt.pie(values,labels=categories , autopct="%1.1f%%" , startangle=90,colors=["pink" , "green", "yellow","orange"])  
plt.title("Pie Chart of Categories") 
plt.show() 
