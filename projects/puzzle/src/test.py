# Importing libraries
import pygame as pg

class Piece(pg.sprite.Sprite):
    # Initalizing a piece
    def __init__(self, img, pos):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
    
    # Function to check if piece was clicked
    def clicked(self, mouse): return self.rect.collidepoint(mouse)
    
    # Function to move the piece
    def move(self, mouse, empty): 
        x = self.rect.centerx
        y = self.rect.centery
        w, h = self.rect.w / 2, self.rect.h / 2
        
        if self.rect.collidepoint(mouse):
            if empty[1] - y > h and empty[1] - y <= 2 * h and mouse[1] - y > 0:
                self.rect.centery = mouse[1]
                
            if empty[1] - y < -h and empty[1] - y >= -2 * h and mouse[1] - y < 0:
                self.rect.centery = mouse[1]    
                
            if empty[0] - x > w and empty[0] - x <= 2 * w and mouse[0] - x > 0:
                self.rect.centerx = mouse[0]
                
            if empty[0] - x < -w and empty[0] - x >= -2 * w and mouse[0] - x < 0:
                self.rect.centerx = mouse[0]
    
    # Function to swap the piece with empty one
    def swap(self, empty): 
        x = self.rect.centerx
        y = self.rect.centery
        center = empty.rect.center  
        w, h = self.rect.w, self.rect.h
        
        if empty.rect.colliderect(self.rect):
            if center[1] - y > 0:
                self.rect.center = center
                empty.rect.centery -= h  
                    
            if center[1] - y < 0:
                self.rect.center = center
                empty.rect.centery += h    
                
            if center[0] - x > 0:
                self.rect.center = center
                empty.rect.centerx -= w
                
            if center[0] - x < 0:
                self.rect.center = center
                empty.rect.centerx += w
                    
    # Function to blit piece onto the screen            
    def blit(self, screen): screen.blit(self.image, self.rect)

# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 400, 300
    scr = pg.display.set_mode(dim)
    
    cell = pg.image.load('images/a.jpg').convert()
    cell = pg.transform.scale(cell, (50, 50))
    
    empty = pg.image.load('cell.jpg').convert()
    empty = pg.transform.scale(empty, (50, 50))
    
    empty = Piece(empty, (200, 200))
    cell = Piece(cell, (200, 150))
    
    move = False
    swap = False
    
    # Main Loop
    fps = pg.time.Clock()
    going = True
    while going:
        # Loop through the events
        for e in pg.event.get():
            # Quit
            if e.type == pg.QUIT:
                going = False
            
            if e.type == pg.MOUSEBUTTONDOWN:
                swap = False
                if cell.clicked(e.pos): move = True

            if e.type == pg.MOUSEMOTION and move:
                cell.move(e.pos, empty.rect.center)
            
            if e.type == pg.MOUSEBUTTONUP:
                swap = True
                move = False
            
        if swap: cell.swap(empty)
        scr.fill(0)
        empty.blit(scr)
        cell.blit(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()