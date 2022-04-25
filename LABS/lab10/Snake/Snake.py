# Import libraries
import pygame as pg, chars, time
from random import *
from functions import *

# Setting up constants
N, M = 30, 20
CELL = 20
dim = width, height = CELL * N, CELL * M

# Function to get wall positions
def wall_poses(screen):
    poses = []
    for i in range(N - 1):
        for j in range(M - 1):
            c = screen.get_at((i * CELL + 1, j * CELL + 1))
            if c[0] < 20 and c[1] < 20 and c[2] < 20:
                poses.append([i, j])
    return poses

walls = wall_poses(pg.image.load('levels/Level 1.jpg'))

# Recursion function to generate food NOT on snake and walls
def NotOnSnake(snake: list):
    x = randint(0, N - 1)
    y = randint(0, M - 1)
    
    # Repeat random if food coor-s are in snake coor-s 
    if snake.count([x, y]) or walls.count([x, y]):
        return NotOnSnake(snake)
    return [x, y]

# Class for food
class Food(pg.sprite.Sprite):
    pg.init()
    
    # Initial position
    def __init__(f, color, weight, time):
        super().__init__()
        f.color = color
        f.pos = NotOnSnake([[1, 1], [0, 0]])
        f.weight = weight
        f.change = pg.USEREVENT + time
        f.time = time
        f.timer = pg.time.set_timer(f.change, f.time * 1000)
    
    # Function to randomly locate food
    def locate(f, snake):
        f.pos = NotOnSnake(snake)
        f.timer = pg.time.set_timer(f.change, f.time * 1000)
    
    # Draw food on screen
    def draw(f, screen):
        x, y = f.pos[0] * CELL, f.pos[1] * CELL 
        pg.draw.rect(screen, pg.Color(f.color), pg.Rect(x, y, CELL, CELL))

# Make food object
F = Food('green', 1, 9)
F2 = Food('purple', 2, 6)
F3 = Food('yellow', 3, 3)
foods = pg.sprite.Group([F, F2, F3])

# Class for snake
class Snake(pg.sprite.Sprite):
    # Initial body, size and direction
    def __init__(s):
        super().__init__()
        s.poses = [[1, 1], [0, 0]]
        s.dir = 2
        s.size = 1
    
    def move(s):
        # Function to move snake    
        for i in range(s.size, 0, -1):
            s.poses[i][0] = s.poses[i - 1][0]
            s.poses[i][1] = s.poses[i - 1][1]
        
        # Change direction    
        if s.dir == 1: s.poses[0][0] -= 1
        if s.dir == 2: s.poses[0][0] += 1
        
        if s.dir == 0: s.poses[0][1] += 1
        if s.dir == 3: s.poses[0][1] -= 1
        
        # Appear from other side    
        if s.poses[0][0] > N: s.poses[0][0] = 0
        if s.poses[0][0] < 0: s.poses[0][0] = N
        if s.poses[0][1] > M: s.poses[0][1] = 0
        if s.poses[0][1] < 0: s.poses[0][1] = M
           
    # Check if snake have eaten the food
    def check(s):
        for f in foods:
            # Check if any food has been eaten
            if s.poses[0][0] == f.pos[0] and s.poses[0][1] == f.pos[1]:
                # Increase the size of the snake with respect to the food
                s.size += f.weight
                for i in range(f.weight): s.poses.append([-1, -1])
                f.locate(s.poses)
                return f.weight

        return 0
    
    # Check snake collision with walls
    def collision(s, walls):
        
        if walls.count(s.poses[0]):
            return 1
        return 0
        
    # Draw the whole snake onto the screen            
    def draw(s, screen):
        for i in range(s.size):
            color = pg.Color('white') if i == 0 else pg.Color('red')
            x, y = s.poses[i][0] * CELL, s.poses[i][1] * CELL
            pg.draw.rect(screen, color, pg.Rect(x, y, CELL, CELL))

