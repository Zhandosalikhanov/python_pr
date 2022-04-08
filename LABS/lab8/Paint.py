import pygame as pg
from math import *

# Class for tools and colors
class Button(pg.sprite.Sprite):
    # Loading image and setting position for our button
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    # Check if button was clicked
    def clicked(self, mouse):
        return self.rect.collidepoint(mouse)

    # Blit the button onto the screen
    def blit(self, surf):
        surf.blit(self.image, self.rect)

# Function to cut the parts of an image
def cut(img, x, y, size_x, size_y):
    cutted = img.copy()
    cutted_rect = pg.Rect(x, y, size_x, size_y)
    
    cutted.set_clip(cutted_rect)
    return img.subsurface(cutted.get_clip())

# Operator for making color buttons
def Color():
    # Loading set of colors as one image
    colors_img = pg.image.load('images/colors.jpg').convert_alpha()
    
    # Slicing the image into parts
    color_rects = [cut(colors_img, i * 22, 0, 22, 20) for i in range(10)]
    
    # Makings objects from images and return
    colors = []
    for c in color_rects:
            colors.append(Button(c, (color_rects.index(c) * 22, 0)))
    return colors

# Driver code
def main():
    # Setting up display
    dim = width, height = 400, 300
    scr = pg.display.set_mode(dim)
    scr.fill(pg.Color('white'))
    
    # Loading imgages
    Pencil = pg.image.load('images/Pencil.png').convert_alpha()
    Eraser = pg.image.load('images/Eraser.png').convert_alpha()
    Plus = pg.image.load('images/Plus.png').convert_alpha()
    Minus = pg.image.load('images/Minus.png').convert_alpha()
    
    # Making tool objects
    Pencil = Button(Pencil, (220, 0))
    Eraser = Button(Eraser, (240, 0))
    Plus = Button(Plus, (260, 0))
    Minus = Button(Minus, (280, 0))
    
    # Making Groups
    colors = pg.sprite.Group(Color())
    all_sprites = pg.sprite.Group([Pencil, Eraser, Color(), Plus, Minus])
    
    # Variables
    cur_color = pg.Color('black')
    cur_tool = 'Pen'
    Pen_Draw = False
    Erase = False
    Pen_width = 5
    dx, dy = 0, 0
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        scr.fill(pg.Color('gray'), pg.Rect(0, 0, width, 20))
        # Loop for checking events
        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
            
            # Check if any color was picked
            if e.type == pg.MOUSEBUTTONDOWN:
                if Eraser.clicked(e.pos):
                    cur_tool = 'Erase'

                if Pencil.clicked(e.pos):
                    cur_tool = 'Pen'
                
                if Plus.clicked(e.pos): Pen_width += 3
                if Minus.clicked(e.pos): Pen_width -= 3

                if cur_tool == 'Pen':
                    Pen_Draw = True
                    for c in colors:
                        if c.clicked(pg.mouse.get_pos()):
                            cur_color = pg.Color(c.image.get_at((11, 10)))

                elif cur_tool == 'Erase':
                    Erase = True
                            
            if e.type == pg.MOUSEBUTTONUP:
                Pen_Draw = False
                Erase = False

            if e.type == pg.MOUSEMOTION:
                dx, dy = e.pos
                            
        if Pen_Draw == True:
            pg.draw.circle(scr, cur_color, (dx, dy), Pen_width)
        
        if Erase:
            pg.draw.circle(scr, pg.Color('white'), (dx, dy), 3 * Pen_width)
        
        # Blit all tools and colors
        for c in all_sprites:
            c.blit(scr)
        
        # Update screen  
        pg.display.flip()
        fps.tick(120)

# Launcher code    
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
