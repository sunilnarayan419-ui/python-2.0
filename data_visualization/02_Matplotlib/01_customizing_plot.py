import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5] 
y = [10, 20, 25, 30, 40] 

plt.plot(x, y, label="Growth") 
plt.title("Growth over time") 
plt.xlabel("time (months)") 
plt.ylabel("value (units)") 
plt.legend(loc="upper left") 
plt.grid(color="pink",linestyle="--",linewidth=0.5) 
plt.show()




