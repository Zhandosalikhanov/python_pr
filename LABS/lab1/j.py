s = input()
s += ' '
l = []
i = 0
j = 0
for c in s:
    if c == ' ':
        if len(s[j : i]) > 2:
            l.append(s[j : i])
        j = i + 1
    i += 1

for c in l:
    print(c, end= ' ')