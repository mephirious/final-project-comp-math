import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from modules.task1 import Task1
from modules.task2 import Task2
from modules.task3 import Task3
from modules.task4 import Task4
from modules.task5 import Task5
# from scipy.optimize import curve_fit
# from scipy.integrate import romberg
# from scipy.misc import derivative

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class NumericalMethodsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Numerical Methods")
        self.geometry(f"{1000}x{450}") 
        
        self.notebook = ctk.CTkTabview(self)
        self.notebook.pack(fill="both", expand=True)
        
        self.tabs = {
            "Task 1": Task1,
            "Task 2": Task2,
            "Task 3": Task3,
            "Task 4": Task4,
            "Task 5": Task5,
            # "Task 6": Task6,
            # "Task 7": Task7,
            # "Task 8": Task8,
        }
        
        for title, cls in self.tabs.items():
            tab = self.notebook.add(title)
            cls(tab).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = NumericalMethodsApp()
    app.mainloop()