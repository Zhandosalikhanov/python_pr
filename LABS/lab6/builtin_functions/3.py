def isPal(s):
    return s == s[::-1]

if __name__ == '__main__':
    print(isPal("mama"))
    print(isPal("mam"))
    print(isPal("a"))
    print(isPal("acaca"))
    print(isPal("acacab"))