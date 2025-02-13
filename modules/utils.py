import numpy as np

def calculate_errors(true_value, approx_value):
    absolute_error = abs(true_value - approx_value)  
    relative_error = absolute_error / true_value if true_value != 0 else float('inf') 
    return absolute_error, relative_error

def false_position_method(f, a, b, tol):
        iterations = 0
        c = a
        while abs(f(c)) > tol:
            c = b - f(b) * (b - a) / (f(b) - f(a))  
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            iterations += 1
        return c, iterations

def bisection_method(f, a, b, tol):
        iterations = 0
        midpoint = (a + b) / 2
        while abs(f(midpoint)) > tol:
            if f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            midpoint = (a + b) / 2
            iterations += 1
        return midpoint, iterations

def gauss_elimination(A, b):
        n = len(b)
        for i in range(n):
            max_row = np.argmax(abs(A[i:n, i])) + i
            A[[i, max_row]] = A[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]

            for j in range(i + 1, n):
                factor = A[j, i] / A[i, i]
                A[j, i:] -= factor * A[i, i:]
                b[j] -= factor * b[i]

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
        return x

def iterative_inverse(A, B, tol, max_iter):
        n = A.shape[0]
        I = np.eye(n) 
        for _ in range(max_iter):
            E = np.dot(A, B) - I  
            B_new = B - np.dot(B, E) 
            if np.linalg.norm(E, ord='fro') < tol:
                return B_new
            B = B_new
        return B_new

def lagrange_interpolation(x, y, x_value):
        n = len(x)
        result = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if j != i:
                    term *= (x_value - x[j]) / (x[i] - x[j])
            result += term
        return result

def romberg_integration(f, a, b, n):
    R = np.zeros((n, n))
    h = (b - a)
    R[0, 0] = (h / 2) * (f(a) + f(b)) 

    for i in range(1, n):
        h /= 2
        summation = sum(f(a + (k * h)) for k in range(1, 2**i, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * summation

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R

# task 8
# Runge-Kutta 4th Order Method (RK4) Implementation
def dydx(x, y):
    # Define the differential equation: y' = -2x - y
    return -2 * x - y

def runge_kutta(x0, y0, xn, h):
    # Count number of iterations
    n = round((xn - x0) / h)
    
    # Initial value of y
    y = y0
    x = x0

    # Iteration using RK2 method
    for i in range(1, n + 1):
        k1 = h * dydx(x, y)
        k2 = h * dydx(x + 0.5 * h, y + 0.5 * k1)
        
        # Update next value of y
        y = y + k2
        
        # Update next value of x
        x = x + h

    return y