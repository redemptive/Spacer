# import the pygame module, so you can use it
import pygame

class Game():
    def __init__(self):
        self.width:int = 500
        self.height:int = 500

        self.running:bool = True
        pygame.display.set_caption("minimal program")

        # create a surface on screen that has the size of 240 x 180
        screen = pygame.display.set_mode((self.width, self.height))

        self.loop()
    
    def loop(self):
        
        # main loop
        while self.running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self.running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    game = Game()