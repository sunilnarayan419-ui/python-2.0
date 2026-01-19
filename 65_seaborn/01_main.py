# Line plot 

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

var = [1, 2, 3, 4, 5, 6, 7]
var_1 = [2, 3, 4, 1, 6, 7, 8]


# DataFrame
x_1 = pd.DataFrame({
    "var": var,
    "var_1": var_1
})

# seaborn call
sns.lineplot(x="var", y="var_1", data=x_1)

plt.show()

# Level up 

y_1 = pd.read_csv(r"c:\Users\HOME\Downloads\penguins.csv").head(50) 

sns.lineplot(
    x="bill_length_mm",
    y="flipper_length_mm",
    data=y_1,
    hue="sex",
    size="sex" ,
    palette="Accent",
    markers=["o",">"],
    dashes=True,
    legend="brief",
) 

plt.grid() 
plt.title("Python") 
plt.show()
 