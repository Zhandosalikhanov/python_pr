s = input()
n = 0
x = 0
if s.find(' ') == -1:
    s1 = int(input())
    n = int(s)
    x = s1
else:
    a = s.split(' ')
    n = int(a[0])
    x = int(a[1])
# arr[i] = x + 2 * i
# arr.size() = n

i = 0
a = 0
ans = 0

while i < n:
    a = x + 2 * i
    i += 1
    ans = ans ^ a

print(ans)