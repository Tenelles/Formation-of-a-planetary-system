import graphics as gr

class Vector3:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def list(self):
        return [self.x, self.y, self.z]
    
    def projectionYZ(self):
        return gr.Point(self.y, self.z)

    def projectionXZ(self):
        return gr.Point(self.x, self.z)

    def projectionXY(self):
        return gr.Point(self.x, self.y)

class Sphere:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def projectionYZ(self):
        return gr.Circle(self.center.projectionYZ(), self.radius)
        
    def projectionXZ(self):
        return gr.Circle(self.center.projectionXZ(), self.radius)
        
    def projectionXY(self):
        return gr.Circle(self.center.projectionXY(), self.radius)

