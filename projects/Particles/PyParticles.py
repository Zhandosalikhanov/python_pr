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

# Function to combine paricles if they collided
def combine(p1, p2):
    if hypot(p1.x - p2.x, p1.y - p2.y) < p1.radius + p2.radius:
        # Calculate total mass and position
        total_mass = p1.mass + p2.mass
        p1.x = (p1.x * p1.mass + p2.x * p2.mass)/ total_mass
        p1.y = (p1.y * p1.mass + p2.y * p2.mass)/ total_mass
        
        # Give new, slower speed to the first particle
        (p1.angle, p1.speed) = addVectors(p1.angle, p1.speed * p1.mass / total_mass, p2.angle, p2.speed * p2.mass / total_mass)
        p1.speed *= (p1.elasticity * p2.elasticity)
        
        # Increase first particle mass and remember collided particle to remove it later
        p1.mass += p2.mass
        p1.collided_with = p2
        
# Class for creatig a particle
class Particle:
    # Set the dimensions, speed, position and other attrbutes
    def __init__(self, x, y, radius, mass= 1, image= None):
        self.rect = image.get_rect() if image is not None else None
        self.colour = 0
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.drag = 1
        self.elasticity = 0.75
        self.speed = 0
        self.angle = 0
        # self.drag = (self.mass / (self.mass + AirMass)) ** self.radius
    
    # Function to move the particle        
    def move(self):
        # Change position according to speed and angle        
        self.x += sin(self.angle) * self.speed
        self.y -= cos(self.angle) * self.speed
    
    # Function for particles to slow down from the air or anything
    def experienceDrag(self):
        self.speed *= self.drag
        
    # Function to accelerate particle downward due to gravity
    def accelerate(self, Gravity):
        # Change speed vector due to gravity
        (self.angle, self.speed) = addVectors(self.angle, self.speed, Gravity[0], Gravity[1])
        
    # To move particle with the mouse 
    def mouseMove(self, mouse):
        dx = mouse[0] - self.x
        dy = mouse[1] - self.y
        self.angle = 0.5 * pi +  atan2(dy, dx)
        self.speed = hypot(dx, dy) * 0.1
    
    # To simulate attraction between two particles
    def attract(self, other):
        dx = (self.x - other.x)
        dy = (self.y - other.y)
        dist = hypot(dx, dy)
            
        theta = atan2(dy, dx)
        force = 0.2 * self.mass * other.mass / dist ** 2
        self.accelerate((theta - 0.5 * pi, force / self.mass))
        other.accelerate((theta + 0.5 * pi, force / other.mass))

# Class for creating a spring object
class Spring:
    # Give the spring two endpoints as particles, length, and Hooke's constant
    def __init__(self, p1, p2, length=50, strength=0.5):
        self.p1 = p1
        self.p2 = p2
        self.length = length
        self.strength = strength
    
    # Function to represent restoring force on spring by Hooke's law
    def update(self):
        # Calculate distance between objects and acceleration by F = ma = -kx ---> a = -kx / m
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        dist = hypot(dx, dy)
        theta = atan2(dy, dx)
        force = (self.length - dist) * self.strength
        
        # Accelerate both objects
        self.p1.accelerate((theta + 0.5 * pi, force / self.p1.mass))
        self.p2.accelerate((theta - 0.5 * pi, force / self.p2.mass))
        
# Environment in which pasticles will be stored
class Environment:
    # Defines the boundary of a simulation and its properties
    def __init__(self, width, height):
        # Set up dimensions
        self.width = width
        self.height = height
        
        # Arrays for objects
        self.particles = []
        self.springs = []
        
        # Create constants
        self.colour = (255,255,255)
        self.mass_of_air = 0.2
        self.elasticity = 0.75
        self.acceleration = (pi, 0.2)

        # All the functions stored in a dictionary
        self.particle_functions1 = []
        self.particle_functions2 = []
        self.function_dict = {
        'move': (1, lambda p: p.move()),
        'drag': (1, lambda p: p.experienceDrag()),
        'bounce': (1, lambda p: self.bounce(p)),
        'accelerate': (1, lambda p: p.accelerate(self.acceleration)),
        'collide': (2, lambda p1, p2: collide(p1, p2)),
        'combine': (2, lambda p1, p2: combine(p1, p2)),
        'attract': (2, lambda p1, p2: p1.attract(p2))
        }
    
    # Look up functions names in dictionary and add to particle function lists
    def addFunctions(self, function_list):
        for func in function_list:
            (n, f) = self.function_dict.get(func, (-1, None))
            if n == 1:
                self.particle_functions1.append(f)
            elif n == 2:
                self.particle_functions2.append(f)
            else:
                print ("No such function: %s" % f)
           
    # Add a spring between particles p1 and p2       
    def addSpring(self, p1, p2, length=50, strength=0.5):
        self.springs.append(Spring(self.particles[p1], self.particles[p2], length, strength))       
                    
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
            if hypot(p.x - x, p.y - y) <= p.radius:
                return p
            
        return None
                
    # Function to update the position, speed and other attributes of the object
    def update(self):
        # Loop through particles and call needed functions
        for i, particle in enumerate(self.particles):
            for f in self.particle_functions1:
                f(particle)
                
            for particle2 in self.particles[i+1:]:
                for f in self.particle_functions2:
                    f(particle, particle2)