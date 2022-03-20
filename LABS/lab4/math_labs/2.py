def trap_area(height, b1, b2):
    base = min(b1, b2) 
    BASE = max(b1, b2)
    return height * (base + ((BASE - base) / 2))

if __name__ == "__main__":
    h = float(input("Enter height: "))
    b1 = float(input("Enter base1: "))
    b2 = float(input("Enter base2: "))
    print("The trapezoid area is:", trap_area(h, b1, b2))
    # Used math as much as possible