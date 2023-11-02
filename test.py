import turtle
import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

import test_fig
# def tree(n, l):
#     if n == 0 or l < 2 or is_clearing == True:
#         return
#     # endif
#     pen.forward(l)
#     pen.left(45)
#     tree(n - 1, l / 2)
#     pen.right(90)
#     tree(n - 1, l / 2)
#     pen.left(45)
#     pen.backward(l)

def draw_shape():
    selected_shape = shape_var.get()
    if selected_shape == "circle":
        test_fig.tree(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_shape == "cube":
        tree(int(entry_a.get()), int(entry_b.get()))

def clear_canvas():
    global is_clearing
    is_clearing = True
    turtle_screen.clear()
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')

window = tk.Tk()
window.title("Turtle GUI")
is_clearing = False
pen = turtle.Pen()
pen.color("red")
pen.speed(0)
pen.width(3)

turtle_screen = turtle.Screen()
turtle_screen.title("Turtle GUI")
turtle_screen.setup(400, 400)

t = turtle.Turtle()
t.speed(1)

Label(window, text="A:").grid(row=0, column=0, padx=5, pady=5)
entry_a = Entry(window)
entry_a.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="B:").grid(row=1, column=0, padx=5, pady=5)
entry_b = Entry(window)
entry_b.grid(row=1, column=1, padx=5, pady=5)

Label(window, text="C:").grid(row=2, column=0, padx=5, pady=5)
entry_c = Entry(window)
entry_c.grid(row=2, column=1, padx=5, pady=5)
entry_c.grid_remove()

shapes = ["circle", "cube"]
shape_var = tk.StringVar()
shape_var.set(shapes[0])

Label(window, text="select:").grid(row=3, column=0, padx=5, pady=5)
shape_menu = OptionMenu(window, shape_var, *shapes)
shape_menu.grid(row=3, column=1, padx=5, pady=5)

draw_button = Button(window, text="draw", command=draw_shape)
draw_button.grid(row=4, column=0, padx=5, pady=5)

clear_button = Button(window, text="clear", command=clear_canvas)
clear_button.grid(row=4, column=1, padx=5, pady=5)

# 启动Tkinter主循环
window.mainloop()
