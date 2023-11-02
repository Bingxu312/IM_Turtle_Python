import turtle
import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

import figureFunc

# Draw figure func 
def draw_figure():
    figureFunc.is_clearing = False

    selected_figure = figure_var.get()
    if selected_figure == "quadratic tree":
        figureFunc.tree(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "d":
        figureFunc.d(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "fern":
        figureFunc.f(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "koch":
        figureFunc.koch(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "flake":
        figureFunc.flake(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "gasket3":
        figureFunc.gasket3(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "levy_c_curve":
        figureFunc.levy_c_curve(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "spiral_curve":
        figureFunc.spiral_curve(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "peano_curve":
        figureFunc.peano_curve(int(entry_a.get()), int(entry_b.get()))
    elif selected_figure == "hexagonal_snowflake":
        figureFunc.hexagonal_snowflake(int(entry_a.get()), int(entry_b.get()))

# Clear canvas func
def clear_canvas():
    print(figureFunc.is_clearing)
    figureFunc.is_clearing = True
    turtle_screen.clear()
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')

# Create Turtle Object
t = turtle.Turtle()
t.speed(1)

# Create Tkinter Interface
window = tk.Tk()
window.title("Figure Operation Board")

# Init Turtle Canvas
turtle_screen = turtle.Screen()
turtle_screen.title("Figure Canvas")
turtle_screen.setup(800, 800)

# Create Figure parameters input field
Label(window, text="Order:").grid(row=0, column=0, padx=5, pady=5)
entry_a = Entry(window)
entry_a.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="Length:").grid(row=1, column=0, padx=5, pady=5)
entry_b = Entry(window)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Create Figure select field
figures = ["quadratic tree", "d", "fern", "koch", "flake", "gasket3", "levy_c_curve", "spiral_curve", "peano_curve", "hexagonal_snowflake"]
figure_var = tk.StringVar()
figure_var.set(figures[0])

Label(window, text="Select figures:").grid(row=3, column=0, padx=5, pady=5)
figure_menu = OptionMenu(window, figure_var, *figures)
figure_menu.grid(row=3, column=1, padx=5, pady=5)

# Create draw and clear button
draw_button = Button(window, text="draw", command=draw_figure)
draw_button.grid(row=4, column=0, padx=5, pady=5)

clear_button = Button(window, text="clear", command=clear_canvas)
clear_button.grid(row=4, column=1, padx=5, pady=5)

# Run Tkinter main loop
window.mainloop()
