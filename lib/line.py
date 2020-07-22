class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.color = "#fff"

    def set_color(self, color):
        self.color = color

    def draw(self, canvas):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=self.color)
        canvas.update_idletasks()
        canvas.update()



