import numpy as np
from scipy.stats import describe
from scipy.stats import ttest_1samp

data = np.array([12, 15, 14, 10, 8, 12, 14, 16])

summary = describe(data)

print("Descriptive Statistics:")
print("Count:", summary.nobs)
print("Mean:", summary.mean)
print("Variance:", summary.variance)
print("Min/Max:", summary.minmax)

# level 

data = np.array([12, 15, 14, 10, 8, 12, 14, 16])

t_stat , p_value = ttest_1samp(data, 10) 

print("t-statistic:" , t_stat) 
print("p-value:", p_value) 