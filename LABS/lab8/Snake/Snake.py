import pygame as pg, levels
from random import *

# Setting up constants
N, M = 30, 20
CELL = 20
dim = width, height = CELL * N, CELL * M

# Recursion function to generate food NOT on snake
def NotOnSnake(snake: list):
    x = randint(0, N - 1)
    y = randint(0, M - 1)
    
    if snake.count([x, y]):
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
class Snake:
    # Initial body, size and direction
    def __init__(s):
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
            # Chaeck if any food has been eaten
            if s.poses[0][0] == f.pos[0] and s.poses[0][1] == f.pos[1]:
                s.size += 1
                s.poses.append([0, 0])
                f.locate(s.poses)
                return f.weight

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
    
    # Creating Snake
    S = Snake()
    
    # Timer for snake to move
    Delay = pg.USEREVENT + 1
    pg.time.set_timer(Delay, 175)
    
    # Setting up font
    myFont = pg.font.SysFont('georgia', 20, True)
    
    # Variables
    Level = 1
    Score = 0
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Fill screen with black
        scr.fill(0)
        
        # Render score and level
        txt = 'Score: ' + str(Score) + ' / ' + str(levels.Score(Level))
        _Score = myFont.render(txt, True, pg.Color('white'))
        txt = 'Level: ' + str(Level) + ' / 6'
        _Levell = myFont.render(txt, True, pg.Color('green'))
        
        # Set speed according to level
        if Level != levels.level(Score):
            Level = levels.level(Score)
            speed = levels.speed(Level)
            pg.time.set_timer(Delay, speed)
        
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT: going = False
            
            # Move snake after 150 milliseconds
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
        
        # Draw and blit            
        S.draw(scr)
        for f in foods:
            f.draw(scr)
        
        # Display score and level
        scr.blit(_Score, (10, 5))
        scr.blit(_Levell, (10, 35))
        
        # Update screen
        pg.display.flip()
        fps.tick(60)

# Launcher Code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()