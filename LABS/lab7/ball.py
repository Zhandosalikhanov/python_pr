import pygame as pg

def main():
    dim = w, h = 600, 360
    surface = pg.display.set_mode(dim)
    
    ball = pg.image.load('data/red_ball.png').convert_alpha()
    ballrect = ball.get_rect()
    wall = pg.image.load('data/wall.jpg')
    
    F_aply = pg.math.Vector2()
    F_grav = pg.math.Vector2()
    F_norm = pg.math.Vector2()
    
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
        surface.blit(ball, ballrect)
        pg.display.flip()

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
