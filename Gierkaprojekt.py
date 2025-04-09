import pygame
from pygame.locals import *
import os

screenwidth = 1000
screenheight = 700
pygame.init()
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def Level1():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, screenheight - 50, screenwidth/3, 50))
        platforms.add(Platform(screenwidth/3, screenheight-125, 300, 125))
        platforms.add(Platform(600, 575, 150, 20))
        platforms.add(Platform(800, 575, 100, 20))
        platforms.add(Platform(900, 575, 100, 125))
        return platforms
    
    def Level2():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, screenheight - 50, 200, 50))
        platforms.add(Platform(150, 350, 50, 300))
        platforms.add(Platform(0, 350, 25, 250))
        platforms.add(Platform(125, 575, 35, 20))
        platforms.add(Platform(0, 500, 50, 20))
        platforms.add(Platform(125, 425, 35, 20))
        platforms.add(Platform(150, 350, 100, 20))
        platforms.add(Platform(600, 575, 150, 20))
        platforms.add(Platform(800, 575, 100, 20))
        platforms.add(Platform(900, 575, 100, 125))
        return platforms

    def Level3():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, screenheight - 50, screenwidth, 50))
        platforms.add(Platform(0, screenheight - 150, screenwidth-300, 16))
        platforms.add(Platform(732, screenheight - 69, 32, 19))
        platforms.add(Platform(0, 0, 300, 550))
        platforms.add(Platform(0, screenheight - 230, 450, 16))
        platforms.add(Platform(550, screenheight - 230, 450, 16))
        platforms.add(Platform(screenwidth-100, screenheight - 300, 100, 16))
        platforms.add(Platform(screenwidth-100, screenheight - 230, 16, 140))
        return platforms
    
    def Level4():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, screenheight - 50, 280, 50))
        platforms.add(Platform(420, screenheight - 50, 78, 50))
        platforms.add(Platform(638, screenheight - 50, 78, 50))
        platforms.add(Platform(820, 590, 180, 110))
        platforms.add(Platform(715, 526, 48, 5))
        platforms.add(Platform(721, 514, 37, 5))
        platforms.add(Platform(731, 505, 16, 4))
        platforms.add(Platform(0, 500, 643, 16))
        platforms.add(Platform(736, 420, 264, 44))
        platforms.add(Platform(0, 431, 30, 7))
        platforms.add(Platform(882, 0, 16, 380))
        return platforms
    
    def Level5():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, 420, 175, 45))
        platforms.add(Platform(282, 408, 16, 285))
        platforms.add(Platform(266, 693, 48, 7))
        platforms.add(Platform(266, 401, 48, 7)) 
        platforms.add(Platform(426, 376, 48, 7))
        platforms.add(Platform(442, 384, 16, 310)) 
        platforms.add(Platform(426, 693, 48, 7)) 
        platforms.add(Platform(589, 358, 48, 7))
        platforms.add(Platform(605, 365, 16, 328)) 
        platforms.add(Platform(589, 693, 48, 7))
        platforms.add(Platform(755, 358, 48, 7))
        platforms.add(Platform(771, 365, 16, 328)) 
        platforms.add(Platform(755, 693, 48, 7)) 
        platforms.add(Platform(831, 684, 169, 16))
        platforms.add(Platform(917, 548, 83, 16))
        platforms.add(Platform(917, 548, 16, 96))
        platforms.add(Platform(848, 310, 152, 16))
        platforms.add(Platform(72, 244, 761, 16))
        return platforms
    
    def Level6():
        platforms = pygame.sprite.Group()
        platforms.add(Platform(0, 684, 1000, 16))
        platforms.add(Platform(0, 540, 96, 16))
        platforms.add(Platform(579, 603, 96, 16))
        platforms.add(Platform(913, 548, 16, 96))
        platforms.add(Platform(913, 548, 87, 16))
        return platforms


