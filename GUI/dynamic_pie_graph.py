# dynamic_pie_graph.py
#
# spring 2025
# prof. lehman
#
# in-class demo for dynamic pie graph
#
# set data values for a, b, c, and d and bar graph will scale
#
# note: format fixed for final project

import tkinter as tk
from tkinter import Canvas

def draw_pie(canvas, a, b, c, d):
    
    # totals needed for extent (ie. degrees to travel)
    total = a + b + c + d
    aExtent = a / total * 360
    bExtent = b / total * 360
    cExtent = c / total * 360
    dExtent = d / total * 360

    # start points based on extents
    aStart = 270
    bStart = aStart + aExtent
    cStart = bStart + bExtent
    dStart = cStart + cExtent

    # draw pie slices using start and extent values
    canvas.create_arc(50, 50, 250, 250, start=aStart, extent=aExtent, fill="red")
    canvas.create_arc(50, 50, 250, 250, start=bStart, extent=bExtent, fill="blue")
    canvas.create_arc(50, 50, 250, 250, start=cStart, extent=cExtent, fill="green")
    canvas.create_arc(50, 50, 250, 250, start=dStart, extent=dExtent, fill="yellow")


# main window setup
main = tk.Tk()
main.geometry('400x350')
main.title('Pie Graph - In Class')

# create canvas
canvas = Canvas(main, width=300, height=300, bg='white')
canvas.pack()

# get values from user
a = int(input("Enter data a: "))
b = int(input("Enter data b: "))
c = int(input("Enter data c: "))
d = int(input("Enter data d: "))

# draw the pie chart
draw_pie(canvas, a, b, c, d)

main.mainloop()
