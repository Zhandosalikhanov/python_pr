import pygame as pg
pg.init()

#Screen and image initalizing
dim = width, height = 600, 300
screen = pg.display.set_mode(dim)
color = (255, 255, 255)
ball = pg.image.load("data/Ball.png")
ballrect = ball.get_rect()
background = pg.image.load("data/wall.jpg")
fps = pg.time.Clock()

#Physical quantites
Vx = 0              # Vy = sqrt(integrate(g - a)^2 + Vx^2)
Vy = 0              # Vy = sqrt(integrate(g - a)^2 + Vx^2)
a = 0
m = 1
g = 9.8
F = 0
Fg = m * g
Ff = 0
k = 0

#Speed change
def key_map(pressed, Vx, Vy):
    if pressed[pg.K_UP]: Vy -= 3
    if pressed[pg.K_DOWN]: Vy += 3
    if pressed[pg.K_LEFT]: Vx -= 3
    if pressed[pg.K_RIGHT]: Vx += 3
    
    return [Vx, Vy]

#Driver Code
going = True

while going:    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            going = False
    
    pressed = pg.key.get_pressed()
    speed = key_map(pressed, Vx, Vy)
    
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height - 45:
        speed[1] = -speed[1]
    
    screen.blit(background, (0, 0)) 
    screen.blit(ball, (0, 0))
        
    pg.display.flip()
    fps.tick(60)