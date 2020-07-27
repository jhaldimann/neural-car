import tkinter as tk
import time
import random as rd
import json

from lib.car import Car
from lib.line import Line
from lib.vector import Vector
from lib.polyline import Polyline
from lib.map import Map

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


def read_map(path):
    polylines = []
    with open(path) as json_file:
        json_data = json.load(json_file)
        for line in json_data['polylines'].split('\n'):
            if line == '':
                break
            pl = Polyline([])
            coords_str = line.split(sep=':')
            coords_n = []
            for c in coords_str:
                xy = c.split(sep=',')
                coords_n.append([int(xy[0]), int(xy[1])])

            for i in range(len(coords_n)-1):
                pl.add_line(Line(Vector(coords_n[i][0], coords_n[i][1]), Vector(coords_n[i+1][0], coords_n[i+1][1])))
            polylines.append(pl)

    return Map(Car(Vector(json_data['start'][0], json_data['start'][1])), polylines)


if __name__ == '__main__':
    setup()
    map = read_map('maps/map_name.json')
    map.car.set_num_rays(50)
    map.car.cast_rays(map.polylines)
    map.draw(canvas)

    while True:
        canvas.delete('all')
        map.car.move(Vector(rd.random() - rd.random(), rd.random() - rd.random()))
        map.car.cast_rays(map.polylines)
        map.draw(canvas)
        time.sleep(.5)
