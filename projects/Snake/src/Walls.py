import pygame as pg, os

CELL = 20
N, M = 30, 20

# Function to get wall positions
def get_walls(screen):
    poses = []
    for i in range(N - 1):
        for j in range(M - 1):
            c = screen.get_at((i * CELL + 1, j * CELL + 1))
            if c[0] < 20 and c[1] < 20 and c[2] < 20:
                poses.append([i, j])
    return poses

def get_ALL_walls():
    walls = []

    for i in range(len(os.listdir('../wallsTemplate'))):
        cur_level = i + 1
        cur_image = pg.image.load(f"../wallsTemplate/Level {cur_level}.jpg")

        walls.append(get_walls(cur_image))
    
    return walls

AllWalls = get_ALL_walls()