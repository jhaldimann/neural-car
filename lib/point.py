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

    def draw(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x + self.r, self.y + self.r, fill=self.color)
