import graphics as gr

class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def list(self):
        return [self.x, self.y, self.z]
    
    def drawYZ(self):
        gr.Point(y, z)

    def drawXZ(self):
        gr.Point(x, z)

    def drawXY(self):
        gr.Point(x, y)

class Sphere:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

