# currencyIPO.py
# spring 2025
# prof. lehman
#
# currency converter demonstrates basic
# tkInter components using IPO model
# 
#

import tkinter as tk
from tkinter import messagebox


# function called by convert button
def calculate_pay():
    try:
        # get amount from text box
        rate = float(rate_entry.get())
        streams = int(streams_entry.get())
        
        print( rate, streams )
        
        total = rate * streams
        
        # set label for result
        result_label.config(text=f"{streams:,d} streams (rate: {rate:.2f}) = ${total:,.2f}")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# clear input aout output
def clear_data():
    rate_entry.delete(0, tk.END)
    streams_entry.delete(0, tk.END)
    
    rate_entry.insert(0,"0.003")
    streams_entry.insert(0,"1")
    
    result_label.config(text="Result will appear here.")

def show_rate():
    
    messagebox.showerror( usd_to_cad_rate )

# Fixed conversion rates
usd_to_cad_rate = 1.42
cad_to_usd_rate = 1 / usd_to_cad_rate



# Initialize the main window
root = tk.Tk()
root.title("Spotify Payout Calculator")
root.geometry("400x500")

# input for rate
rate_label = tk.Label(root, text="Rate:")
rate_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')

rate_entry = tk.Entry(root, width=30)
rate_entry.insert(0,"0.003")
rate_entry.grid(row=0, column=1, padx=10, pady=10)

# input for streams
streams_label = tk.Label(root, text="Streams:")
streams_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')

streams_entry = tk.Entry(root, width=30)
streams_entry.insert(0,"1")
streams_entry.grid(row=1, column=1, padx=10, pady=10)


# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_pay)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result will appear here.")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Menu
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear_data)
file_menu.add_command(label="Rate", command=show_rate)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Start the main loop
root.mainloop()
