def num_to_zero(n):
    for i in range(n, 0, -1):
        yield i

if __name__ == "__main__":
    n = int(input())
    res = list(num_to_zero(n))
    cnt = 0
    for i in res:
        cnt += 1
        print(i, end= '')
        if cnt != len(res):
            print(", ", end= '')