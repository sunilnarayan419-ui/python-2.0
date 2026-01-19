# Strip Plot with Jitter and Hue using Seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex.csv")
df_sample = df.head(200).copy()

# Reduce hue complexity safely
df_sample["gen_group"] = df_sample["generation"].apply(
    lambda g: "Gen 1–4" if g <= 4 else "Gen 5+"
)

sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

sns.stripplot(
    data=df_sample,
    x="type_1",
    y="speed",
    hue="gen_group",
    dodge=True,
    jitter=0.25,
    palette="Pastel1", 
    alpha=0.7,
    size=5,
    edgecolor="gray",
    linewidth=0.5
)

plt.title("Pokemon Speed Distribution by Type (Early vs Later Generations)")
plt.xlabel("Primary Type")
plt.ylabel("Speed")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