class Block(pygame.sprite.Sprite):
    def __init__(self):

        self.idle = [pygame.image.load(os.path.join("Graphics",'idle1.png')), pygame.image.load(os.path.join("Graphics",'idle2.png')), pygame.image.load(os.path.join("Graphics",'idle3.png')), pygame.image.load(os.path.join("Graphics",'idle4.png')), pygame.image.load(os.path.join("Graphics",'idle5.png')), pygame.image.load(os.path.join("Graphics",'idle6.png')), pygame.image.load(os.path.join("Graphics",'idle7.png')), pygame.image.load(os.path.join("Graphics",'idle8.png')), pygame.image.load(os.path.join("Graphics",'idle9.png')),pygame.image.load(os.path.join("Graphics",'idle10.png'))]
        self.runright = [pygame.image.load(os.path.join("Graphics",'run1.png')), pygame.image.load(os.path.join("Graphics",'run2.png')), pygame.image.load(os.path.join("Graphics",'run3.png')), pygame.image.load(os.path.join("Graphics",'run4.png')), pygame.image.load(os.path.join("Graphics",'run5.png')), pygame.image.load(os.path.join("Graphics",'run6.png')), pygame.image.load(os.path.join("Graphics",'run7.png')), pygame.image.load(os.path.join("Graphics",'run8.png')), pygame.image.load(os.path.join("Graphics",'run9.png')),pygame.image.load(os.path.join("Graphics",'run10.png'))]
        self.runleft = [pygame.image.load(os.path.join("Graphics",'left1.png')), pygame.image.load(os.path.join("Graphics",'left2.png')), pygame.image.load(os.path.join("Graphics",'left3.png')), pygame.image.load(os.path.join("Graphics",'left4.png')), pygame.image.load(os.path.join("Graphics",'left5.png')), pygame.image.load(os.path.join("Graphics",'left6.png')), pygame.image.load(os.path.join("Graphics",'left7.png')), pygame.image.load(os.path.join("Graphics",'left8.png')), pygame.image.load(os.path.join("Graphics",'left9.png')),pygame.image.load(os.path.join("Graphics",'left10.png'))]
        self.idleleftanim = [pygame.image.load(os.path.join("Graphics",'idleleft1.png')), pygame.image.load(os.path.join("Graphics",'idleleft2.png')), pygame.image.load(os.path.join("Graphics",'idleleft3.png')), pygame.image.load(os.path.join("Graphics",'idleleft4.png')), pygame.image.load(os.path.join("Graphics",'idleleft5.png')), pygame.image.load(os.path.join("Graphics",'idleleft6.png')), pygame.image.load(os.path.join("Graphics",'idleleft7.png')), pygame.image.load(os.path.join("Graphics",'idleleft8.png')), pygame.image.load(os.path.join("Graphics",'idleleft9.png')),pygame.image.load(os.path.join("Graphics",'idleleft10.png'))]
        self.jumpright = [pygame.image.load(os.path.join("Graphics",'jumpright1.png')), pygame.image.load(os.path.join("Graphics",'jumpright2.png')), pygame.image.load(os.path.join("Graphics",'jumpright3.png'))]
        self.fallright = [pygame.image.load(os.path.join("Graphics",'fallright1.png')), pygame.image.load(os.path.join("Graphics",'fallright2.png')), pygame.image.load(os.path.join("Graphics",'fallright3.png'))]
        self.jumpleft = [pygame.image.load(os.path.join("Graphics",'jumpleft1.png')), pygame.image.load(os.path.join("Graphics",'jumpleft2.png')), pygame.image.load(os.path.join("Graphics",'jumpleft3.png'))]
        self.fallleft = [pygame.image.load(os.path.join("Graphics",'fallleft1.png')), pygame.image.load(os.path.join("Graphics",'fallleft2.png')), pygame.image.load(os.path.join("Graphics",'fallleft3.png'))]


        self.blockwidth = 29
        self.blockheight = 38


        self.x = 10
        self.y = 0


        self.vel_y = 8

        self.doublejump = True
        self.jumping = False
        self.jumped = False
        

        self.left = False
        self.right = False 
        self.walkcount = 0
        self.idlecount = 0
        self.idleright = True
        self.idleleft = False
        self.jumpcountanim = 0
        self.fallcountanim = 0   
        self.life = 1

        self.char1 = self.idle[0].get_rect()
        self.char1.x = self.x
        self.char1.y = self.y

        self.gamedisplay = 1

        self.havepotion = False


        
    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            if not self.havepotion:
                if not self.jumped:  # Warunek sprawdzający, czy postać nie jest w trakcie skoku ani podwójnego skoku
                    self.vel_y = -12
                    self.jumping = True
                    self.jumped = True
                elif self.jumped and self.doublejump and self.vel_y >= 0:  # Warunek sprawdzający, czy można wykonać podwójny skok
                    self.vel_y = -8
                    self.jumping = True
                    self.jumped = True
                    self.doublejump = False
            else:
                if not self.jumped:  # Warunek sprawdzający, czy postać nie jest w trakcie skoku ani podwójnego skoku
                    self.vel_y = -16
                    self.jumping = True
                    self.jumped = True
                elif self.jumped and self.doublejump and self.vel_y >= 0:  # Warunek sprawdzający, czy można wykonać podwójny skok
                    self.vel_y = -10
                    self.jumping = True
                    self.jumped = True
                    self.doublejump = False


        if key[pygame.K_a]:
            dx -= 6
            self.left = True
            self.right = False
            self.idleleft = True
            self.idleright = False
        elif key[pygame.K_d]:
            dx += 6
            self.left = False
            self.right = True
            self.idleleft = False
            self.idleright = True
        else:
            self.left = False
            self.right = False
            self.walkcount = 0
        
        #add gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        
        if(self.gamedisplay == 1):
            platforms = Platform.Level1()
        elif(self.gamedisplay == 2):
            platforms = Platform.Level2()
        elif(self.gamedisplay == 3):
            platforms = Platform.Level3()
        elif(self.gamedisplay == 4):
            platforms = Platform.Level4()
        elif(self.gamedisplay == 5):
            platforms = Platform.Level5()
        elif(self.gamedisplay == 6):
            platforms = Platform.Level6()

        
        # Collision
        for platform in platforms:
            if platform.rect.colliderect(self.char1.x + dx, self.char1.y, self.blockwidth, self.blockheight):
                dx = 0
            if platform.rect.colliderect(self.char1.x, self.char1.y + dy,self.blockwidth, self.blockheight):
                if self.vel_y < 0:
                    dy = platform.rect.bottom - self.char1.top
                    self.vel_y = 0
                elif self.vel_y >= 0:
                    dy = platform.rect.top - self.char1.bottom
                    self.vel_y = 0
                    self.jumping = False
                    self.jumped = False
                    self.doublejump = True
                    
		#update player coordinates
        self.x += dx
        self.y += dy

        if self.char1.bottom > screenheight:
            self.char1.bottom = screenheight
            dy = 0
            self.life = 0
        elif self.x <= 0:
            self.x = 6
        elif self.x >= screenwidth:
            self.x = screenwidth-6
        

        self.char1.center = (self.x,self.y+self.char1.height/2)
        if self.walkcount + 1 >= 30:
            self.walkcount = 0
        if self.idlecount + 1 >= 30:
            self.idlecount = 0
        if self.jumpcountanim + 1 >= 9:
            self.jumpcountanim = 0    
        if self.fallcountanim + 1 >= 9:
            self.fallcountanim = 0   

        if self.jumping and self.idleright:
            if dy <= 0:
                screen.blit(self.jumpright[self.jumpcountanim//3],self.char1)
                self.jumpcountanim += 1
            elif dy > 0:
                screen.blit(self.fallright[self.fallcountanim//3],self.char1)
                self.fallcountanim += 1
        elif self.jumping and self.idleleft:
            if dy <= 0:
                screen.blit(self.jumpleft[self.jumpcountanim//3],self.char1)
                self.jumpcountanim += 1
            elif dy > 0:
                screen.blit(self.fallleft[self.fallcountanim//3],self.char1)
                self.fallcountanim += 1
        elif self.right:
            screen.blit(self.runright[self.walkcount//3],self.char1)
            self.walkcount += 1
        elif self.left:
            screen.blit(self.runleft[self.walkcount//3],self.char1)
            self.walkcount += 1
        elif not self.right and self.idleright:
            screen.blit(self.idle[self.idlecount//3],self.char1)  
            self.idlecount += 1
            self.walkcount = 0
        elif not self.left and self.idleleft:
            screen.blit(self.idleleftanim[self.idlecount//3],self.char1)  
            self.idlecount += 1
            self.walkcount = 0








class Fire(pygame.sprite.Sprite):
    def __init__(self):
        self.fireanim = [pygame.image.load(os.path.join("Graphics",'fire1.png')), pygame.image.load(os.path.join("Graphics",'fire2.png')), pygame.image.load(os.path.join("Graphics",'fire3.png')), pygame.image.load(os.path.join("Graphics",'fire4.png'))]
        self.firecount = 0
        self.firechar = self.fireanim[0].get_rect()
        self.animation_delay = 100  # Opóźnienie czasowe między klatkami animacji (w milisekundach)
        self.last_update = pygame.time.get_ticks()  # Początkowy czas animacji

    def place(self, x, y, screen):
        self.firechar.center = (x, y + self.firechar.height/2)
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_delay:
            self.last_update = current_time
            if self.firecount + 1 >= len(self.fireanim):
                self.firecount = 0
            else:
                self.firecount += 1
        screen.blit(self.fireanim[self.firecount], self.firechar)


class Door(pygame.sprite.Sprite):
    def __init__(self):
        self.doorimg = pygame.image.load(os.path.join("Graphics",'door.png'))
        self.doorchar = self.doorimg.get_rect()
        
        self.keyimg = pygame.image.load(os.path.join("Graphics",'key.png'))
        self.keychar = self.keyimg.get_rect()

    def place(self, dx, dy, screen, kx, ky):
        self.doorchar.center = (dx, dy + self.doorchar.height/2)
        self.keychar.center = (kx, ky + self.keychar.height/2)
        screen.blit(self.doorimg, self.doorchar)
        screen.blit(self.keyimg, self.keychar)


class Potion(pygame.sprite.Sprite):
    def __init__(self):
        self.potionimg = pygame.image.load(os.path.join("Graphics",'potion.png'))
        self.potionchar = self.potionimg.get_rect()

    def place(self, dx, dy, screen):
        self.potionchar.center = (dx, dy + self.potionchar.height/2)
        screen.blit(self.potionimg, self.potionchar)



class Bat(pygame.sprite.Sprite):
    def __init__(self):
        
        self.batrunleft = [pygame.image.load(os.path.join("Graphics",'bat1.png')), pygame.image.load(os.path.join("Graphics",'bat2.png')), pygame.image.load(os.path.join("Graphics",'bat3.png')), pygame.image.load(os.path.join("Graphics",'bat4.png')), pygame.image.load(os.path.join("Graphics",'bat5.png')), pygame.image.load(os.path.join("Graphics",'bat6.png')), pygame.image.load(os.path.join("Graphics",'bat7.png')), pygame.image.load(os.path.join("Graphics",'bat8.png')), pygame.image.load(os.path.join("Graphics",'bat9.png')),pygame.image.load(os.path.join("Graphics",'bat10.png'))]
        self.batrunright = [pygame.image.load(os.path.join("Graphics",'batright1.png')), pygame.image.load(os.path.join("Graphics",'batright2.png')), pygame.image.load(os.path.join("Graphics",'batright3.png')), pygame.image.load(os.path.join("Graphics",'batright4.png')), pygame.image.load(os.path.join("Graphics",'batright5.png')), pygame.image.load(os.path.join("Graphics",'batright6.png')), pygame.image.load(os.path.join("Graphics",'batright7.png')), pygame.image.load(os.path.join("Graphics",'batright8.png')), pygame.image.load(os.path.join("Graphics",'batright9.png')),pygame.image.load(os.path.join("Graphics",'batright10.png'))]

        self.batx = 0
        self.baty = 0

        self.batwidth = 40
        self.batheight = 20

        
        self.batflycounter = 0
        self.batspeedx = 2.5
    

        self.batchar = self.batrunleft[0].get_rect()
        self.batcount = 0
        self.batsize = (40, 20)

    def batplace(self,screen):
        self.batchar.center = (self.batx,self.baty+self.batchar.height/2)
        if self.batcount + 1 >= 30:
            self.batcount = 0
        if self.batspeedx < 0:
            screen.blit(pygame.transform.scale(self.batrunleft[self.batcount//3],self.batsize),self.batchar)
            self.batcount += 1
        elif self.batspeedx >= 0:
            screen.blit(pygame.transform.scale(self.batrunright[self.batcount//3],self.batsize),self.batchar)
            self.batcount += 1


    def batmove(self,batflylen):
        if(self.batflycounter == batflylen):
            self.batspeedx *= -1
            self.batflycounter = 0
        
        else:
            self.batx += self.batspeedx
            self.batflycounter += 1



class Rat(pygame.sprite.Sprite):
    def __init__(self):
        
        self.ratrunleft = [pygame.image.load(os.path.join("Graphics",'rat1.png')), pygame.image.load(os.path.join("Graphics",'rat2.png')), pygame.image.load(os.path.join("Graphics",'rat3.png')), pygame.image.load(os.path.join("Graphics",'rat4.png')), pygame.image.load(os.path.join("Graphics",'rat5.png')), pygame.image.load(os.path.join("Graphics",'rat6.png')), pygame.image.load(os.path.join("Graphics",'rat7.png')), pygame.image.load(os.path.join("Graphics",'rat8.png')), pygame.image.load(os.path.join("Graphics",'rat9.png')),pygame.image.load(os.path.join("Graphics",'rat10.png'))]
        self.ratrunright = [pygame.image.load(os.path.join("Graphics",'ratright1.png')), pygame.image.load(os.path.join("Graphics",'ratright2.png')), pygame.image.load(os.path.join("Graphics",'ratright3.png')), pygame.image.load(os.path.join("Graphics",'ratright4.png')), pygame.image.load(os.path.join("Graphics",'ratright5.png')), pygame.image.load(os.path.join("Graphics",'ratright6.png')), pygame.image.load(os.path.join("Graphics",'ratright7.png')), pygame.image.load(os.path.join("Graphics",'ratright8.png')), pygame.image.load(os.path.join("Graphics",'ratright9.png')),pygame.image.load(os.path.join("Graphics",'ratright10.png'))]

        self.ratx = 0
        self.raty = 0

        self.ratwidth = 80
        self.ratheight = 40

        
        self.ratmovecounter = 0
        self.ratspeedx = 2
    

        self.ratchar = self.ratrunleft[0].get_rect()
        self.ratcount = 0
        self.ratsize = (55, 30)
    def ratplace(self,screen):
        self.ratchar.center = (self.ratx,self.raty+self.ratchar.height/2)
        if self.ratcount + 1 >= 30:
            self.ratcount = 0
        if self.ratspeedx < 0:
            screen.blit(pygame.transform.scale(self.ratrunleft[self.ratcount//3],self.ratsize),self.ratchar)
            self.ratcount += 1
        elif self.ratspeedx >= 0:
            screen.blit(pygame.transform.scale(self.ratrunright[self.ratcount//3],self.ratsize),self.ratchar)
            self.ratcount += 1

    def ratmove(self,ratmovelen):
        if(self.ratmovecounter == ratmovelen):
            self.ratspeedx *= -1
            self.ratmovecounter = 0
        
        else:
            self.ratx += self.ratspeedx
            self.ratmovecounter += 1


class Flag(pygame.sprite.Sprite):
    def __init__(self):
        self.flagimg = pygame.image.load(os.path.join("Graphics",'flag.png'))

        self.flagx = 0
        self.flagy = 0
        self.flagsize = (30,60)
        self.flagchar = self.flagimg.get_rect()

    def flagplace(self,screen):
        self.flagchar.center = (self.flagx,self.flagy)
        screen.blit(pygame.transform.scale(self.flagimg,self.flagsize),self.flagchar)


def collision(testblock,fireblock,batblock,ratblock):
    
    if(testblock.char1.colliderect(fireblock.firechar)):
        testblock.life = 0

    if(testblock.char1.colliderect(batblock.batchar)):
        testblock.life = 0

    if(testblock.char1.colliderect(ratblock.ratchar)):
        testblock.life = 0


        
        

def main():
    gamedisplay = 0
    menuselector = 0
    levelselector = 1
    levelselectorbool = False
    levelselmain = False

    havekey = False
    pygame.display.set_caption('Medieval Pixels') # Title

    # Fill background
    mainmenu = pygame.image.load(os.path.join("Graphics",'background.png'))
    bg = pygame.image.load(os.path.join("Graphics",'background.png'))
    levelselgraphic = pygame.image.load(os.path.join("Graphics",'background.png'))
    level6img = pygame.image.load(os.path.join("Graphics",'level6.png'))
    level5img = pygame.image.load(os.path.join("Graphics",'level5.png'))
    level4img = pygame.image.load(os.path.join("Graphics",'level4.png'))
    level3img = pygame.image.load(os.path.join("Graphics",'level3.png'))
    level2img = pygame.image.load(os.path.join("Graphics",'level2.png'))
    level1img = pygame.image.load(os.path.join("Graphics",'level1.png'))
    bgsize = (screenwidth, screenheight)
    bg = pygame.transform.scale(bg,bgsize)
    mainmenu = pygame.transform.scale(mainmenu,bgsize)
    levelselgraphic = pygame.transform.scale(levelselgraphic,bgsize)

    # Displaying text
    fonttitle = pygame.font.Font("medieval.ttf", 80)
    font = pygame.font.Font("medieval.ttf", 45)


    title = fonttitle.render("Medieval Pixels", 3, (64, 64, 64))
    titlepos = title.get_rect()
    titlepos.center = (screenwidth//2 , screenheight//7)

    play = font.render("Play", 3, (0, 0, 0))
    playpos = play.get_rect()
    playpos.center = (screenwidth//2 , screenheight//1.6)

    levelsel = font.render("Select level", 3, (0, 0, 0))
    levelselpos = levelsel.get_rect()
    levelselpos.center = (screenwidth//2 , screenheight//1.3)

    exit = font.render("Exit", 3, (0, 0, 0))
    exitpos = exit.get_rect()
    exitpos.center = (screenwidth//2 , screenheight//1.1)

    level1 = font.render("Level1", 3, (0, 0, 0))
    level1pos = level1.get_rect()
    level1pos.center = (200 , screenheight//5)

    level2 = font.render("Level2", 3, (0, 0, 0))
    level2pos = level2.get_rect()
    level2pos.center = (500 , screenheight//5)

    level3 = font.render("Level3", 3, (0, 0, 0))
    level3pos = level3.get_rect()
    level3pos.center = (800 , screenheight//5)

    level4 = font.render("Level4", 3, (0, 0, 0))
    level4pos = level4.get_rect()
    level4pos.center = (200 , screenheight//3)

    level5 = font.render("Level5", 3, (0, 0, 0))
    level5pos = level5.get_rect()
    level5pos.center = (500 , screenheight//3)

    level6 = font.render("Level6", 3, (0, 0, 0))
    level6pos = level6.get_rect()
    level6pos.center = (800 , screenheight//3)

    mainmen = font.render("Main menu", 3, (0, 0, 0))
    mainmenpos = mainmen.get_rect()
    mainmenpos.center = (screenwidth//2 , 600)

    mainmenu.blit(title, titlepos)
    mainmenu.blit(play, playpos)
    mainmenu.blit(levelsel, levelselpos)
    mainmenu.blit(exit, exitpos)

    testblock = Block()

    fireblock = Fire()

    batblock = Bat()
    
    ratblock = Rat()

    flagblock = Flag()

    doorblock = Door()

    potionblock = Potion()

    havekey = False
    open = False
    
    # Event loop
    while True:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and gamedisplay == 0:
                    menuselector -= 1
                elif event.key == pygame.K_s and gamedisplay == 0:
                    menuselector += 1
                if event.key == pygame.K_d and levelselectorbool and levelselmain == False:
                    levelselector += 1
                elif event.key == pygame.K_a and levelselectorbool and levelselmain == False:
                    levelselector -= 1
                if event.key == pygame.K_w and levelselectorbool:
                    levelselector = 1
                    levelselmain = False
                elif event.key == pygame.K_s and levelselectorbool:
                    levelselmain = True
                if event.key == pygame.K_ESCAPE and gamedisplay > 0:
                    gamedisplay = 0
                    testblock.x = 10
                    havekey = False
                    open = False
                    testblock.havepotion = False

    
        if(gamedisplay == 0): # MAIN MENU HERE
            screen.blit(mainmenu, (0,0))
            if menuselector == 0:
                play = font.render("Play", True, (255, 0, 0))
                levelsel = font.render("Select level", True, (0, 0, 0))
                exit = font.render("Exit", True, (0, 0, 0))
                mainmenu.blit(play, playpos)
                mainmenu.blit(levelsel, levelselpos)
                mainmenu.blit(exit, exitpos)
            else:
                play = font.render("Play", True, (0, 0, 0))
                mainmenu.blit(play, playpos)

            if menuselector == 1:
                play = font.render("Play", True, (0, 0, 0))
                levelsel = font.render("Select level", True, (255, 0, 0))
                exit = font.render("Exit", True, (0, 0, 0))
                mainmenu.blit(exit, exitpos)
                mainmenu.blit(levelsel, levelselpos)
                mainmenu.blit(play, playpos)
            else:
                levelsel = font.render("Select level", True, (0, 0, 0))
                mainmenu.blit(levelsel, levelselpos)

            if menuselector == 2:
                play = font.render("Play", True, (0, 0, 0))
                levelsel = font.render("Select level", True, (0, 0, 0))
                exit = font.render("Exit", True, (255, 0, 0))
                mainmenu.blit(exit, exitpos)
                mainmenu.blit(levelsel, levelselpos)
                mainmenu.blit(play, playpos)
            else:
                exit = font.render("Exit", True, (0, 0, 0))
                mainmenu.blit(exit, exitpos)
                

            if menuselector < 0:
                menuselector = 2
            elif menuselector > 2:
                menuselector = 0
            testblock.havepotion = False
            if(pygame.key.get_pressed()[pygame.K_RETURN] and menuselector == 0):
                gamedisplay = 1
                batblock.batx = 650 # Cordinates for first level, for bat sprite 
                batblock.baty = 500

                ratblock.ratx = 325 # Cordinates for first level, for rat sprite 325
                ratblock.raty = screenheight-115 - ratblock.ratheight # 115
                

                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 573 - flagblock.flagsize[1] / 1.4
                
                testblock.x = 10
                testblock.y = screenheight- 59 - testblock.blockheight

                platforms = Platform.Level1()
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and menuselector == 1):
                levelselectorbool = True
                gamedisplay = -1
                pygame.time.wait(100)
            
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and menuselector == 2):
                return

        elif(gamedisplay == -1):
            screen.blit(levelselgraphic, (0, 0))
            if levelselector == 1:
                level1 = font.render("Level1", True, (255, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level1 = font.render("Level1", True, (0, 0, 0))
                levelselgraphic.blit(level1, level1pos)

            if levelselector == 2:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (255, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level2 = font.render("Level2", True, (0, 0, 0))
                levelselgraphic.blit(level2, level2pos)

            if levelselector == 3:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (255, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level3 = font.render("Level3", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)

            if levelselector == 4:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                level4 = font.render("Level4", True, (255, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level4 = font.render("Level4", True, (0, 0, 0))
                levelselgraphic.blit(level4, level4pos)

            if levelselector == 5:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                level4 = font.render("Level4", True, (0, 0, 0))
                level5 = font.render("Level5", True, (255, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level5 = font.render("Level5", True, (0, 0, 0))
                levelselgraphic.blit(level5, level5pos)

            if levelselector == 6:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                level4 = font.render("Level4", True, (0, 0, 0))
                level5 = font.render("Level5", True, (0, 0, 0))
                level6 = font.render("Level6", True, (255, 0, 0))
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                level6 = font.render("Level6", True, (0, 0, 0))
                levelselgraphic.blit(level6, level6pos)


            if levelselmain:
                level1 = font.render("Level1", True, (0, 0, 0))
                level2 = font.render("Level2", True, (0, 0, 0))
                level3 = font.render("Level3", True, (0, 0, 0))
                level4 = font.render("Level4", True, (0, 0, 0))
                level5 = font.render("Level5", True, (0, 0, 0))
                level6 = font.render("Level6", True, (0, 0, 0))
                mainmen = font.render("Main menu", True, (255, 0, 0))
                levelselgraphic.blit(level3, level3pos)
                levelselgraphic.blit(level2, level2pos)
                levelselgraphic.blit(level1, level1pos)
                levelselgraphic.blit(level4, level4pos)
                levelselgraphic.blit(level5, level5pos)
                levelselgraphic.blit(level6, level6pos)
                levelselgraphic.blit(mainmen, mainmenpos)
            else:
                mainmen = font.render("Main menu", True, (0, 0, 0))
                levelselgraphic.blit(mainmen, mainmenpos)

            if levelselector < 1:
                levelselector = 6
            elif levelselector > 6:
                levelselector = 1


            if(pygame.key.get_pressed()[pygame.K_RETURN] and levelselmain):
                gamedisplay = 0
                pygame.time.wait(100)
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 1):
                gamedisplay = 1
                batblock.batx = 650 # Cordinates for first level, for bat sprite 
                batblock.baty = 500

                ratblock.ratx = 325 # Cordinates for first level, for rat sprite 325
                ratblock.raty = screenheight-115 - ratblock.ratheight # 115


                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 573 - flagblock.flagsize[1] / 1.4
                testblock.x = 10
                testblock.y = screenheight- 59 - testblock.blockheight
                platforms = Platform.Level1()
                levelselectorbool = False
                pygame.time.wait(100)
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 2):
                gamedisplay = 2
                platforms = Platform.Level2()
                batblock.batx = 400
                batblock.baty = 400
                ratblock.ratx = 600
                ratblock.raty = screenheight - 115 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                    batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = screenheight - 59 - testblock.blockheight   
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 573 - flagblock.flagsize[1] / 1.4
                testblock.gamedisplay = 2  
                levelselectorbool = False
                levelselector = 1
                pygame.time.wait(100)
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 3):
                gamedisplay = 3
                platforms = Platform.Level3()
                batblock.batx = 750
                batblock.baty = 350
                ratblock.ratx = 600
                ratblock.raty = screenheight - 220 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 650
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = screenheight - 50 - flagblock.flagsize[1] / 1.4
                testblock.gamedisplay = 3  
                levelselectorbool = False
                levelselector = 1
                pygame.time.wait(100)
                
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 4):
                gamedisplay = 4
                platforms = Platform.Level4()
                batblock.batx = 650
                batblock.baty = 350
                ratblock.ratx = 120
                ratblock.raty = screenheight - 190 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 612
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 375
                testblock.gamedisplay = 4  
                levelselectorbool = False
                levelselector = 1
                testblock.vel_y = 0
                pygame.time.wait(100)

            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 5):
                gamedisplay = 5
                platforms = Platform.Level5()
                batblock.batx = 476
                batblock.baty = 300
                ratblock.ratx = 167
                ratblock.raty = 215
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 382
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 640
                testblock.gamedisplay = 5  
                levelselectorbool = False
                levelselector = 1
                testblock.vel_y = 0
                pygame.time.wait(100)
                
            elif(pygame.key.get_pressed()[pygame.K_RETURN] and levelselector == 6):
                gamedisplay = 6
                platforms = Platform.Level5()
                batblock.batx = 101
                batblock.baty = 555
                ratblock.ratx = 333
                ratblock.raty = 655
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.vel_y = 0
                testblock.x = 10
                testblock.y = 646
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 640
                testblock.gamedisplay = 6  
                levelselectorbool = False
                levelselector = 1
                testblock.vel_y = 0
                pygame.time.wait(100)


        elif(gamedisplay == 1): # FIRST LEVEL HERE
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                screen.blit(bg, (0, 0))
                screen.blit(level1img, (0, 0))
                fireblock.place(screenwidth//5,screenheight-90,screen) # X position , Y position , screen
                collision(testblock,fireblock,batblock,ratblock)
                fireblock.place(screenwidth//4,screenheight-90,screen) # X position , Y position , screen
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                collision(testblock,fireblock,batblock,ratblock)
                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level2()
                    batblock.batx = 400
                    batblock.baty = 400
                    ratblock.ratx = 600
                    ratblock.raty = screenheight - 115 - ratblock.ratheight
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.x = 10
                    testblock.y = screenheight - 50 - testblock.blockheight   
                    gamedisplay = 2
                    testblock.gamedisplay = 2               
                batblock.batmove(100) # Length of flight
                ratblock.ratmove(100) # Length of movement
                
                testblock.update()


            elif(testblock.life == 0):
                batblock.batx = 650
                batblock.baty = 500
                ratblock.ratx = 325
                ratblock.raty = screenheight - 115 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                    batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 612
                testblock.vel_y = 0
                testblock.life = 1

        elif(gamedisplay == 2): # SECOND LEVEL
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                screen.blit(bg, (0, 0))
                screen.blit(level2img, (0, 0))
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                fireblock.place(-100,-100,screen)
                collision(testblock,fireblock,batblock,ratblock)
                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level3()
                    batblock.batx = 750
                    batblock.baty = 350
                    ratblock.ratx = 600
                    ratblock.raty = screenheight - 220 - ratblock.ratheight
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.x = 10
                    testblock.y = 612
                    flagblock.flagx = screenwidth - flagblock.flagsize[0]
                    flagblock.flagy = screenheight - 50 - flagblock.flagsize[1] / 1.4
                    gamedisplay = 3
                    testblock.gamedisplay = 3   
                batblock.batmove(100) # Length of flight
                ratblock.ratmove(50) # Length of movement
                
                testblock.update()


            elif(testblock.life == 0):
                batblock.batx = 400
                batblock.baty = 400
                ratblock.ratx = 600
                ratblock.raty = screenheight - 115 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                    batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 612
                testblock.vel_y = 0
                testblock.life = 1
    

        elif(gamedisplay == 3): # Third level
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                if(havekey and not open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level3img, (0, 0))
                    doorblock.place(908,screenheight-90,screen,-100,-100)
                elif(havekey and open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level3img, (0, 0))
                    doorblock.place(-100,-100,screen,-100,-100)
                else:
                    screen.blit(bg, (0, 0))
                    screen.blit(level3img, (0, 0))
                    doorblock.place(908,screenheight-90,screen,screenwidth-50,375)
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                fireblock.place(800,screenheight-90,screen)
                collision(testblock,fireblock,batblock,ratblock)
                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level4()
                    batblock.batx = 650
                    batblock.baty = 350
                    ratblock.ratx = 120
                    ratblock.raty = screenheight - 190 - ratblock.ratheight
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.x = 10
                    testblock.y = 672
                    testblock.vel_y = 0
                    flagblock.flagx = screenwidth - flagblock.flagsize[0]
                    flagblock.flagy = 375
                    havekey = False
                    open = False
                    gamedisplay = 4
                    testblock.gamedisplay = 4   

                if(testblock.char1.colliderect(doorblock.keychar)):
                    havekey = True
                if(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and not havekey and testblock.y >= doorblock.doorchar.y):
                    testblock.x = doorblock.doorchar.x - testblock.blockwidth + 10
                elif(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and havekey and testblock.y >= doorblock.doorchar.y):
                    open = True
                batblock.batmove(40) # Length of flight
                ratblock.ratmove(80) # Length of movement
                testblock.update()
            


            elif(testblock.life == 0):
                batblock.batx = 750
                batblock.baty = 350
                ratblock.ratx = 600
                ratblock.raty = screenheight - 220 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.y = 612
                testblock.vel_y = 0
                testblock.x = 10
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = screenheight - 50 - flagblock.flagsize[1] / 1.4
                havekey = False
                open = False
                testblock.life = 1
                
            
        elif(gamedisplay == 4): # Fourth level
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                if(havekey and not open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level4img, (0, 0))
                    doorblock.place(890,380,screen,-100,-100)
                elif(havekey and open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level4img, (0, 0))
                    doorblock.place(-100,-100,screen,-100,-100)
                else:
                    screen.blit(bg, (0, 0))
                    screen.blit(level4img, (0, 0))
                    doorblock.place(890,380,screen,9,406)

                fireblock.place(87,455,screen)
                collision(testblock,fireblock,batblock,ratblock)
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                fireblock.place(326,455,screen)
                collision(testblock,fireblock,batblock,ratblock)
                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level5()
                    batblock.batx = 476
                    batblock.baty = 300
                    ratblock.ratx = 167
                    ratblock.raty = 215
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.x = 10
                    testblock.y = 382
                    flagblock.flagx = screenwidth - flagblock.flagsize[0]
                    flagblock.flagy = 640
                    havekey = False
                    open = False
                    gamedisplay = 5
                    testblock.gamedisplay = 5

                if(testblock.char1.colliderect(doorblock.keychar)):
                    havekey = True
                if(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and not havekey and testblock.y >= doorblock.doorchar.y):
                    testblock.x = doorblock.doorchar.x - testblock.blockwidth + 10
                elif(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and havekey and testblock.y >= doorblock.doorchar.y):
                    open = True
                batblock.batmove(40) # Length of flight
                ratblock.ratmove(70) # Length of movement
                testblock.update()
            
            


            elif(testblock.life == 0):
                batblock.batx = 650
                batblock.baty = 350
                ratblock.ratx = 120
                ratblock.raty = screenheight - 190 - ratblock.ratheight
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 612
                testblock.vel_y = 0
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 375
                havekey = False
                open = False
                testblock.life = 1


        elif(gamedisplay == 5): # Fifth level
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                if(havekey and not open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level5img, (0, 0))
                    doorblock.place(925,645,screen,-100,-100)
                elif(havekey and open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level5img, (0, 0))
                    doorblock.place(-100,-100,screen,-100,-100)
                else:
                    screen.blit(bg, (0, 0))
                    screen.blit(level5img, (0, 0))
                    doorblock.place(925,645,screen,413,206)
                fireblock.place(100,375,screen)
                collision(testblock,fireblock,batblock,ratblock)
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                fireblock.place(740,200,screen)
                collision(testblock,fireblock,batblock,ratblock)
                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level6()
                    batblock.batx = 101
                    batblock.baty = 555
                    ratblock.ratx = 333
                    ratblock.raty = 655
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.vel_y = 0
                    testblock.x = 10
                    testblock.y = 646
                    flagblock.flagx = screenwidth - flagblock.flagsize[0]
                    flagblock.flagy = 640
                    havekey = False
                    open = False
                    gamedisplay = 6
                    testblock.gamedisplay = 6

                if(testblock.char1.colliderect(doorblock.keychar)):
                    havekey = True
                if(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and not havekey and testblock.y >= doorblock.doorchar.y):
                    testblock.x = doorblock.doorchar.x - testblock.blockwidth + 10
                elif(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and havekey and testblock.y >= doorblock.doorchar.y):
                    open = True
                batblock.batmove(40) # Length of flight
                ratblock.ratmove(70) # Length of movement
                testblock.update()
            


            elif(testblock.life == 0):
                batblock.batx = 476
                batblock.baty = 300
                ratblock.ratx = 167
                ratblock.raty = 215
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.x = 10
                testblock.y = 382
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 640
                havekey = False
                open = False
                testblock.life = 1


        elif(gamedisplay == 6): # Sixth level
            if(testblock.life == 1):
                for platform in platforms:
                    screen.blit(platform.image, platform.rect)
                if(havekey and not open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level6img, (0, 0))
                    doorblock.place(921,645,screen,-100,-100)
                elif(havekey and open):
                    screen.blit(bg, (0, 0))
                    screen.blit(level6img, (0, 0))
                    doorblock.place(-100,-100,screen,-100,-100)
                else:
                    screen.blit(bg, (0, 0))
                    screen.blit(level6img, (0, 0))
                    doorblock.place(921,645,screen,44,515)
                if testblock.havepotion:
                    potionblock.place(-100,-100,screen)
                else:
                    potionblock.place(625,590,screen)
                fireblock.place(235,640,screen)
                collision(testblock,fireblock,batblock,ratblock)
                batblock.batplace(screen)
                ratblock.ratplace(screen)
                flagblock.flagplace(screen)
                fireblock.place(795,640,screen)
                collision(testblock,fireblock,batblock,ratblock)

                if(testblock.char1.colliderect(potionblock.potionchar)):
                    testblock.havepotion = True

                if(testblock.char1.colliderect(flagblock.flagchar)):
                    platforms = Platform.Level1()
                    batblock.batx = 476
                    batblock.baty = 334
                    ratblock.ratx = 550
                    ratblock.raty = screenheight - 130 - ratblock.ratheight
                    batblock.batflycounter = 0
                    if (batblock.batspeedx < 0):
                        batblock.batspeedx *= -1
                    ratblock.ratmovecounter = 0
                    if (ratblock.ratspeedx < 0):
                        ratblock.ratspeedx *= -1
                    testblock.x = 10
                    testblock.y = 420-testblock.blockheight  
                    gamedisplay = 0
                    testblock.gamedisplay = 1

                if(testblock.char1.colliderect(doorblock.keychar)):
                    havekey = True
                if(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and not havekey and testblock.y >= doorblock.doorchar.y):
                    testblock.x = doorblock.doorchar.x - testblock.blockwidth + 10
                elif(testblock.x + testblock.blockwidth >= doorblock.doorchar.x +10 and havekey and testblock.y >= doorblock.doorchar.y):
                    open = True
                batblock.batmove(50) # Length of flight
                ratblock.ratmove(150) # Length of movement
                testblock.update()
            


            elif(testblock.life == 0):
                batblock.batx = 101
                batblock.baty = 555
                ratblock.ratx = 333
                ratblock.raty = 655
                batblock.batflycounter = 0
                if (batblock.batspeedx < 0):
                     batblock.batspeedx *= -1
                ratblock.ratmovecounter = 0
                if (ratblock.ratspeedx < 0):
                    ratblock.ratspeedx *= -1
                testblock.vel_y = 0
                testblock.x = 10
                testblock.y = 646
                flagblock.flagx = screenwidth - flagblock.flagsize[0]
                flagblock.flagy = 640
                havekey = False
                open = False
                testblock.havepotion = False
                testblock.life = 1

        pygame.display.flip()
main()