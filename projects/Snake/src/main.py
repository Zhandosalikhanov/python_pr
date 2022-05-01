# Import libraries
import pygame as pg, time
from random import *
from functions import *
pg.init()

# Setting up constants
N, M = 30, 20
CELL = 20
dim = width, height = CELL * N, CELL * M

# Return speed and max-score according to level
GET_ATTRIBUTES = {
    1 : (200, 10, 'Level 1'),
    2 : (175, 15, 'Level 2'),
    3 : (150, 20, 'Level 3'),
    4 : (125, 25, 'Level 4'),
    5 : (100, 30, 'Level 5'),
    6 : (75 , 35, 'Level 6'),
    7 : (50 , 40, 'Level 7')
}

# Function to get wall positions
def get_walls(screen):
    poses = []
    for i in range(N - 1):
        for j in range(M - 1):
            c = screen.get_at((i * CELL + 1, j * CELL + 1))
            if c[0] < 20 and c[1] < 20 and c[2] < 20:
                poses.append([i, j])
    return poses

WALLS = get_walls(pg.image.load('../levels/Level 1.jpg'))

# Recursion function to generate food NOT on snake and walls
def NotOnSnake(snake: list):
    x = randint(0, N - 1)
    y = randint(0, M - 1)
    
    # Repeat random if food coor-s are in snake coor-s 
    if snake.count([x, y]) or WALLS.count([x, y]):
        return NotOnSnake(snake)
    return [x, y]

# Class for snake
class Snake(pg.sprite.Sprite):
    # Initial body, size and direction
    def __init__(s):
        super().__init__()
        s.poses = [[1, 1]]
        s.dir = "No direction. Don't move at the start)"
        s.size = 1
    
    def move(s):
        # Function to move snake   
        if s.size > 1: 
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
    def CheckFood(s, foods):
        for f in foods:
            # Check if any food has been eaten
            if s.poses[0][0] == f.pos[0] and s.poses[0][1] == f.pos[1]:
                # Increase the size of the snake with respect to the food
                s.size += f.weight
                f.pos = NotOnSnake(s.poses)
                for i in range(s.size): s.poses.append([-1, -1])
                return f.weight

        return 0
    
    # Check snake collision with walls
    def CheckWall(s, walls):
        if walls.count(s.poses[0]):
            return 1
        return 0
        
    # Draw the whole snake onto the screen            
    def draw(s, screen):
        for i in range(s.size):
            color = pg.Color('white') if i == 0 else pg.Color('red')
            x, y = s.poses[i][0] * CELL, s.poses[i][1] * CELL
            pg.draw.rect(screen, color, pg.Rect(x, y, CELL, CELL))
                 
# Class for food
class Food(pg.sprite.Sprite):
    
    # Initial position
    def __init__(f, weight, image_path):
        super().__init__()
        f.image = pg.image.load(image_path).convert_alpha()
        f.image = pg.transform.scale(f.image, (CELL, CELL))
        f.rect = f.image.get_rect()
        f.pos = NotOnSnake([[1, 1]])
        f.weight = weight
    
    # Draw food on the screen
    def blit(f, screen):
        x, y = f.pos[0] * CELL, f.pos[1] * CELL 
        f.rect.topleft = (x, y)
        screen.blit(f.image, f.rect)

