from turtle import *
import math

# make a turtle pen and setup its features
pen = Pen()
pen.color("blue")
pen.speed(0)
pen.width(3)


# make a screen and setup the bg
screen = Screen()
screen.bgcolor("red")

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

#end


# quadratic tree
def d(n,l):
     # termination
     if n ==0 or l<2:
          return
     #endif
     pen.forward(l)
     pen.left(90)
     d(n-1, l/2)
     pen.right(60)
     d(n-1, l/2)
     pen.right(60)
     d(n-1, l/2)
     pen.right(60)
     d(n-1, l/2)
     pen.left(90)
     pen.backward(l)
#end d
     
#fern
def f(n,l):
# termination
     if n ==0 or l<2:
          return
     #endif
     pen.forward(0.3*l)
     pen.right(45);f(n-1,l/2);pen.left(45)
     pen.forward(0.7*l)
     pen.left(30);f(n-1,l/2);pen.right(30)
     pen.forward(l)
     pen.right(10);f(n-1,0.8*l);pen.left(10)
     pen.backward(2*l)

     #end
def koch(n,l):
     if n ==0 or l<2:
          pen.forward(l)
          return
     #endif
     koch(n-1,l/3)
     pen.left(60);koch(n-1,l/3)
     pen.right(120);koch(n-1,l/3)
     pen.left(60);koch(n-1,l/3)


#end k
def flake(n,l):
     for i in range(3):
          koch(n,l)
          pen.right(120)
     #endflake



def gasket3(n,l):
     #termination
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          #end for
          return
     #end if
     gasket3(n-1,l/2);pen.forward(l);pen.left(120)
     gasket3(n-1,l/2);pen.forward(l);pen.left(120)
     gasket3(n-1,l/2);pen.forward(l);pen.left(120)
#end gasket3

 


