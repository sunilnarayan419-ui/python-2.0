import matplotlib.pyplot as plt
import numpy as np



x = np.arange(2023, 2027)   # stop is exclusive
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17,23,38,5]) 
y3 = np.array([13,15,20,30]) 


plt.plot(x,  y1, marker="*", 
         markersize=30 , 
         markerfacecolor="#1cd3fc",
         markeredgecolor="#1cd3fc",
         linestyle="dashed",
         linewidth=4,
         color="#1c5bfc")
plt.plot(x,  y2, marker="*", 
         markersize=30 , 
         markerfacecolor="#1cd3fc",
         markeredgecolor="#1cd3fc",
         linestyle="dashed",
         linewidth=4,
         color="#1c5bfc")        
plt.show()

# Level up 
line_style = dict(
    marker="*",
    markersize=30,
    markerfacecolor="#1cd3fc",
    markeredgecolor="#1cd3fc",
    linestyle="dashed",
    linewidth=4,
    color="#1c5bfc"
)

plt.plot(x, y1, **line_style)
plt.plot(x, y2, **line_style)
plt.plot(x, y3, **line_style)

plt.plot(x, y1, color="#1c5bfc" ,**line_style)
plt.plot(x, y2, color="#1cfc45",**line_style)
plt.plot(x, y3, color="#fc1c1c",**line_style)

plt.show()
