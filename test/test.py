import pyautogui
import time, math
from time import sleep

start_time = time.time()
end_time = start_time + 10  # 10 seconds



while time.time() < end_time:
    curr_second = math.ceil(end_time - time.time())
    print(curr_second)
    position = pyautogui.position()
    x, y = position[0], position[1]
    pyautogui.moveTo(x, y, duration=0) if curr_second%2 == 0 else pyautogui.moveTo(x+2, y+2, duration=0)
    sleep(1)


