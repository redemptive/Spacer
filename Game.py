import pygame

from GameObject import GameObject

class Game():
    def __init__(self):
        self.title:str = "Spacer"
        self.width:int = 500
        self.height:int = 500
        self.running:bool = True
        self.fps:int = 60

        pygame.init()
        pygame.display.set_caption(self.title)

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.width, self.height))

        self.player = GameObject.GameObject(0,0,100,100)

        self.loop()
    
    def loop(self):
        
        # main loop
        while self.running:
            self.check_events()        
            pygame.display.update()
            self.clock.tick(self.fps)
        
        pygame.quit()
        quit()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

     
if __name__=="__main__":
    game = Game()