from Circle import Circle

class Planet(Circle):
    def __init__(self, x:int, y:int, diameter:int, colour):
        Circle.__init__(self, x, y, diameter, colour)