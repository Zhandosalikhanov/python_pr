from re import S


def rev_print(string):
    for c in reversed(string):
        print(c, end= ' ')

if __name__ == "__main__":
    s = input().split()
    rev_print(s)