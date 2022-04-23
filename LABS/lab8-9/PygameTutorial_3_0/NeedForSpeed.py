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
PLAYER_SPEED = 3
SCORE = 0
MONEY = 0

#Setting up Font
my_font = pg.font.SysFont("Verdana", 25)

background = pg.image.load("images/bcg.png")

#Create a white screen 
DISPLAYSURF = pg.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pg.display.set_caption("Game")

class Coin(pg.sprite.Sprite):
    def __init__(self, name, fraquency):
        super().__init__()
        self.image = pg.image.load('images/' + name + '.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.f = fraquency
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -1500 * self.f)

    def move(self):
        self.rect.move_ip(0,6)
        if (self.rect.bottom > 600):
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -random.randint(300, 1600))

    def new(self):
        # Allocate coin on height according to frequency
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), -1000 * self.f)

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
C1 = Coin('coin', 0.8)
C2 = Coin('star', 5)
C3 = Coin('spike', 7)

#Creating Sprites Groups
enemies = pg.sprite.Group(E1)
coins = pg.sprite.Group([C1, C2, C3])

all_sprites = pg.sprite.Group([P1, E1, C1, C2, C3])

#Adding a new User event 
INC_ENEMY_SPEED = pg.USEREVENT + 1
pg.time.set_timer(INC_ENEMY_SPEED, 1000)

INVISIBILITY = pg.USEREVENT + 2
STOP = pg.USEREVENT + 3

#Variables
make_inv = False
stop = False
inv_img = pg.image.load('images/tr_car.png')
orig_img = P1.image
orig_spd = 3
HIGHEST_SCORE = 0

#Highest score
f = open('HighestScore', 'r')
HIGHEST_SCORE = f.readline()
f.close()
    
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
        
        # Return to original condition
        if event.type == INVISIBILITY:
            make_inv = False
            P1.image = orig_img
        elif event.type == STOP:
            stop = False
            PLAYER_SPEED = orig_spd
        
        # Change music by space
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            Next = True
            cur_song += 1

        # Quit
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    # To make invisible or stop player
    if make_inv: P1.image = inv_img
    if stop:
        stop = False
        orig_spd = PLAYER_SPEED
        PLAYER_SPEED = 0

    #Music Stuff
    if pg.mixer.music.get_pos() / 1000 > song_s[cur_song % 2]:
        cur_song += 1
        Next = True
    if Next:
        Next = False
        pg.mixer.music.load(songs[cur_song])
        pg.mixer.music.play()
    
    #Making text
    scores = my_font.render('Score: ' + str(SCORE), True, BLACK)
    h_score = my_font.render('Highest Score: ' + str(HIGHEST_SCORE), True, BLACK)
    money = my_font.render(str(MONEY), True, pg.Color('yellow'))
    speed = my_font.render('SPEED: ' + str(PLAYER_SPEED), True, pg.Color('red'))
    
    
    #Displaying text
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(h_score, (10, 50))
    DISPLAYSURF.blit(money, (SCREEN_WIDTH - 40, 10))
    DISPLAYSURF.blit(speed, (SCREEN_WIDTH - 130, 50))

    #Speed-boost for money
    if MONEY == 5:
        PLAYER_SPEED = 5
    elif MONEY == 10:
        PLAYER_SPEED = 8
    elif MONEY == 15:
        PLAYER_SPEED = 12
    elif MONEY == 20:
        PLAYER_SPEED = 15
    elif MONEY == 15:
        PLAYER_SPEED = 20

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

     
    if pg.sprite.spritecollideany(P1, coins):
        #To be run when coin collected   
        if P1.rect.colliderect(C1.rect):
            pg.mixer.Sound('sounds/coin.wav').play()
            MONEY += 1
            C1.new()
        #To be run when star collected      
        if P1.rect.colliderect(C2.rect):
            make_inv = True
            pg.mixer.Sound('sounds/star.wav').play()
            pg.time.set_timer(INVISIBILITY, 7000)
            C2.new()
        #To be run when spike collected       
        if P1.rect.colliderect(C3.rect):
            stop = True
            pg.mixer.Sound('sounds/spike.wav').play()
            pg.time.set_timer(STOP, 3000)
            C3.new()
            
        pg.display.update()
        
    #To be run if collision occurs between Player and Enemy
    if pg.sprite.spritecollideany(P1, enemies) and not make_inv:
        #Write down current score
        f = open('HighestScore', 'w')
        f.write(str(SCORE))
        f.close()
        
        #Play crash sound
        pg.mixer.Sound('sounds/crash.wav').play()
        pg.mixer.music.stop()
        
        time.sleep(1)
        
        pg.quit()
        sys.exit()
        
    pg.display.update()
    FramePerSec.tick(FPS)
