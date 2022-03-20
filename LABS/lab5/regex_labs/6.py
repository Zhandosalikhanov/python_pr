import re

def chang_f(text):
    return re.sub("\s|[,]|[.]", ':', text)

s = input()
print(chang_f(s))