import math
from lib.point import Point
from lib.vector import Vector
from lib.ray import Ray

class Car:
    def __init__(self, position):
        self.position = Point(position.x, position.y)
        self.speed = 20
        self.num_rays = 10
        self.rays = []

    def set_num_rays(self, amount):
        self.num_rays = amount

    def move(self, direction):
        direction = direction.normalized()
        self.position.x += direction.a * self.speed
        self.position.y += direction.b * self.speed

    def cast_rays(self, polylines):
        angle = 2 * math.pi / self.num_rays
        direction = Vector(0, -1)
        for i in range(self.num_rays - 1):
            x = direction.a * math.cos(angle) - direction.b * math.sin(angle)
            y = direction.a * math.sin(angle) + direction.b * math.cos(angle)
            direction = Vector(x, y)
            ray = Ray(self.position, direction)
            self.rays.append(ray)
            ray.cast(polylines)

    def draw(self, canvas):
        self.position.set_radius(5)
        self.position.set_color("#FF0000")
        self.position.draw(canvas)
        for ray in self.rays:
            ray.draw(canvas)
        canvas.update_idletasks()
        canvas.update()


