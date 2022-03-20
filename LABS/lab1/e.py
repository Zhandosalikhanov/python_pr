from math import sqrt

def isPrime(a):
    c = 2
    while c <= sqrt(a):
        if(a % c == 0):
            return 0
        c += 1
    return 1

d, cart = input().split()
d = int(d)
cart = int(cart)

if(d <= 500 and isPrime(d) and cart % 2 == 0):
    print("Good job!")
else:
    print("Try next time!")