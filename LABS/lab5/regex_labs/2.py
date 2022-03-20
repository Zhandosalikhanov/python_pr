import re

def isMatch(text):
    item = "ab{2,3}"
    if re.search(item, text):
        return True
    return False

s = input()
print(isMatch(s))