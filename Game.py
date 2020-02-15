import pygame
import random
import math

from GameObject import GameObject
from Circle import Circle
from SpriteObject import SpriteObject
from Player import Player
from BackgroundStar import BackgroundStar
from Planet import Planet

class Game():
    def __init__(self):
        self.title:str = "Spacer"
        self.window_width:int = 1500
        self.window_height:int = 1000
        self.map_height:int = 10000
        self.map_width:int = 10000
        self.running:bool = True
        self.fps:int = 60
        self.keyboard:dict = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        self.colours:dict = {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "blue": (0, 0, 255),
            "grey": (100, 100, 100)
        }

        pygame.init()
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.window_width, self.window_height))

        self.player:GameObject = GameObject(0, 0, 100, 100)

        # Initialise GameObjects
        self.game_objects:list = []

        # Create some stars
        for i in range(0, 300):
            self.game_objects.append(BackgroundStar(random.randint(0, self.map_width), random.randint(0, self.map_height), 4, self.colours["white"]))

        for i in range(0, 5):
            self.game_objects.append(Planet(random.randint(0, self.map_width), random.randint(0, self.map_height), random.randint(50, 2000), self.colours["blue"]))
            self.game_objects.append(Planet(2000, 2000, 50, self.colours["grey"]))

        self.player = Player(400, 400, 50, 50)

        self.loop()
    
    def loop(self):
        
        # main loop
        while self.running:
            self.check_events()

            self.display.fill((0, 0, 0))

            if self.player.x - (self.window_width / 2) < 0:
                camera_left = 0
            elif self.player.x + (self.window_width / 2) > self.map_width:
                camera_left = self.map_width - self.window_width
            else:
                camera_left = self.player.x - (self.window_width / 2)

            if self.player.y - (self.window_height / 2) < 0:
                camera_top = 0
            elif self.player.y + (self.window_height / 2) > self.map_height:
                camera_top = self.map_height - self.window_height
            else:
                camera_top = self.player.y - (self.window_height / 2)

            for game_object in self.game_objects:
                # if ((game_object.x < camera_left + self.window_width)
                # and (game_object.x + game_object.width > camera_left)
                # and (game_object.y < camera_top + self.window_height)
                # and (game_object.y + game_object.height > camera_top)):
                game_object.draw(self.display, camera_left, camera_top)

            self.player.update(self.keyboard)
            self.player.draw(self.display, camera_left, camera_top)

            pygame.display.update()
            self.clock.tick(self.fps)
        
        pygame.quit()
        quit()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                self.update_keyboard(event.key, True)
            
            if event.type == pygame.KEYUP:
                self.update_keyboard(event.key, False)

    def update_keyboard(self, key, active:bool):
        if key == pygame.K_UP:
            self.keyboard["up"] = active
        elif key == pygame.K_DOWN:
            self.keyboard["down"] = active
        elif key == pygame.K_RIGHT:
            self.keyboard["right"] = active
        elif key == pygame.K_LEFT:
            self.keyboard["left"] = active
     
if __name__=="__main__":
    game = Game()