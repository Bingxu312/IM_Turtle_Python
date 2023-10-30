# import tkinter
from tkinter import *
from tkinter.ttk import *
import turtleFigures
from turtle import TurtleScreen, RawTurtle


# make the window
root = Tk()
root.title("Turtle Convertor")
root.geometry("800x800+100+100")

# make the interface
titleLabel = Label(root, text = "Turtle Generator")
titleLabel.grid(row = 0, column = 1, columnspan = 2)

# make the canvas
canvasFrame = LabelFrame(root, text = "Canvas New")
canvasFrame.grid(row = 1, column = 0, columnspan = 5, rowspan = 5)
canvas = Canvas(canvasFrame, width = 500, height = 500)
canvas.pack()

# link TurtleScreen with Canvas
screen = TurtleScreen(canvas)
screen.bgcolor("black")
w, h = screen.screensize()

# make a turtle pen connected with the screen
pen = RawTurtle(screen)
pen.color("white")
pen.speed(0)
pen.width(3)

# make the control panel
controlFrame = LabelFrame(root, text="Control Panel")
controlFrame.grid(row=6, column=0, columnspan=5, rowspan=3)

orderLabel = Label(controlFrame, text="Order")
orderLabel.grid(row=1, column=0)

orderStr = StringVar()
orderEntry = Entry(controlFrame, textvariable=orderStr)
orderEntry.grid(row=1, column=1, columnspan=2)

lengthLabel = Label(controlFrame, text="Length")
lengthLabel.grid(row=2, column=0)

lengthStr = StringVar()
lengthEntry = Entry(controlFrame, textvariable=lengthStr)
lengthEntry.grid(row=2, column=1, columnspan=2)

angleLabel = Label(controlFrame, text="Angle")
angleLabel.grid(row=3, column=0)

angleStr = StringVar()
angleEntry = Entry(controlFrame, textvariable=angleStr)
angleEntry.grid(row=3, column=1, columnspan=2)

figureNames = ["Binary Tree", "Dandelion", "Fern"]
figureStr = StringVar()
figureList = OptionMenu(controlFrame, figureStr, figureNames[0], *figureNames)
figureList.grid(row=4,column=0)

def clearF():
    # clear the entries
    orderStr.set("")
    lengthStr.set("")


clearButton = Button(controlFrame, text = "clear", command = clearF)
clearButton.grid(row = 5, column = 0, columnspan = 2)

def drawF():
    # get the convert order , length and angle values
    order  = int(orderEntry.get())
    length = int(lengthEntry.get())
    angle = int(angleEntry.get())
    # get the selection from option menu
    figureIndex = figureNames.index(figureStr.get())
    # use the figureIndex to call the selected turtle method
    if figureIndex == 0:
        pen.up(); pen.backward(w / 2); pen.down()
        turtleFigures.tree(order, length)
    elif figureIndex == 1:
        pen.up(); pen.backward(w / 2); pen.down()
        turtleFigures.gasket(order, length)
    else:
        pen.up(); pen.backward(w / 2); pen.down()
        turtleFigures.gasket(order, length)

    # and ect


drawButton = Button(controlFrame, text = "Draw", command = drawF)
drawButton.grid(row = 5, column = 2, columnspan = 2)

#loop it
root.mainloop()