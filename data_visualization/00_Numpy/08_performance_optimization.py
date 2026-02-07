import numpy as np

data = np.random.randint(0, 100, size=10)  

result_loop = [x**2 for x in data]
result_vectorized = data**2

print("Loop result:", result_loop)
print("Vectorized result:", result_vectorized)
print("Vectorized operation complete.")

# level 

data  = np.arange(10) 

view = data[2:7] 

view[:] = 99 

print(data) 