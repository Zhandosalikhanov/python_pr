s = input()

def tolower(a):
    s1 = ""

    for c in a:
        if ord(c) < 91 and ord(c) > 64:
            s1 += chr(ord(c) + 32)
        else:
            s1 += c

    return s1

print(tolower(s))