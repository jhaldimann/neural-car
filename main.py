import tkinter as tk
import time

from lib.car import Car
from lib.point import Point
from lib.vector import Vector

WIDTH = 500
HEIGHT = 500
window = tk.Tk()
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack(expand=1, fill=tk.BOTH)


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
    window.update_idletasks()
    window.update()


if __name__ == '__main__':
    setup()
