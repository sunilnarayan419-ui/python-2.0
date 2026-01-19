# Bar Plot with FacetGrid using Seaborn for Multiple Plots
import seaborn as sns
import matplotlib.pyplot as plt

# data
df = sns.load_dataset("tips")

# FacetGrid with proper categorical x-axis
g = sns.FacetGrid(
    data=df,
    col="time",
    row="smoker",
    height=4,
    aspect=1.5
)

# Map seaborn barplot (statistical aggregation)
g.map_dataframe(
    sns.barplot,
    x="day",
    y="tip",
    estimator="mean",
    errorbar="sd",
    palette="Set2"
)

# Labels and title
g.set_axis_labels("Day", "Average Tip")
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Average Tip by Day, Time, and Smoking Status")

plt.show()
     
 

