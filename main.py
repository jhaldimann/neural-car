import tkinter as tk

WIDTH = 500
HEIGHT = 500
window = tk.Tk()


def setup():
    global window
    window.title('The game')
    window.geometry(f"{WIDTH}x{HEIGHT}")

    window_width = WIDTH
    window_height = HEIGHT

    pos_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
    pos_down = int(window.winfo_screenheight() / 2 - window_height / 2)

    window.geometry("+{}+{}".format(pos_right, pos_down))
    window.resizable(0, 0)
    window.mainloop()


if __name__ == '__main__':
    setup()
