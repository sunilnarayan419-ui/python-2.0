# Heatmap Plot using Seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

matrix = np.linspace(1, 100, 100).reshape(10, 10)

plt.figure(figsize=(8, 6))

sns.heatmap(
    matrix,
    annot=True,
    fmt=".1f",
    linewidths=0.5,
    linecolor="black",
    cmap="YlGnBu",
    cbar_kws={"shrink": 0.8, "label": "Scale"}
)

plt.title("Heatmap")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.tight_layout()
plt.show()
