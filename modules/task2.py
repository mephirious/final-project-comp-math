import customtkinter as ctk
from scipy.optimize import root_scalar
from modules.utils import false_position_method
from modules.utils import bisection_method
from modules.utils import calculate_errors

class Task2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the grid layout for the frame
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create a main frame to hold all widgets
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configure the grid layout for the main frame
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)
        main_frame.grid_columnconfigure(3, weight=1)
        main_frame.grid_columnconfigure(4, weight=1)

        # Add a label for the function
        ctk.CTkLabel(main_frame, text="Function: ax⁴ + bx³ + cx² + dx + e").grid(row=0, column=0, columnspan=5, pady=10)

        # Add entry fields for coefficients a, b, c, d, and e
        ctk.CTkLabel(main_frame, text="A").grid(row=1, column=0, sticky="nsew")
        self.a_entry = ctk.CTkEntry(main_frame, width=80)
        self.a_entry.insert(0, "1")  # Default value for a
        self.a_entry.grid(row=2, column=0, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="B").grid(row=1, column=1, sticky="nsew")
        self.b_entry = ctk.CTkEntry(main_frame, width=80)
        self.b_entry.insert(0, "0")  # Default value for b
        self.b_entry.grid(row=2, column=1, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="C").grid(row=1, column=2, sticky="nsew")
        self.c_entry = ctk.CTkEntry(main_frame, width=80)
        self.c_entry.insert(0, "-5")  # Default value for c
        self.c_entry.grid(row=2, column=2, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="D").grid(row=1, column=3, sticky="nsew")
        self.d_entry = ctk.CTkEntry(main_frame, width=80)
        self.d_entry.insert(0, "0")  # Default value for d
        self.d_entry.grid(row=2, column=3, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="E").grid(row=1, column=4, sticky="nsew")
        self.e_entry = ctk.CTkEntry(main_frame, width=80)
        self.e_entry.insert(0, "4")  # Default value for e
        self.e_entry.grid(row=2, column=4, pady=2, sticky="nsew")

        # Add entry fields for the interval [min, max]
        ctk.CTkLabel(main_frame, text="Interval").grid(row=3, column=0, columnspan=5, pady=5)

        ctk.CTkLabel(main_frame, text="Min").grid(row=4, column=1, sticky="nsew")
        self.min_entry = ctk.CTkEntry(main_frame, width=80)
        self.min_entry.insert(0, "0")  # Default value for min
        self.min_entry.grid(row=5, column=1, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Max").grid(row=4, column=3, sticky="nsew")
        self.max_entry = ctk.CTkEntry(main_frame, width=80)
        self.max_entry.insert(0, "3")  # Default value for max
        self.max_entry.grid(row=5, column=3, pady=2, sticky="nsew")

        # Add an entry field for the tolerance
        ctk.CTkLabel(main_frame, text="Tolerance").grid(row=6, column=0, columnspan=5, sticky="nsew")
        self.tol_entry = ctk.CTkEntry(main_frame, width=80)
        self.tol_entry.insert(0, "1e-6")  # Default value for tolerance
        self.tol_entry.grid(row=7, column=2, pady=2, sticky="nsew")

        # Add buttons for running the False Position and Bisection methods
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=5, pady=5)
        ctk.CTkButton(button_frame, text="False Position", command=self.run_false_position).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Bisection", command=self.run_bisection).pack(side=ctk.LEFT, padx=5)

        # Add a label to display results
        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=9, column=0, columnspan=5, pady=5, sticky="nsew")

    def run_false_position(self):
        # Get the coefficients, interval, and tolerance from the entry fields
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())
        d = float(self.d_entry.get())
        e = float(self.e_entry.get())
        min = float(self.min_entry.get())
        max = float(self.max_entry.get())
        tol = float(self.tol_entry.get())

        # Define the function to solve
        def f(x): return a * x**4 + b * x**3 + c * x**2 + d * x + e

        # Check if the interval is valid (f(a) and f(b) must have opposite signs)
        if f(min) * f(max) >= 0:
            self.result_label.configure(text="Invalid interval: f(a) and f(b) must have opposite signs.")
            return

        # Run the False Position method
        root, iterations = false_position_method(f, min, max, tol)

        if root is not None:
            # Find the true root using the Brentq method for comparison
            result = root_scalar(f, bracket=[min, max], method='brentq')
            true_root = result.root
        
            # Calculate the relative error
            _, relative_error = calculate_errors(true_root, root)
            self.result_label.configure(
                text=f"False Position Method:\n"
                     f"Root: {root:.6f}\n"
                     f"Iterations: {iterations}\n"
                     f"Relative Error: {relative_error:.6f}"
            )

    def run_bisection(self):
        # Get the coefficients, interval, and tolerance from the entry fields
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())
        d = float(self.d_entry.get())
        e = float(self.e_entry.get())
        min = float(self.min_entry.get())
        max = float(self.max_entry.get())
        tol = float(self.tol_entry.get())

        # Define the function to solve
        def f(x): return a * x**4 + b * x**3 + c * x**2 + d * x + e

        # Check if the interval is valid (f(a) and f(b) must have opposite signs)
        if f(min) * f(max) >= 0:
            self.result_label.configure(text="Invalid interval: f(a) and f(b) must have opposite signs.")
            return

        # Run the Bisection method
        root, iterations = bisection_method(f, min, max, tol)

        if root is not None:
            # Find the true root using the Brentq method for comparison
            result = root_scalar(f, bracket=[min, max], method='brentq')
            true_root = result.root

            # Calculate the relative error
            _, relative_error = calculate_errors(true_root, root)
            self.result_label.configure(
                text=f"Bisection Method:\n"
                     f"Root: {root:.6f}\n"
                     f"Iterations: {iterations}\n"
                     f"Relative Error: {relative_error:.6f}"
            )