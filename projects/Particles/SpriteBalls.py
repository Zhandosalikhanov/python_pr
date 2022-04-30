# Importing libraries
import pygame as pg
import PyParticles

# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 400 * 3, 300 * 2
    scr = pg.display.set_mode(dim)
    pg.display.set_caption("Particles! G for gravity and ENTER or BACKSPACE to add/remove")
    
    # Set up background and menu
    menu = pg.image.load('images/Menu.jpg').convert()
    
    # Set up environment
    env = PyParticles.Environment(W, H)
    
    # Add some particles to the environment
    env.addParticles(10)
    
    # Variables
    selected_particle = None        # Variable to store selected particle object
    IsMenu = True                   # Variable to whether blit the menu or not
    
    # Text to display
    NAME = "Particles simulator!"
    INST = "Press SPACE to start"
    
    # Set up Fonts and render
    Bfont = pg.font.SysFont('georgia', 40, True, False)
    Sfont = pg.font.SysFont('georgia', 25, False, True)
    NAME = Bfont.render(NAME, True, (255, 255, 255))
    INST = Sfont.render(INST, True, (255, 255, 255))
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Display menu or playground
        if IsMenu:
            # Loop through the events
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False
                
                # Start if SPACE was pressed and quit if ESCAPE
                if e.type == pg.KEYDOWN:
                    if e.key == pg.K_ESCAPE:
                        going = False
                    if e.key == pg.K_SPACE:
                        IsMenu = False

            # Display menu background
            scr.blit(menu, (0, 0))
            
            # Display Text
            scr.blit(NAME, (W / 2 - 150, 150))
            scr.blit(INST, (W / 2 - 150, 300))
        
        # Play if not on menu
        else:
            # Loop through the events
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT:
                    going = False
                    
                # Check if particle was picked
                elif e.type == pg.MOUSEBUTTONDOWN:
                    selected_particle = env.findParticle(e.pos)
                
                # Release any particle
                elif e.type == pg.MOUSEBUTTONUP:
                    selected_particle = None   
                    
                # Check for key commands
                elif e.type == pg.KEYDOWN:
                    # Turn on or off gravity
                    if e.key == pg.K_g:
                        env.gravity = 0 if env.gravity else 0.1
                        env.SaveSettings() 
                    
                    # Add or Delete particle    
                    if e.key == pg.K_RETURN:
                        env.addParticles()
                    elif e.key == pg.K_BACKSPACE:
                        env.particles.pop()
                    
            # Fill screen with the color of the environment
            scr.fill(env.colour)
            
            # Move selected particle
            if selected_particle:
                selected_particle.mouseMove(pg.mouse.get_pos())
            
            # Update all particles
            env.update()
            
            # Draw all particles
            for p in env.particles:
                pg.draw.circle(scr, p.colour, (p.x, p.y), p.radius)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()