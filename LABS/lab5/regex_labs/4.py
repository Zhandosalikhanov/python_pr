import re

s = input()
pattern = "[A-Z][a-z]+"
ans = re.findall(pattern, s)
print(ans)