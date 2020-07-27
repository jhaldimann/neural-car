from lib.vector import Vector

class Map:
    def __init__(self, car, polylines):
        self.car = car
        self.polylines = polylines
        self.start = Vector(car.position.x, car.position.y)
        self.start.set_color("#00FF99")
        self.start.set_radius(5)

    def draw(self, canvas):
        self.start.draw(canvas)
        for pl in self.polylines:
            pl.draw(canvas)
        self.car.draw(canvas)
