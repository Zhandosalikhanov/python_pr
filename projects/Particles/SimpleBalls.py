# Importing libraries
import pygame as pg, random
from math import *

# Function to add two vectors
def addVectors(angle1, length1, angle2, length2):
    # Calculate position of the new vector
    x = sin(angle1) * length1 + sin(angle2) * length2
    y = cos(angle1) * length1 + cos(angle2) * length2
    
    # Find Length and angle of the new vector
    Length = hypot(x, y)
    Angle = 0.5 * pi - atan2(y, x)
    
    return (Angle, Length)

# Function to find the picked particle
def findParticle(particles, x, y):
    # Loop through list
    for p in particles:
        if hypot(p.x-x, p.y-y) <= p.radius:
            return p
        
    return None

# Function to simulate collision
def collide(p1, p2):
    # Calculate distance
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    d = hypot(dx, dy)
    
    # Check if collision occured and collide
    if d < p1.radius + p2.radius:
        # Find angle between and total mass
        angle = atan2(dy, dx) + 0.5 * pi
        total_mass = p1.mass + p2.mass

        # Using Elastic collision formulae
        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed * (p1.mass - p2.mass) / total_mass, angle, 2 * p2.speed * p2.mass / total_mass)
        (p2.angle, p2.speed) = addVectors(p2.angle, p2.speed * (p2.mass - p1.mass) / total_mass, angle + pi, 2 * p1.speed * p1.mass / total_mass)

        # Decrease speed due to collision
        p1.speed *= elasticity
        p2.speed *= elasticity

        # Prevent from overlapping and sticking together
        overlap = 0.5*(p1.radius + p2.radius - d + 1)
        p1.x += sin(angle) * overlap
        p1.y -= cos(angle) * overlap
        p2.x -= sin(angle) * overlap
        p2.y += cos(angle) * overlap
        
# Class for creatig a particle
class Particle:
    # Set the dimensions, speed, and position
    def __init__(self, x, y, radius, density):
        self.colour = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.area = pi * radius ** 2
        self.mass = density * self.area
        self.drag = (self.mass / (self.mass + AirMass)) ** self.radius
        self.speed = 0
        self.angle = 0
    
    # Function to move the particle        
    def move(self):
        # Change speed vector due to gravity
        (self.angle, self.speed) = addVectors(self.angle, self.speed, Gravity[0], Gravity[1])
        
        self.x += sin(self.angle) * self.speed
        self.y -= cos(self.angle) * self.speed
        
        # Decrease speed due to air friction
        self.speed *= self.drag
    
    # Function to bounce off the wall
    def bounce(self):
        # Check if right or left walls collision
        if self.x > W - self.radius:
            self.x = 2 * (W - self.radius) - self.x
            self.angle = - self.angle
            self.speed *= elasticity
            
        elif self.x < self.radius:
            self.x = 2 * self.radius - self.x
            self.angle = - self.angle
            self.speed *= elasticity
            
        # Check if top or bottom walls collision
        if self.y > H - self.radius:
            self.y = 2 * (H - self.radius) - self.y
            self.angle = pi - self.angle
            self.speed *= elasticity
            
        elif self.y < self.radius:
            self.y = 2 * self.radius - self.y
            self.angle = pi - self.angle
            self.speed *= elasticity
    
    # Function to draw the particle            
    def draw(self, screen):
        pg.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
    
# Driver code
def main():
    # Setting up dimensions and screen
    global W, H
    dim = W, H = 400 * 3, 300 * 2
    scr = pg.display.set_mode(dim)
    
    # Colors
    WHITE = pg.Color('white')
    
    # Constants
    global Gravity, elasticity, AirMass
    
    Gravity = pi, 0.01          # A downward force
    elasticity = 0.75           # Enegy loss due to collision
    AirMass = 0.2               # Mass of one part of air
    USER_POWER = 0.02           # Force you apply with mouse
    
    # Variables
    N = 10                       # Number of particles
    particles = []              # Array for particles
    selected_particle = None    # Object for selected particle
    
    # Create particles
    while N:
        N -= 1
        # Randomly generate radius, density, and position
        r = random.randint(10, 20)
        density = random.randint(1, 10)
        x = random.randint(r, W - r)
        y = random.randint(r, H - r)
        
        # Create particle
        p = Particle(x, y, r, density)
        
        # Vary color with density, set random speed and angle
        p.colour = (200 - density * 20, 200 - density * 20, 255)
        p.speed = random.random()
        p.angle = random.uniform(0, pi * 2)
        
        particles.append(p)
    
    # Main Loop 
    fps = pg.time.Clock()
    going = True
    while going:
        # Fill screen with white
        scr.fill(WHITE)
        
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
                
            # Allow to drag particle
            elif e.type == pg.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = e.pos
                selected_particle = findParticle(particles, mouseX, mouseY)
                
            # Do not drag anything
            elif e.type == pg.MOUSEBUTTONUP:
                selected_particle = None
        
        # Drag selected particle
        if selected_particle:
            # Calculate change in position
            (mouseX, mouseY) = pg.mouse.get_pos()
            dx = mouseX - selected_particle.x
            dy = mouseY - selected_particle.y
            
            # Set speed and angle
            selected_particle.angle = 0.5 * pi + atan2(dy, dx)
            selected_particle.speed = hypot(dx, dy) * USER_POWER
        
        # Loop throuhg all particles
        for i, p in enumerate(particles):
            # Move and bounce particles
            p.move()
            p.bounce()
            
            # Coolide particles if needed
            for p2 in particles[i + 1 : ]:
                collide(p, p2)
            
            # Draw a particle
            p.draw(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(480)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()