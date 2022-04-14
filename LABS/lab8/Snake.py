import pygame as pg

def main():
    dim = width, height = 400, 300
    scr = pg.display.set_mode(dim)
    
    fps = pg.time.Clock()
    going = True
    while going:
        
        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
        
        
        scr.blit()
        pg.display.flip()
        fps.tick(60)
    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()