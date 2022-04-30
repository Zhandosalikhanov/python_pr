# Importing libraries
import pygame as pg

# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 400, 300
    scr = pg.display.set_mode(dim)
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
                
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()