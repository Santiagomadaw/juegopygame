import pygame, sys, random
class bola():
    def __init__(self, x=0, y=0):
        self.sprite =pygame.image.load('./images/boladedragon.png')
        self.position = [x, y]
    def relocation(self):
        self.position[0] += random.randint(-1,1)
        self.position[1] += random.randint(-1,1)
class fondo():
    def __init__(self, x=0):
        self.sprite =pygame.image.load('./images/pista.png')
        self.position = [x, 0]
        self.startposition = [x, 0]
    def move(self):
        if self.startposition[0] - self.position[0] >= 1199:
            self.position[0] = self.startposition[0]
            print('una vuelta')
        self.position[0] -=12
        
class Runner():
    
    
    def __init__(self, spriteName, x=0, y=0):
      
        self.sprite =pygame.image.load('./images/{}'.format(spriteName))
        self.position = [x, y]
        self.name = "runner"
        
    def avanza(self, x, y):
        
        try:
            self.position[0] += random.randint(-1, 2)*(x-self.position[0])/abs((x-self.position[0]))
            self.position[1] += random.randint(0, 2)*(y-self.position[1])/abs((x-self.position[0]))
        except:
            pass
        print('la bola esta en {} - {} y {} va hacia {} - {}'.format(x, y, self.name, self.position[0],self.position[1]))
class Game():
    
    width = 1200
    heigth = 300
    runners = []
    __startLine = 40
    __finishLine = width -60
    __names = ['Goku', 'Yancha', 'Ten Sian', 'Picolo']
    __posY = [heigth/8,heigth/8 + heigth/4,heigth/8 + heigth/2,heigth/16 + 3*heigth/4 ]
    __sprites = ['sprite1.png', 'sprite2.png', 'sprite3.png', 'sprite4.png']
    ball = bola(__finishLine-200, 150)
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1200, 300))
        self.__bg = fondo()
        self.__bg1 = fondo(1199)
        
        

        pygame.display.set_caption("Pilla la bola")
        for runner in self.__posY:
            indice = self.__posY.index(runner)
         
            loadedRunner = Runner(self.__sprites[indice],self.__startLine, runner)
            loadedRunner.name =self.__names[indice]
            self.runners.append(loadedRunner)
         
        

    def run(self):
        
        gameOver = False
        while not gameOver:
            #gestion de eventos
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    gameOver=True
            
                
            for activerunner in self.runners:
            
                
            
                #print ('{} ESTA EN  {}/{} de {}'.format(activerunner.name,activerunner.position[0],activerunner.position[1], self.__finishLine))        
                if activerunner.position == self.ball.position:
                    print ('{} ha atrapado la bola de dragon'.format(activerunner.name))
                    gameOver=True
                activerunner.avanza(self.ball.position[0],self.ball.position[1])   
            self.__bg.move()
            self.__bg1.move()
            self.ball.relocation()    
            
            #Refresco de pantalla
            
            self.__screen.blit(self.__bg.sprite,self.__bg.position)
            self.__screen.blit(self.__bg1.sprite,self.__bg1.position)
        
            self.__screen.blit(self.ball.sprite,self.ball.position)
            for activeRunner in self.runners:

                self.__screen.blit(activeRunner.sprite,activeRunner.position)
            
            pygame.display.flip()

        while True:
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    pygame.quit()
                

if __name__ == '__main__':
    game = Game()  
    pygame.init()
    game.run()