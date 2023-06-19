from tkinter import Tk, BooleanVar, Checkbutton
from mouse_functions import get_cursor_position, get_current_second, set_cursor_to_position, is_cursor_moving


def jiggling_process():
    if is_on and not is_cursor_moving():
        current_x, current_y = get_cursor_position()
        set_cursor_to_position(current_x, current_y, get_current_second())
    window.after(800, jiggling_process)  


def toggle_checkbox():
    global is_on
    is_on = checkbox_var.get()
    # print("Button state:", "ON" if is_on else "OFF")


is_on = False

window = Tk()

window.title("Mouse jiggler")
window.geometry("400x100")
window.resizable(False, False)
window.iconbitmap("images\main_mouse_icon.ico")

button_font = ("Roboto", 12)
checkbox_var = BooleanVar()
checkbox = Checkbutton(window, text="Jiggle", font=button_font, variable=checkbox_var,
                          onvalue=True, offvalue=False, command=toggle_checkbox)

checkbox.grid(row=0, column=0, padx=10, pady=20)

jiggling_process()

window.mainloop()