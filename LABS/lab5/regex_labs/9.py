import re

def spl_uppcase(text):
    res = re.findall("[A-Z][a-z]+", text)
    ans = ''
    for c in res:
        ans += c + '_'
    return ans[:-1]

print(spl_uppcase("HiJohnHowAreYou"))