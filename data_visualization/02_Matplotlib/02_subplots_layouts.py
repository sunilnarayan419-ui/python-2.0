import matplotlib.pyplot as plt 

plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [4, 5, 6], label="line 1") 
plt.title("First subplot") 
plt.legend() 

plt.subplot(2, 1, 2)
plt.plot([1, 2, 3], [7, 8, 9], label="bar 1", color="pink") 
plt.title("Second subplot") 
plt.legend() 

plt.tight_layout() 
plt.show()


# level 

fig, axes = plt.subplots(
    3, 1,
    figsize=(8, 10),
    gridspec_kw={'height_ratios': [1, 2, 1]}
)

axes[0].plot([1, 2, 3], [4, 5, 6], color="pink")
axes[0].set_title("Top Subplot")

axes[1].bar([1, 2, 3], [4, 5, 6], color="cyan")
axes[1].set_title("Middle Subplot")

axes[2].scatter([1, 2, 3], [4, 5, 6], color="magenta")
axes[2].set_title("Bottom Subplot")

plt.tight_layout()
plt.show()
