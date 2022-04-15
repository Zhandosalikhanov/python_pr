import pygame as pg, math

# Function to draw rectangle
def draw_rect(screen, prev, color, pivot, pos, width):
    # Coordinates of points
    top_left = pivot
    top_right = pos[0], pivot[1]
    bottom_right = pos
    bottom_left = pivot[0], pos[1]
    
    points = top_left, top_right, bottom_right, bottom_left
    
    screen.blit(prev, (0, 0))
    pg.draw.polygon(screen, color, points, width)
    
# Function to draw circle
def draw_circle(screen, prev, color, pivot, pos, width):
    # Calculate radius by Pythagorean theorem
    x = pos[0] - pivot[0]
    y = pos[1] - pivot[1]
    radius = math.sqrt(x * x + y * y)
    
    screen.blit(prev, (0, 0))
    pg.draw.circle(screen, color, pivot, radius, width)

# Function to draw square 
def draw_square(screen, prev, color, pivot, pos, width):
    # Rect with same width and height
    rect = pg.Rect(pivot[0], pivot[1], pos[0] - pivot[0], pos[0] - pivot[0])
    
    screen.blit(prev, (0, 0))
    pg.draw.rect(screen, color, rect, width)

# Function to draw right triangle
def draw_rightTr(screen, prev, color, pivot, pos, width):
    # Coordinates of points
    top = pivot
    bottom = pivot[0], pos[1]
    right = pos[0], pos[1]
    
    points = top, bottom, right
    
    screen.blit(prev, (0, 0))
    pg.draw.polygon(screen, color, points, width)
    
# Function to draw rhomb    
def draw_rhomb(screen, prev, color, pivot, pos, width):
    # Coordinates of points
    top = pivot[0], 2 * pivot[1] - pos[1]
    left = 2 * pivot[0] - pos[0], pivot[1]
    right = pos[0], pivot[1]
    bottom = pivot[0], pos[1]
    
    points = top, left, bottom, right
    
    screen.blit(prev, (0, 0))
    pg.draw.polygon(screen, color, points, width)