from scipy.integrate import quad 
from scipy.optimize import minimize 
from scipy.optimize import root 

def f(x): 
    return x**2 

result, error = quad(f, 0, 2) 
print(f"Result: {result}, Error estimate: {error}")

# level 

def objective(x): 
    return (x -3)**2 + 4 

result = minimize(objective , x0=0) 
print(f"Minimum value: {result.fun} at x = {result.x[0]}") 

# level 

def equation(x): 
    return x**3 - 4*x**2 + 6*x - 24 

solution = root(equation , x0=5) 
print(f"Root: {solution.x[0]}") 