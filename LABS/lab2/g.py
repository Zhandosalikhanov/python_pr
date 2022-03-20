n = int(input())
i = 0
ddt = {
}

while i < n:
    name, weak = input().split()
    if weak not in ddt:
        ddt[weak] = 0
    ddt[weak] += 1
    i += 1

n = int(input())
hdt = {
}
i = 0

while i < n:
    name, abil, k = input().split()
    k = int(k)
    if abil not in hdt:
        hdt[abil] = 0
    hdt[abil] += k
    i += 1

for c in hdt:
    if c  in ddt:
        a = ddt[c] - hdt[c]
        if a <= 0:
            ddt.pop(c)
        else:
            ddt[c] = a

print("Demons left:", sum(ddt.values()))