import re
def snake_case(s):
    # return '_'.join(re.sub("([A-Z][a-z]+)", r' \1', s).split()).lower()
    # return '_'.join(re.sub("\W", ' ', s).split()).lower()
    # return '_'.join(re.sub("([A-Z]+)", r' \1', s).lower().split())
    # combine code for all of the cases:
    return '_'.join(re.sub("([A-Z][a-z]+)", r' \1', re.sub("([A-Z]+)", r' \1', re.sub("\W", ' ', s))).lower().split())

s = input()
print(snake_case(s))