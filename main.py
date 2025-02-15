import customtkinter as ctk
from modules.task1 import Task1
from modules.task2 import Task2
from modules.task3 import Task3
from modules.task4 import Task4
from modules.task5 import Task5
from modules.task6 import Task6
from modules.task7 import Task7
from modules.task8 import Task8

# Set the appearance mode and default color theme for the application
ctk.set_appearance_mode("Dark")  # Use a dark theme
ctk.set_default_color_theme("blue")  # Use a blue color theme

class NumericalMethodsApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Set the title and size of the application window
        self.title("Final project CompMath (UNIS team)")
        self.geometry(f"{1000}x{500}")  # Set the window size to 1000x500 pixels
        
        # Create a tabbed interface using CTkTabview
        self.notebook = ctk.CTkTabview(self)
        self.notebook.pack(fill="both", expand=True)  # Make the notebook fill the entire window
        
        # Define the tasks (tabs) to be included in the application
        self.tabs = {
            "Task 1": Task1,
            "Task 2": Task2,
            "Task 3": Task3,
            "Task 4": Task4,
            "Task 5": Task5,
            "Task 6": Task6,
            "Task 7": Task7,
            "Task 8": Task8,
        }
        
        # Add each task as a tab in the notebook
        for title, cls in self.tabs.items():
            tab = self.notebook.add(title)  # Add a new tab with the given title
            cls(tab).pack(fill="both", expand=True)  # Instantiate the task class and pack it into the tab

# Entry point of the application
if __name__ == "__main__":
    app = NumericalMethodsApp()  # Create an instance of the NumericalMethodsApp
    app.mainloop()  # Start the application's main event loop