def main():
    # Setting up screen
    scr = pg.display.set_mode(dim)
    
    # Set the title
    pg.display.set_caption("Snake game")
    
    # LogIn, Loading, and menu screen
    LogIn = pg.image.load('images/LogIn.jpg').convert()
    menu_bcg = pg.image.load('images/menu.jpg').convert()
    load_bcg = pg.image.load('images/Load.jpg').convert()

    # Setting up fonts
    myFont = pg.font.SysFont('georgia', 20, True)
    coolFont = pg.font.SysFont('nsimsun', 20, False, True)

    # Variables
    Initialize = True
    Playing = False
    _LogIn = True
    Level = 1
    Score = 0
    Name = ''
    
    # Function to Initialize everything
    def init(level):
        global S, bcg, walls, Delay
        
        # Loading screen
        scr.blit(load_bcg, (0, 0))
        pg.display.flip()
        time.sleep(3)
        
        # Setting up background
        bcg = pg.image.load(f'levels/Level {level}.jpg').convert()

        # Write positions of new walls
        walls = wall_poses(bcg)
        
        # Recreate food
        global F, F2, F3, foods
        F = Food('green', 1, 9)
        F2 = Food('purple', 2, 6)
        F3 = Food('yellow', 3, 3)
        foods = pg.sprite.Group([F, F2, F3])
        
        # Creating Snake
        S = Snake()
        
        # Set cursor back to default
        pg.mouse.set_cursor()
        
        # Timer for snake to move
        Delay = pg.USEREVENT + 1
        pg.time.set_timer(Delay, chars.speed(level))
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        
        # To be run if we're not playing
        if not Playing:     
            # To be run if user is logging in
            if _LogIn:
                
                # Play music
                if not pg.mixer.music.get_busy():
                    pg.mixer.music.load('songs/Intro.mp3')
                    pg.mixer.music.play(100)    
                
                # Blit LogIn background
                scr.blit(LogIn, (0, 0))
                
                for e in pg.event.get():
                    # Quit
                    if e.type == pg.QUIT: going = False

                    # Check typed keys
                    if e.type == pg.KEYDOWN:
                        # Save name if Enter presesd
                        if e.key == pg.K_RETURN:
                            _LogIn = False
                            
                            # If such user doesn't exist, create new one
                            if not len(view(Name, 'name')):
                                InsertData(Name)
                            else:
                                Score = view(Name, 'score')[0][0]
                                Level = view(Name, 'level')[0][0]
                            
                        # Delete one char if backspace was pressed
                        elif e.key == pg.K_BACKSPACE: Name = Name[:-1]
                        # Write down characters
                        elif len(Name) < 24: Name += e.unicode
                
                # Blit typed word onto the screen
                txt = myFont.render(Name, True, 0)
                scr.blit(txt, (155, 230))
            
            # To be run if user LOGGED IN
            else:
                # Play music
                if not pg.mixer.music.get_busy():
                    pg.mixer.music.load('songs/Intro.mp3')
                    pg.mixer.music.play(100)
                
                # Check if paly or logIn button was pressed
                clicked_logIn = lambda pos: pos[0] > 220 and pos[0] < 380 and pos[1] > 160 and pos[1] < 240
                clicked_play = lambda pos: pos[0] > 220 and pos[0] < 380 and pos[1] > 263 and pos[1] < 325

                # Blit menu background
                scr.blit(menu_bcg, (0, 0))
                
                for e in pg.event.get():
                    # Quit
                    if e.type == pg.QUIT: going = False

                    # Check if button was clicked
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if clicked_logIn(e.pos):
                            _LogIn = True
                            Name = ''
                        elif clicked_play(e.pos):
                            pg.mixer.music.load('songs/Play.mp3')
                            pg.mixer.music.play(100)
                            Playing = True
                            Initialize = True

                # Set hand cursor on buttons and default elsewhere
                pos = pg.mouse.get_pos()
                
                if clicked_logIn(pos) or clicked_play(pos): pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                else: pg.mouse.set_cursor()
                
                txt = coolFont.render(f"You are playing as '{Name}' :)", True, 0)
                scr.blit(txt, (3, 3))
        
        # To be run if we're logged in and playing                
        else:
            # Initialize everything according to level
            if Initialize:
                Initialize = False
                init(Level)
                
            # Display current level background
            scr.blit(bcg, (0, 0))
            
            # Render score and level
            txt = 'Score: ' + str(Score) + ' / ' + str(chars.Score(Level))
            _Score = myFont.render(txt, True, pg.Color('white'))
            txt = 'Level: ' + str(Level) + ' / 10'
            _Levell = myFont.render(txt, True, pg.Color('green'))
            
            # Set speed according to level
            if Level != chars.level(Score):
                Initialize = True
                Level = chars.level(Score)
                speed = chars.speed(Level)
                pg.time.set_timer(Delay, speed)
            
            for e in pg.event.get():
                # Quit and save data
                if e.type == pg.QUIT:
                    going = False
                    ChangeData(Name, Score, Level)

                # Save everyting if Escape was pressed and quit    
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        going = False
                        ChangeData(Name, Score, Level)
                    if e.key == pg.K_m:
                        if pg.mixer.music.get_busy(): pg.mixer.music.pause()
                        else: pg.mixer.music.unpause()
                    
                # Move snake after some milliseconds
                if e.type == Delay: S.move()
                
                # Change location of food when time is up
                for f in foods:
                    if e.type == f.change: f.locate(S.poses)
                
                # Change direction with keys
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_LEFT and S.dir != 2: S.dir = 1
                    if e.key == pg.K_RIGHT and S.dir != 1: S.dir = 2
                    if e.key == pg.K_UP and S.dir != 0: S.dir = 3
                    if e.key == pg.K_DOWN and S.dir != 3: S.dir = 0
                
                        
            # Increase score if food was eaten
            Score += S.check()
            
            # Die if collision occurs
            if S.collision(walls):
                S.kill()
                for f in foods: f.kill()
                Score, Level = 0, 1
                ChangeData(Name, Score, Level)
                Playing = False
            
            # Draw and blit            
            S.draw(scr)
            for f in foods:
                f.draw(scr)
            
            # Display score and level
            scr.blit(_Score, (10, 5))
            scr.blit(_Levell, (10, 35))
        
        # Update screen
        pg.display.flip()
        fps.tick(480)

# Launcher Code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()