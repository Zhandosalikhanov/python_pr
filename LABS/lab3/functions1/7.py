def has_33(nums):
    nums = list(nums)
    if nums.count(3) > 1:
        return (nums.index(3) - nums.index(3, nums.index(3) + 1) == -1)
    return False

if __name__ == "__main__":
    l = [1, 2, 3, 3, 5]
    l1 = [3, 2, 3, 7]
    l2 = [1, 2, 3, 4, 9]

    print(has_33(l))
    print(has_33(l1))
    print(has_33(l2))