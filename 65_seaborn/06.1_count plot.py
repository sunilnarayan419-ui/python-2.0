# Count Plot with Customizations using Seaborn  
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set style 
sns.set_style("whitegrid")

var = sns.load_dataset("tips")

plt.figure(figsize=(8, 5))

sns.countplot(
    x="day",
    data=var,
    hue="sex", 
    order=["Thur", "Fri", "Sat", "Sun"],
    palette="pastel",
    saturation=0.9,
    dodge=True,
    alpha=0.8,
    edgecolor="black",
    linewidth=1
)

plt.title("Count Plot of Tips")
plt.xlabel("Day of the Week")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
