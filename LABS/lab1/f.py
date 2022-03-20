n = int(input())

i = 0
while i < n:
    c = int(input())
    if c <= 10:
        print("Go to work!")
    elif c > 10 and c <= 25:
        print("You are weak")
    elif c > 25 and c <= 45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")
    i += 1