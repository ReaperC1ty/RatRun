from tokenize import String
import pygame, random
from sys import exit
from random import randint


pygame.init()
j= (0,0)
k= (1000,100)#use to despawn fonts and other blits(blit outside given range)

funX = 0 
funY = 0
aclock = 0
jimmithy = 0
highscore = 0
direction = 1
qalse = False
timeofstart = 0
botsquad = 0
buffman = 0

speed = [0,0]

menu_clock =  0


class RUNNER: 
    def draw_runner(self):
            self.x_pos = int(300)
            self.y_pos = int(700)
            block_rect = pygame.Rect(self.x_pos, self.y_pos,1000,1000)
            pygame.draw.rect(screen,(183,111,122), block_rect)

    def move_runner(self):
        self.x_pos += main_game.runner.direction

class MAIN:
    def __init__(self):
        self.runner = RUNNER()

    def update(self):
        self.runner.move_runner()
       

    def draw_elements(self):
         self.runner.draw_runner()



class Rombap: 
    def _init_ (self):
        self.speed = [50,-50]




Rspeedx = [20,20]
Rspeed = [10,10]
Rspeed2 = [-10,-10]
Rspeed3 = [10,-10]
Rspeed4 = [-10,10]
Rspeed5 = [10,10]
NekoSpeed = [-5,-5]
run = True
start = False

width = 1270
height = 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RatRun')
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
test_font = pygame.font.Font('Font/Pixely.ttf', 50)

menu_screen= pygame.image.load('Rgraphics/Space_to_start.png').convert()

background_surface = pygame.image.load('Rgraphics/Background Z.png').convert()
logo_surface = pygame.image.load('Rgraphics/RatRunTruLogogame.png').convert_alpha()

runner_surface = pygame.image.load('Rgraphics/RatRunnerx.png').convert_alpha()
runner_rect =  runner_surface.get_rect(center = (200,400))

#text_surface = test_font.render('0', False, 'Tan')
#ticks = pygame.time.get_ticks()


xl= random.randint(100, 628)
yl = random.randint(100, 746)

r = random.randint(100, 628)
z = random.randint(100, 746)

q = random.randint(100, 628)
w = random.randint(100, 746)

q1 = random.randint(100, 628)
w1 = random.randint(100, 746)

q2 = random.randint(100, 628)
w2 = random.randint(100, 746)

q3 = random.randint(100, 628)
w3 = random.randint(100, 746)


rombap_surface = pygame.image.load('Rgraphics/RombaP.png').convert_alpha()
rombap_rect = rombap_surface.get_rect(topright = (q3, w3))

romba5_surface = pygame.image.load('Rgraphics/Romba5.png').convert_alpha()
romba5_rect = romba5_surface.get_rect(topright = (q2, w2))

romba4_surface = pygame.image.load('Rgraphics/Romba4.png').convert_alpha()
romba4_rect = romba4_surface.get_rect(topright = (q1, w1))


romba3_surface = pygame.image.load('Rgraphics/Romba3.png').convert_alpha()
romba3_rect = romba3_surface.get_rect(topright = (q, w))


romba2_surface = pygame.image.load('Rgraphics/Romba2.png').convert_alpha()
romba2_rect = romba2_surface.get_rect(bottomleft = (xl, yl))


romba1_surface = pygame.image.load('Rgraphics/Romba.png').convert_alpha()
romba1_rect = romba1_surface.get_rect(center = (r, z))

neko_surface = pygame.image.load('Rgraphics/Neko.png').convert_alpha()
neko_rect = neko_surface.get_rect(center = (r, z))

#if run = false: 
# Run menu 
#if menu = done 
# run = true 


#vx, vy = -5, 5
main_game = MAIN()
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:      
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                funY = -11
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                funY = 9
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                funX = -11
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                funX = 9
            if event.key == pygame.K_SPACE:
                start = True 
                buffman = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                funY = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                funY = 0
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                funX = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                funX = 0

    if start == True: 
        j = (2000,2000)
     
    runner_rect.x += funX
    if runner_rect.x > width-35 or runner_rect.x < 0:
        runner_rect.x -= funX
    runner_rect.y += funY
    if runner_rect.y > height-35 or runner_rect.y < 0:
        runner_rect.y -= funY
    
    #if runner_rect.collidepoint((romba_rect.x, mousetrap_rect.y)):
    #    runner_rect.x = 0
     #   runner_rect.y = 0
    #if runner_rect.collidepoint((mousetrap2_rect.x, mousetrap2_rect.y)):
     #   runner_rect.x = 0
      #  runner_rect.y = 0

    
    screen.blit(background_surface,(0,0))
    screen.blit(logo_surface,(950,120))
    screen.blit(runner_surface,runner_rect)
    
    #screen.blit(text_surface,(1100,100))
   
    #if romba1_rect.left < 0:
       # Rspeed[4] = -Rspeed[4]

   # if romba1_rect.right > 700:
      #  Rspeed[4] = -Rspeed[4]
    #Romba's
   # if romba1_rect.left <= 20 or romba1_rect.right >= 580:
   #     direction *= -1
   #     Rspeedx = randint(0, 8) * direction
