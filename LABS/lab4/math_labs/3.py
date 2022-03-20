import math

def reg_pol_area(n, l):
    return (1 / 4) * n * pow(l, 2) * (1 / math.tan(math.pi / n))

if __name__ == "__main__":
    n_of_sides = int(input("Input number of sides: "))
    l_of_side = float(input("Input the length of a side: "))
    print("The area of the polygon is:", reg_pol_area(n_of_sides, l_of_side))