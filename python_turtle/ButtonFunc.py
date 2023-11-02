import figureFunc

# Draw figure func
def draw_figure(figure_var, pen, entry_a, entry_b):
    figureFunc.is_clearing = False

    selected_figure = figure_var.get()
    if selected_figure == "quadratic tree":
        figureFunc.tree(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "d":
        figureFunc.d(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "fern":
        figureFunc.f(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "koch":
        figureFunc.koch(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "flake":
        figureFunc.flake(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "gasket3":
        figureFunc.gasket3(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "levy_c_curve":
        figureFunc.levy_c_curve(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "spiral_curve":
        figureFunc.spiral_curve(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "peano_curve":
        figureFunc.peano_curve(int(entry_a.get()), int(entry_b.get()), pen)
    elif selected_figure == "hexagonal_snowflake":
        figureFunc.hexagonal_snowflake(int(entry_a.get()), int(entry_b.get()), pen)

# Clear canvas func
def clear_canvas(turtle_screen, entry_a, entry_b):
    figureFunc.is_clearing = True
    turtle_screen.clear()
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
