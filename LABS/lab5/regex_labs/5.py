import re

def isMatch(text):
    item = "^a.+b$"
    if re.search(item, text):
        return True
    return False

s = input()
print(isMatch(s))