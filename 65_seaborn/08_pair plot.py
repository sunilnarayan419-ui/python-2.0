# Pair Plot with Seaborn for Pokemon Dataset 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex.csv")
df_sample = df.head(100)

# Reduce categories for hue
df_sample["type_group"] = df_sample["type_1"].where(
    df_sample["type_1"].isin(["Fire", "Water", "Grass"]),
    "Other"
)

sns.set_style("whitegrid")

sns.pairplot(
    df_sample[
        ["hp", "attack", "defense", "speed", "weight_kg", "type_group"]
    ],
    hue="type_group",
    palette="Set1",
    diag_kind="kde",
    plot_kws={"alpha": 0.6}
)

plt.suptitle("Pokemon Pair Plot (selected types)", y=1.02) 
plt.show()
