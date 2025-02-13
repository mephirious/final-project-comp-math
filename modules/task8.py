import customtkinter as ctk
from modules.utils import runge_kutta

class Task8(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for i in range(4):
            main_frame.grid_columnconfigure(i, weight=1)

        ctk.CTkLabel(main_frame, text="Differential Equation dy/dx:").grid(row=0, column=0, columnspan=2, pady=5, sticky="nsew")
        self.dydx_entry = ctk.CTkEntry(main_frame, width=150)
        self.dydx_entry.insert(0, "np.exp(x) - y")  
        self.dydx_entry.grid(row=0, column=2, columnspan=2, pady=5, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Initial Condition y(0):").grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")
        self.y0_entry = ctk.CTkEntry(main_frame, width=50)
        self.y0_entry.insert(0, "0") 
        self.y0_entry.grid(row=1, column=2, columnspan=2, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Compute at x =").grid(row=2, column=0, columnspan=2, pady=5, sticky="nsew")
        self.x_entry = ctk.CTkEntry(main_frame, width=50)
        self.x_entry.insert(0, "0.2")  
        self.x_entry.grid(row=2, column=2, columnspan=2, pady=2, sticky="nsew")

        ctk.CTkLabel(main_frame, text="Step Size (h):").grid(row=3, column=0, columnspan=2, pady=5, sticky="nsew")
        self.h_entry = ctk.CTkEntry(main_frame, width=50)
        self.h_entry.insert(0, "0.1")  
        self.h_entry.grid(row=3, column=2, columnspan=2, pady=2, sticky="nsew")

        ctk.CTkButton(main_frame, text="Compute", command=self.compute).grid(row=4, column=0, columnspan=4, pady=10, sticky="nsew")

        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=5, column=0, columnspan=4, pady=10, sticky="nsew")

    def compute(self):
        try:
            equation = self.dydx_entry.get()
            y0 = float(self.y0_entry.get())
            x_target = float(self.x_entry.get())
            h = float(self.h_entry.get())

            y_result = runge_kutta(0, y0, x_target, h, equation)

            self.result_label.configure(text=f"Solution at x = {x_target}: y = {y_result:.6f}")

        except ValueError:
            self.result_label.configure(text="Invalid input. Please enter numeric values.")
        except Exception as e:
            self.result_label.configure(text=f"Error: {str(e)}")

