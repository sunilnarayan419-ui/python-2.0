import matplotlib.pyplot as plt
import numpy as np



x = np.arange(2023, 2027)   # stop is exclusive
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17,23,38,5]) 
y3 = np.array([13,15,20,30]) 

plt.title("Class size" , 
          fontsize=25,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")
plt.xlabel("Year",
           fontsize=20,
           family="Arial",
           fontweight="bold",
           color="#2dbefc") 
plt.ylabel("Student",
           fontsize=20,
           family="Arial",
           fontweight="bold",
           color="#2dbefc") 
plt.tick_params(axis="both",
                colors="#2dbefc") 


plt.plot(x , y1)
plt.plot(x , y2)
plt.plot(x , y3)

plt.xticks(x) 

plt.show() 