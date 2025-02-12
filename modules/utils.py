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