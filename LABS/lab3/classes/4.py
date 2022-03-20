from math import sqrt

class Point():
    def __init__(point, x_coor, y_coor):
        point.x_coor = x_coor
        point.y_coor = y_coor
    
    def show(point):
        print("The coordinates of a point:", point.x_coor, "and", point.y_coor)

    def move(point, new_x, new_y):
        point.x_coor = new_x
        point.y_coor = new_y
        print("Coordinates have been changed to", new_x, "and", new_y)

    def dist(point, x, y):
        X = point.x_coor
        Y = point.y_coor
        print("The distance between points (", 
        point.x_coor, ',', point.y_coor, ") and (", 
        x, ',', y, ") is: ", 
        sqrt(pow(X - x, 2) + pow(Y - y, 2)))

if __name__ == "__main__":
    p1 = Point(0, 1)
    p1.show()
    p1.move(5, 7)
    p1.dist(0, 0)