import ten
import four

l = [1, 2, 7, 13, 18, 1, 2, 7, 23, 6, 9, 12]

ans = lambda arr: list(filter(lambda x: four.is_prime(x), arr))

ans1 = ten.del_dupl(l)

print(ans(l))
print(ans1)