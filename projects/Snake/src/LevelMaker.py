import pygame as pg, os
import Walls

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
    Mode = input("Do you want to make levels by yourself or load coordinates? (Y / load): ")
    
    # Setting up screen and background
    scr = pg.display.set_mode(dim)
    bcg = pg.image.load('../images/bcg.jpg').convert()
    bcg = pg.transform.scale(bcg, dim)
    bcg0 = bcg.copy()
    
    # Set title
    pg.display.set_caption("Level Maker. Mouse to Build. 'S' to save. Z to UNDO")
    
    # To store screens for UNDO command
    before = [bcg0]
    
    # To draw or not
    Draw = False
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    if Mode == 'Y':
        while going:
            scr.blit(bcg, (0, 0))
            grid(scr)
            
            for e in pg.event.get():
                # Quit
                if e.type == pg.QUIT: going = False

                # Draw if mouse pressed and save screen before change
                if e.type == pg.MOUSEBUTTONDOWN:
                    Draw = True
                    before.append(bcg.copy())
                    
                # Stop drawing
                if e.type == pg.MOUSEBUTTONUP: Draw = False
                
                if e.type == pg.KEYDOWN:
                    # Save if 'S' pressed and clear list of screens
                    if e.key == pg.K_s:
                        before.clear()
                        cur_level = len(os.listdir('../levels')) + 1
                        pg.image.save(bcg, f"../levels/Level {cur_level}.jpg")
                        bcg.blit(bcg0, (0, 0))

                    # Show the screen before the last change
                    elif e.key == pg.K_z and len(before):
                        bcg = before.pop()
            
            if Draw:
                pos = pg.mouse.get_pos()
                top  = pos[0] // CELL
                left = pos[1] // CELL
                pg.draw.rect(bcg, 0, pg.Rect(top * CELL, left * CELL, CELL, CELL))
                
            # Update screen
            pg.display.flip()
            fps.tick(60)
    
    else:
        for walls in Walls.AllWalls:
            for pos in walls:
                pg.draw.rect(bcg, 0, pg.Rect(pos[0] * CELL, pos[1] * CELL, CELL, CELL))
        
            cur_level = len(os.listdir('../levels')) + 1
            pg.image.save(bcg, f"../levels/Level {cur_level}.jpg")
            bcg.blit(bcg0, (0, 0))

# Launcher Code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()