# Count Plot with Customizations using Seaborn for styling plot 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

df = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv")
df = df.dropna(subset=["sex"])

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="island",
    hue="sex",
    palette="Set1",
    dodge=True
)

plt.title("Penguin Count by Island and Sex")
plt.xlabel("Island")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
