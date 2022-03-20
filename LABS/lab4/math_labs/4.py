def paral_area(base, height):
    return base * height

if __name__ == "__main__":
    base = float(input("Length of base: "))
    height = float(input("Height of parallelogram: "))
    print("The area of the parallelogram is:", paral_area(base, height))