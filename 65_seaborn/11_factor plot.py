# Factor Plot (Catplot) with Customizations using Seaborn 
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

# Set style
sns.set_style("whitegrid")

# Load and clean data
df = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv")
df = df.dropna(subset=["sex"])

# Create figure-level plot
g = sns.catplot(
    data=df,
    x="island",
    hue="sex",
    kind="count",
    palette="Set1",
    height=6,
    aspect=1.5
)

# Set labels and title properly
g.set_axis_labels("Island", "Count")
g.fig.suptitle("Penguin Count by Island and Sex", y=1.02)
plt.show()