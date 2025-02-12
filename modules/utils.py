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
