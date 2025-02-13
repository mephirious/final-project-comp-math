# Final Project on Computitional Mathematics

This application provides a graphical user interface (GUI) for solving various numerical methods problems, including root-finding, integration, interpolation, and differential equations. It is built using `customtkinter` for the GUI and `numpy`, `matplotlib`, and `scipy` for numerical computations and visualizations.

## Features

The application includes the following tasks:

*   **Task 1:** Graphical Method and Absolute Error
    *   Plot the graph of a cubic function and find an approximate root.
    *   Calculate the absolute error compared to the root found using a numerical method.
*   **Task 2:** Comparison of Root-Finding Methods
    *   Find the root of a function using the False Position and Bisection methods.
    *   Measure iterations and calculate relative errors.
*   **Task 3:** Gaussian Elimination with Partial Pivoting
    *   Solve a system of linear equations using Gaussian elimination with partial pivoting.
*   **Task 4:** Iterative Method for Matrix Inversion
    *   Compute the inverse of a matrix using an iterative method.
*   **Task 5:** Polynomial Curve Fitting
    *   Fit a quadratic curve to a set of data points using the least squares method.
*   **Task 6:** Lagrange’s Interpolation Formula
    *   Estimate the value of a function at a given point using Lagrange’s interpolation.
*   **Task 7:** Romberg’s Integration
    *   Approximate the integral of a function using Romberg’s integration method.
*   **Task 8:** Runge-Kutta 4th Order
    *   Solve a first-order ordinary differential equation using the Runge-Kutta 4th-order method.

## Installation

To run this application, you need to install the required Python packages. Follow these steps:

**1. Install Python:**

Ensure you have Python 3.8 or higher installed. You can download it from [python.org](python.org).

**2. Clone the Repository:**

```bash
git clone git@github.com:mephirious/final-project-comp-math.git
```

**3. Install Dependencies:**

```bash
pip install customtkinter numpy matplotlib scipy
```

## Usage

1.  **Navigate to the project directory:**

    ```bash
    cd final-project-comp-math
    ```
2.  **Run the Application:**


    ```bash
    python main.py
    ```
    
## Dependencies

The application relies on the following Python packages:

*   **customtkinter:** For the modern GUI.  Install with: `pip install customtkinter`
*   **numpy:** For numerical computations. Install with: `pip install numpy`
*   **matplotlib:** For plotting graphs. Install with: `pip install matplotlib`
*   **scipy:** For advanced numerical methods (e.g., root-finding, integration). Install with: `pip install scipy`
