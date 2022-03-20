l = []

while 1:
    s = input().split()
    if s[0] == '0':
        break
    s.reverse()
    l.append(s)
l.sort()

for c in l:
    for i in reversed(c):
        print(i, end= ' ')
    print()