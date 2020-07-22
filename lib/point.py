import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 2
        self.color = "#000"

    def set_radius(self, r):
        self.r = r

    def set_color(self, color):
        self.color = color

    def dist(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x + self.r, self.y + self.r, fill=self.color)
        canvas.update_idletasks()
        canvas.update()
