# Importing libraries
import pygame as pg
import math

def addVectors(angle1, length1, angle2, length2):
    """Function to add two vectors

    Args:
        angle1 (float): angle of the 1st vector
        length1 (float): The magnitude of the 1st vector
        angle2 (float): angle of the 2nd vector
        length2 (float): The magnitude of the 2nd vector

    Returns:
        Vector: The resultant vector with new the angle and magnitude 
    """
    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2
    
    Length = math.hypot(x, y)
    Angle = 0.5 * math.pi - math.atan2(y, x)
    
    return (Angle, Length)

class Rope:
    def __init__(self, lenght, pivot, ball, color= 0):
        """Class for rope that connects two points

        Args:
            lenght (float): The lenght of the rope
            pivot (float): The fixed point of the rope
            ball (object): The ball object that will be connected at the end of the rope
            color (RGB color, optional): The (Red, Green, Blue) colour value. Defaults to (0, 0, 0), i.e. black.
        """
        self.lenght = lenght
        self.x, self.y = pivot[0], pivot[1]
        self.ball = ball
        self.k = 0.001
        self.color = color
        
    def restore(self):
        """Function to create the restoring force of the spring defined by Hooke's law
        """
        dx = self.ball.x - self.x
        dy = self.ball.y - self.y
        d = math.hypot(dx, dy)
        thetta = math.atan2(dy, dx) + 0.5 * math.pi
        force = (self.lenght - d) * self.k
        
        self.ball.accelerate((thetta, force / self.ball.mass))
        
    def draw(self, screen):
        """Function to draw the line between fixed point and ball object, representing the rope

        Args:
            screen (Pygame Surface): The screen on which the rope will be displayed on
        """
        pg.draw.line(screen, self.color, (self.x, self.y), (self.ball.x, self.ball.y), 2)
        
class Ball:
    """Class to create a ball with the given image and size"""
    def __init__(self, image_name, size):
        """Function to initialize ball object

        Args:
            image_name (string): Name of the image to import from 'images' folder
            size (int): Radius of the ball
        """
        self.image = pg.image.load(f"images/{image_name}").convert_alpha()
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect  = self.image.get_rect()
        self.size = size / 2
        self.mass = math.sqrt(self.size) / 5
        self.x = 200
        self.y = 200
        self.speed = 5
        self.angle = math.pi / 2
        self.elasticity = 0.75
        
    def move(self, AIR_FRICTION):
        """Function to move the ball with its velocity and angle and decrease its speed due to air friction

        Args:
            AIR_FRICTION (float): Friction of the air that causes decceleration in the balls speed
        """
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        self.speed *= AIR_FRICTION
    
    def bounce(self, width, height):
        """Function to bounce off the screen boundaries

        Args:
            width (int): screen width
            height (int): screen height
        """
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle *= -1
            self.speed *= self.elasticity
            
        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle *= -1
            self.speed *= self.elasticity
            
        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle
            self.speed *= self.elasticity
            
        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle += math.pi / 2
            self.speed *= self.elasticity

    def MouseMove(self, mouse):
        """To move the ball with the mouse

        Args:
            mouse (tuple): coordinates of the mouse cursor
        """
        dx = mouse[0] - self.x 
        dy = mouse[1] - self.y 
        self.angle = 0.5 * math.pi + math.atan2(dy, dx)
        self.speed = math.hypot(dx, dy) * 0.2
    
    def accelerate(self, gravity):
        """Function to accelerate the ball due to gravity

        Args:
            gravity (Vector2): Gravitational vector with angle and magnitude
        """
        self.angle, self.speed = addVectors(self.angle, self.speed, gravity[0], self.mass * gravity[1])
    
    def blit(self, screen):
        """Function to blit the object onto the screen

        Args:
            screen (Pygame Surface): Surface on which the ball will be displayed
        """
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
    
# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 800, 600
    scr = pg.display.set_mode(dim)
    pg.display.set_caption("Double Pendulum on Springs! Press W to create walls and Mouse to control")
    
    # Set up background
    bcg = pg.image.load('images/bcg.jpg').convert()
    bcg = pg.transform.scale(bcg, dim)
    
    # Create the ball and rope objects
    ball = Ball('Ball.png', 50)
    rope = Rope(100, (W / 2, 50), ball)
    ball2 = Ball('Ball.png', 50)
    ball2.x, ball2.y = 300, 300
    rope2 = Rope(100, (ball.x, ball.y), ball2, (255, 255, 255))
    rope3 = Rope(100, (ball2.x, ball2.y), ball, (255, 255, 255))
    
    # Variables
    Move1 = False
    Move2 = False
    Boundary = False
    
    # Constants
    AIR_FRICTION = 0.996
    GRAVITY = math.pi, 0.1
    
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
                if ball.rect.collidepoint(pg.mouse.get_pos()):
                    Move1 = True
                if ball2.rect.collidepoint(pg.mouse.get_pos()):
                    Move2 = True
            
            if e.type == pg.MOUSEBUTTONUP:
                Move1 = False
                Move2 = False
                
            if e.type == pg.KEYDOWN and e.key == pg.K_w:
                Boundary = not Boundary
                
        if Move1: ball.MouseMove(pg.mouse.get_pos())
        if Move2: ball2.MouseMove(pg.mouse.get_pos())
        
        # Update the objects position and other attributes
        if Boundary:
            ball.bounce(W, H)
            ball2.bounce(W, H)
        ball.accelerate(GRAVITY)
        ball.move(AIR_FRICTION)
        ball2.accelerate(GRAVITY)
        ball2.move(AIR_FRICTION)
        rope.restore()
        rope2.restore()
        rope3.restore()
        rope3.x, rope3.y = ball2.x, ball2.y
        rope2.x, rope2.y = ball.x, ball.y
        
        # Blit the background
        scr.blit(bcg, (0, 0))
        
        # Blit the objects
        rope.draw(scr)
        rope2.draw(scr)
        rope3.draw(scr)
        ball.blit(scr)
        ball2.blit(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()