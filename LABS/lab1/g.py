s = input()

res = 0
j = 1
for i in s:
    res += (ord(i) - 48) * pow(2, len(s) - j)
    j += 1

print(res)
