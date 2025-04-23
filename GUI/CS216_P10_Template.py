# CS216_P10_Template.py
#
# spring 2025
# prof. lehman
#
# template for final project

import tkinter as tk
from tkinter import Canvas

# function read CSV file, summarizes data, draws graph, writes summary to CSV
# called by File, Open
def process_data():
    
    # (1) read text or CSV file and (2) summarize data
    
    
    # (3) draw graph (sample code for pie graph shown)
    
    # sample data (update to use data from file (2)
    a = 20
    b = 30
    c = 15
    
    # totals needed for extent (ie. degrees to travel)
    total = a + b + c
    aExtent = a / total * 360
    bExtent = b / total * 360
    cExtent = c / total * 360
    
    # start points based on extents
    aStart = 270
    bStart = aStart + aExtent
    cStart = bStart + bExtent
    
    # draw pie slices using start and extent values
    canvas.create_arc(50, 50, 250, 250, start=aStart, extent=aExtent, fill="red")
    canvas.create_arc(50, 50, 250, 250, start=bStart, extent=bExtent, fill="blue")
    canvas.create_arc(50, 50, 250, 250, start=cStart, extent=cExtent, fill="green")
    

    # write summary to CSV file
    
    # end process data
    

# clear graph - called by File, New
def clear_graph():
    canvas.delete("all")
      
# exit program - called by File, Exit
def exit_program():
    main.destroy()

# main window setup
main = tk.Tk()
main.geometry('400x350')
main.title('P10 Project')

# create canvas
canvas = Canvas(main, width=300, height=300, bg='white')
canvas.pack()

# Create a menu bar
menu_bar = tk.Menu(main)

# Add "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=clear_graph)
file_menu.add_separator()
file_menu.add_command(label="Open", command=process_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)

# Set the menu bar
main.config(menu=menu_bar)

# wait for menu selections
main.mainloop()

