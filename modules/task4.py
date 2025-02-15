import customtkinter as ctk
import numpy as np
from modules.utils import iterative_inverse

class Task4(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # Configure the frame layout
        self.grid(row=0, column=0, sticky="nsew")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create a main frame to hold the UI elements
        main_frame = ctk.CTkFrame(self)
        main_frame.grid(row=0, column=0, padx=10, sticky="nsew")

        # Configure column weights for equal spacing
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=1)

        # Label for matrix input
        ctk.CTkLabel(main_frame, text="Matrix A (3x3)").grid(
            row=0, column=0, columnspan=3, sticky="nsew"
        )

        # Predefined matrix values for input fields
        predefined_matrix = [
            [1, 2, 3],
            [0, -1, 4],
            [5, 6, -1]
        ]

        self.a_entries = []  # List to store entry widgets for matrix A
        
        # Create entry fields for matrix A input
        for i in range(3):
            row_entries = []
            for j in range(3):
                entry = ctk.CTkEntry(main_frame, width=50)
                entry.insert(0, str(predefined_matrix[i][j]))  # Set default values
                entry.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")
                row_entries.append(entry)
            self.a_entries.append(row_entries)

        # Tolerance input field
        ctk.CTkLabel(main_frame, text="Tolerance").grid(
            row=4, column=0, columnspan=3, sticky="nsew"
        )
        self.tol_entry = ctk.CTkEntry(main_frame, width=80)
        self.tol_entry.insert(0, "1e-6")  # Default tolerance value
        self.tol_entry.grid(row=5, column=0, columnspan=3, sticky="nsew")

        # Maximum iterations input field
        ctk.CTkLabel(main_frame, text="Max Iterations").grid(
            row=6, column=0, columnspan=3, sticky="nsew"
        )
        self.max_iter_entry = ctk.CTkEntry(main_frame, width=80)
        self.max_iter_entry.insert(0, "100")  # Default max iteration value
        self.max_iter_entry.grid(row=7, column=0, columnspan=3, sticky="nsew")

        # Compute Inverse button
        ctk.CTkButton(main_frame, text="Compute Inverse", command=self.compute_inverse).grid(
            row=8, column=0, columnspan=3, sticky="nsew", pady=10
        )

        # Label to display results
        self.result_label = ctk.CTkLabel(main_frame, text="", wraplength=400)
        self.result_label.grid(row=9, column=0, columnspan=3, sticky="nsew")

    def compute_inverse(self):
        try:
            # Read matrix A from input fields
            A = np.zeros((3, 3))
            for i in range(3):
                for j in range(3):
                    A[i, j] = float(self.a_entries[i][j].get())

            # Read tolerance and max iterations
            tol = float(self.tol_entry.get())
            max_iter = int(self.max_iter_entry.get())

            # Generate an initial approximation of the inverse
            B = np.linalg.inv(A) + 0.1 * np.random.randn(3, 3)

            # Compute the inverse iteratively
            B_inv = iterative_inverse(A, B, tol, max_iter)

            # Format and display the result
            result_text = "Inverse of A:\n"
            for row in B_inv:
                result_text += " ".join(f"{val:.6f}" for val in row) + "\n"

            self.result_label.configure(text=result_text)
        
        except ValueError:
            # Handle invalid numeric inputs
            self.result_label.configure(text="Invalid input. Please enter numeric values.")
        
        except np.linalg.LinAlgError:
            # Handle singular matrix case
            self.result_label.configure(text="Matrix A is singular and cannot be inverted.")