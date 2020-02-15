import pygame

from GameObject import GameObject

class Circle(GameObject):
    def __init__(self, x:int, y:int, diameter:int, colour):
        GameObject.__init__(self, x, y, diameter, diameter)
        self.colour = colour
    
    def draw(self, display, camera_left:int, camera_top:int):
        pygame.draw.circle(display, self.colour, (int(self.x - camera_left), int(self.y - camera_top)), int(self.height / 2), 0)