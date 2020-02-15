class GameObject():
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x:int = x
        self.y:int = y
        self.width:int = width
        self.height:int = height

    def move(self, dX:int, dY:int):
        self.x = self.x + dX
        self.y = self.y + dY