# Importing libraries
import pygame as pg
import random
import PyParticles

# Class for screen to display with several functions like zoom and scroll
class UniverseScreen:
    # Set up screen dimensions
    def __init__ (self, width, height):
        self.width = width
        self.height = height
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0
    
    # Scroll the screen    
    def scroll(self, dx=0, dy=0):
        self.dx += dx * self.width / (self.magnification*10)
        self.dy += dy * self.height / (self.magnification*10)
    
    # Zoom in or out    
    def zoom(self, zoom):
        self.magnification *= zoom
        self.mx = (1-self.magnification) * self.width/2
        self.my = (1-self.magnification) * self.height/2
    
    # Reset back to original position    
    def reset(self):
        (self.dx, self.dy) = (0, 0)
        (self.mx, self.my) = (0, 0)
        self.magnification = 1.0

# Dictionary with specific function for a given key
key_to_function = {
    pg.K_LEFT:   (lambda x: x.scroll(dx = 1)),
    pg.K_RIGHT:  (lambda x: x.scroll(dx = -1)),
    pg.K_DOWN:   (lambda x: x.scroll(dy = -1)),
    pg.K_UP:     (lambda x: x.scroll(dy = 1)),
    pg.K_EQUALS: (lambda x: x.zoom(2)),
    pg.K_MINUS:  (lambda x: x.zoom(0.5)),
    pg.K_r:      (lambda x: x.reset())
    }

# Driver code
def main():
    # Setting up screen
    (width, height) = (1200, 600)
    universe_screen = UniverseScreen(width, height)
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption('Star formation')

    # Set up our space
    universe = PyParticles.Environment(width, height)
    universe.colour = (0,0,0)
    universe.addFunctions(['move', 'attract', 'combine'])

    # Calculate Radius for given mass
    def calculateRadius(mass):
        return 0.5 * mass ** (0.5)

    # Create 200 dust paticles
    for p in range(200):
        particle_mass = random.randint(1,4)
        particle_size = calculateRadius(particle_mass)
        universe.addParticles(mass=particle_mass, radius=particle_size, speed=0, colour=(255,255,255))

    # Variables
    paused = False              # Conditional to show wether game is paused or not

    # Main Loop
    running = True
    while running:
        # Loop through events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                running = False

            if e.type == pg.KEYDOWN:
                # Add particle with ENTER
                if e.key == pg.K_RETURN:
                    universe.addParticles(mass=particle_mass, radius=particle_size, speed=0, colour=(255,255,255))

                # Call zoom, scroll and other functions with keys
                if e.key in key_to_function:
                    key_to_function[e.key](universe_screen)

                # Pause the simulation with space
                elif e.key == pg.K_SPACE:
                    paused = not paused
        
        # Update attributes and fill universe with black            
        if not paused: universe.update()
        screen.fill(universe.colour)
        
        # Store unneccessary particle objects that collided
        particles_to_remove = []
        for p in universe.particles:
            # Store particles with 'collided_with' attribute
            if 'collided_with' in p.__dict__:
                particles_to_remove.append(p.collided_with)
                p.radius = calculateRadius(p.mass)
                del p.__dict__['collided_with']

            # Calculate display position with respect to universe_screen variable
            mag = universe_screen.magnification
            x = int(universe_screen.mx + (universe_screen.dx + p.x) * mag)
            y = int(universe_screen.my + (universe_screen.dy + p.y) * mag)
            size = int(p.radius * mag)
            
            # If radius is too small then draw rect
            if p.radius < 2:
                pg.draw.rect(screen, p.colour, (x, y, 2, 2))
            else:
                pg.draw.circle(screen, p.colour, (x, y), size, 0)
        
        # Remove unneccessary particles
        for p in particles_to_remove:
            if p in universe.particles:
                universe.particles.remove(p)

        # Flip the display
        pg.display.flip()

# Launcher code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()