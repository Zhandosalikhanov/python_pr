s = input()
ch = input()

case = 0
i = 0
j = 0

ind1 = -1

for c in s:
    if c == ch and case == 0:
        ind1 = i
        case += 1
    elif c == ch and case != 0:
        j = i
    i += 1

if j != 0:
    print(str(ind1) + ' ' + str(j))
elif ind1 != -1:
    print(ind1)