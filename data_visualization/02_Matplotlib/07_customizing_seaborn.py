import seaborn as sns 
import matplotlib.pyplot as plt 

data = sns.load_dataset("penguins") 
sns.set_style("whitegrid")

sns.scatterplot(
    data=data,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    palette="dark"
)

plt.title("Penguins") 
plt.show()


# level 

data = sns.load_dataset("penguins")  
sns.set_palette("pastel") 

sns.boxenplot(data=data, x="species",y="flipper_length_mm")
plt.title("Flipper length by species") 
plt.show() 

# level 

data = sns.load_dataset("penguins") 
plt.figure(figsize=(8,6)) 

sns.violinplot(data=data,x="species",y="body_mass_g",palette="coolwarm") 
plt.title("Violin Plot") 
plt.show() 