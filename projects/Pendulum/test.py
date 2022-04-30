# Importing libraries
import pygame as pg
import math

class Ball(pg.sprite.Sprite):
    def __init__(self, Tetta):
        super().__init__()
        self.image = pg.image.load('Ball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.Tetta = Tetta
        self.x = pivot[0] - math.sin(Tetta) * l
        self.y = math.cos(Tetta) * l - pivot[1]
        
    def move(self, Tetta):
        self.x = pivot[0] - math.sin(Tetta) * l
        self.y = pivot[1] + math.cos(Tetta) * l
        
    
# Driver code
def main():
    # Tetta0 = float(input("Please enter the initial angle: "))
    
    # Setting up dimensions and screen
    dim = W, H = 400, 300
    scr = pg.display.set_mode(dim)
    
    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    # Constants
    global pivot, l
    
    l = 150
    pivot = (W / 2, 0)
    g = 9.8
    t = 0
    A = 1.5
    w = math.sqrt(g / l)
    Tetta = A * math.sin(w * t)
    
    # Creating object
    B = Ball(Tetta)
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
                
        # Fill screen with white
        scr.fill(WHITE)
        
        # Change angle
        t += 0.04
        Tetta = A * math.sin(w * t)
        
        # Move the ball
        B.move(Tetta)
        
        # Draw Ball and Rope
        pg.draw.line(scr, RED, (B.x, B.y), pivot, 2)        
        pg.draw.circle(scr, 0, (B.x, B.y), 5)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()