from math import sqrt
p = X, Y = input().split()
X = int(X)
Y = int(Y)
n = int(input())
i = 0
a = []

while i < n:
    x, y = input().split()
    x = int(x)
    y = int(y)
    a.append((x, y))
    i += 1
def dis(int: x, y):
    return sqrt(pow(X - x, 2) + pow(Y - y, 2))

dt = {
}
for c in a:
    dt[c] = dis(c[0], c[1])
print()
for c in sorted(dt, key= dt.get):
    print(c[0], c[1])