#COURSEWORK
import pygame
import pygame_menu
from sprites import *

pygame.init()

screen_width = 460
screen_height = 690
win = pygame.display.set_mode((screen_width,screen_height))
#walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
#walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
mudkip = pygame.image.load('mudkip_sprite.png')
charizard = pygame.image.load('charizard_sprite.png')
bg = pygame.image.load('backdrop1.jpg')

#player_ss = spritesheet(os.path.join('Assets','naruto_sheet.bmp'))
#stance, left, left, right, right, jump, air_jump_left, air_jump_right
#player_images = player_ss.images_at( (pygame.Rect(4,11,29,44), pygame.Rect(200,493,42,33),pygame.Rect(38,446,56,32), 
                               #pygame.Rect(11,402,36,28), pygame.Rect(43,401,33,28),
                               #pygame.Rect(4,268,28,51),
                               #pygame.Rect(407,4712,67,64), pygame.Rect(410,4715,62,60)), colorkey=(73,176,255))


clock = pygame.time.Clock()



class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.standing = True
        self.walkCount = 0
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.standing = True
        
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                #win.blit(player_images[b], (self.x, self.y))
                win.blit(mudkip,(self.x,self.y))
                #win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(mudkip,(self.x,self.y))
                #win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
                
            elif self.up:
                win.blit(mudkip,(self.x,self.y))
                self.walkCount +=1
                
            elif self.down:
                win.blit(mudkip,(self.x,self.y))
                self.walkCount +=1
        
        else:
            if self.right:
                win.blit(mudkip,(self.x,self.y))
                #win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(mudkip,(self.x,self.y))
                #win.blit(walkLeft[0], (self.x, self.y))
                
        
        
    def hit(self):
        self.x = 100
        self.y = 410
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                

class rival(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fought = False
    
    def draw():
        win.blit(charizard,(self.x,self.y))
        

    
        
def redraw():
    win.blit(bg, (0,0))
    man.draw(win)
    
    pygame.display.update()

man = player(200,410,64,64)
dragon = rival(300,500,64,64)
def game():
    
    run = True
    while run:
        clock.tick(27)
        
        
        if rival.fought == False:
            if player.x == rival.x and player.y < rival.y:
                battle()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
     
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x-= man.vel
            man.right = False
            man.left = True
            man.up = False
            man.down = False
            man.standing = False
            
        elif keys[pygame.K_RIGHT] and man.x < screen_width - man.width - man.vel:
            man.x+= man.vel
            man.right = True
            man.left = False
            man.up = False
            man.down = False
            man.standing = False
            
        elif keys[pygame.K_UP] and man.y > man.vel:
            man.y-= man.vel
            man.right = False
            man.left = False
            man.up = True
            man.down = False
            man.standing = False
            
        elif keys[pygame.K_DOWN] and man.y < screen_height - man.height - man.vel:
            man.y+= man.vel
            man.right = False
            man.left = False
            man.up = False
            man.down = True
            man.standing = False
            
        
        redraw()




def battle():
    pass


def main():
    menu = pygame_menu.Menu('Pokemon Reza!', screen_width,screen_height,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.button('Play', game)
    menu.add.button('Controls', controls)
    menu.add.button('Quit', quits)
    #myimage = pygame_menu.baseimage.BaseImage(
        #'bg.jpg'=pygame_menu.baseimage.IMAGE_EXAMPLE_GRAY_LINES,
        #drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
        #offset=(0,0)
    #)
    #mytheme.background_color = myimage
    menu.mainloop(win)
   

def controls():
    menu = pygame_menu.Menu('Controls!', screen_width,screen_height,theme=pygame_menu.themes.THEME_BLUE)
    menu.add.label("Arrow keys for movement.")
    menu.add.label("Click for anything else.")
    menu.add.button('Back', main)
    menu.mainloop(win)
    

def quits():
    pygame.quit()

main()

