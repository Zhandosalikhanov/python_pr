# Importing libraries
import pygame as pg
import random, PyParticles
from math import pi

# Function to create a line
def makeLine(universe, p1, p2):
    # Add spring between paticles p1, p2 to create a line
    universe.addSpring(p1, p2, length=100, strength=0.5)

# Function to create a triangle
def makeTriangle(universe, p1, p2, p3):
    # Add spring between paticles p1, p2, and p3 to create a triangle
    universe.addSpring(p1, p2, length=100, strength=0.5)
    universe.addSpring(p2, p3, length=100, strength=0.1)
    universe.addSpring(p3, p1, length=80, strength=0.05)
    
# Function to create a polygon
def makePolygon(universe, points):
    n = len(points)
    # Add spring between each particle to create a n-vertex polygon
    for i in range(n):
        universe.addSpring(points[i], points[(i + 1) % n], length=100, strength=0.5)
    
# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 1200, 600
    scr = pg.display.set_mode(dim)
    pg.display.set_caption("Springs")
    
    # Set up environment for the simulation
    universe = PyParticles.Environment(W, H)
    universe.colour = (255,255,255)
    universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
    universe.acceleration = (pi, 0.2)
    universe.mass_of_air = 0.02

    # Add some particles into our environment
    for p in range(9):
        universe.addParticles(mass= 100, size= 16, speed= 0, elasticity= 1, colour= (20,40,200))
        
    # Create shapes
    makeTriangle(universe, 0, 1, 2)
    makePolygon(universe, [3, 4, 5, 6])
    makeLine(universe, 7, 8)

    # Variables
    going = True
    paused = False
    selected_particle = None
    
    # Main Loop
    fps = pg.time.Clock()
    while going:
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
            
            # Check for Key Commands
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_SPACE:
                    paused = not paused

            # Select particle with mouse
            elif e.type == pg.MOUSEBUTTONDOWN:
                selected_particle = universe.findParticle(e.pos)

            # Release a particle
            elif e.type == pg.MOUSEBUTTONUP:
                selected_particle = None
        
        # Move the selected particle with mouse
        if selected_particle:
            selected_particle.mouseMove(pg.mouse.get_pos())
                        
        # Update universe and springs if simulation is not paused
        if not paused:
            universe.update()
            for s in universe.springs:
                s.update()
            
        # Fill screen with WHITE
        scr.fill(universe.colour)    
        
        # Display our particles
        for p in universe.particles:
            pg.draw.circle(scr, p.colour, (int(p.x), int(p.y)), p.radius, 0)
        
        # Draw springs (lines) between particles
        for s in universe.springs:
            pg.draw.aaline(scr, (0,0,0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()