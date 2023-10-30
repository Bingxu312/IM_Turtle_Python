from turtle import *
import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

turtle = Turtle()
# create Tkinter interface
window = tk.Tk()
window.title("Turtle GUI")

# make a turtle pen and setup its features
pen = Pen()
pen.color("red")
pen.speed(0)
pen.width(3)

# make a screen and setup the bg
screen = Screen()
screen.bgcolor("blue")

def circle():
    a = int(entry_a.get())
    b = int(entry_b.get())
    t.circle(a)
    t.hideturtle()

def cube():
    a = int(entry_a.get())
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.hideturtle()

# draw on canvas
def draw_shape():
    selected_shape = shape_var.get()
    if selected_shape == "circle":
        circle()
    elif selected_shape == "cube":
        cube()

# func: clear canvas
def clear_canvas():
    turtle_screen.clear()
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')

# init Turtle canvas
# turtle_screen = turtle.Screen()
turtle_screen = screen
turtle_screen.title("Turtle GUI")
turtle_screen.setup(800, 800)

# create Turtle object
# t = turtle.Turtle()
t = turtle
t.speed(1)

# create label and button
Label(window, text="A:").pack()
entry_a = Entry(window)
entry_a.pack()

Label(window, text="B:").pack()
entry_b = Entry(window)
entry_b.pack()

Label(window, text="C:").pack()
entry_c = Entry(window)
entry_c.pack()
entry_c.configure(state='disabled')


shapes = ["circle", "cube"]
shape_var = tk.StringVar()
shape_var.set(shapes[0])
Label(window, text="Select shape:").pack()
shape_menu = OptionMenu(window, shape_var, *shapes, command=lambda event: toggle_entry(event))

shape_menu.pack()

draw_button = Button(window, text="draw", command=draw_shape)
draw_button.pack()

clear_button = Button(window, text="clear", command=clear_canvas)
clear_button.pack()

# func: shift label num
def toggle_entry(event):
    selected_shape = shape_var.get()
    if selected_shape == "cube":
        entry_c.configure(state='normal')
    else:
        entry_c.configure(state='disabled')

# start Tkinter loop
window.mainloop()
