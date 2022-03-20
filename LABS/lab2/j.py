def isStrong(s):
    s = str(s)
    if s != s.lower() and s != s.upper() and not s.isalpha():
        return 1
    return 0

n = int(input())
a = []

for i in range(n):
    s = input()
    if isStrong(s):
        a.append(s)

a = set(a)
print(len(a))
for c in sorted(a):
    print(c)