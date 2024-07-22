import numpy as np

def euler_method(func, y0, x0, xn, n):
    """
    This function uses Euler's method to approximate a solution to an ODE.

    Parameters:
    func: The ODE as a function of x and y.
    y0: The initial value of y.
    x0: The initial value of x.
    xn: The final value of x.
    n: The number of steps to take.

    Returns:
    y: The approximated solution to the ODE.
    """
    h = (xn - x0) / n  # Step size
    y = y0

    for i in range(n):
        y = y + h * func(x0 + i * h, y)

    return y

def dy_dx(x, y):
    return -2 * y

# Initial conditions
y0 = 5
x0 = 0
xn = 2
n = 20

# Using Euler's method to approximate the solution
solution = euler_method(dy_dx, y0, x0, xn, n)
print(f"The approximate value of y at x={xn} is {solution}")