def main():
    # Setting up screen
    scr = pg.display.set_mode(dim)
    
    # LogIn, Loading, and menu screen
    LOGIN_BCG   = pg.image.load('../images/LogIn.jpg').convert()
    MENU_BCG    = pg.image.load('../images/menu.jpg').convert()
    LOADING_BCG = pg.image.load('../images/Load.jpg').convert()

    # Setting up fonts
    myFont   = pg.font.SysFont('georgia', 20, True)
    coolFont = pg.font.SysFont('nsimsun', 20, False, True)

    # Variables
    Initialize = True
    Playing    = False
    _LogIn     = True
    LEVEL      = 1
    SCORE      = 0
    Name       = ''
    
    # Function to Initialize everything
    def init(cur_level):
        global S, bcg, WALLS, DELAY
        
        # Loading screen
        scr.blit(LOADING_BCG, (0, 0))
        pg.display.flip()
        time.sleep(3)
        
        # Setting up background
        bcg = pg.image.load(f'../levels/Level {cur_level}.jpg').convert()

        # Write positions of new walls
        WALLS = get_walls(bcg)
        
        # Recreate food
        global F1, F2, FOODS
        F1 = Food(1, '../images/apple.png')
        F2 = Food(2, '../images/star.png')
        FOODS = pg.sprite.Group([F1, F2])
        
        # Creating Snake
        S = Snake()
        
        # Set cursor back to default
        pg.mouse.set_cursor()
        
        # Timer for snake to move
        DELAY = pg.USEREVENT + 1
        pg.time.set_timer(DELAY, GET_ATTRIBUTES[cur_level][0])
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        
        # To be run if we're not playing
        if not Playing:     
            
            # Set the title
            pg.display.set_caption("Snake game")
            
            # Play music
            if not pg.mixer.music.get_busy():
                pg.mixer.music.load('../songs/Intro.mp3')
                pg.mixer.music.play(100)    
                
            # To be run if user is logging in
            if _LogIn:
                
                # Blit LogIn background
                scr.blit(LOGIN_BCG, (0, 0))
                
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
                                SCORE = view(Name, 'score')[0][0]
                                LEVEL = view(Name, 'level')[0][0]
                            
                        # Delete one char if backspace was pressed
                        elif e.key == pg.K_BACKSPACE: Name = Name[:-1]
                        # Write down characters
                        elif len(Name) < 24: Name += e.unicode
                
                # Blit typed word onto the screen
                txt = myFont.render(Name, True, 0)
                scr.blit(txt, (155, 230))
            
            # To be run if user LOGGED IN
            else:
                # Check if paly or logIn button was pressed
                clicked_logIn = lambda pos: pos[0] > 220 and pos[0] < 380 and pos[1] > 160 and pos[1] < 240
                clicked_play = lambda pos: pos[0] > 220 and pos[0] < 380 and pos[1] > 263 and pos[1] < 325

                # Blit menu background
                scr.blit(MENU_BCG, (0, 0))
                
                for e in pg.event.get():
                    # Quit
                    if e.type == pg.QUIT: going = False

                    # Check if button was clicked
                    if e.type == pg.MOUSEBUTTONDOWN:
                        if clicked_logIn(e.pos):
                            _LogIn = True
                            Name = ''
                        elif clicked_play(e.pos):
                            pg.mixer.music.load('../songs/Play.mp3')
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
                # Set the title
                pg.display.set_caption(GET_ATTRIBUTES[LEVEL][2])
                Initialize = False
                init(LEVEL)
                pg.event.clear()
                
            # Display current level background
            scr.blit(bcg, (0, 0))
            
            # Render score and level
            txt = 'Score: ' + str(SCORE) + ' / ' + str(GET_ATTRIBUTES[LEVEL][1])
            SCORE_TXT = myFont.render(txt, True, pg.Color('green'))
            
            # Increase the level if max-score is reached
            if SCORE > GET_ATTRIBUTES[LEVEL][1]:
                Initialize = True
                SCORE = 0
                LEVEL += 1
            
            # Handle events
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False

                if e.type == pg.KEYDOWN:
                    # Quit if Escape was pressed  
                    if e.key == pg.K_ESCAPE:
                        going = False

                    # Stop music
                    if e.key == pg.K_m:
                        if pg.mixer.music.get_busy(): pg.mixer.music.pause()
                        else: pg.mixer.music.unpause()
                    
                # Move snake after some milliseconds
                if e.type == DELAY: S.move()
                
                # Change direction with keys
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_LEFT and S.dir != 2:   S.dir = 1
                    if e.key == pg.K_RIGHT and S.dir != 1:  S.dir = 2
                    if e.key == pg.K_UP and S.dir != 0:     S.dir = 3
                    if e.key == pg.K_DOWN and S.dir != 3:   S.dir = 0
                
            # Increase score if food was eaten
            SCORE += S.CheckFood(FOODS)
            
            # Die if collision occurs
            if S.CheckWall(WALLS):
                SCORE, LEVEL = 0, 1
                Playing = False
            
            # Draw and blit            
            S.draw(scr)
            for f in FOODS:
                f.blit(scr)
            
            # Display score and level
            scr.blit(SCORE_TXT, (10, 5))
        
        # Update screen
        pg.display.flip()
        fps.tick(480)

    # Save everything
    ChangeData(Name, SCORE, LEVEL)
    
# Launcher Code    
if __name__ == '__main__':
    main()
    pg.quit()