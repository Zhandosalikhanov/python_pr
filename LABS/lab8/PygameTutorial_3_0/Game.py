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
SPEED = 5
SCORE = 0
MONEY = 0

#Setting up Fonts
font = pg.font.SysFont("Verdana", 60)
font_small = pg.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pg.image.load("images/AnimatedStreet.png")

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
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), random.randint(40, (SCREEN_HEIGHT // 2) - 50))

    def new(self):
        if rand
        self.rect.top = 0
            
class Enemy(pg.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pg.image.load("images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
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
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

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
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

#Adding a new User event 
INC_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_SPEED, 1000)

#Songs
songs = ['songs/GasGasGas.mp3', 'songs/Rampant.mp3']
song_s = [273, 179]
cur_song = 0
Next = True

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pg.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5      
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    if pg.mixer.music.get_pos() / 1000 > song_s[cur_song % 2]:
        cur_song += 1
        Next = True
    
    if not pg.mixer.music.get_busy() and Next:
        Next = False
        pg.mixer.music.load(songs[cur_song])
        pg.mixer.music.play()
    
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    money = font_small.render(str(MONEY), True, pg.Color('yellow'))
    DISPLAYSURF.blit(money, (SCREEN_WIDTH - 20, 10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        
    if pg.sprite.spritecollideany(P1, coins):
        pg.mixer.Sound('sounds/coin.wav').play()
        MONEY += 1
        C1.new()
        pg.display.update()
        
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P1, enemies):
          pg.mixer.Sound('sounds/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pg.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pg.quit()
          sys.exit()        
        
    pg.display.update()
    FramePerSec.tick(FPS)
