from  datetime import datetime
from pyautogui import moveTo, position
from time import sleep, time


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




