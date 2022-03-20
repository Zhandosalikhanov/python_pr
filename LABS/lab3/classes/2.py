class Shape:
    class Square:
        def __init__(square, length):
            square.length = length

        def Area(square):
            return(square.length * square.length)
    
    def Area(self):
        return 0

if __name__ == "__main__":
    p1 = Shape()
    print("Shape area: ", p1.Area())
    print("Square area: ", p1.Square(5).Area())