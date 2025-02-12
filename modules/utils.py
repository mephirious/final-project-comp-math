def calculate_errors(true_value, approx_value):
    absolute_error = abs(true_value - approx_value)  
    relative_error = absolute_error / true_value if true_value != 0 else float('inf') 
    return absolute_error, relative_error