from posixpath import split


n = int(input())
q = []
ans = []
for i in range(n):
    x = input()
    if x.find(' ') != -1:
        x, y = x.split()
    if x == '1':
        q.append(y)
    else:
        ans.append(q.pop(0))

for c in ans:
    print(c, end= ' ')