from turtle import *

pen = Pen()
pen.color("red")
pen.speed(0)
pen.width(3)

global is_clearing
is_clearing = False

def tree(n, l):
    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(l)
    pen.left(45)
    tree(n - 1, l / 2)
    pen.right(90)
    tree(n - 1, l / 2)
    pen.left(45)
    pen.backward(l)

def d(n, l):
    # termination
    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(l)
    pen.left(90)
    d(n - 1, l / 2)
    pen.right(60)
    d(n - 1, l / 2)
    pen.right(60)
    d(n - 1, l / 2)
    pen.right(60)
    d(n - 1, l / 2)
    pen.left(90)
    pen.backward(l)

# fern
def f(n, l):
    # termination
    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(0.3 * l)
    pen.right(45);
    f(n - 1, l / 2);
    pen.left(45)
    pen.forward(0.7 * l)
    pen.left(30);
    f(n - 1, l / 2);
    pen.right(30)
    pen.forward(l)
    pen.right(10);
    f(n - 1, 0.8 * l);
    pen.left(10)
    pen.backward(2 * l)

def koch(n, l):
    if n == 0 or l < 2 or is_clearing == True:
        pen.forward(l)
        return
    # endif
    koch(n - 1, l / 3)
    pen.left(60);
    koch(n - 1, l / 3)
    pen.right(120);
    koch(n - 1, l / 3)
    pen.left(60);
    koch(n - 1, l / 3)

def flake(n, l):
    if is_clearing ==True:
        return

    for i in range(3):
        koch(n, l)
        pen.right(120)
    # endflake

def gasket3(n, l):
    # termination
    if n == 0 or l < 2 or is_clearing == True:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        # end for
        return
    # end if
    gasket3(n - 1, l / 2);
    pen.forward(l);
    pen.left(120)
    gasket3(n - 1, l / 2);
    pen.forward(l);
    pen.left(120)
    gasket3(n - 1, l / 2);
    pen.forward(l);
    pen.left(120)

def levy_c_curve(n, l):
    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    pen.left(45)
    levy_c_curve(n - 1, l / (2 ** 0.5))
    pen.right(90)
    levy_c_curve(n - 1, l / (2 ** 0.5))
    pen.left(45)

def hilbert_curve(n, l, angle=90):
    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    pen.left(angle)
    hilbert_curve(n - 1, l, -angle)
    pen.forward(l)
    pen.right(angle)
    hilbert_curve(n - 1, l, angle)
    pen.forward(l)
    hilbert_curve(n - 1, l, angle)
    pen.right(angle)
    pen.forward(l)
    hilbert_curve(n - 1, l, -angle)
    pen.left(angle)

def peano_curve(n, l):
    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    peano_curve(n - 1, l / 3)
    pen.left(90)
    peano_curve(n - 1, l / 3)
    pen.right(90)
    peano_curve(n - 1, l / 3)
    peano_curve(n - 1, l / 3)
    pen.left(90)
    peano_curve(n - 1, l / 3)
    pen.left(90)
    peano_curve(n - 1, l / 3)
    pen.right(90)
    peano_curve(n - 1, l / 3)
    peano_curve(n - 1, l / 3)
    pen.right(90)
    peano_curve(n - 1, l / 3)
    peano_curve(n - 1, l / 3)
    pen.left(90)
    peano_curve(n - 1, l / 3)

def hexagonal_snowflake(n, l):
    if n == 0 or l < 2 or is_clearing:
        for _ in range(6):
            pen.forward(l)
            pen.left(60)
        return
    l /= 3
    hexagonal_snowflake(n - 1, l)
    pen.left(60)
    hexagonal_snowflake(n - 1, l)
    pen.right(60)
    hexagonal_snowflake(n - 1, l)
    pen.right(60)
    hexagonal_snowflake(n - 1, l)
    pen.left(60)

def spiral_curve(n, l, angle=90):
    if n == 0 or l < 2 or is_clearing:
        return
    pen.forward(l)
    pen.left(angle)
    spiral_curve(n - 1, l - 2, angle)
