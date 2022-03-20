class Shape:
    class Square:
        def __init__(square, length):
            square.length = length

        def Area(square):
            return(square.length * square.length)

    def Area(self):
        return 0

class Rectangle(Shape):
    def __init__(rectangle, length, width):
        rectangle.length = length
        rectangle.width = width

    def rec_Area(rectangle):
        return(rectangle.length * rectangle.width)

if __name__ == "__main__":
    p1 = Rectangle(5, 2).rec_Area()
    print("Rectangle area: ", p1)
    p2 = Rectangle(5, 2).Area()
    print("Shape area: ", p2)
    p3 = Rectangle(5, 2).Square(2)
    print("Square area: ", p3.Area())