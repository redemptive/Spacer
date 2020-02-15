import math

from SpriteObject import SpriteObject

class Player(SpriteObject):
    def __init__(self, x:int, y:int, width:int, height:int):
        SpriteObject.__init__(self, x, y, width, height, 
            {
                "player": "assets/player.png",
                "forward": "assets/forward_player.png",
                "backward": "assets/backward_player.png"
            }
        )
        self.max_forward_velocity:int = 20
        self.max_backward_velocity:int = 5
        self.orientation_velocity:float = 0
        self.max_orientation_velocity:float = 2
        self.y_velocity:float = 0
        self.current_sprite:str = "player"

    def update(self, keyboard:dict):
        if (keyboard["down"] == True) and (self.y_velocity > -(self.max_backward_velocity)):
            self.y_velocity = self.y_velocity - 0.1
            self.current_sprite = "backward"
        elif (keyboard["up"] == True) and (self.y_velocity < self.max_forward_velocity):
            self.y_velocity = self.y_velocity + 0.1
            self.current_sprite = "forward"
        elif (keyboard["down"] == False) and (keyboard["up"] == False):
            self.current_sprite = "player"

        if keyboard["down"] == True:
            self.current_sprite = "backward"
        
        if keyboard["up"] == True:
            self.current_sprite = "forward"

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
    
    def draw(self, display, camera_left:int, camera_top:int, sprite:str = ""):
        super().draw(display, camera_left, camera_top, self.current_sprite)