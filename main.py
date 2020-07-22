import tkinter as tk
import time

from lib.car import Car
from lib.point import Point
from lib.line import Line
from lib.vector import Vector
from lib.polyline import Polyline
from lib.ray import Ray

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
    polyline1 = Polyline([Line(Point(0, 0), Point(500, 500))])
    polyline1.draw(canvas)
    polyline2 = Polyline([Line(Point(250, 0), Point(250, 500))])
    polyline2.draw(canvas)
    car = Car(Point(100, 250))
    car.set_num_rays(30)
    car.cast_rays([polyline1, polyline2])
    car.draw(canvas)
    window.mainloop()
