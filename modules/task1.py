import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from modules.utils import calculate_errors

class Task1(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Initialize the approximate root as None
        self.approx_root = None 

        # Configure the grid layout for the frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)  

        # Create left and right frames for the UI
        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configure the grid layout for the left frame
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_columnconfigure(1, weight=1)
        left_frame.grid_columnconfigure(2, weight=1)
        left_frame.grid_columnconfigure(3, weight=1)
        left_frame.grid_columnconfigure(4, weight=1)

        # Add a label for the function
        ctk.CTkLabel(left_frame, text="Function: ax³ + bx² + cx + d").grid(row=0, column=0, columnspan=5, pady=20)

        # Add entry fields for coefficients a, b, c, and d
        ctk.CTkLabel(left_frame, text="A").grid(row=1, column=0, sticky="nsew")
        self.a_entry = ctk.CTkEntry(left_frame, width=80)
        self.a_entry.insert(0, "1")
        self.a_entry.grid(row=2, column=0, pady=2, sticky="nsew")

        ctk.CTkLabel(left_frame, text="B").grid(row=1, column=1, sticky="nsew")
        self.b_entry = ctk.CTkEntry(left_frame, width=80)
        self.b_entry.insert(0, "0")
        self.b_entry.grid(row=2, column=1, pady=2, sticky="nsew")

        ctk.CTkLabel(left_frame, text="C").grid(row=1, column=2, sticky="nsew")
        self.c_entry = ctk.CTkEntry(left_frame, width=80)
        self.c_entry.insert(0, "-3")
        self.c_entry.grid(row=2, column=2, pady=2, sticky="nsew")

        ctk.CTkLabel(left_frame, text="D").grid(row=1, column=3, sticky="nsew")
        self.d_entry = ctk.CTkEntry(left_frame, width=80)
        self.d_entry.insert(0, "2")
        self.d_entry.grid(row=2, column=3, pady=2, sticky="nsew")

        # Add entry fields for the interval
        ctk.CTkLabel(left_frame, text="Interval").grid(row=3, column=0, columnspan=5, pady=5)
        ctk.CTkLabel(left_frame, text="Min").grid(row=4, column=1, sticky="nsew")
        self.xmin_entry = ctk.CTkEntry(left_frame, width=80)
        self.xmin_entry.insert(0, "-2")
        self.xmin_entry.grid(row=5, column=1, pady=2, sticky="nsew")

        ctk.CTkLabel(left_frame, text="Max").grid(row=4, column=2, sticky="nsew")
        self.xmax_entry = ctk.CTkEntry(left_frame, width=80)
        self.xmax_entry.insert(0, "2")
        self.xmax_entry.grid(row=5, column=2, pady=2, sticky="nsew")

        # Add buttons for plotting and calculating error
        button_frame = ctk.CTkFrame(left_frame)
        button_frame.grid(row=6, column=0, columnspan=5, pady=10)
        ctk.CTkButton(button_frame, text="Plot", command=self.plot).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Calculate Error", command=self.calculate_error).pack(side=ctk.LEFT, padx=5)

        # Add a label to display results
        self.result_label = ctk.CTkLabel(left_frame, text="", wraplength=200)
        self.result_label.grid(row=7, column=0, columnspan=5, pady=10, sticky="nsew")

        # Create a matplotlib figure and canvas for plotting
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(fill=ctk.BOTH, expand=True)

        # Connect the click event to the on_click method
        self.canvas.mpl_connect('button_press_event', self.on_click)

    def plot(self):
        # Get the coefficients and interval from the entry fields
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())
        d = float(self.d_entry.get())
        x_min = float(self.xmin_entry.get())
        x_max = float(self.xmax_entry.get())

        # Generate x and y values for the plot
        x = np.linspace(x_min, x_max, 400)
        y = a * x**3 + b * x**2 + c * x + d

        # Clear the previous plot and plot the new function
        self.ax.clear()
        self.ax.plot(x, y, label=f"f(x) = {a}x³ + {b}x² + {c}x + {d}")
        self.ax.axhline(0, color='gray', linestyle='--')
        self.ax.set_title("Function Plot")
        self.ax.legend()
        self.canvas.draw()

    def on_click(self, event):
        # Check if the click is within the plot axes
        if event.inaxes == self.ax:
            # Store the x-coordinate of the click as the approximate root
            self.approx_root = event.xdata

            # Get the coefficients and interval from the entry fields
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            d = float(self.d_entry.get())
            x_min = float(self.xmin_entry.get())
            x_max = float(self.xmax_entry.get())

            # Generate x and y values for the plot
            x = np.linspace(x_min, x_max, 400)
            y = a * x**3 + b * x**2 + c * x + d
            self.ax.clear()
            self.ax.plot(x, y, label=f"f(x) = {a}x³ + {b}x² + {c}x + {d}")
            self.ax.axhline(0, color='gray', linestyle='--')

            # Plot the approximate root as a red dot
            self.ax.plot(self.approx_root, 0, 'ro', label="Approximate Root")
            self.ax.legend()
            self.canvas.draw()

    def calculate_error(self):
        # Check if an approximate root has been selected
        if self.approx_root is None:
            self.result_label.configure(text="Please select an approximate root on the graph.")
            return

        # Get the coefficients and interval from the entry fields
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        c = float(self.c_entry.get())
        d = float(self.d_entry.get())
        x_min = float(self.xmin_entry.get())
        x_max = float(self.xmax_entry.get())

        # Define the function and its derivative
        def f(x): return a * x**3 + b * x**2 + c * x + d
        def df(x): return 3 * a * x**2 + 2 * b * x + c

        # Find the true root using the Brentq method
        result = root_scalar(f, bracket=[x_min, x_max], method='brentq')
        self.true_root = result.root
        
        # Calculate the absolute and relative errors
        absolute_error, relative_error = calculate_errors(self.true_root, self.approx_root)

        # Display the results
        self.result_label.configure(
            text=f"True Root: {self.true_root:.6f}\n"
                 f"Approximate Root: {self.approx_root:.6f}\n"
                 f"Absolute Error: {absolute_error:.6f}\n"
                 f"Relative Error: {relative_error:.6f}"
        )