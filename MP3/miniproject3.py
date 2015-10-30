import pygame
from pygame.locals import *




class RythemgameModel:
    def __init__(self):
        self.bricky1 = [180,110,-160,-410,-1440,-2480,-2640,-3015,-3300,-3565,-3630] #put brick1s in these coordinates
        self.bricky2 = [-560,-810,-1090,-1330,-2400,-2670,-3140,-3840] #put brick2s in these coordinates
        self.bricky3 = [-590,-690,-780,-1110,-1220,-1600,-1850,-2240,-2860,-3500,-3705,-4455]
        self.bricky4 = [-620,-1150,-1640,-1720,-2110,-2200,-2700,-2880,-3300,-3735,-3940,-3980,-4525]
        self.bricky5 = [-1670,-2150,-2720,-2950,-3420,-3765,-4100,-4220,-4330,-4595]
        self.brickx = [5,100,195,290,385] # brick1s to brick5s is in these x coordinates
        self.brickcolor = [(50,60,130),(150,215,230),(255,175,200),(255,255,130),(180,230,30)] # brick1s to brick5s have colors in these orders.




class RythemgameWindowView:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen


    def draw(self):
        # background image
        nightsky = pygame.image.load("nightsky2.jpg") 
        screen.fill(pygame.Color(0,0,0))
        screen.blit(nightsky,(0,0))

        # view score on the screen
        view.score(str(score))


        # draw background bricks on the bottom of screen
        for i in range(5):
            pygame.draw.rect(screen,model.brickcolor[i],pygame.Rect(model.brickx[i],y2,90,40))

        # draw lines between bricks
        for i in range(4):
            pygame.draw.line(screen,(255,255,255),(model.brickx[i+1]-3,40),(model.brickx[i+1]-3,680),2)

        # move brick1s below as time passes
        for i in range(len(model.bricky1)):
            view.movingbrick(model.brickcolor[0],model.brickx[0],model.bricky1[i]+dy)

        # move brick2s below as time passes
        for i in range(len(model.bricky2)):
            view.movingbrick(model.brickcolor[1],model.brickx[1],model.bricky2[i]+dy)

        for i in range(len(model.bricky3)):
            view.movingbrick(model.brickcolor[2],model.brickx[2],model.bricky3[i]+dy)

        for i in range(len(model.bricky4)):
            view.movingbrick(model.brickcolor[3],model.brickx[3],model.bricky4[i]+dy)

        for i in range(len(model.bricky5)):
            view.movingbrick(model.brickcolor[4],model.brickx[4],model.bricky5[i]+dy)
            



    # put brick on (x,y) coordinate with color
    def movingbrick(self,color,x,y):
        pygame.draw.rect(screen,color,(x,y,90,40))


    # write text about score on the right top of screen
    def score(self,score):
        font = pygame.font.SysFont("None",28)
        textsurface = font.render("SCORE : "+score, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (380,20)
        screen.blit(textsurface,textRect)


    # countdown numbers from 3 to 1 before game starting
    def first(self,number):
        screen.fill(pygame.Color(0,0,0))
        font = pygame.font.SysFont("None",150)
        textsurface = font.render(number, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (240,320)
        screen.blit(textsurface,textRect)
        pygame.display.update()



    # view the final score after game finishing
    def final(self,score):
        screen.fill(pygame.Color(0,0,0))
        font = pygame.font.SysFont("None",100)
        textsurface = font.render("score : " +score, True, (255,170,0))
        textRect = textsurface.get_rect()
        textRect.center = (240,320)
        screen.blit(textsurface,textRect)
        pygame.display.update()

        



class RythemgameController:
    def __init__(self,model,screen):
        self.model = model
        self.screen = screen

    def handle_keyboard_event(self,event):
        if event.type == pygame.KEYDOWN:
            global score
            if event.key == pygame.K_f:
                for i in range(len(model.bricky1)): # for all brick1s in model class, if player put f button when moving bricks are near the bottom bricks, give score +10
                    if y2-level+10 <= model.bricky1[i]+dy <= y2+level:
                        score += 10
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
    
    

    
    
    running = True

    # countdown before game starting
    view.first(str(3))
    pygame.time.delay(1000)
    view.first(str(2))
    pygame.time.delay(1000)
    view.first(str(1))
    pygame.time.delay(1000)

    
    # often used value
    y1 = 40 
    y2 = 580


    width = 90 # width of all bricks
    height = 40 # height of all bricks
    dy = 0
    score = 0 
    level = 20 # as value is lower, game level is harder

    clock = pygame.time.Clock()
    FPS = 500

    # insert music into the game
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
  
        # to move bricks as time passes
        dy = dy + seconds*130
        

        # after final brick is out of screen(game finishes), view final score screen
        if model.bricky5[9]+dy>=1000:
            view.final(str(score))


        pygame.display.update()


    pygame.quit()
        




