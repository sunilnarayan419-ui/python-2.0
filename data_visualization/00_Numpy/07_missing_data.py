import numpy as np

data = np.array([10, 20, np.nan, 40, 50, np.nan], dtype=float)

mean_value = np.nanmean(data)
data = np.nan_to_num(data, nan=mean_value)

print("Array after replacing missing values:", data)

# level 

data = np.array([ 
    [1, 2, np.nan],
    [4, 5, 6],
    [np.nan, 8, 9]
])

cleaned_data = data[~np.isnan(data).any(axis=1)]

print(cleaned_data)


