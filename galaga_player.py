"""
Made by injoon5, codingcup04 (codingPro01)
Do not copy & paste everything without this message
Do not edit this
2020.
"""
"""
_kr
Enermy에 오타가 있습니다. 수정하실 때 유의해 주시기 바랍니다.
"""
"""
_en
"Enermy" is a typo. Please be aware.
"""
import pygame, sys, random, time, playsound
from pygame.locals import *
pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga Launcher")
loaded = False
gaming = False
BLACK = (0, 0, 0)
fired = 0
font = pygame.font.SysFont(None, 50)
text = font.render("Loading...", True,(255, 255, 255))
show_text = screen.blit(text, [10, 10])
pygame.display.update()
class Enermy:
    def __init__(self):
            self.x = random.randint(0, 570)
            self.y = -100
            self.dy = 0
            self.dy = random.randint(2, 6)
            self.dx = random.choice((-(self.dy), (self.dy)))

    def move(self):
            self.dy += 0.1
            self.y += self.dy
            self.x += self.dx
    def draw(self):
            screen.blit(enermy_image, (self.x, self.y))
            
    def hit(self,missile):
            return pygame.Rect((self.x,self.y), (101, 100)).collidepoint(missile.x,missile.y)
            
    def off_screen(self):
            return self.y > 640

    def bounce(self):
            if self.x>570 or self.x<0:
                self.dx = -(self.dx)

class Forces:
    def __init__(self):
            self.x = 320
            self.y = 574

    def move(self):
            if pressed_keys[K_LEFT] and self.x>0:
                self.x -= 3
            if pressed_keys[K_RIGHT] and self.x<540:
                self.x += 3

    def draw(self):
            screen.blit(forces_image, (self.x, self.y))

    def fire(self):
            missiles.append(Missile(self.x+50))
            global fired
            fired += 1

    def boom(self,enermy):
            return (enermy.x+100>forces.x) and (enermy.y+100 > forces.y) and (enermy.x < forces.x+100)

class Missile:
    def __init__(self,x):
            self.x = x
            self.y = 574

    def move(self):
            self.y -= 5

    def off_screen(self):
            return self.y < -8
    
    def draw(self):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            
            pygame.draw.line(screen, (r,g,b),(self.x, self.y), (self.x,self.y+8), 6)

class Button:
    def __init__(self):
            self.x = 250
            self.y = 510
    def click(self):
            pos = pygame.mouse.get_pos()
            mx = pos[0]
            my = pos[1]
            return pygame.Rect((self.x,self.y), (150, 100)).collidepoint(mx,my)   
                
        
enermys = []
forces = Forces()
missiles = []
btn = Button()
points = 0
mx = 0
my = 0
gaming = False 
time.sleep(1)
gaming = True
myfont = pygame.font.Font(None, 40)

enermy_image = pygame.image.load("enemy.png").convert()
enermy_image.set_colorkey((0,0,0))

forces_image = pygame.image.load("forces.png").convert()
forces_image.set_colorkey((0,0,0))
surface = pygame.image.load("forces.png").convert()
game_over = pygame.image.load("game-over.png").convert()

restart_btn = pygame.image.load("restart.png").convert()
pygame.display.set_icon(surface)
last_enermy_spawn_time = 0
pygame.display.set_caption("Galaga")

clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    
    while loaded == False:
        print("Done loading!")
        screen.fill(BLACK)
        pygame.display.update()
        loaded = True
    while loaded == True:
        font = pygame.font.SysFont(None, 20)
        text = font.render("Game version: v 0.0.1 beta ", True,(255, 255, 255))
        show_text = screen.blit(text, [10, 10])
        pygame.display.update()
        time.sleep(0.3)
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 20)
        text = font.render("Position code: #2 ", True,(255, 255, 255))
        show_text = screen.blit(text, [10, 10])
        pygame.display.update()
        time.sleep(0.3)
        screen.fill(BLACK)
        pygame.display.update()
        loaded = ""
        ldnxt = True    
    while ldnxt == True:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                        sys.exit()
                if event.type == KEYDOWN and event.key == K_SPACE:
                        forces.fire()
                if event.type == KEYDOWN and event.key == K_LCTRL:
                        gaming = True
                if event.type == KEYDOWN and event.key == K_LALT:
                        gaming = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if btn.click():           
                                print('Restart')
                                gaming = True
                                fired = 0
                if event.type == KEYDOWN and event.key == K_F1:
                        print(Forces.__init__)
                        print(Enermy.__init__)
                        print(Missile.__init__)

        pressed_keys = pygame.key.get_pressed()

        pos = pygame.mouse.get_pos()
        mx = pos[0]
        my = pos[1]
                  
        if time.time() - last_enermy_spawn_time > 1:
            enermys.append(Enermy())
            last_enermy_spawn_time = time.time()
            
        screen.fill((0, 0, 0))
        forces.move()
        forces.draw()

        i = 0
        while i < len(enermys):   
                enermys[i].move()
                enermys[i].bounce()
                enermys[i].draw()
        
                if enermys[i].off_screen():
                    del enermys[i]
                    i-= 1
                i += 1
        i = 0
        while i < len(missiles):
                missiles[i].move()
                missiles[i].draw()
                if missiles[i].off_screen():
                    del missiles[i]
                    i-= 1
                i += 1
    
        i = 0
        while i < len(enermys) :     
                j = 0
                while j < len(missiles):
                    if enermys[i].hit(missiles[j]):
                            del enermys[i]
                            del missiles[j]
                            i -= 1
                            points += 1
                            gamepoint = points - fired / 2
                            if gamepoint >= 16:
                                    print("You won the game! Congratulations! ")
                                    wongame = myfont.render("You won the game! Congratulations! ")
                                    screen.blit(wongame, (10, 100))
                            break
                    j += 1
                i+= 1


        score_img = myfont.render("Score: " + str(int(points)), True, (255,255,255))
        ms_img = myfont.render("Missiles fired: " + str(fired), True, (255, 255, 255))
        gp_img = myfont.render("Gamepoint: " + str(points - fired / 2), True, (255, 255, 255))
        screen.blit(ms_img, (10, 40))
        screen.blit(score_img , (10, 10))
        screen.blit(gp_img, (10, 70))

        for enermy in enermys:
            if forces.boom(enermy):
                  screen.blit(game_over, (170, 200))
                  screen.blit(restart_btn, (250, 510))
                  print('Score: ', str(int(points)))
                  print("Missiles fired: " + str(fired))
                  print("Gamepoint: " + str(points - fired / 2))
                  pygame.display.update()
                  gaming  = False
                  break
                  
                                          


        if gaming:
                pygame.display.update()
        else:
            enermys = []
            points  = 0
            fired = 0

    pygame.display.update()