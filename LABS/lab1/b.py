s = input()
sum = 0

for c in s:
    sum += ord(c)

if sum > 300:
    print("It is tasty!")
else:
    print("Oh, no!")