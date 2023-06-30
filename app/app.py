from  datetime import datetime
from pyautogui import moveTo, position
from time import sleep
from tkinter import Tk, BooleanVar, Checkbutton

SLEEP_TIME = 0.1

def is_cursor_moving():
    previous_position = position()
    sleep(SLEEP_TIME)
    current_position = position()
    return False if previous_position == current_position else True


def get_cursor_position():
    position_corrs = position()
    return position_corrs[0], position_corrs[1]


def set_cursor_to_position(x, y, current_second):
    # print('Current second:', current_second)
    moveTo(x-2, y-2, duration=0.01) if current_second % 2 == 0 else moveTo(x+2, y+2, duration=0)


def get_current_second():
    current_time = datetime.now()
    return current_time.second


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