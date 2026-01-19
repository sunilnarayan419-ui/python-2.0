# Box Plot with Customizations using Seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

df = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv")
df = df.dropna(subset=["sex", "flipper_length_mm"])

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="species",
    y="flipper_length_mm",
    hue="sex",
    palette="Set2",
    width=0.6,
    fliersize=4,
    dodge=True
)

plt.title("Penguin Flipper Length by Species and Sex")
plt.xlabel("Species")
plt.ylabel("Flipper Length (mm)")
plt.tight_layout()
plt.show()
