# Importing libraries
import pygame as pg
import os, random

# Class for one Piece
class Piece(pg.sprite.Sprite):
    # Initalizing a piece
    def __init__(self, img, pos):
        super().__init__()
        
        # Setting image and its position
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        
        # Whether move or swap
        self._move = False
        self._swap = False
        self.swapped = False
    
    # Function to check if piece was clicked
    def clicked(self, mouse): return self.rect.collidepoint(mouse)
    
    # Function to move the piece
    def move(self, mouse, empty): 
        x = self.rect.centerx                       # Piece current x position
        y = self.rect.centery                       # Piece current y position  
        w, h = self.rect.w / 2, self.rect.h / 2     # Half of the block
        
        if self.rect.collidepoint(mouse):
            # Move along y-axis if empty cell is on the same x-coordiante
            if empty[0] == x:
                
                # Move only downward and till the half of the empty block             
                if empty[1] - y > h and empty[1] - y <= 2 * h and mouse[1] - y > 0:
                    self.rect.centery = mouse[1]
                    
                # Move only upward and till the half of the empty block             
                if empty[1] - y < -h and empty[1] - y >= -2 * h and mouse[1] - y < 0:
                    self.rect.centery = mouse[1]    
            
            # Move along x-axis if empty cell is on the same y-coordiante
            if empty[1] == y:   
                
                # Move only right and till the half of the empty block             
                if empty[0] - x > w and empty[0] - x <= 2 * w and mouse[0] - x > 0:
                    self.rect.centerx = mouse[0]
                    
                # Move only left and till the half of the empty block             
                if empty[0] - x < -w and empty[0] - x >= -2 * w and mouse[0] - x < 0:
                    self.rect.centerx = mouse[0]
    
    # Function to swap the piece with another one
    def swap(self, empty, BezSeremonii): 
        x = self.rect.centerx               # Piece current x position
        y = self.rect.centery               # Piece current y position  
        w, h = self.rect.w, self.rect.h     # Dimeansion of the block
        center = empty.rect.center          # Center of the empty cell
        
        # Swap places if on top of eachother or if it is UNDO of REDO command
        if empty.rect.colliderect(self.rect) or BezSeremonii:
            # Swap with the bottom cell
            if center[1] - y > 0:
                self.rect.center = center
                empty.rect.centery -= h
                
            # Swap with the top cell
            if center[1] - y < 0:
                self.rect.center = center
                empty.rect.centery += h    
                
            # Swap with the right cell
            if center[0] - x > 0:
                self.rect.center = center
                empty.rect.centerx -= w
                
            # Swap with the left cell
            if center[0] - x < 0:
                self.rect.center = center
                empty.rect.centerx += w
            
            # Write that block was swapped
            self.swapped = True        

    # Function to blit piece onto the screen            
    def blit(self, screen): screen.blit(self.image, self.rect)
    
# Function to slice the image
def cut(img, top, left, w, h):
    copy = img.copy()
    rect =  pg.Rect(top, left, w, h)
    
    copy.set_clip(rect)
    return copy.subsurface(copy.get_clip())

# Operator to cut image into pieces
def cutter(image, num):
    dict = { }                  # Dictionary to store images with positions
    imgs, poses = [], []        # Arrays for images and positions
    x, y = W / num, H / num     # Dimensions of the cell
    
    # Cut image into 10x10 pieces
    for i in range(num):
        for j in range(num):
            # Cutting one piece
            img = cut(image, i * x, j * y, x, y)
            pos = (i * x, j * y)
            
            # Storing image and its positions into arrays
            imgs.append(img)
            poses.append(pos)

    # Deleting last image and position
    imgs.pop()
    poses.pop()
    random.shuffle(imgs)    # Randomize images 
    
    # Store array elements into dictionary
    for i in range(num * num - 1):
        dict.update({imgs[i] : poses[i]})
    
    return dict

