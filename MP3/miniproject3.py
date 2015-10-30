import pygame
from pygame.locals import *
import time







class Brick:
    def __init__(self,screen):
    	self.screen = screen
        

    def draw(self,color,x,y,height):
        pygame.draw.rect(self.screen,color,pygame.Rect(x,y,90,height))






class RythemgameModel:
    def __init__(self):
        self.bricky1 = [180,110,-160,-410,-1440,-2480,-2640,-3015,-3300,-3565,-3630]
        self.bricky2 = [-560,-810,-1090,-1330,-2400,-2670,-3140,-3840]
        self.bricky3 = [-590,-690,-780,-1110,-1220,-1600,-1850,-2240,-2860,-3500,-3705,-4455]
        self.bricky4 = [-620,-1150,-1640,-1720,-2110,-2200,-2700,-2880,-3300,-3735,-3940,-3980,-4525]
        self.bricky5 = [-1670,-2150,-2720,-2950,-3420,-3765,-4100,-4220,-4330,-4595]
        self.brickx = [5,100,195,290,385]
        self.brickcolor = [(50,60,130),(150,215,230),(255,175,200),(255,255,130),(180,230,30)]








class RythemgameWindowView:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen


    def draw(self):
        nightsky = pygame.image.load("nightsky2.jpg")
        self.screen.fill(pygame.Color(0,0,0))
        self.screen.blit(nightsky,(0,0))

        view.score(str(score))



        for i in range(5):
            pygame.draw.rect(self.screen,model.brickcolor[i],pygame.Rect(model.brickx[i],y2,90,40))

        for i in range(4):
            pygame.draw.line(self.screen,(255,255,255),(model.brickx[i+1]-3,40),(model.brickx[i+1]-3,680),2)


        for i in range(len(model.bricky1)):
            view.movingbrick(model.brickcolor[0],x1,model.bricky1[i]+dy)

        for i in range(len(model.bricky2)):
            view.movingbrick(model.brickcolor[1],x2,model.bricky2[i]+dy)

        for i in range(len(model.bricky3)):
            view.movingbrick(model.brickcolor[2],x3,model.bricky3[i]+dy)

        for i in range(len(model.bricky4)):
            view.movingbrick(model.brickcolor[3],x4,model.bricky4[i]+dy)

        for i in range(len(model.bricky5)):
            view.movingbrick(model.brickcolor[4],x5,model.bricky5[i]+dy)
            




    def movingbrick(self,color,x,y):
        return pygame.draw.rect(self.screen,color,(x,y,90,40))



    def score(self,score):
        font = pygame.font.SysFont("None",28)
        textsurface = font.render("SCORE : "+score, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (380,20)
        self.screen.blit(textsurface,textRect)


    def first(self,number):
        self.screen.fill(pygame.Color(0,0,0))
        font = pygame.font.SysFont("None",150)
        textsurface = font.render(number, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (240,320)
        self.screen.blit(textsurface,textRect)
        pygame.display.update()



    def final(self,score):
        self.screen.fill(pygame.Color(0,0,0))
        font = pygame.font.SysFont("None",100)
        textsurface = font.render("score : " +score, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (240,320)
        self.screen.blit(textsurface,textRect)
    
        pygame.display.update()

        






class RythemgameController:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen

    def handle_keyboard_event(self,event):
        if event.type == pygame.KEYDOWN:
            global score
            if event.key == pygame.K_f:
                for i in range(len(model.bricky1)):
                    if y2-level+10 <= model.bricky1[i]+dy <= y2+level:
                        score += 10
                A = USEREVENT+1
                pygame.time.set_timer(A,1000)
                if pygame.event.get(A):
                    column.draw1()

            if event.key == pygame.K_g:
                for i in range(len(model.bricky2)):
                    if y2-level+10 <= model.bricky2[i]+dy <= y2+level:
                        score += 10
            if event.key == pygame.K_h:
                for i in range(len(model.bricky3)):
                    if y2-level+10 <= model.bricky3[i]+dy <= y2+level:
                        score += 10
            if event.key == pygame.K_j:
                for i in range(len(model.bricky4)):
                    if y2-level+10 <= model.bricky4[i]+dy <= y2+level:
                        score += 10
            if event.key == pygame.K_k:
                for i in range(len(model.bricky5)):
                    if y2-level+10 <= model.bricky5[i]+dy <= y2+level:
                        score += 10




if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((480,640))
    model = RythemgameModel()
    view = RythemgameWindowView(model,screen)
    controller = RythemgameController(model,screen)
    Brick = Brick(screen)
    

    
    
    running = True
    view.first(str(3))
    pygame.time.delay(1000)
    view.first(str(2))
    pygame.time.delay(1000)
    view.first(str(1))
    pygame.time.delay(1000)

    
    x1 = 5
    x2 = 100
    x3 = 195
    x4 = 290
    x5 = 385
    y1 = 40
    y2 = 580
    width = 90
    height = 40
    dy = 0
    score = 0
    level = 20

    clock = pygame.time.Clock()
    FPS = 500

    file = 'IsntSheLovely.wav'
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    



    while running:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
                
            if event.type == pygame.KEYDOWN:
                controller.handle_keyboard_event(event)




        view.draw()

        milliseconds = clock.tick(FPS)
        seconds = milliseconds / 1000.0
  
        dy = dy + seconds*130
        

        if model.bricky5[9]+dy>=1000:
            view.final(str(score))


        pygame.display.update()


    pygame.quit()
        




