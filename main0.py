import pygame
import sys

class Game():
    corredores = []

    def __init__(self):

        self.__screen = pygame.display.set_mode((1200, 300))
        pygame.display.set_caption("Carrera de mocos")
        self.background = pygame.image.load("./images/pista.png")
        self.runner = pygame.image.load("./images/smallball.png")

    def competicion(self):
        ganador = False
        x = 0
        while not ganador:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    ganador = True

            self.__screen.blit(self.background,(0,0))
            self.__screen.blit(self.runner, (x, 150))
            pygame.display.flip()
            x += 1
            if x>=1100:
                ganador = True
        print('finish')

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competicion()
