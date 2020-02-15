import pygame

from GameObject import GameObject

class SpriteObject(GameObject):
    def __init__(self, x:int, y:int, width:int, height:int, sprite_paths:list):
        GameObject.__init__(self, x, y, width, height)
        self.sprites:dict = {}

        for sprite in sprite_paths:
            self.sprites[sprite] = pygame.transform.scale(pygame.image.load(sprite_paths[sprite]), (width, height))
        
        self.orientation:int = 0

    def change_orientation(self, d_degrees):
        if (self.orientation + d_degrees > 360):
            self.orientation = (self.orientation + 360) + d_degrees
        if (self.orientation + d_degrees < 0):
            self.orientation = (self.orientation - 360) + d_degrees
        else:
            self.orientation = self.orientation + d_degrees

    def draw(self, display, camera_left:int, camera_top:int, sprite:str = ""):
        if sprite == "":
            sprite = next(iter(self.sprites))
        rotated_sprite = pygame.transform.rotate(self.sprites[sprite], self.orientation)
        display.blit(rotated_sprite, (int(self.x - camera_left), int(self.y - camera_top)))