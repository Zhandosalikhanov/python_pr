import math, random, pygame as pg

class Ball():
    def __init__(circle, pos, radius, speed= 0, angle= 0):
        circle.x = pos[0]
        circle.y = pos[1]
        circle.radius = radius
        circle.colour = pg.Color('red')
        circle.thickness = 2
        circle.speed = speed
        circle.angle = angle
    
    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        
    def display(self, screen):
        pg.draw.circle(screen, self.colour, (self.x, self.y), self.radius, self.thickness)

def main():
    dim = w, h, = 400, 300
    surface = pg.display.set_mode(dim)
    
    n = 10
    balls = []
    for i in range(n):
        radius = random.randint(10, 20)
        x = random.uniform(radius, w - radius)
        y = random.uniform(radius, h - radius)
        
        balls.append(Ball((x, y), radius, random.random(), random.uniform(0, math.pi * 2)))
    
    going = True
    fps = pg.time.Clock()
    while going:

        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
         
        surface.fill(0)
        for i in balls:
            i.move()
            i.display(surface)
        
        pg.display.flip()
        fps.tick(60)
    
    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()