# Importing libraries
import pygame as pg

class Slider:
    def __init__(self, left, top, width, height, name, min_val, max_val, current_value= 0, color= 'white', isFloat = False):
        """Class to create a toddler to pick the value

        Args:
            left (int): Position along x-coordinate
            top (int): Position along y-coordinate
            width (int): The width of the toddler
            height (int): The height of the toddler
            name (str): The name of the slider
            min_val (float): The minimum value of the slider
            max_val (float): The maximum value of the slider
            current_value (float, optional): The inital value of the slider. Defaults to 0.
            color (str, optional): Name of the colour for the slider. Defaults to 'white'.
            isFloat (Bool, optional): To round the value each time or not
        """
        self.color = pg.Color(color)
        self.rect = pg.Rect(left, top, width, height)
        self.name = name
        self.min= min_val
        self.max= max_val
        self.value = current_value
        self.step = max(width, max_val) / min(width, max_val)
        self.float = isFloat
        self.change = False

    def move(self, mouse):
        """To move the value of the slider with mouse

        Args:
            mouse (tuple): The coordinates of the mouse
        """
        dx = mouse[0] - self.rect.left
        if dx / self.step <= self.max and dx / self.step >= self.min:
            if self.float:
                self.value = round(dx / self.step, 4)
            else:
                self.value = int(dx / self.step)
        
    def blit(self, screen):
        """To blit the slider onto the given screen

        Args:
            screen (Pygame Surface): Screen on which the slider will be displayed
        """
        f = pg.font.SysFont('timesnewroman', 15)
        rend = lambda x: f.render(str(x), True, (255, 255, 255))
        name, max, cur = rend(self.name), rend(self.max), rend(self.value)
        
        pg.draw.rect(screen, self.color, self.rect)
        screen.blit(name, (self.rect.left, self.rect.top - 20))
        screen.blit(max, (self.rect.right, self.rect.top))
        screen.blit(cur, (self.rect.left + self.rect.w / 2, self.rect.bottom))
        pg.draw.circle(screen, (255, 255, 255), (self.rect.left + (self.value - self.min) * self.step, self.rect.centery), self.rect.height / 1.8)

# Driver code
def main():
    # Setting up dimensions and screen
    dim = W, H = 400, 300
    scr = pg.display.set_mode(dim)
    
    # Making slider objects
    s1 = Slider(20, 20, 100, 10, 'm1', 0, 50, 20, 'black')
    
    # Variables
    Move = False
    
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
                if s1.rect.collidepoint(e.pos):    
                    Move = True
            
            if e.type == pg.MOUSEBUTTONUP:
                Move = False
                
        scr.fill(pg.Color('green'))            
        
        if Move:
            s1.move(pg.mouse.get_pos())
            
        s1.blit(scr)
        
        # Tick and flip
        pg.display.flip()
        fps.tick(60)

# Launcher code
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()