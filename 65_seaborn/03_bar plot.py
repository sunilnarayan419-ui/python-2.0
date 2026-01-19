# Bar plot with various customizations using seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 

df = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv")  

sns.barplot(x=df.island,
            y=df.bill_length_mm,
            hue=df.sex,
            order=["Biscoe", "Dream", "Torgersen"],
            ci=100,
            estimator=sum,
            capsize=0.2,
            errcolor="0.3",
            n_boot=200,
            orient="v",
            color="cyan",
            saturation=1,
            errwidth=2,
            alpha=0.7  
            )    

plt.title("Penguin Bill") 
sns.set_style("whitegrid")           

plt.show() 