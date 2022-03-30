import sys, pygame
pygame.init()

size = width, height = 800, 350
speed = [3, 3]
black = 0, 0, 0
fps = pygame.time.Clock()
screen = pygame.display.set_mode(size)

ball = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\python_pr\MyGames\simple_ones\data\ball.jpg")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.height > height or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    fps.tick(60)    