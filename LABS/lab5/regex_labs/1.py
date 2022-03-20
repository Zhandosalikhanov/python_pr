import re
#if I'll take item = ".*ab*" it doesn't make sense
#because it is the same as taking item = ".*a*"
#It will return True whenever 'a' was found
def isMatch(text):
    item = "^a(b*)$"
    if re.search(item, text):
        return True
    return False

s = input()
print(isMatch(s))