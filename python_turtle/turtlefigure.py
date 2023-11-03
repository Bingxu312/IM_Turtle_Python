global is_clearing
is_clearing = False

def tree(n, l, pen, speed):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(l)
    pen.left(45)
    tree(n - 1, l / 2, pen, speed)
    pen.right(90)
    tree(n - 1, l / 2, pen, speed)
    pen.left(45)
    pen.backward(l)

def d(n, l, pen, speed):
    pen.speed(speed)

    # termination
    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(l)
    pen.left(90)
    d(n - 1, l / 2, pen, speed)
    pen.right(60)
    d(n - 1, l / 2, pen, speed)
    pen.right(60)
    d(n - 1, l / 2, pen, speed)
    pen.right(60)
    d(n - 1, l / 2, pen, speed)
    pen.left(90)
    pen.backward(l)

# fern
def f(n, l, pen, speed):
    pen.speed(speed)

    # termination
    if n == 0 or l < 2 or is_clearing == True:
        return
    # endif
    pen.forward(0.3 * l)
    pen.right(45);
    f(n - 1, l / 2, pen, speed);
    pen.left(45)
    pen.forward(0.7 * l)
    pen.left(30);
    f(n - 1, l / 2, pen, speed);
    pen.right(30)
    pen.forward(l)
    pen.right(10);
    f(n - 1, 0.8 * l, pen, speed);
    pen.left(10)
    pen.backward(2 * l)

def koch(n, l, pen, speed):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing == True:
        pen.forward(l)
        return
    # endif
    koch(n - 1, l / 3, pen, speed)
    pen.left(60);
    koch(n - 1, l / 3, pen, speed)
    pen.right(120);
    koch(n - 1, l / 3, pen, speed)
    pen.left(60);
    koch(n - 1, l / 3, pen, speed)

def flake(n, l, pen, speed):
    pen.speed(speed)

    if is_clearing ==True:
        return

    for i in range(3):
        flake(n, l, pen, speed)
        pen.right(120)
    # endflake

def gasket3(n, l, pen, speed):
    pen.speed(speed)

    # termination
    if n == 0 or l < 2 or is_clearing == True:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        # end for
        return
    # end if
    gasket3(n - 1, l / 2, pen, speed);
    pen.forward(l);
    pen.left(120)
    gasket3(n - 1, l / 2, pen, speed);
    pen.forward(l);
    pen.left(120)
    gasket3(n - 1, l / 2, pen, speed);
    pen.forward(l);
    pen.left(120)

def levy_c_curve(n, l, pen, speed):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    pen.left(45)
    levy_c_curve(n - 1, l / (2 ** 0.5), pen, speed)
    pen.right(90)
    levy_c_curve(n - 1, l / (2 ** 0.5), pen, speed)
    pen.left(45)

def hilbert_curve(n, l, pen, speed, angle=90):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    pen.left(angle)
    hilbert_curve(n - 1, l, pen, speed, -angle)
    pen.forward(l)
    pen.right(angle)
    hilbert_curve(n - 1, l, pen, speed, angle)
    pen.forward(l)
    hilbert_curve(n - 1, l, pen, speed, angle)
    pen.right(angle)
    pen.forward(l)
    hilbert_curve(n - 1, l, pen, speed, -angle)
    pen.left(angle)

def peano_curve(n, l, pen, speed):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing:
        pen.forward(l)
        return
    peano_curve(n - 1, l / 3, pen, speed)
    pen.left(90)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.right(90)
    peano_curve(n - 1, l / 3, pen, speed)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.left(90)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.left(90)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.right(90)
    peano_curve(n - 1, l / 3, pen, speed)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.right(90)
    peano_curve(n - 1, l / 3, pen, speed)
    peano_curve(n - 1, l / 3, pen, speed)
    pen.left(90)
    peano_curve(n - 1, l / 3, pen, speed)

def hexagonal_snowflake(n, l, pen, speed):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing:
        for _ in range(6):
            pen.forward(l)
            pen.left(60)
        return
    l /= 3
    hexagonal_snowflake(n - 1, l, pen, speed)
    pen.left(60)
    hexagonal_snowflake(n - 1, l, pen, speed)
    pen.right(60)
    hexagonal_snowflake(n - 1, l, pen, speed)
    pen.right(60)
    hexagonal_snowflake(n - 1, l, pen, speed)
    pen.left(60)

def spiral_curve(n, l, pen, speed, angle=90):
    pen.speed(speed)

    if n == 0 or l < 2 or is_clearing:
        return
    pen.forward(l)
    pen.left(angle)
    spiral_curve(n - 1, l - 2, pen, speed, angle)

def olimpic_ring(n, l, pen, speed):
    pen.speed(speed)

    # blue ring
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color("blue")
    pen.circle((n+l)/2)

    # yellow ring
    pen.penup()
    pen.goto(120, 0)
    pen.pendown()
    pen.color("yellow")
    pen.circle((n+l)/2)

    # black ring
    pen.penup()
    pen.goto(240, 0)
    pen.pendown()
    pen.color("black")
    pen.circle((n+l)/2)

    # green ring
    pen.penup()
    pen.goto(60, -50)
    pen.pendown()
    pen.color("green")
    pen.circle((n+l)/2)

    # red ring
    pen.penup()
    pen.goto(180, -50)
    pen.pendown()
    pen.color("red")
    pen.circle((n+l)/2)