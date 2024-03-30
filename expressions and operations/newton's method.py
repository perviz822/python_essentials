import numpy as np
# Define the function
def f(x, y):
    return x**2 + x*y + 1.5*y**2

# Define the gradient of the function
def grad_f(x, y):
    df_dx = 2*x + y  # Partial derivative with respect to x
    df_dy = x + 3*y  # Partial derivative with respect to y
    return np.array([df_dx, df_dy])

# Define the Hessian matrix of the function
def hessian_f(x, y):
    d2f_dx2 = 2  # Second partial derivative with respect to x
    d2f_dxdy = 1 # Second mixed partial derivative
    d2f_dy2 = 3  # Second partial derivative with respect to y
    return np.array([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])

# Newton's method for optimization
def newtons_method(f, grad_f, hessian_f, x0, max_iter=4):
    x = x0
    for _ in range(max_iter):
        H_inv = np.linalg.inv(hessian_f(*x))
        grad = grad_f(*x)
        x = x - H_inv @ grad
    return x

# Initial point
x0 = np.array([1, 2])

# Perform 4 iterations of Newton's method
minimum = newtons_method(f, grad_f, hessian_f, x0)

print(minimum)
