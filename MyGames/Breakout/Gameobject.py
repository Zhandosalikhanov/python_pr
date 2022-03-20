from pygame.rect import Rect

class GameObject:
    def __init__(self, x, y, w, h, speed = (0, 0)):
        self.bounds = Rect(x, y, w, h)
        self.speed = speed
    def left(self):
        return self.bounds.left
 
    def right(self):
        return self.bounds.right
 
    def top(self):
        return self.bounds.top
 
    def bottom(self):
        return self.bounds.bottom
 
    def width(self):
        return self.bounds.width
 
    def height(self):
        return self.bounds.height
 
    def center(self):
        return self.bounds.center
 
    def centerx(self):
        return self.bounds.centerx
 
    def centery(self):
        return self.bounds.centery
 
    def draw(self, surface):
        pass
 
    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)
 
    def update(self):
        if self.speed == [0, 0]:
            return
 
        self.move(*self.speed)   