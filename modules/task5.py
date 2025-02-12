import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Task5(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=2)  
        self.grid_rowconfigure(0, weight=1)

        left_frame = ctk.CTkFrame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        right_frame = ctk.CTkFrame(self)
        right_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(left_frame, text="Data Points (x, y)").grid(
            row=0, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        self.x_entries = []
        self.y_entries = []
        for i in range(5): 
            ctk.CTkLabel(left_frame, text=f"x{i+1}:").grid(row=i + 1, column=0, padx=5, pady=5, sticky="nsew")
            x_entry = ctk.CTkEntry(left_frame, width=50)
            x_entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="nsew")
            self.x_entries.append(x_entry)

            ctk.CTkLabel(left_frame, text=f"y{i+1}:").grid(row=i + 1, column=2, padx=5, pady=5, sticky="nsew")
            y_entry = ctk.CTkEntry(left_frame, width=50)
            y_entry.grid(row=i + 1, column=3, padx=5, pady=5, sticky="nsew")
            self.y_entries.append(y_entry)

        predefined_x = [0, 1, 2, 3, 4]
        predefined_y = [0, 1, 4, 9, 16]
        for i in range(5):
            self.x_entries[i].insert(0, str(predefined_x[i]))
            self.y_entries[i].insert(0, str(predefined_y[i]))

        ctk.CTkButton(left_frame, text="Fit Curve", command=self.fit_curve).grid(
            row=6, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        self.result_label = ctk.CTkLabel(left_frame, text="", wraplength=200)
        self.result_label.grid(row=7, column=0, columnspan=4, pady=10, sticky="nsew")

        self.fig = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def fit_curve(self):
        try:
            x = np.array([float(entry.get()) for entry in self.x_entries])
            y = np.array([float(entry.get()) for entry in self.y_entries])

            coefficients = np.polyfit(x, y, 2)  
            a, b, c = coefficients

            x_fit = np.linspace(min(x), max(x), 100)
            y_fit = a * x_fit**2 + b * x_fit + c

            self.result_label.configure(
                text=f"Fitted Quadratic Curve:\n"
                     f"y = {a:.4f}x² + {b:.4f}x + {c:.4f}"
            )

            self.ax.clear()
            self.ax.scatter(x, y, color='red', label="Data Points")
            self.ax.plot(x_fit, y_fit, label="Fitted Curve")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.set_title("Quadratic Curve Fitting")
            self.ax.legend()
            self.canvas.draw()
        except ValueError:
            self.result_label.configure(text="Invalid input. Please enter numeric values.")
