import pygame, sys, random
from pygame.locals import *
class Frezzer():
    def __init__(self, x=0, y=0):
        self.sprite =pygame.image.load('./images/sprite5.png')
        self.position = [x, y]
        self.iniDir = 0
    def flipLateral(self):
        
        self.sprite = pygame.transform.flip(self.sprite, True, False) 
    
    def move(self, direc):
        if self.iniDir == 0 and direc == 1:
            self.flipLateral()
            self.iniDir = 1
            
        if self.iniDir == 1 and direc == 0:
            self.flipLateral()
            self.iniDir = 0
        keys = pygame.key.get_pressed()
        if keys[K_w]:
                self.position[1] -= 4
        if keys[K_s]:
            self.position[1] += 4
        if keys[K_a]:
            self.position[0] -= 4
        if keys[K_d]:
            self.position[0] += 4
        
class fondo():
    def __init__(self, x=0):
        self.sprite =pygame.image.load('./images/pista.png')
        self.position = [x, 0]
        self.startposition = [x, 0]
    def move(self,dir):
        
        if self.startposition[0] - self.position[0] >= 1199 and dir == 0:
            self.position[0] = self.startposition[0]
           
        if self.position[0] - self.startposition[0] >= 1199 and dir == 1:
            self.position[0] = self.startposition[0]
            
        if dir == 0:
            self.position[0] -=12
           
        if dir == 1:
            self.position[0] +=12
           
class Runner():
    
    
    
    def __init__(self, spriteName, x=0, y=0):
       
        self.sprite =pygame.image.load('./images/{}'.format(spriteName))
        self.position = [x, y]
        self.name = "runner"
        self.iniDir = 0
    def flipLateral(self):
        
        self.sprite = pygame.transform.flip(self.sprite, True, False)    
    def avanza(self, x, y):
        if self.iniDir == 0 and self.position[0] > x:
            self.flipLateral()
            self.iniDir = 1
            
        if self.iniDir == 1 and self.position[0] < x:
            self.flipLateral()
            self.iniDir = 0
        try:
            self.position[0] += random.randint(-1, 5)*(x-self.position[0])/abs((x-self.position[0]))/5
            self.position[1] += random.randint(-4, 5)*(y-self.position[1])/abs(max(12,(x-self.position[0])))
        except:
            pass
        
class Shot():
    
    def __init__(self, spriteName, x0=0, y0=0, x1=0, y1=0, name="runner"):
        self.name = name
        self.sprite =pygame.image.load('./images/{}'.format(spriteName))
        self.startposition = [x0, y0]
        self.position = [x0, y0]
        self.iniDir = 0
        self.ballposition = [x1, y1]
    def flipLateral(self): 
        self.sprite = pygame.transform.flip(self.sprite, True, False)   
         
    def avanza(self):
        if self.iniDir == 0 and self.startposition[0] > self.ballposition[0]:
            self.flipLateral()
            self.iniDir = 1
            
        if self.iniDir == 1 and self.startposition[0] < self.ballposition[0]:
            self.flipLateral()
            self.iniDir = 0
        
        try:
            self.position[0] += (self.ballposition[0]-self.startposition[0])/abs((self.ballposition[0]-self.startposition[0]))
            self.position[1] += (self.ballposition[1]-self.startposition[1])/abs(self.ballposition[0]-self.startposition[0])
        except:
            pass      
 
class Game():
    
    width = 1200
    heigth = 300
    runners = []
    shots = []
    __startLine = 40
    __finishLine = width -60
    __ballSprites = ['ball1.png', 'ball2.png', 'ball3.png', 'ball4.png']
    __names = ['Goku', 'Yancha', 'Ten Sian', 'Picolo']
    __posY = [heigth/8,heigth/8 + heigth/4,heigth/8 + heigth/2,heigth/16 + 3*heigth/4 ]
    __sprites = ['sprite1.png', 'sprite2.png', 'sprite3.png', 'sprite4.png']
    ball = Frezzer(__finishLine-200, 150)
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((1200, 300))
        self.__bg = fondo()
        self.__bg1 = fondo(1199)
        self.__bg2 = fondo(-1199)
        

        pygame.display.set_caption("Pilla la Frezzer")
        for runner in self.__posY:
            indice = self.__posY.index(runner)
            
            loadedRunner = Runner(self.__sprites[indice],self.__startLine, runner)
            loadedRunner.name =self.__names[indice]
            
            self.runners.append(loadedRunner)


    def run(self):
        
        pygame.mixer.music.load('./music/dragon_ball_z_8_bits.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)
        dir=0
        gameOver = False
        while not gameOver:
            #gestion de eventos
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    gameOver=True
                    
                
            
            
            for activeRunner in self.runners:
            
                
                dir = activeRunner.iniDir
                       
                if abs(activeRunner.position[0]+activeRunner.position[1] - self.ball.position[0]- self.ball.position[1])< 3 and abs(activeRunner.position[1] - self.ball.position[1])< 3:
                    print ('{} ha atrapado Freezer'.format(activeRunner.name))
                    gameOver=True
                    
                 
                activeRunner.avanza(self.ball.position[0],self.ball.position[1])
                rdn = random.randint(-100,100)
              
                if rdn == 0:
                    
                    loadedShot = Shot(self.__ballSprites[self.runners.index(activeRunner)],activeRunner.position[0], activeRunner.position[1],self.ball.position[0],self.ball.position[1],activeRunner.name)
                    self.shots.append(loadedShot)
                      
                    
            for activeShot in self.shots:
         
                activeShot.avanza()
                #print ('distancia {} {} '.format(activeShot.position[0]+6 - self.ball.position[0],activeShot.position[1]-4 - self.ball.position[1]))

                if abs(activeShot.position[0]-7 - self.ball.position[0])< 6 and abs(activeShot.position[1]-6 - self.ball.position[1])< 12:
                    print ('{} ha derribado Freezer en {}-{} disparo en {}-{} margen {}-{}'.format(activeShot.name,self.ball.position[0],self.ball.position[1],activeShot.position[0],activeShot.position[1],activeShot.position[0]-6 - self.ball.position[0],activeShot.position[1]-4 - self.ball.position[1]))
                    gameOver=True
                
              
                
                
            self.ball.move(dir)
            self.__bg.move(dir)
            self.__bg1.move(dir)
            self.__bg2.move(dir)
            if self.ball.position[0] > 1150:
                self.ball.position[0] = 1150
            elif self.ball.position[0] < 10:
                self.ball.position[0] = 10
            if self.ball.position[1] < 0:
                self.ball.position[1] = 0
            if self.ball.position[1] > 265:
                self.ball.position[1] = 265
            #Refresco de pantalla
               
                 
            self.__screen.blit(self.__bg.sprite,self.__bg.position)
            self.__screen.blit(self.__bg1.sprite,self.__bg1.position)
            self.__screen.blit(self.__bg2.sprite,self.__bg2.position)
            self.__screen.blit(self.ball.sprite,self.ball.position)
                
            for activeShot in self.shots:

                self.__screen.blit(activeShot.sprite,activeShot.position)
                
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