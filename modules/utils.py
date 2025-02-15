import numpy as np

# Function to calculate absolute and relative errors
def calculate_errors(true_value, approx_value):
    absolute_error = abs(true_value - approx_value)  # Absolute error
    relative_error = absolute_error / true_value if true_value != 0 else float('inf')  # Relative error
    return absolute_error, relative_error

# False Position Method for root finding
def false_position_method(f, a, b, tol):
    iterations = 0
    c = a
    while abs(f(c)) > tol:
        c = b - f(b) * (b - a) / (f(b) - f(a))  # Compute new approximation
        if f(a) * f(c) < 0:
            b = c  # Root is in left subinterval
        else:
            a = c  # Root is in right subinterval
        iterations += 1
    return c, iterations

# Bisection Method for root finding
def bisection_method(f, a, b, tol):
    iterations = 0
    midpoint = (a + b) / 2
    while abs(f(midpoint)) > tol:
        if f(a) * f(midpoint) < 0:
            b = midpoint  # Root is in left subinterval
        else:
            a = midpoint  # Root is in right subinterval
        midpoint = (a + b) / 2
        iterations += 1
    return midpoint, iterations

# Gaussian Elimination with partial pivoting
def gauss_elimination(A, b):
    n = len(b)
    for i in range(n):
        max_row = np.argmax(abs(A[i:n, i])) + i  # Find row with max pivot
        A[[i, max_row]] = A[[max_row, i]]  # Swap rows
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]  # Eliminate lower entries
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]  # Back substitution
    return x

# Iterative method for computing matrix inverse
def iterative_inverse(A, B, tol, max_iter):
    n = A.shape[0]
    I = np.eye(n)  # Identity matrix
    for _ in range(max_iter):
        E = np.dot(A, B) - I  # Compute error matrix
        B_new = B - np.dot(B, E)  # Update approximation
        if np.linalg.norm(E, ord='fro') < tol:
            return B_new  # Return when within tolerance
        B = B_new
    return B_new

# Lagrange Interpolation for polynomial fitting
def lagrange_interpolation(x, y, x_value):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_value - x[j]) / (x[i] - x[j])  # Compute basis polynomial
        result += term
    return result

# Romberg Integration for numerical integration
def romberg_integration(f, a, b, n):
    R = np.zeros((n, n))
    h = (b - a)
    R[0, 0] = (h / 2) * (f(a) + f(b))  # Initial trapezoidal estimate

    for i in range(1, n):
        h /= 2
        summation = sum(f(a + (k * h)) for k in range(1, 2**i, 2))  # Compute sum of midpoints
        R[i, 0] = 0.5 * R[i - 1, 0] + h * summation  # Refine estimate

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)  # Richardson extrapolation

    return R

# Function to evaluate differential equation
def dydx(x, y, equation):
    return eval(equation, {"x": x, "y": y, "np": np})  # Evaluate user-defined equation

# Runge-Kutta 2nd order method for solving ODEs
def runge_kutta(x0, y0, xn, h, equation):
    n = round((xn - x0) / h)
    y = y0
    x = x0

    for _ in range(n):
        k1 = h * dydx(x, y, equation)
        k2 = h * dydx(x + 0.5 * h, y + 0.5 * k1, equation)
        y = y + k2  # Update y value
        x = x + h  # Update x value

    return y
