import math

from lib.point import Point
from lib.line import Line

class Ray:
    def __init__(self, start, direction):
        self.start = start
        self.direction = direction.normalized()
        self.hit = None

    def cast(self, polylines):
        min_dist = float('inf')
        self.hit = None

        for pl in polylines:
            for line in pl.lines:
                x1 = line.start.x
                y1 = line.start.y
                x2 = line.end.x
                y2 = line.end.y

                x3 = self.start.x
                y3 = self.start.y
                x4 = self.direction.a * 1000
                y4 = self.direction.b * 1000

                den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

                t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
                u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den

                if 0 < t < 1 and u > 0:
                    point = Point(0, 0)
                    point.x = x1 + t * (x2 - x1)
                    point.y = y1 + t * (y2 - y1)

                    if self.hit is None:
                        self.hit = point
                    else:
                        dist = self.start.dist(point)
                        if dist < min_dist:
                            min_dist = dist
                            self.hit = point

        return self.hit

    def draw(self, canvas):
        end = Point(self.direction.a * 1000, self.direction.b * 1000)
        if self.hit is not None:
            end = Point(self.hit.x, self.hit.y)
        line = Line(self.start, end)
        line.set_color("#00FF00")
        line.draw(canvas)
