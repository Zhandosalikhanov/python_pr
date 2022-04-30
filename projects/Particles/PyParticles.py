import random
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
        elasticity = p1.elasticity * p2.elasticity
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
    # Set the dimensions, speed, position and other attrbutes
    def __init__(self, x, y, radius, density, image= None):
        self.rect = image.get_rect() if image is not None else None
        self.colour = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.area = pi * radius ** 2
        self.mass = density * self.area
        self.drag = (self.mass / (self.mass + AirMass)) ** self.radius
        self.elasticity = 0.75
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
        
    # To move particle with the mouse 
    def mouseMove(self, mouse):
        dx = mouse[0] - self.x
        dy = mouse[1] - self.y
        self.angle = 0.5 * pi +  atan2(dy, dx)
        self.speed = hypot(dx, dy) * 0.1
    
# Environment in which pasticles will be stored
class Environment:
    # Initialize environment
    def __init__(self, width, height):
        # Set up dimensions
        self.width = width
        self.height = height
        
        # Create constants
        self.particles = []
        self.colour = (255,255,255)
        self.mass_of_air = 0.1
        self.elasticity = 0.75
        self.gravity = 0.1

        # Make global conatants
        global Gravity, AirMass
        Gravity = pi, self.gravity
        AirMass = self.mass_of_air
    
    # Function to save updated settings
    def SaveSettings(self):
        global Gravity, AirMass
        Gravity = pi, self.gravity
        AirMass = self.mass_of_air
        
    # Function to add particles into our environment        
    def addParticles(self, n=1, **kargs):
        # Create n particles with given arguments (kargs)
        for i in range(n):
            radius = kargs.get('radius', random.randint(10, 20))
            mass = kargs.get('mass', random.randint(100, 10000))
            x = kargs.get('x', random.uniform(radius, self.width - radius))
            y = kargs.get('y', random.uniform(radius, self.height - radius))
            p = Particle(x, y, radius, mass)
            p.speed = kargs.get('speed', random.random())
            p.angle = kargs.get('angle', random.uniform(0, pi * 2))
            p.colour = kargs.get('colour', (0, 0, 255))
            p.drag = (p.mass / (p.mass + self.mass_of_air)) ** p.radius
            self.particles.append(p)
    
     # Function to bounce off the wall
    def bounce(self, particle):
        # Check right or left walls collision
        if particle.x > self.width - particle.radius:
            particle.x = 2 * (self.width - particle.radius) - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
            
        elif particle.x < particle.radius:
            particle.x = 2 * particle.radius - particle.x
            particle.angle = - particle.angle
            particle.speed *= self.elasticity
            
        # Check top or bottom walls collision
        if particle.y > self.height - particle.radius:
            particle.y = 2 * (self.height - particle.radius) - particle.y
            particle.angle = pi - particle.angle
            particle.speed *= self.elasticity
            
        elif particle.y < particle.radius:
            particle.y = 2 * particle.radius - particle.y
            particle.angle = pi - particle.angle
            particle.speed *= self.elasticity
    
    # Function to find the picked particle
    def findParticle(self, mouse):
        x, y = mouse[0], mouse[1]
        # Loop through list
        for p in self.particles:
            if hypot(p.x-x, p.y-y) <= p.radius:
                return p
            
        return None
                
    # Function to update the position, speed and other attributes of the object
    def update(self):
        for i, particle in enumerate(self.particles):
            particle.move()
            self.bounce(particle)
            for particle2 in self.particles[i+1:]:
                collide(particle, particle2)