def permutList(l):
    if not l:
        return [[]]
    res = []
    for e in l:
        temp = l[:]
        temp.remove(e)
        res.extend([[e] + r for r in permutList(temp)])

    return res

if __name__ == "__main__":
    l = [1, 2, 3, 4]
    for c in permutList(l):
        print(c)