import pygame
import random

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

class Player(GameObject):
    def __init__(self, x:int, y:int, width:int, height:int):
        GameObject.__init__(self, x, y, width, height)
        self.max_velocity:int = 10
        self.x_velocity:float = 0
        self.y_velocity:float = 0

    def update(self, keyboard:dict):
        if (keyboard["up"] == True) and (self.y_velocity > -(self.max_velocity)):
            self.y_velocity = self.y_velocity - 0.1
        if (keyboard["up"] == False) and (self.y_velocity < 0):
            self.y_velocity = self.y_velocity + 0.1

        if (keyboard["down"] == True) and (self.y_velocity < self.max_velocity):
            self.y_velocity = self.y_velocity + 0.1
        if (keyboard["down"] == False) and (self.y_velocity > 0):
            self.y_velocity = self.y_velocity - 0.1

        if (keyboard["right"] == True) and (self.x_velocity < self.max_velocity):
            self.x_velocity = self.x_velocity + 0.1
        if (keyboard["right"] == False) and (self.x_velocity > 0):
            self.x_velocity = self.x_velocity - 0.1

        if (keyboard["left"] == True) and (self.x_velocity > -(self.max_velocity)):
            self.x_velocity = self.x_velocity - 0.1
        if (keyboard["left"] == False) and (self.x_velocity < 0):
            self.x_velocity = self.x_velocity + 0.1
        
        if (self.x_velocity > 0) and (self.x_velocity < 0.1):
            self.x_velocity = 0

        self.move(self.x_velocity, self.y_velocity)

        print(self.x_velocity)

    def draw(self, display, camera_left:int, camera_top:int):
        pygame.draw.rect(display, (255, 255, 255), pygame.Rect(int(self.x - camera_left), int(self.y - camera_top), self.width, self.height))

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