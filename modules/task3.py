import customtkinter as ctk
import numpy as np
from modules.utils import gauss_elimination

class Task3(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the grid layout for the frame
        self.grid(row=0, column=0, sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a main frame to hold all widgets
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Configure the grid layout for the main frame
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)

        # Add a label for the matrix A
        ctk.CTkLabel(main_frame, text="Matrix A (3x3)").grid(
            row=0, column=0, columnspan=3, pady=10, sticky="nsew"
        )

        # Predefined 3x3 matrix for matrix A
        predefined_2dmatrix = [
            [2, 1, -1],
            [-3, 1, 2],
            [-2, 1, 3]
        ]

        # Create entry fields for matrix A
        self.a_entries = []
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = ctk.CTkEntry(main_frame, width=50)
                entry.insert(0, str(predefined_2dmatrix[i][j]))  # Insert predefined values
                entry.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
                row_entries.append(entry)
            self.a_entries.append(row_entries)

        # Add a label for the vector b
        ctk.CTkLabel(main_frame, text="Vector b").grid(
            row=4, column=0, columnspan=3, pady=10, sticky="nsew"
        )

        # Predefined vector for vector b
        predefined_matrix = [8, -11, -3]

        # Create entry fields for vector b
        self.b_entries = []
        for i in range(3):
            entry = ctk.CTkEntry(main_frame, width=50)
            entry.insert(0, str(predefined_matrix[i]))  # Insert predefined values
            entry.grid(row=5, column=i, padx=5, pady=5, sticky="nsew")
            self.b_entries.append(entry)

        # Add a button to solve the system
        ctk.CTkButton(main_frame, text="Solve", command=self.solve).grid(
            row=8, column=0, columnspan=3, pady=10, sticky="nsew"
        )

        # Add a label to display the results
        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=9, column=0, columnspan=3, pady=5, sticky="nsew")

    def solve(self):
        try:
            # Read matrix A from the entry fields
            A = np.zeros((3, 3))
            for i in range(3):
                for j in range(3):
                    A[i, j] = float(self.a_entries[i][j].get())

            # Read vector b from the entry fields
            b = np.zeros(3)
            for i in range(3):
                b[i] = float(self.b_entries[i].get())

            # Solve the system using Gaussian Elimination
            x = gauss_elimination(A, b)

            # Display the solution
            self.result_label.configure(
                text=f"Solution:\n"
                     f"x = {x[0]:.6f}\n"
                     f"y = {x[1]:.6f}\n"
                     f"z = {x[2]:.6f}"
            )
        except ValueError:
            # Handle invalid input (non-numeric values)
            self.result_label.configure(text="Invalid input. Please enter numeric values.")