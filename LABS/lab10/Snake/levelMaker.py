import pygame as pg, os

# Setting up constants
N, M = 30, 20
CELL = 20
dim = width, height = CELL * N, CELL * M

def grid(screen):
    for i in range(N):
        for j in range(M):
            pg.draw.line(screen, 0, (0, j * CELL), (N * CELL, j * CELL), 1)
            
        pg.draw.line(screen, 0, (i * CELL, 0), (i * CELL, M * CELL), 1)
    
    pg.display.flip()

def main():
    # Setting up screen and background
    scr = pg.display.set_mode(dim)
    bcg = pg.image.load('images/bcg.jpg').convert()
    bcg0 = bcg.copy()
    
    # Set title
    pg.display.set_caption("Level Maker. Mouse to Build & 'S' to save")
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        scr.blit(bcg, (0, 0))
        grid(scr)
        
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT: going = False

            # Draw if mouse pressed
            if e.type == pg.MOUSEBUTTONDOWN:
                top = e.pos[0] // 20
                left = e.pos[1] // 20
                pg.draw.rect(bcg, 0, pg.Rect(top * CELL, left * CELL, CELL, CELL))
                
            # Save if 'S' pressed    
            if e.type == pg.KEYDOWN and e.key == pg.K_s:
                cur_level = len(os.listdir('levels')) + 1
                pg.image.save(bcg, f"levels/Level {cur_level}.jpg")
                bcg.blit(bcg0, (0, 0))
            
        # Update screen
        pg.display.flip()
        fps.tick(60)

# Launcher Code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()