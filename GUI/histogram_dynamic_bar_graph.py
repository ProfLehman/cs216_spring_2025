# histogram_dynamic_bar_graph.py
#
# spring 2025
# prof. lehman
#
# in-class demo for dynamic bar graph
#
# set data values for a, b, and c and bar graph will scale
#

import tkinter as tk
from tkinter import Canvas, Frame, BOTH

class HistogramViewer(tk.Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('Histogram Viewer')
        self.pack(fill=BOTH, expand=1)

        
        canvas = Canvas(self)
        
        # get largest value  
        largest = max(a,b,c)
        print( largest )
        
        # scale data values, the larges will be 100% of 370
        a_width = a / largest * 370
        b_width = b / largest * 370
        c_width = c / largest * 370
  
        # draw bars with scaled width
        
        #A
        canvas.create_rectangle(10, 10, 10 + a_width, 60, outline='black', fill='red')
        
        #B
        canvas.create_rectangle(10, 75, 10 + b_width, 125, outline='black', fill='blue')
        
        #C
        canvas.create_rectangle(10, 140, 10 + c_width, 190, outline='black', fill='green')
           
                    
        canvas.pack(fill=BOTH, expand=1)
        self.pack()

# get data values for a, b, and c
a =  int( input("Enter data a: ") )
b =  int( input("Enter data b: ") )
c =  int( input("Enter data c: ") )

app_frame = tk.Tk()
app_frame.geometry('400x250')
histogram_viewer = HistogramViewer(master=app_frame)
histogram_viewer.mainloop()