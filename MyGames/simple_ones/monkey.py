import os
import pygame as pg
import random

if not pg.font:
    print("Error: Fonts disabled")
if not pg.mixer:
    print("Error: Sound disabled")

main_dir = os.path.split(os.path.abspath("__file__"))[0]
data_dir = os.path.join(main_dir, "data")

def load_image(name, colorkey = None, scale = 1):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)

    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pg.transform.scale(image, size)

    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()

def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)

    return sound

class Fist(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("fist.png")
        self.fist_offset = (-0, -80)
        self.punchng = False

    def update(self):
        pos = pg.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punchng:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        if not self.punchng:
            self.punchng = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        self.punchng = False


class Chimp(pg.sprite.Sprite):

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("chimp.png", -1, 4)
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 20
        self.dizzy = False

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        newPos = self.rect.move((self.move, 0))
        if not self.area.contains(newPos):
            if self.rect.left < self.area.left:
                self.move = random.random() * 100
                newPos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, True, False)
            if self.rect.right > self.area.right:
                self.move = -random.random() * 100
                newPos = self.rect.move((self.move, 0))
                self.image = pg.transform.flip(self.image, True, False)
        self.rect = newPos

    def _spin(self):
        center = self.rect.center
        self.dizzy += 12

        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pg.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center= center)

    def punched(self):
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image  

if __name__ == '__main__':
    pg.init()

    screen = pg.display.set_mode((1500 * 2, 500))
    pg.display.set_caption("Monke! Monke! Monke!")
    pg.mouse.set_visible(False)

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    if pg.font:
        font = pg.font.Font(None, 64)
        text = font.render("KILL ME! IF YOU CAN... HA-HA-HA", True, (10, 10, 10))
        textpos = text.get_rect(centerx= background.get_width() / 2, y= 10)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pg.display.flip()

    laugh = load_sound("laugh.wav")
    punch_sound = load_sound("punch.mp3")
    
    chimp = Chimp()
    fist = Fist()

    allsprites = pg.sprite.RenderPlain((fist, chimp))
    clock = pg.time.Clock()

    going = True
    while going:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN or event.type == pg.K_ESCAPE:
                going = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()
                    chimp.punched()
                else:
                    laugh.play()
            elif event.type == pg.MOUSEBUTTONUP:
                fist.unpunch()

        allsprites.update()

        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pg.display.flip()

    pg.quit()
    