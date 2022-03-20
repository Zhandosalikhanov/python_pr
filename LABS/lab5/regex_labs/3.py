import re

s = input()
pattern = "[a-z]+_[a-z]+"
ans = re.findall(pattern, s)
print(ans)