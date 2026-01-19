# Histogram Plot 

import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 

df = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv") 

sns.displot(
    data=df,
    x="bill_length_mm",
    bins=50, 
    kde=True,
    rug=True,
    color="pink",
    log_scale=True
)

plt.show() 