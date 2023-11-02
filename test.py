import turtle
import tkinter as tk
from tkinter import Label, Entry, Button, OptionMenu

# 创建Tkinter窗口
window = tk.Tk()
window.title("Turtle GUI")

# 函数：绘制圆形
def circle():
    a = int(entry_a.get())
    b = int(entry_b.get())
    entry_c.grid_remove()  # 隐藏输入框C
    t.circle(a)
    t.hideturtle()

# 函数：绘制方形
def cube():
    a = int(entry_a.get())
    c = int(entry_c.get())
    entry_c.grid()  # 显示输入框C
    for _ in range(4):
        t.forward(a)
        t.left(90)
    t.hideturtle()

# 函数：绘制图形
def draw_shape():
    selected_shape = shape_var.get()
    if selected_shape == "圆形":
        circle()
    elif selected_shape == "方形":
        cube()

# 函数：清空画布
def clear_canvas():
    global is_clearing
    is_clearing = True
    turtle_screen.clear()
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    entry_c.delete(0, 'end')
    is_clearing = False

# 初始化Turtle画布
turtle_screen = turtle.Screen()
turtle_screen.title("Turtle GUI")
turtle_screen.setup(400, 400)

# 创建Turtle对象
t = turtle.Turtle()
t.speed(1)

# 创建标签和输入框
Label(window, text="A:").grid(row=0, column=0, padx=5, pady=5)
entry_a = Entry(window)
entry_a.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="B:").grid(row=1, column=0, padx=5, pady=5)
entry_b = Entry(window)
entry_b.grid(row=1, column=1, padx=5, pady=5)

# 创建C输入框，但初始时是隐藏的
Label(window, text="C:").grid(row=2, column=0, padx=5, pady=5)
entry_c = Entry(window)
entry_c.grid(row=2, column=1, padx=5, pady=5)
entry_c.grid_remove()  # 隐藏输入框C

shapes = ["圆形", "方形"]
shape_var = tk.StringVar()
shape_var.set(shapes[0])

Label(window, text="选择图形:").grid(row=3, column=0, padx=5, pady=5)
shape_menu = OptionMenu(window, shape_var, *shapes)
shape_menu.grid(row=3, column=1, padx=5, pady=5)

draw_button = Button(window, text="绘制", command=draw_shape)
draw_button.grid(row=4, column=0, padx=5, pady=5)

clear_button = Button(window, text="清空", command=clear_canvas)
clear_button.grid(row=4, column=1, padx=5, pady=5)

is_clearing = False

# 启动Tkinter主循环
window.mainloop()
