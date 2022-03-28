import pygame as pg
from pygame.mixer import music
import os

def turn_on(surface):
    fps = pg.time.Clock()
    for i in range(1, 48):
            screen = pg.image.load('data/frames/f (' + str(i) + ').jpg')
            surface.blit(screen, (0, 0))
            pg.display.flip()
            fps.tick(50)

def turn_off(surface):
    fps = pg.time.Clock()
    for i in range(48, 1, -1):
            screen = pg.image.load('data/frames/f (' + str(i) + ').jpg')
            surface.blit(screen, (0, 0))
            pg.display.flip()
            fps.tick(50)

def rotate(surf, image, pos, pivot, angle):

    image_rect = image.get_rect(topleft = (pos[0] - pivot[0], pos[1]-pivot[1]))
    offset_center_to_pivot = pg.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pg.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    surf.blit(rotated_image, rotated_image_rect)
    
def main():
    dim = w, h = 400, 300
    surface = pg.display.set_mode(dim)

    global songs
    songs = []
    for song in os.listdir('data/songs'):
        music.load('data/songs/' + song)
        songs.append('data/songs/' + song)
    
    icon = pg.image.load('data/mus_icon.png').convert_alpha()
    disk = pg.image.load('data/disk.png').convert_alpha()
    player = pg.image.load('data/no_disk.png').convert_alpha()
    bcg = pg.image.load('data/frames/f (1).jpg')
    
    surface.blit(bcg, (0, 0))
    pg.display.set_icon(icon)
    pg.display.set_caption('Music player')
    
    angle = 33
    disk_pivot = pg.math.Vector2(w/2 - 109, h/2 - 1)
    rotate(surface, disk, (93, 150), disk_pivot, angle)
    
    cur_song = 0
    On = False
    Paused = False
    Next = False
    Prev = False
    
    fps = pg.time.Clock()
    going = True    
    
    while going:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
            if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                going = False

            if e.type == pg.KEYDOWN and e.key == pg.K_SPACE and not On:
                turn_on(surface)
                On = True
                
            elif On and e.type == pg.KEYDOWN and e.key == pg.K_SPACE:
                turn_off(surface)
                On = False
                
            if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
                Next = True
            if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
                Prev = True
                
        if On and not music.get_busy():
            if Paused:
                music.unpause()
            else:
                music.play()
                    
        if On:                
            rotate(surface, disk, (93, 150), disk_pivot, angle)
            surface.blit(player, (0, 0))    
            angle -= 10
            
        if not On and music.get_busy():
            music.pause()
            Paused = True
        
        if Next:
            Next = False
            cur_song += 1
            
            music.stop()
            music.load(songs[cur_song])
        
        if Prev:
            Prev = False
            cur_song -= 1
            
            music.stop()
            music.load(songs[cur_song])    
                                
        pg.display.flip()
        fps.tick(60)
            
    

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()