import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def res(my_list):
    return lambda arr: list(filter(lambda x: is_prime(x), arr))(my_list)

if __name__ == "__main__":
    ans = lambda arr: list(filter(lambda x: is_prime(x), arr))
    print(ans([10,21,3,8,9,11,44,62,100,19]))