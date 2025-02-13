import customtkinter as ctk
import numpy as np
from modules.utils import romberg_integration

class Task7(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=10, sticky="nsew")

        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(main_frame, text="Integral Function").grid(
            row=0, column=0, columnspan=2, sticky="nsew", pady=5
        )
        self.func_entry = ctk.CTkEntry(main_frame, width=150)
        self.func_entry.insert(0, "x**2") 
        self.func_entry.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Integration Limits").grid(
            row=2, column=0, columnspan=2, sticky="nsew"
        )

        ctk.CTkLabel(main_frame, text="A").grid(
            row=3, column=0, padx=5, sticky="nsew"
        )
        self.a_entry = ctk.CTkEntry(main_frame, width=50)
        self.a_entry.insert(0, "0") 
        self.a_entry.grid(row=4, column=0, padx=5, sticky="nsew")

        ctk.CTkLabel(main_frame, text="B").grid(
            row=3, column=1, padx=5, sticky="nsew"
        )
        self.b_entry = ctk.CTkEntry(main_frame, width=50)
        self.b_entry.insert(0, "1")
        self.b_entry.grid(row=4, column=1, padx=5, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Number of rows in Romberg table").grid(
            row=5, column=0, columnspan=2, sticky="nsew", pady=5
        )
        self.n_entry = ctk.CTkEntry(main_frame, width=50)
        self.n_entry.insert(0, "4")  
        self.n_entry.grid(row=6, column=0, columnspan=2, sticky="nsew")

        ctk.CTkButton(main_frame, text="Compute", command=self.compute).grid(
            row=7, column=0, columnspan=2, pady=5, sticky="nsew"
        )

        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=8, column=0, columnspan=2, pady=10, sticky="nsew")

    def compute(self):
        try:
            func_str = self.func_entry.get()
            self.f = lambda x: eval(func_str, {"np": np, "x": x})

            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            n = int(self.n_entry.get())

            R = romberg_integration(self.f, a, b, n)

            result_text = "Romberg Table:\n"
            for row in R:
                result_text += " ".join(f"{val:.6f}" for val in row) + "\n"
            result_text += f"\nApproximate value of the integral: {R[-1, -1]:.6f}"

            self.result_label.configure(text=result_text)
        except ValueError:
            self.result_label.configure(text="Invalid input. Please enter numeric values.")
        except Exception as e:
            self.result_label.configure(text=f"Error: {str(e)}")