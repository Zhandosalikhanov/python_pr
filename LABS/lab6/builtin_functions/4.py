from math import sqrt
from time import sleep

def sqrt_of(n, sec):
    sleep(sec * 0.001)
    return(sqrt(n))

if __name__ == '__main__':
    print(sqrt_of(16, 2000))
    print(sqrt_of(81, 0))
    print(sqrt_of(44, 251))