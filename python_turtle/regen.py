import turtle
import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

import ButtonFunc

# Create Tkinter Interface
window = tk.Tk()
window.title("Figure Operation Board")

pen = turtle.Pen()
pen.color("red")
pen.speed(0)
pen.width(3)

# Init Turtle Canvas
turtle_screen = turtle.Screen()
turtle_screen.title("Figure Canvas")
turtle_screen.setup(800, 800)

# Create Turtle Object
t = turtle.Turtle()
t.speed(1)

# Create Figure parameters input field
Label(window, text="Order:").grid(row=0, column=0, padx=5, pady=5)
entry_a = Entry(window)
entry_a.insert(0, "")
entry_a.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="Length:").grid(row=1, column=0, padx=5, pady=5)
entry_b = Entry(window)
entry_b.insert(0, "")
entry_b.grid(row=1, column=1, padx=5, pady=5)

# Create Figure select field
figures = ["quadratic tree", "d", "fern", "koch", "flake", "gasket3", "levy_c_curve", "spiral_curve", "peano_curve", "hexagonal_snowflake"]
figure_var = tk.StringVar()
figure_var.set(figures[0])

Label(window, text="Select figures:").grid(row=3, column=0, padx=5, pady=5)
figure_menu = OptionMenu(window, figure_var, *figures)
figure_menu.grid(row=3, column=1, padx=5, pady=5)

# Create draw and clear button
draw_button = Button(window, text="draw", command=lambda: ButtonFunc.draw_figure(figure_var, pen, entry_a, entry_b))
draw_button.grid(row=4, column=0, padx=5, pady=5)

clear_button = Button(window, text="clear", command=lambda: ButtonFunc.clear_canvas(turtle_screen, entry_a, entry_b))
clear_button.grid(row=4, column=1, padx=5, pady=5)

# Run Tkinter main loop
window.mainloop()
