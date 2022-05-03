# Importing libraries
import pygame as pg
import math 
from slider import Slider
        
class Pendulum:
    """Class to create a ball with the given image and size"""
    def __init__(self, length, pivot, Angle0, amplitude= 1.5):
        """Function to initialize ball object

        Args:
            size (int): Radius of the ball
            length (int): Length of the rope the ball will be attached to
            amplitude (float): The maximum displacement og the ball from the equilibrium
            pivot (tuple): The fixed point on which the rope will be attached on
            Angle0 (float): The initial angle of the pendulum
        """
        self.image = pg.image.load("images/Ball.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect  = self.image.get_rect()
        self.angle0 = Angle0
        self.AMPLITUDE = amplitude
        self.lenght = length
        self.pivot = pivot
        self.OMEGA = math.sqrt(9.8 / length)
        
    def move(self, AIR_FRICTION, time):
        """Function to move the ball with its velocity and angle and decrease its speed due to air friction

        Args:
            AIR_FRICTION (float): Friction of the air that causes decceleration in the balls speed
            time (float): Current time to calculate the angle
        """
        self.angle = self.AMPLITUDE  * math.sin(self.OMEGA * time + self.angle0)
        self.x = self.pivot[0] - math.sin(self.angle) * self.lenght
        self.y = self.pivot[1] + math.cos(self.angle) * self.lenght
        self.AMPLITUDE *= AIR_FRICTION
    
    def blit(self, screen):
        """Function to blit the object onto the screen

        Args:
            screen (Pygame Surface): Surface on which the ball will be displayed
        """
        self.rect.center = (self.x, self.y)
        pg.draw.line(screen, (255, 255, 255), self.pivot, (self.x, self.y), 2)
        screen.blit(self.image, self.rect)
    
# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 1000, 600
    scr = pg.display.set_mode(dim)
    pg.display.set_caption("Simple Pendulums! Press R to restart")
    
    # Set up background
    bcg = pg.image.load('images/bcg.jpg').convert()
    bcg = pg.transform.scale(bcg, dim)
    
    # Create Pendulums
    def init():
        global Pendulums
        Pendulums = []
        for i in range(7):
            p = Pendulum(125 + i * 60, (W / 2, 75), math.radians(0 * 22.5 + 90))
            Pendulums.append(p)
    init()    
        
    # Variables
    t = 0
    dt = 0.1
    
    # Constants
    AIR_FRICTION = 1
    VARIANTS = [0.99, 0.993, 0.995, 0.997, 1]
    
    # Make Sliders
    AirS = Slider(900, 20, 90, 20, "Air Friction", 0, 4, 0, 'grey', False)
    DT   = Slider(900, 100, 90, 20, "Time Rate", 0.01, 2, dt, 'grey', True)
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Loop through the events                                       
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
            
            if e.type == pg.MOUSEBUTTONDOWN:
                if AirS.rect.collidepoint(e.pos): AirS.change = True
                if DT.rect.collidepoint(e.pos): DT.change = True
                
            if e.type == pg.MOUSEBUTTONUP:
                AirS.change = False
                DT.change = False
            
            if e.type == pg.KEYDOWN and e.key == pg.K_r:
                t = 0
                init()
            
        pos = pg.mouse.get_pos()
        if AirS.change:
            AirS.move(pos)
            AIR_FRICTION = VARIANTS[-(AirS.value + 1)]
            
        if DT.change: 
            DT.move(pos)
            dt = DT.value
            
        # Tick
        t += dt
        
        # Blit the background
        scr.blit(bcg, (0, 0))
        
        # Blit the and move objects
        for p in Pendulums:
            p.move(AIR_FRICTION, t)
            p.blit(scr)
        
        AirS.blit(scr)
        DT.blit(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()