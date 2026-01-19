# Violin Plot with Customizations using Seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# data 
df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex.csv")
df_sample = df.head(200)

sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

sns.violinplot(
    data=df_sample,
    x="type_1",
    y="weight_kg",
    hue="generation",
    inner="quartile",
    palette="Set3",
    density_norm="count",
    bw_adjust=0.4,
    cut=0,
    linewidth=1,
    saturation=0.8
)

plt.title("Pokemon Weight Distribution by Type and Generation")
plt.xlabel("Primary Type")
plt.ylabel("Weight (kg)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
