import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to evaluate a quadratic equation ax^2 + bx + c
def quadratic_equation(x, a, b, c):
    return a * x**2 + b * x + c

# Function to display the point where the root value is zero
def display_root_zero(x, y, root):
    plt.scatter(root, 0, color='red', label=f'Root: {root}')
    plt.legend()

# (a) Graphically
def plot_graphical_solution(x_values, y_values, a, b, c):
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, label=f'f(x) = {a}x^2 + {b}x + {c}')
    ax.axhline(0, color='black', linestyle='--', label='y = 0')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Graphical Solution')
    ax.legend()
    st.pyplot(fig)

# (b) Using the quadratic formula
def solve_quadratic_formula(x_values, y_values, a, b, c):
    fig, ax = plt.subplots()
    
    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2 * a)
        root2 = (-b - np.sqrt(discriminant)) / (2 * a)
        st.write(f'Real roots using quadratic formula: {root1}, {root2}')

        # Display root zero point in the graphical solution
        display_root_zero(x_values, y_values, root1)
        display_root_zero(x_values, y_values, root2)
        st.pyplot(fig)

    else:
        st.write('No real roots using quadratic formula (discriminant < 0)')

# (c) Using the bisection method
def bisection_method(func, xl, xu, tol=1e-6, max_iter=100):
    fig, ax = plt.subplots()

    iterations = 0
    while iterations < max_iter:
        xr = (xl + xu) / 2
        if func(xl) * func(xr) < 0:
            xu = xr
        elif func(xl) * func(xr) > 0:
            xl = xr
        else:
            break

        ea = abs((xu - xl) / xu) * 100
        et = abs((xu - xr) / xu) * 100

        st.write(f'Iteration {iterations + 1}: xr = {xr}, εa = {ea}%, εt = {et}%')

        if ea < tol:
            break

        iterations += 1

    st.pyplot(fig)
    return xr

def main():
    st.title('Quadratic Equation Solver')

    # User input for the quadratic equation coefficients
    a = st.number_input('Enter coefficient a:')
    b = st.number_input('Enter coefficient b:')
    c = st.number_input('Enter coefficient c:')

    if a == b == c == 0:
        st.warning('All coefficients are zero. Please enter valid coefficients.')
        return

    # Generate x_values and y_values
    x_values = np.linspace(0, 10, 100)
    y_values = quadratic_equation(x_values, a, b, c)

    # Plot graphical solution
    st.subheader('Graphical Solution')
    plot_graphical_solution(x_values, y_values, a, b, c)

    # Solve using the quadratic formula
    if st.button('Calculate Quadratic Formula Solution'):
        st.subheader('Quadratic Formula Solution')
        solve_quadratic_formula(x_values, y_values, a, b, c)

    # (c) Using the bisection method
    # Initial guesses for bisection method
    xl_guess = 0
    xu_guess = 10

    # Find the highest root using bisection method
    if st.button('Calculate Bisection Method'):
        st.subheader('Bisection Method')
        bisection_root = bisection_method(lambda x: quadratic_equation(x, a, b, c), xl_guess, xu_guess)
        st.write(f'Highest root using bisection method: {bisection_root}')

        # Display root zero point in the graphical solution for bisection method
        display_root_zero(x_values, y_values, bisection_root)

if __name__ == '__main__':
    main()
