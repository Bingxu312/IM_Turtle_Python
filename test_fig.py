# import turtle

# pen = turtle.Pen()

global is_clearing
is_clearing = False

def tree(n, l, pen):
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
