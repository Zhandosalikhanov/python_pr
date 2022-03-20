n = int(input())
dt = {
}
i = 0
max = 0

while i < n:
    sur, val = input().split()
    val = int(val)

    if sur in dt:
        dt[sur] += val
    else:
        dt[sur] = val
    i += 1

for c in dt.values():
    if max < c:
        max = c

for key in sorted(dt):
    if(dt[key] != max):
        print(key + " has to receive", end= ' ')
        print(max - dt[key], end= ' ')
        print("tenge")
    else:
        print(key + " is lucky!")