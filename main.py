import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from modules.task1 import Task1
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

class Task2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        input_frame = ctk.CTkFrame(self)
        input_frame.pack(pady=10)
        
        ctk.CTkLabel(input_frame, text="Interval [a,b]:").grid(row=0, column=0)
        self.a_entry = ctk.CTkEntry(input_frame, width=80)
        self.a_entry.insert(0, "0")
        self.a_entry.grid(row=0, column=1)
        
        self.b_entry = ctk.CTkEntry(input_frame, width=80)
        self.b_entry.insert(0, "3")
        self.b_entry.grid(row=0, column=2)
        
        ctk.CTkLabel(input_frame, text="Tolerance:").grid(row=1, column=0)
        self.tol_entry = ctk.CTkEntry(input_frame, width=80)
        self.tol_entry.insert(0, "1e-6")
        self.tol_entry.grid(row=1, column=1)
        
        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)
        ctk.CTkButton(button_frame, text="False Position", command=self.run_false_position).pack(side=ctk.LEFT, padx=5)
        ctk.CTkButton(button_frame, text="Bisection", command=self.run_bisection).pack(side=ctk.LEFT, padx=5)
        
        self.result_text = ctk.CTkTextbox(self, height=150)
        self.result_text.pack(fill=ctk.BOTH, expand=True)
    
    def run_false_position(self):
        def f(x): return x**4 - 5*x**2 + 4
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        tol = float(self.tol_entry.get())
        
        if f(a) * f(b) >= 0:
            self.result_text.insert("end", "Invalid interval: no sign change\n")
            return
        
        iterations = 0
        c = a
        while abs(f(c)) > tol:
            c = b - f(b)*(b - a)/(f(b) - f(a))
            iterations += 1
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
        
        true_root = 2.0 
        rel_error = abs(c - true_root)/true_root
        self.result_text.insert("end", 
            f"False Position:\nRoot: {c:.6f}\nIterations: {iterations}\nRel Error: {rel_error:.6f}\n\n")
    
    def run_bisection(self):
        def f(x): return x**4 - 5*x**2 + 4
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())
        tol = float(self.tol_entry.get())
        
        if f(a) * f(b) >= 0:
            self.result_text.insert("end", "Invalid interval: no sign change\n")
            return
        
        iterations = 0
        while (b - a)/2 > tol:
            c = (a + b)/2
            if f(c) == 0: break
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
            iterations += 1
        
        true_root = 2.0  
        rel_error = abs(c - true_root)/true_root
        self.result_text.insert("end",
            f"Bisection:\nRoot: {c:.6f}\nIterations: {iterations}\nRel Error: {rel_error:.6f}\n\n")


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