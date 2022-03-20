def square_gen(n):
    for i in range(1, n):
        yield i * i

if __name__ == "__main__":
    n = int(input())
    res = square_gen(n)
    for i in res:
        print(i, end= " ")