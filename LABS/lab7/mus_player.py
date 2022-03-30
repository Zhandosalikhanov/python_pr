import os, pygame as pg
from mutagen.mp3 import MP3
from pygame.mixer import music

def turn_on(surface):
    fps = pg.time.Clock()
    for i in range(1, 48):
            screen = pg.image.load('data/frames/f (' + str(i) + ').jpg')
            surface.blit(screen, (0, 0))
            surface.blit(name_text, pos)
            surface.blit(name_time, time_pos)                                
            pg.display.flip()
            fps.tick(50)

def turn_off(surface):
    fps = pg.time.Clock()
    for i in range(48, 1, -1):
            screen = pg.image.load('data/frames/f (' + str(i) + ').jpg')
            surface.blit(screen, (0, 0))
            surface.blit(name_text, pos)
            surface.blit(name_time, time_pos)                                
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
    song_sizes = { }
    for s in os.listdir('data/songs'):
        song = 'data/songs/' + s
        songs.append(song)
        music.load(song)
        size = int(MP3(song).info.length)
        song_sizes.update({song : size})
    
    s = len(songs)
    
    icon = pg.image.load('data/mus_icon.png').convert_alpha()
    disk = pg.image.load('data/disk.png').convert_alpha()
    player = pg.image.load('data/no_disk.png').convert_alpha()
    bcg = pg.image.load('data/frames/f (1).jpg')
    
    pg.display.set_icon(icon)
    pg.display.set_caption('Music player')
    
    angle = 33
    disk_pivot = pg.math.Vector2(w/2 - 109, h/2 - 1)
    rotate(surface, disk, (93, 150), disk_pivot, angle)
    
    cur_song = 0
    cur_vol = 0.1
    music.load(songs[cur_song % s])
    music.set_volume(cur_vol)
    On = False
    Paused = False
    Next = False
    Prev = False
    V_up = False
    V_down = False
    
    fps = pg.time.Clock()
    going = True
    
    while going:
        
        global name_time, time_pos
        min = int((music.get_pos() // 1000) / 60)
        sec = int(music.get_pos() // 1000) % 60
        duration = str(min) + ':' + str(sec) + ' / ' + str(int(song_sizes[songs[cur_song % s]] / 60)) + ':' + str(int(song_sizes[songs[cur_song % s]] % 60))
        time_font = pg.font.SysFont("comicsansms", 10)
        name_time = time_font.render(duration, True, 0, (225, 221, 218))
        time_pos = (245 - name_time.get_width() // 2, 180 - name_time.get_height() // 2)
        
        global name_text, pos
        name_font = pg.font.SysFont("comicsansms", 14)
        song_name = os.path.split(songs[cur_song % s])[1][:-4]
        song_name = song_name.center(25)
        name_text = name_font.render(song_name, True, 0, (225, 221, 218))  
        pos = (240 - name_text.get_width() // 2, 122 - name_text.get_height() // 2)
        
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
            if e.type == pg.KEYDOWN and e.key == pg.K_UP:
                V_up = True
            if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
                V_down = True
                 
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
            Paused = True
            music.pause()
        
        if not On and not music.get_busy():
            surface.blit(bcg, (0, 0))
        
        if music.get_pos() / 1000 > song_sizes[songs[cur_song % s]] and music.get_busy():
            Next = True
        
        if Next:
            Next = False
            cur_song += 1
            music.stop()
            music.load(songs[cur_song % s])
        
        if Prev:
            Prev = False
            cur_song -= 1
            music.stop()
            music.load(songs[cur_song % s])
        
        if V_up:
            V_up = False
            cur_vol += 0.1
            music.set_volume(cur_vol)  
        
        if V_down:
            V_down = False       
            cur_vol -= 0.1
            music.set_volume(cur_vol)     
        
        surface.blit(name_text, pos)                                
        surface.blit(name_time, time_pos)                                
        pg.display.flip()
        fps.tick(60)
            
    

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()