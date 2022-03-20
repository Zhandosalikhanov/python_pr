l = []
while 1:
    x = int(input())
    if(x == 0):
        break
    l.append(x)

if len(l) % 2 == 0:
    for i in range(int(len(l) / 2)):
        print(l[i] + l[len(l) - i - 1], end= ' ')
else:
    for i in range(int(len(l) / 2)):
        print(l[i] + l[len(l) - i - 1], end= ' ')
    print(l[int(len(l) / 2)], end= ' ')