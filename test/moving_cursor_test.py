from pynput.mouse import Listener, Controller
import threading
from time import sleep

# Global variable to track cursor movement
is_cursor_moving = False

# Callback function for cursor movement
def on_move(x, y):
    global is_cursor_moving
    is_cursor_moving = True

# Start listening for cursor movements
def start_cursor_listener():
    with Listener(on_move=on_move) as listener:
        listener.join()

# Function to check if cursor is moving
def a():
    return is_cursor_moving

while True:
    cursor_listener_thread = threading.Thread(target=start_cursor_listener)
    cursor_listener_thread.daemon = True
    cursor_listener_thread.start()
    moving = a()
    print(moving)  # Output: True or False
    sleep(1)
