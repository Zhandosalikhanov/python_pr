import pygame as pg     
import draw     # Import file draw.py with all draw functions

# Class for tools and colors
class Button(pg.sprite.Sprite):
    # Loading image and setting position for our button
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

    # Check if button was clicked
    def clicked(self, mouse): return self.rect.collidepoint(mouse)

    # Blit the button onto the screen
    def blit(self, surf): surf.blit(self.image, self.rect)

# Function to cut the parts of an image
def cut(img, x, y, size_x, size_y):
    cutted = img.copy()     # Saving a copy
    cutted_rect = pg.Rect(x, y, size_x, size_y)     # Area to be cutted
    
    cutted.set_clip(cutted_rect)        # Cut
    return img.subsurface(cutted.get_clip())    # Return image

# Operator for making color buttons
def Color():
    # Loading set of colors as one image
    colors_img = pg.image.load('images/colors.jpg').convert_alpha()
    
    # Slicing the image into parts
    color_rects = [cut(colors_img, i * 22, 0, 22, 20) for i in range(10)]
    
    # Makings objects from images and returning
    colors = []
    for c in color_rects:
            colors.append(Button(c, (color_rects.index(c) * 22, 0)))
    return colors

# Driver code
def main():
    # Setting up display
    dim = width, height = 400 * 2, 300 * 2
    scr = pg.display.set_mode(dim)
    scr.fill(pg.Color('white'))
    
    # Loading imgages for tools
    ld = lambda name: pg.image.load('images/' + name + '.png').convert_alpha()
    Pencil, Eraser, Plus, Minus= ld('Pencil'), ld('Eraser'), ld('Plus'), ld('Minus')
    
    # Loading imgages for shapes
    ld = lambda name: pg.image.load('shapes/' + name + '.png').convert_alpha()
    Rect, Circle, Square, RightTr, Rhomb = ld('Rect'), ld('Circle'), ld('Square'), ld('RightTr'), ld('Rhomb')
    
    # Making objects
    bt = lambda img, x: Button(img, (x, 0))
    Pencil, Eraser, Plus, Minus = bt(Pencil, 220), bt(Eraser, 240), bt(Plus, 260), bt(Minus, 280)
    Rect, Circle, Square, RightTr, Rhomb = bt(Rect, 305), bt(Circle, 330), bt(Square, 355), bt(RightTr, 375), bt(Rhomb, 395)
    
    # Making Groups
    colors = pg.sprite.Group(Color())
    all_sprites = pg.sprite.Group([Color(), Pencil, Eraser, Plus, Minus, Rect, Circle, Square, RightTr, Rhomb])
    
    # Variables
    cur_color = 0
    erase_color = 0
    cur_tool = 'Pen'
    Pen_Draw, Erase = 0, 0
    _Rect, _Circle, _Square, _RightTr, _Rhomb = 0, 0, 0, 0, 0
    draw_width = 5
    Fix = True
    Pivot = (0, 0)
    dx, dy = 0, 0
    
    # Saving screen
    Save_scr = True
    _scr = 0
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Fill panel with gray background
        scr.fill(pg.Color('gray'), pg.Rect(0, 0, width, 20))
        
        # Loop for checking events
        for e in pg.event.get():
            if e.type == pg.QUIT:
                going = False
            
            # Check if any color was picked
            if e.type == pg.MOUSEBUTTONDOWN:
                
                # Save a screen copy before any changes applied
                if Save_scr:
                    Save_scr = 0
                    _scr = scr.copy()                    
                
                # Make a pivot point for shape
                if Fix:
                    Fix = False
                    Pivot = e.pos
                
                # Check if any tool or shape was picked
                if Pencil.clicked(e.pos): cur_tool = 'Pen'                    
                if Eraser.clicked(e.pos): cur_tool = 'Erase'
                if Rect.clicked(e.pos): cur_tool = 'Rect'                    
                if Circle.clicked(e.pos): cur_tool = 'Circle'                    
                if Square.clicked(e.pos): cur_tool = 'Square'                    
                if RightTr.clicked(e.pos): cur_tool = 'RightTr'                    
                if Rhomb.clicked(e.pos): cur_tool = 'Rhomb'                    
                
                # Inccrease or Decrease draw width
                if Plus.clicked(e.pos): draw_width += 3
                if Minus.clicked(e.pos) and draw_width - 3 > 0: draw_width -= 3

                # Check if any color was selected
                for c in colors:
                    if c.clicked(pg.mouse.get_pos()):
                        if cur_tool == 'Erase':
                            erase_color = pg.Color(c.image.get_at((11, 10)))
                        else:
                            cur_color = pg.Color(c.image.get_at((11, 10)))

                # Allow to draw with tool or shape
                if cur_tool == 'Pen': Pen_Draw = True
                elif cur_tool == 'Erase': Erase = True
                else: 
                    if cur_tool == 'Rect': _Rect = True
                    if cur_tool == 'Circle': _Circle = True
                    if cur_tool == 'Square': _Square = True
                    if cur_tool == 'RightTr': _RightTr = True
                    if cur_tool == 'Rhomb': _Rhomb = True
                            
            if e.type == pg.MOUSEBUTTONUP:
                # Set all variavles to initial value
                Save_scr = True
                Fix = True
                Pen_Draw, Erase, _Rect, _Circle, _Square, _RightTr, _Rhomb = 0, 0, 0, 0, 0, 0, 0

            if e.type == pg.MOUSEMOTION:
                # Save mouse curent position
                dx, dy = e.pos
        
        # To draw only when cursor is not on the panel
        if pg.mouse.get_pos()[1] > 20:      
            # Set cross-like cursor to draw
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
            
            # Draw multiple circles when pen is picked              
            if Pen_Draw == True:
                pg.draw.circle(scr, cur_color, (dx, dy), draw_width)

            # Draw multiple squares when eraser is picked              
            elif Erase:
                edge = 1.5 * draw_width
                pg.draw.rect(scr, erase_color, pg.Rect(dx - edge, dy - edge, edge * 2, edge * 2))

            # Draw shapes else    
            else:
                if _Rect: draw.draw_rect(scr, _scr, cur_color, Pivot, (dx, dy), draw_width)
                if _Circle: draw.draw_circle(scr, _scr, cur_color, Pivot, (dx, dy), draw_width)
                if _Square: draw.draw_square(scr, _scr, cur_color, Pivot, (dx, dy), draw_width)
                if _RightTr: draw.draw_rightTr(scr, _scr, cur_color, Pivot, (dx, dy), draw_width)
                if _Rhomb: draw.draw_rhomb(scr, _scr, cur_color, Pivot, (dx, dy), draw_width)

        # Set picking-cursor on panel area
        else: pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            
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
