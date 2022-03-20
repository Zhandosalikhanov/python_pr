n = int(input())
l = []

i = 0
while i < n:
    s = input()
    if s.find("@gmail.com") != -1:
        l.append(s[0 : len(s) - 10])
    i += 1

for c in l:
    print(c)