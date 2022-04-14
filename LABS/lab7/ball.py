import pygame as pg

class Ball:
    def __init__(self, PosIn, path, screen):
        self.PosIn = PosIn
        self.ball = pg.image.load(path).convert_alpha()
        self.ballrect = self.ball.get_rect()
        self.screen = screen
        
    def move(self, speed, angle):
        a = 1
    
    def blit(self)

def main():
    dim = w, h = 600, 360
    surface = pg.display.set_mode(dim)
    
    wall = pg.image.load('data/wall.jpg')
    
    fps = pg.time.Clock()
    going = True
    
    Vx = 0
    Vy = 0

    while going:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_UP:
                   Vy -= 3
                if e.key == pg.K_DOWN:
                   Vy += 3
                if e.key == pg.K_RIGHT:
                   Vx -= 3
                if e.key == pg.K_LEFT:
                   Vx += 3
                
        if ballrect.left < 0 or ballrect.right > w:
           Vx *= -1
        if ballrect.top < 0 or ballrect.bottom > (h - 102):
           Vy *= -1
        
        ballrect.move_ip(Vx, Vy)
        
        fps.tick(60)
        surface.blit(wall, (0, 0))
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