#
   #     if Rspeedx == 0:
   #         Rspeedx = randint(2, 8) * direction

    if romba1_rect.top <= 20 or romba1_rect.bottom >= 580:
        direction *= -1
        Rspeedx = randint(0, 8) * direction

        if Rspeedx == 0: 
            Rspeedx = randint(2, 8) * direction

    
    if romba1_rect.left < 0:
        Rspeed[0] = -Rspeed[0]
    if romba1_rect.right > width:
        Rspeed[0] = -Rspeed[0]
    if romba1_rect.top < 0: 
        Rspeed[1] = -Rspeed[1]
    if romba1_rect.bottom > height:
        Rspeed[1] = -Rspeed[1]

    if romba2_rect.left < 0:
        Rspeed2[0] = -Rspeed2[0]
    if romba2_rect.right > width:
        Rspeed2[0] = -Rspeed2[0]
    if romba2_rect.top < 0: 
        Rspeed2[1] = -Rspeed2[1]
    if romba2_rect.bottom > height:
        Rspeed2[1] = -Rspeed2[1]

    if romba3_rect.left < 0:
        Rspeed3[0] = -Rspeed3[0]
    if romba3_rect.right > width:
        Rspeed3[0] = -Rspeed3[0]
    if romba3_rect.top < 0: 
        Rspeed3[1] = -Rspeed3[1]
    if romba3_rect.bottom > height:
        Rspeed3[1] = -Rspeed3[1]

    if romba4_rect.left < 0:
        Rspeed4[0] = -Rspeed4[0]
    if romba4_rect.right > width:
        Rspeed4[0] = -Rspeed4[0]
    if romba4_rect.top < 0: 
        Rspeed4[1] = -Rspeed4[1]
    if romba4_rect.bottom > height:
        Rspeed4[1] = -Rspeed4[1]

    if romba5_rect.left < 0:
        Rspeed5[0] = -Rspeed5[0]
    if romba5_rect.right > width:
        Rspeed5[0] = -Rspeed5[0]
    if romba5_rect.top < 0: 
        Rspeed5[1] = -Rspeed5[1]
    if romba5_rect.bottom > height:
        Rspeed5[1] = -Rspeed5[1]

    if rombap_rect.left < 0:
        Rspeed5[0] = -Rspeed5[0]
    if rombap_rect.right > width:
        Rspeed5[0] = -Rspeed5[0]
    if rombap_rect.top < 0: 
        Rspeed5[1] = -Rspeed5[1]
    if rombap_rect.bottom > height:
        Rspeed5[1] = -Rspeed5[1]

    if neko_rect.left < 120:
        NekoSpeed[0] = -NekoSpeed[0]
    if neko_rect.right > width-120:
        NekoSpeed[0] = -NekoSpeed[0]
    if neko_rect.top < 120: 
        NekoSpeed[1] = -NekoSpeed[1]
    if neko_rect.bottom > height-120:
        NekoSpeed[1] = -NekoSpeed[1]


    if abs(neko_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - neko_rect.top) < 50:
        runner_rect.x = 25
        runner_rect.y = 25
        buffman = 0
    if abs(romba5_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - romba5_rect.top) < 50:
        runner_rect.x = 25
        runner_rect.y = 25
        buffman = 0
    if abs(romba4_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - romba4_rect.top) < 50:
        runner_rect.x = 25
        runner_rect.y = 25
        buffman = 0
    if abs(romba3_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - romba3_rect.top) < 50:
        runner_rect.x = 25
        runner_rect.y = 25
        buffman = 0
    if abs(romba2_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - romba2_rect.top) < 50:
        runner_rect.x = (width/2) - 25
        runner_rect.y = (height/2) - 25
        buffman = 0
    if abs(romba1_rect.left - (runner_rect.x+5)) < 50 and abs((runner_rect.y+5) - romba1_rect.top) < 50:
        runner_rect.x = 25
        runner_rect.y = 25
        buffman = 0

    
  
        

  
    aclock = pygame.time.get_ticks()
   # romba1_rect.left += Rspeedx[0]
  #  romba1_rect.top += Rspeedx[1]   


    romba1_rect.left += Rspeed[0]
    romba1_rect.top += Rspeed[1]    

    romba2_rect.left += Rspeed2[0]
    romba2_rect.top += Rspeed2[1]   

    romba3_rect.left += Rspeed3[0]
    romba3_rect.top += Rspeed3[1] 

    romba4_rect.left += Rspeed4[0]
    romba4_rect.top += Rspeed4[1] 

    romba5_rect.left += Rspeed5[0]
    romba5_rect.top += Rspeed5[1] 

    neko_rect.left += NekoSpeed[0]
    neko_rect.top += NekoSpeed[1] 

   #RatRunner 

    keys = pygame.key.get_pressed()


    



    # Timer Display 
    ticks = clock.get_time()
    
    buffman += ticks/1000
    if start == True: 
        if highscore < buffman:
            highscore = buffman
        
    text_surface = test_font.render(str(round(buffman, 2)), False, 'Tan')
    htext_surface = test_font.render(str(round(highscore, 2)), False, 'Lime')
    

   
    #main_game.draw_elements()
    screen.blit(romba5_surface, romba5_rect)
    screen.blit(romba4_surface, romba4_rect)
    screen.blit(romba3_surface, romba3_rect)
    screen.blit(romba1_surface, romba1_rect)
    screen.blit(romba2_surface, romba2_rect)
    screen.blit(neko_surface, neko_rect)
    screen.blit(text_surface,k)
    screen.blit(htext_surface,(1000,40))
    screen.blit(menu_screen,j)

   
    #screen.blit(menu_screen,j)
    pygame.display.update()
    clock.tick(60)