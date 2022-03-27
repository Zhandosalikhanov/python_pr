import pygame as pg
from datetime import datetime

def rotate(screen, image, angle, pos, pivot):
    
    rotated_image = pg.transform.rotozoom(image, -angle, 1)
    rotated_pivot = pivot.rotate(angle)
    rect = rotated_image.get_rect(center=pos+rotated_pivot)
    screen.blit(rotated_image, rect)

def main():
    dim = width, height = 400, 300
    screen = pg.display.set_mode(dim)
    screen.fill((0, 128, 0))
    
    red = pg.Color('red')
    
    clock = pg.image.load('data/clock.png').convert_alpha()
    min = pg.image.load('data/min.png').convert_alpha()
    sec = pg.image.load('data/sec.png').convert_alpha()
    red_line = pg.image.load('data/red.jpg')
            
    min_pos = [(width/2), (height/2)]
    sec_pos = [(width/2), (height/2)]

    min_pivot = pg.math.Vector2(0, min.get_size()[1] / 2)
    sec_pivot = pg.math.Vector2(0, sec.get_size()[1] / 2)
    
    going = True
    fps = pg.time.Clock()
    
    while going:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
                    
        screen.blit(clock, (0, 0))
        
        cur_min = datetime.now().strftime('%M')
        cur_sec = datetime.now().strftime('%S')

        min_angle = (int(cur_min) - 30) * 6
        sec_angle = (int(cur_sec) - 30) * 6
        
        rotate(screen, min, min_angle, min_pos, min_pivot)
        rotate(screen, sec, sec_angle, sec_pos, sec_pivot)
        
        pg.display.flip()
        fps.tick(60)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()