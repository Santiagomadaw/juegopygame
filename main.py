import pygame, sys
class Game():
    
    width = 640
    heigth = 480
    runners = []
    __startLine = 20
    __finishLine = width -20
    def __init__(self):  
        self.__screen = pygame.display.set_mode((640, 480))
        self.__screen.fill((255,151,44))
        pygame.display.set_caption("Carrera de cosos")

    def run(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver=True
            pygame.display.flip()
        pygame.quit()
        sys.exit()
            
if __name__ == '__main__':
    game = Game()  
    pygame.init()
    game.run()