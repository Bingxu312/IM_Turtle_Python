from turtle import *
import math

# make a turtle pen and setup its features
pen = Pen()
pen.color("red")
pen.speed(0)
pen.width(3)

# make a screen and setup the bg
screen = Screen()
screen.bgcolor("blue")

# binary tree
def tree(n, l):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2)
     pen.right(90)
     tree(n-1, l/2)
     pen.left(45)
     pen.backward(l)

def gasket(n, l):
     if n == 0 or l < 2:
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          return
     gasket(n - 1, l / 2)
     pen.forward(l)
     pen.left(120)

     gasket(n - 1, l / 2)
     pen.forward(l)
     pen.left(120)

     gasket(n - 1, l / 2)
     pen.forward(l)
     pen.left(120)
