# Importing libraries
import pygame as pg
import math

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
        self.image = pg.image.load("images/Steel Ball.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect  = self.image.get_rect()
        self.angle0 = Angle0
        self.AMPLITUDE = amplitude
        self.lenght = length
        self.pivot = pivot
        self.OMEGA = math.sqrt(9.8 / length)
        self.angle = self.AMPLITUDE  * math.sin(self.angle0)
        self.x = self.pivot[0] - math.sin(self.angle) * self.lenght
        self.y = self.pivot[1] + math.cos(self.angle) * self.lenght
        
    def move(self, AIR_FRICTION, time):
        """Function to move the ball with its velocity and angle and decrease its speed due to air friction

        Args:
            AIR_FRICTION (float): Friction of the air that causes decceleration in the balls speed
            time (float): Current time to calculate the angle
        """
        self.angle = (self.AMPLITUDE  * math.sin(self.OMEGA * time + self.angle0))
        self.x = self.pivot[0] - math.sin(self.angle) * self.lenght
        self.y = self.pivot[1] + math.cos(self.angle) * self.lenght
        self.AMPLITUDE *= AIR_FRICTION
    
    def blit(self, screen):
        """Function to blit the object onto the screen

        Args:
            screen (Pygame Surface): Surface on which the ball will be displayed
        """
        self.rect.center = (self.x, self.y)
        pg.draw.line(screen, 0, self.pivot, (self.x, self.y), 2)
        screen.blit(self.image, self.rect)
    
# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 450, 200
    scr = pg.display.set_mode(dim)
    pg.display.set_caption("Newton Craddle!")

    # Make Pendulums
    Pendulums = []
    for i in range(7):
        p = Pendulum(125, (75 + i * 51, 30), math.radians(0))
        Pendulums.append(p)

    t = 0
    ONE = pg.USEREVENT + 1
    pg.time.set_timer(ONE, 1000)
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False

            if e.type == ONE:
                pg.mixer.Sound('tick.mp3').play()
        
        scr.fill(pg.Color('white'))
        
        # Move two pendulums
        p1 = Pendulums[0]
        p7 = Pendulums[6]
        p1.move(1, t)
        p7.move(1, t)
        
        # Stop two end pendulums
        if p1.angle < math.radians(0): p1.move(1, 0)
        if p7.angle > math.radians(0): p7.move(1, 0)
        
        t += 0.185
        
        # Blit all pendulums
        for p in Pendulums:
            p.blit(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()