def histogram(nums):
    for c in nums:
        for i in range(c):
            print('*', end= '')
        print()

if __name__ == "__main__":
    l = [4, 7, 9, 3, 6]
    histogram(l)