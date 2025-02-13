import customtkinter as ctk
from modules.utils import lagrange_interpolation

class Task6(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for i in range(4):  
            main_frame.grid_columnconfigure(i, weight=1)

        ctk.CTkLabel(main_frame, text="Data Points (x, y)").grid(
            row=0, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        self.x_entries = []
        self.y_entries = []
        for i in range(3):  
            ctk.CTkLabel(main_frame, text=f"x{i+1}:").grid(
                row=i + 1, column=0, padx=5, pady=5, sticky="nsew"
            )
            x_entry = ctk.CTkEntry(main_frame, width=50)
            x_entry.grid(row=i + 1, column=1, padx=5, pady=5, sticky="nsew")
            self.x_entries.append(x_entry)

            ctk.CTkLabel(main_frame, text=f"y{i+1}:").grid(
                row=i + 1, column=2, padx=5, pady=5, sticky="nsew"
            )
            y_entry = ctk.CTkEntry(main_frame, width=50)
            y_entry.grid(row=i + 1, column=3, padx=5, pady=5, sticky="nsew")
            self.y_entries.append(y_entry)

        predefined_x = [1, 3, 5]
        predefined_y = [2, 8, 18]
        for i in range(3):
            self.x_entries[i].insert(0, str(predefined_x[i]))
            self.y_entries[i].insert(0, str(predefined_y[i]))

        ctk.CTkLabel(main_frame, text="Value of x").grid(
            row=4, column=0, columnspan=4, pady=5, sticky="nsew"
        )
        self.x_value_entry = ctk.CTkEntry(main_frame, width=50)
        self.x_value_entry.insert(0, "4")  
        self.x_value_entry.grid(row=5, column=0, columnspan=4, pady=2, sticky="nsew")

        ctk.CTkButton(main_frame, text="Estimate f(x)", command=self.estimate).grid(
            row=6, column=0, columnspan=4, pady=10, sticky="nsew"
        )

        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=7, column=0, columnspan=4, pady=10, sticky="nsew")

    def estimate(self):
        try:
            x = [float(entry.get()) for entry in self.x_entries]
            y = [float(entry.get()) for entry in self.y_entries]

            x_value = float(self.x_value_entry.get())

            result = lagrange_interpolation(x, y, x_value)

            self.result_label.configure(
                text=f"Estimated f({x_value}): {result:.6f}"
            )
        except ValueError:
            self.result_label.configure(text="Invalid input. Please enter numeric values.")