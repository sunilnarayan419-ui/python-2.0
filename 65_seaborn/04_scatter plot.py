# Scatter Plot with Seaborn 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# data
df = pd.read_csv(r"c:\Users\HOME\Downloads\pokedex.csv")
df_sample = df.head(100) 

sns.scatterplot(
    data=df_sample,
    x="height_m",
    y="weight_kg",
    hue="type_1",
    style="generation",
    size="hp",
    sizes=(20, 200),
    palette="Set2",
    alpha=0.7,
    linewidth=0.5
)

plt.title("Pokemon Height vs Weight")
plt.xlabel("Height (m)")
plt.ylabel("Weight (kg)")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()
plt.show()
