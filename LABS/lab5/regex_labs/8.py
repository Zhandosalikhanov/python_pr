import re

def spl_uppcase(text):
    return re.findall("[A-Z][a-z]+", text)

for c in spl_uppcase("HiJohnHowAreYou"):
    print(c, end= ' ')