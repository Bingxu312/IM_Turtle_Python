import turtlefigure

# Draw figure func
def draw_figure(figure_var, pen, speed, entry_a, entry_b):
    turtlefigure.is_clearing = False

    selected_figure = figure_var.get()
    if selected_figure == "quadratic tree":
        turtlefigure.tree(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "d":
        turtlefigure.d(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "fern":
        turtlefigure.f(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "koch":
        turtlefigure.koch(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "flake":
        turtlefigure.flake(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "gasket3":
        turtlefigure.gasket3(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "levy_c_curve":
        turtlefigure.levy_c_curve(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "spiral_curve":
        turtlefigure.spiral_curve(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "peano_curve":
        turtlefigure.peano_curve(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "hexagonal_snowflake":
        turtlefigure.hexagonal_snowflake(int(entry_a.get()), int(entry_b.get()), pen, speed)
    elif selected_figure == "olimpic_ring":
        turtlefigure.olimpic_ring(int(entry_a.get()), int(entry_b.get()), pen, speed)

# Clear canvas func
def clear_canvas(turtle_screen, pen, entry_a, entry_b):
    turtlefigure.is_clearing = True
    turtle_screen.clear()
    pen.goto(0, 0)
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
