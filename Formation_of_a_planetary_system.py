import graphics as gr

class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def list(self):
        return [self.x, self.y, self.z]