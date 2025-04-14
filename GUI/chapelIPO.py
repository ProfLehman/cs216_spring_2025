# chapelPercent.py
# spring 2025
# prof. lehman
#
# chapel tracker calculates % remaining to reach 30
# using tkInter input, processing, output model
#

import tkinter as tk
from tkinter import messagebox

# function called by Calculate button
def calculate_percentage():
    try:
        attended = int(attended_entry.get())
        remaining = int(remaining_entry.get())

        percent = (30 - attended) / remaining * 100

        if percent > 100.00:
            x = 30 - attended - remaining
            result_label.config(text=f"Ope, you will be short {x} chapels")  
        else:        
            result_label.config(text=f"{percent:.1f}% of the remaining required chapels are still needed.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid whole numbers.")

# clear input and output
def clear_data():
    attended_entry.delete(0, tk.END)
    remaining_entry.delete(0, tk.END)
    attended_entry.insert(0, "0")
    remaining_entry.insert(0, "0")
    result_label.config(text="Result will appear here.")

# Initialize the main window
root = tk.Tk()
root.title("Chapel Attendance Tracker")
root.geometry("400x400")

# input for attended
attended_label = tk.Label(root, text="Chapels Attended:")
attended_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

attended_entry = tk.Entry(root, width=30)
attended_entry.insert(0, "0")
attended_entry.grid(row=0, column=1, padx=10, pady=10)

# input for remaining
remaining_label = tk.Label(root, text="Chapels Remaining:")
remaining_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

remaining_entry = tk.Entry(root, width=30)
remaining_entry.insert(0, "0")
remaining_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_percentage)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result will appear here.")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Menu
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Start the main loop
root.mainloop()
