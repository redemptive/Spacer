import random

from Circle import Circle

class BackgroundStar(Circle):
    def __init__(self, x:int, y:int, diameter:int, colour):
        Circle.__init__(self, x, y, diameter, colour)
        self.max_ticks:int = 100
        self.ticks:int = random.randint(0, self.max_ticks)
        self.d_luminosity:int = 2
        self.positive_twinkle:bool = True
    
    def draw(self, display, camera_left:int, camera_top:int):

        # This makes the background stars slightly fade in and out
        # It looks like they are twinkling
        if self.ticks > self.max_ticks:
            self.ticks = 0
            self.positive_twinkle = not self.positive_twinkle
        else:
            self.ticks += 1

        colour_list = list(self.colour)

        if self.positive_twinkle and (colour_list[0] < 255):
            colour_list[0] += self.d_luminosity
            colour_list[1] += self.d_luminosity
            colour_list[2] += self.d_luminosity
        elif colour_list[0] > 1:
            colour_list[0] -= self.d_luminosity
            colour_list[1] -= self.d_luminosity
            colour_list[2] -= self.d_luminosity

        self.colour = tuple(colour_list)

        super().draw(display, camera_left, camera_top)