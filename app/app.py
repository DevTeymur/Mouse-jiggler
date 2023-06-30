from pyautogui import moveTo, position
from time import sleep
from tkinter import Tk, BooleanVar, Checkbutton, Scale, Label

SLEEP_TIME = 0.1
in_start_pos = True
is_on = False
scale_value = 2

def is_cursor_moving():
    previous_position = position()
    sleep(SLEEP_TIME)
    current_position = position()
    return False if previous_position == current_position else True

def get_cursor_position():
    position_corrs = position()
    return position_corrs[0], position_corrs[1]

def set_cursor_to_position(x, y):
    global in_start_pos
    if in_start_pos:
        moveTo(x-2, y-2, duration=0.01)
        in_start_pos = False
    else:
        moveTo(x+2, y+2, duration=0.01)
        in_start_pos = True

def jiggling_process():
    if is_on and not is_cursor_moving():
        current_x, current_y = get_cursor_position()
        # print(f'Current positions: ({current_x}, {current_y})')
        set_cursor_to_position(current_x, current_y)
    window.after(int(scale_value)*1000, jiggling_process)  

def toggle_checkbox():
    global is_on
    is_on = checkbox_var.get()
    # print("Button state:", "ON" if is_on else "OFF")

def scale_changed(value):
    global scale_value
    scale_value = value
    # print("Scale value:", scale_value)


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

scale_label = Label(window, text="Duration", font=("Roboto", 12))
scale_label.grid(row=0, column=3, padx=10)

scale = Scale(window, from_=1, to=10, orient="horizontal", command=scale_changed)
scale.grid(row=0, column=5, padx=10, pady=20)

jiggling_process()

window.mainloop()