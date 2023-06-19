import tkinter as tk

def toggle_button():
    global is_on
    is_on = checkbox_var.get()
    print("Button state:", "ON" if is_on else "OFF")

# Create the main Tkinter window
window = tk.Tk()
window.title("Toggle Button Example")

# Set custom styles
button_font = ("Arial", 16, "bold")

# Create a variable to store the button state
is_on = False

# Create a checkbox variable
checkbox_var = tk.BooleanVar()

# Create the checkbox
checkbox = tk.Checkbutton(window, text="Toggle", font=button_font, variable=checkbox_var,
                          onvalue=True, offvalue=False, command=toggle_button)

# Position the checkbox using grid layout
checkbox.grid(row=0, column=0, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
