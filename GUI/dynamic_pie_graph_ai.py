#
# dynamic_pie_graph_ai.py
# Prof. Lehman
#
# In-class demonstration
# AI generate pie graph creation using uploaded image of interface
# spring 2025 chatGPT 4o model
#
# prompt
# Create a python gui using tkinter based on the attached image.
# Use tkinger graphics commands to create the pie graph using
# int values from the text entry boxes.
# Graph should be created when calculate is pressed.
#
# note: labels need to be fixed
#       spacing needs work
#
#

import tkinter as tk

def draw_pie():
    canvas.delete("all")
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        total = a + b + c

        if total == 0:
            return

        x0, y0, x1, y1 = 50, 50, 350, 350
        angle_a = (a / total) * 360
        angle_b = (b / total) * 360
        angle_c = 360 - angle_a - angle_b

        canvas.create_arc(x0, y0, x1, y1, start=0, extent=angle_a, fill="red")
        canvas.create_arc(x0, y0, x1, y1, start=angle_a, extent=angle_b, fill="blue")
        canvas.create_arc(x0, y0, x1, y1, start=angle_a + angle_b, extent=angle_c, fill="green")

        # Label positions can be tweaked for better alignment
        canvas.create_text(200, 110, text="A", font=("Arial", 14, "bold"))
        canvas.create_text(270, 260, text="B", font=("Arial", 14, "bold"))
        canvas.create_text(130, 260, text="C", font=("Arial", 14, "bold"))

    except ValueError:
        canvas.create_text(200, 200, text="Please enter integers", fill="red", font=("Arial", 16))

# GUI setup
root = tk.Tk()
root.title("Pie Chart Grapher")

tk.Label(root, text="Data A").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=0)

tk.Label(root, text="Data B").grid(row=2, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=3, column=0)

tk.Label(root, text="Data C").grid(row=4, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=5, column=0)

tk.Button(root, text="Calculate", command=draw_pie).grid(row=6, column=0, pady=10)

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.grid(row=0, column=1, rowspan=7, padx=10)

root.mainloop()
