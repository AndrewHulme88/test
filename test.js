import numpy as np
import matplotlib.pyplot as plt
from run_kut5 import integrate

# Example 1: y' = -y, y(0) = 1
# Exact solution: y(x) = e^(-x)
def f1(x, y):
    return -y

x1, y1 = integrate(f1, 0, 1, 10, 0.01)
x1_exact = np.linspace(0, 10, 100)
y1_exact = np.exp(-x1_exact)

plt.figure(figsize=(10, 6))
plt.plot(x1, y1, label='Numerical solution', color='blue')
plt.plot(x1_exact, y1_exact, label='Exact solution', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Example 1: y' = -y")
plt.legend()
plt.show()

# Example 2: y'' = -y, y(0) = 1, y'(0) = 0
# Exact solution: y(x) = cos(x)
def f2(x, y):
    return np.array([y[1], -y[0]])

x2, y2 = integrate(f2, 0, np.array([1, 0]), 10, 0.01)
x2_exact = np.linspace(0, 10, 100)
y2_exact = np.cos(x2_exact)

plt.figure(figsize=(10, 6))
plt.plot(x2, y2[:, 0], label='Numerical solution', color='blue')
plt.plot(x2_exact, y2_exact, label='Exact solution', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Example 2: y'' = -y")
plt.legend()
plt.show()

# Example 3: y' = 2x, y(0) = 1
# Exact solution: y(x) = x^2 + 1
def f3(x, y):
    return 2 * x

x3, y3 = integrate(f3, 0, 1, 10, 0.01)
x3_exact = np.linspace(0, 10, 100)
y3_exact = x3_exact**2 + 1

plt.figure(figsize=(10, 6))
plt.plot(x3, y3, label='Numerical solution', color='blue')
plt.plot(x3_exact, y3_exact, label='Exact solution', color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Example 3: y' = 2x")
plt.legend()
plt.show()
