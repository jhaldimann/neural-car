import math


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def normalized(self):
        length = math.sqrt(self.a*self.a + self.b*self.b)
        return Vector(self.a/length, self.b/length)
