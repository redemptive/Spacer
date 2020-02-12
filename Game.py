import pygame
import random
import math

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
        for i in range(0, 200):
            self.game_objects.append(Circle(random.randint(0, self.map_width), random.randint(0, self.map_height), 2, self.colours["white"]))


        self.game_objects.append(Planet(100, 1000, 2000, self.colours["blue"]))
        self.game_objects.append(Planet(2000, 2000, 100, self.colours["grey"]))

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

class GameObject():
    def __init__(self, x:int, y:int, width:int, height:int):
        self.x:int = x
        self.y:int = y
        self.width:int = width
        self.height:int = height

    def move(self, dX:int, dY:int):
        self.x = self.x + dX
        self.y = self.y + dY

class SpriteObject(GameObject):
    def __init__(self, x:int, y:int, width:int, height:int, sprite_path:str):
        GameObject.__init__(self, x, y, width, height)
        self.sprite = pygame.transform.scale(pygame.image.load(sprite_path), (width, height))
        self.orientation:int = 0

    def change_orientation(self, d_degrees):
        if (self.orientation + d_degrees > 360):
            self.orientation = (self.orientation + 360) + d_degrees
        if (self.orientation + d_degrees < 0):
            self.orientation = (self.orientation - 360) + d_degrees
        else:
            self.orientation = self.orientation + d_degrees

    def draw(self, display, camera_left:int, camera_top:int):
        rotated_sprite = pygame.transform.rotate(self.sprite, self.orientation)
        display.blit(rotated_sprite, (int(self.x - camera_left), int(self.y - camera_top)))

class Player(SpriteObject):
    def __init__(self, x:int, y:int, width:int, height:int):
        SpriteObject.__init__(self, x, y, width, height, "assets/player.png")
        self.max_forward_velocity:int = 20
        self.max_backward_velocity:int = 5
        self.orientation_velocity:float = 0
        self.max_orientation_velocity:float = 5
        self.y_velocity:float = 0

    def update(self, keyboard:dict):
        if (keyboard["down"] == True) and (self.y_velocity > -(self.max_backward_velocity)):
            self.y_velocity = self.y_velocity - 0.1

        if (keyboard["up"] == True) and (self.y_velocity < self.max_forward_velocity):
            self.y_velocity = self.y_velocity + 0.1

        if (keyboard["right"] == True) and (self.orientation_velocity < self.max_orientation_velocity):
            self.orientation_velocity += 0.05

        if (keyboard["left"] == True) and (self.orientation_velocity > -(self.max_orientation_velocity)):
            self.orientation_velocity -= 0.05
        
        if (self.orientation_velocity > 0) and (self.orientation_velocity < 0.05):
            self.orientation_velocity = 0

        self.change_orientation(-self.orientation_velocity)
        self.move_at_orientation()

    def move_at_orientation(self):
        self.move(-(self.y_velocity*math.cos(math.radians(self.orientation))), (self.y_velocity*math.sin(math.radians(self.orientation))))


class Circle(GameObject):
    def __init__(self, x:int, y:int, diameter:int, colour):
        GameObject.__init__(self, x, y, diameter, diameter)
        self.colour = colour
    
    def draw(self, display, camera_left:int, camera_top:int):
        pygame.draw.circle(display, self.colour, (int(self.x - camera_left), int(self.y - camera_top)), int(self.height / 2), 0)

class Planet(Circle):
    def __init__(self, x:int, y:int, diameter:int, colour):
        Circle.__init__(self, x, y, diameter, colour)
        
     
if __name__=="__main__":
    game = Game()