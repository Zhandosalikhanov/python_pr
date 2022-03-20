def thr_fou_div(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

if __name__ == "__main__":
    n = int(input())
    res = list(thr_fou_div(n))
    cnt = 0
    for i in res:
        cnt += 1
        print(i, end= '')
        if cnt != len(res):
            print(", ", end= '')