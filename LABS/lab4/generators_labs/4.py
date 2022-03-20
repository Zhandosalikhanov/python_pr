def squares(a, b):
    for i in range(a, b):
            yield i * i

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    res = list(squares(a, b))
    cnt = 0
    for i in res:
        cnt += 1
        print(i, end= '')
        if cnt != len(res):
            print(", ", end= '')