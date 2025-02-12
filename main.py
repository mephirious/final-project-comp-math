import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from modules.task1 import Task1
from modules.task2 import Task2
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
            # "Task 4": Task4,
            # "Task 5": Task5,
            # "Task 6": Task6,
            # "Task 7": Task7,
            # "Task 8": Task8,
        }
        
        for title, cls in self.tabs.items():
            tab = self.notebook.add(title)
            cls(tab).pack(fill="both", expand=True)

class Task3(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.matrix_entries = []
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10)
        
        for i in range(3):
            row = []
            for j in range(3):
                entry = ctk.CTkEntry(input_frame, width=50)
                entry.grid(row=i, column=j, padx=2)
                row.append(entry)
            self.matrix_entries.append(row)
        
        self.vector_entries = []
        vector_frame = ctk.CTkFrame(self)
        vector_frame.pack(pady=10)
        for i in range(3):
            entry = ctk.CTkEntry(vector_frame, width=50)
            entry.grid(row=0, column=i, padx=2)
            self.vector_entries.append(entry)
        
        ctk.CTkButton(self, text="Solve", command=self.solve).pack(pady=10)
        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack()
    
    def solve(self):
        A = np.zeros((3,3))
        b = np.zeros(3)
        for i in range(3):
            for j in range(3):
                A[i,j] = float(self.matrix_entries[i][j].get())
            b[i] = float(self.vector_entries[i].get())
        
        n = len(b)
        for i in range(n):
            max_row = np.argmax(np.abs(A[i:, i])) + i
            A[[i, max_row]] = A[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]
            
            for j in range(i+1, n):
                factor = A[j,i]/A[i,i]
                A[j,i:] -= factor * A[i,i:]
                b[j] -= factor * b[i]
        
        x = np.zeros(n)
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
        
        self.result_label.configure(text=f"Solution: {x}")

if __name__ == "__main__":
    app = NumericalMethodsApp()
    app.mainloop()