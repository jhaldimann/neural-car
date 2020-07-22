from lib.point import Point


class Car:
    def __init__(self, position):
        self.position = Point(position.x, position.y)
        self.speed = 20

    def move(self, direction):
        direction = direction.normalized()
        self.position.x += direction.a * self.speed
        self.position.y += direction.b * self.speed

    def draw(self, canvas):
        self.position.set_radius(5)
        self.position.set_color("#FF0000")
        self.position.draw(canvas)
        canvas.update_idletasks()
        canvas.update()


