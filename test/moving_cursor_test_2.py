import pyautogui
import time

def is_cursor_moving():
    previous_position = pyautogui.position()

    time.sleep(1)

    current_position = pyautogui.position()

    if previous_position == current_position:
        return False
    else:
        return True


while True:
    print(is_cursor_moving())
    # time.sleep(1)