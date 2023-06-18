import tkinter as tk

window = tk.Tk()

window.title("Mouse jiggler")
window.geometry("400x100")
window.resizable(False, False)
window.iconbitmap("images\main_mouse_icon.ico")

# start_time = time()
# end_time = start_time + 10  # 10 seconds
window.mainloop()