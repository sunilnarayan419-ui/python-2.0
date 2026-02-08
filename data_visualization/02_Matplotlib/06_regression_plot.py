import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd

data = sns.load_dataset("penguins") 

sns.pairplot(data, hue="species", palette="dark")
plt.show() 

# level 

data = sns.load_dataset("penguins") 

numeric_data = data.select_dtypes(include='number')
correlation = numeric_data.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")

plt.show()

# level 

data = sns.load_dataset("penguins") 

sns.regplot(data=data , x="bill_length_mm" , y="bill_depth_mm" , color="pink")
plt.title("Regression plot") 
plt.show() 
