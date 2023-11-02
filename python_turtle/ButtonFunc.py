import figureFunc
from turtle import *

screen = Screen()
turtle_screen = screen
def draw_shape(figure_name, entry_a, entry_b, entry_c):
    order = int(entry_a.get())
    length = int(entry_b.get())
    angle = int(entry_c.get())

    if figure_name == "tree":
        figureFunc.tree(order, length)

# func: clear canvas
def clear_canvas(order, length, angle):
    turtle_screen.clear()
    order.delete(0, 'end')
    length.delete(0, 'end')
    angle.delete(0, 'end')