# Driver code
def main():
    # Setting up dimensions and screen
    global W, H
    W, H = 400, 300
    dim = W, H
    scr = pg.display.set_mode(dim)
    
    # Set Caption
    pg.display.set_caption('Puzzle')
    
    # Storing images
    ld = lambda name: pg.transform.scale(pg.image.load('../images/' + name).convert(), dim)
    img_names = os.listdir('../images')
    imgs = [ld(name) for name in img_names]
    
    # Initial Variables
    Initialize = True               # Whether to initialize everything or not
    num = 3                         # Number of pieces in a row
    cur = 1                         # Index of a current image
    show = 0                        # Whether to show or not final image
    play = 1                        # Whether to play or not sound effect
    
    def init(cur, num):
        global cur_img, dict, pieces, all_sprites, empty, swapped, _swapped
        # Making piece objects and grouping
        cur_img = imgs[cur % len(imgs)]
        dict = cutter(cur_img, num)
        pieces = [Piece(img, dict[img]) for img in dict.keys()]
        all_sprites = pg.sprite.Group(pieces)
        
        swapped, _swapped = [], []  # Arrays for UNDO and REDO commands

        # Making empty object
        x, y = W / num, H / num     # Dimensions of one piece
        empty = pg.image.load('cell.jpg').convert()
        empty = pg.transform.scale(empty, (x, y))
        empty = Piece(empty, ((num - 1) * x, (num - 1) * y))
        
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        
        if Initialize:
            Initialize = False
            init(cur, num)
        
        # Fill background with black
        scr.fill(0)
        
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
            
            # Check if piece was clicked
            if e.type == pg.MOUSEBUTTONDOWN:
                for p in all_sprites:
                    # Don't swap while mousebutton is down
                    p._swap = False
                    if p.clicked(e.pos): p._move = True

            # To move pieces that should be moved
            if e.type == pg.MOUSEMOTION:
                for p in all_sprites:
                    if p._move:
                        p.move(e.pos, empty.rect.center)
            
            # Allow to swap and stop moving
            if e.type == pg.MOUSEBUTTONUP:
                if 1 + play: pg.mixer.Sound('wood.wav').play()   # Play wooden sound
                for p in all_sprites: 
                    p._swap = True
                    p._move = False
                    
            # Return to piced image if space is not pressed
            if e.type == pg.KEYUP and e.key == pg.K_SPACE: show = False
            
            # UNDO and REDO operations and more
            if e.type == pg.KEYDOWN:
                
                # Re-Initialize if R was pressed
                if e.key == pg.K_r: Initialize = True
                
                # Increase the number of divisions and Re-Initialize
                if e.key == pg.K_UP:
                    if num + 1 < 10:
                        Initialize = True
                        num += 1
                        
                # Decrease the number of divisions and Re-Initialize
                if e.key == pg.K_DOWN:
                    if num - 1 > 1:
                        Initialize = True
                        num -= 1
                
                # Show final image                    
                if e.key == pg.K_SPACE: show = True
                
                # Next image and Re-Initialize
                if e.key == pg.K_RIGHT:
                    Initialize = True
                    cur += 1
                    
                # Next image and Re-Initialize
                if e.key == pg.K_LEFT:
                    Initialize = True
                    cur -= 1
                
                # Disable or enable sound effect
                if e.key == pg.K_s: play *= -1
                
                if e.key == pg.K_z and len(swapped):
                    last = swapped.pop()
                    empty.swap(last, True)              # Swap empty cell with the last swapped one
                    _swapped.append(last)               # Remember the piece that was UNDO-ed
                    
                if e.key == pg.K_y and len(_swapped):
                    last = _swapped.pop()
                    last.swap(empty, True)              # Swap last swapped cell with the empty one
                    swapped.append(last)                # Remember the piece that was REDO-ed
                    last.swapped = False                # To show that it's not moved by mouse
                
        # Blitting empty cell                
        empty.blit(scr)
        
        # Moving and Blitting all pieces
        for p in all_sprites:
            if p._swap: p.swap(empty, False)        # To swap necessary pieces

            if p.swapped: 
                if len(_swapped): _swapped.clear()  # clear REDO-list if new change appeared while REDO is not finshed
                p.swapped = False                   # Swap only once
                swapped.append(p)                   # Remember the change
                
            if show: scr.blit(cur_img, (0, 0))      # Blit original image onto the screen
            else: p.blit(scr)                       # Blit piece onto the screen

        # Tick and flip
        pg.display.flip()
        fps.tick(60)

        
# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()