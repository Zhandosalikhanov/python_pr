def even_gen(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    n = int(input())
    res = list(even_gen(n))
    cnt = 0
    for i in res:
        cnt += 1
        print(i, end= '')
        if cnt != len(res):
            print(", ", end= '')