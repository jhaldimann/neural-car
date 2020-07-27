import tkinter as tk
import json

WIDTH = 500
HEIGHT = 500
window = tk.Tk()
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack(expand=1, fill=tk.BOTH)

coords = []
json_data = {}
json_data['polylines'] = ""
json_data['start'] = [0, 0]

mouse_pos = [0, 0]

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


def draw_line(event):
    coords.append([event.x, event.y])
    l = len(coords)
    if l > 1:
        canvas.create_line(coords[l-2][0], coords[l-2][1], coords[l-1][0], coords[l-1][1])


def keypress(event):
    global json_data

    if event.char == 's':
        json_data['start'] = [mouse_pos[0], mouse_pos[1]]
        canvas.create_oval(mouse_pos[0]-5, mouse_pos[1]-5, mouse_pos[0]+5, mouse_pos[1]+5, fill='#00FF00')
    elif event.char == ' ':
        with open('maps/map_name.json', 'w') as outfile:
            json.dump(json_data, outfile)


def mouse_moved(event):
    global mouse_pos

    mouse_pos = [event.x, event.y]

def save_line(event):
    global coords
    global json_data

    first = True
    for c in coords:
        if first:
            json_data['polylines'] += f"{c[0]},{c[1]}"
            first = False
        else:
            json_data['polylines'] += f":{c[0]},{c[1]}"
    json_data['polylines'] += "\n"
    coords = []


setup()
window.bind('<Motion>', mouse_moved)
window.bind('<Button-1>', draw_line)
window.bind('<Button-2>', save_line)
window.bind('<Button-3>', save_line)
window.bind('<Key>', keypress)
window.mainloop()