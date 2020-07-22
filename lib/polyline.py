class Polyline:

    def __init__(self, lines):
        self.lines = lines
        self.color = "#000"

    def set_color(self, color):
        self.color = color

    def draw(self, canvas):
        for line in self.lines:
            canvas.create_line(line.start.x, line.start.y, line.end.x, line.end.y, fill=self.color)
