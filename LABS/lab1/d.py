x = int(input())
z = input()
c = 0

if z == 'k':
    c = int(input())

if c:
    print("%.*f" % (c, x / 1024))
else:
    print(x * 1024)