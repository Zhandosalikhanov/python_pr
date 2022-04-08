#Imports
import pygame as pg
from pygame.locals import *
import random, time, sys

#Initialzing 
pg.init()

#Setting up FPS 
FPS = 60
FramePerSec = pg.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ENEMY_SPEED = 5
PLAYER_SPEED = 5
SCORE = 0
MONEY = 0

#Setting up Fonts
font_small = pg.font.SysFont("Verdana", 35)
my_font = pg.font.SysFont("Verdana", 25)

background = pg.image.load("images/bcg.png")

#Create a white screen 
DISPLAYSURF = pg.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pg.display.set_caption("Game")

class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load('images/coin.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        self.rect.move_ip(0,6)
        if (self.rect.bottom > 600):
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -random.randint(300, 1600))

    def new(self):
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -random.randint(300, 1600))

class Button(pg.sprite.Sprite):
    def __init__(self, name, pos):
        super().__init__()
        self.image = pg.image.load('images/' + name + '.png')
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = pos

    def clicked(self, mouse):
        return self.rect.collidepoint(mouse)

class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,ENEMY_SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pg.image.load("images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pg.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-PLAYER_SPEED, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(PLAYER_SPEED, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pg.sprite.Group()
enemies.add(E1)

coins = pg.sprite.Group()
coins.add(C1)

all_sprites = pg.sprite.Group()
all_sprites.add(P1, E1, C1)

#Adding a new User event 
INC_ENEMY_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_ENEMY_SPEED, 2000)

#Songs
songs = ['songs/GasGasGas.mp3', 'songs/Rampant.mp3']
song_s = [273, 179]
cur_song = 0
Next = True

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pg.event.get():
        if event.type == INC_ENEMY_SPEED:
              ENEMY_SPEED += 0.2     
        
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            Next = True
            cur_song += 1

        if event.type == QUIT:
            pg.quit()
            sys.exit()

    #Music Stuff
    if pg.mixer.music.get_pos() / 1000 > song_s[cur_song % 2]:
        cur_song += 1
        Next = True
    
    if Next:
        Next = False
        pg.mixer.music.load(songs[cur_song])
        pg.mixer.music.play()
    
    #Displaying Score and Money
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    money = font_small.render(str(MONEY), True, pg.Color('yellow'))
    DISPLAYSURF.blit(money, (SCREEN_WIDTH - 40, 10))
    speed = my_font.render('SPEED: ' + str(PLAYER_SPEED), True, pg.Color('red'))
    DISPLAYSURF.blit(speed, (SCREEN_WIDTH - 120, 40))

    #Speed-boost for money
    if MONEY == 5:
        PLAYER_SPEED = 7
    elif MONEY == 10:
        PLAYER_SPEED = 9
    elif MONEY == 15:
        PLAYER_SPEED = 12

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #To be run when coin collected    
    if pg.sprite.spritecollideany(P1, coins):
        pg.mixer.Sound('sounds/coin.wav').play()
        MONEY += 1
        C1.new()
        pg.display.update()
        
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P1, enemies):
        pg.mixer.Sound('sounds/crash.wav').play()
        pg.mixer.music.stop()
        time.sleep(1)
        pg.quit()
        sys.exit()
        
    pg.display.update()
    FramePerSec.tick(FPS)
