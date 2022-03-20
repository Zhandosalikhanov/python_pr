def has_007(nums):
    nums = list(nums)
    if nums.count(0) > 1:
        if (nums[nums.index(0, nums.index(0) + 1):]).count(7) > 0:
            return (nums.index(0) - nums.index(0, nums.index(0) + 1) == -1 and nums.index(7, nums.index(0) + 2) - nums.index(0, nums.index(0) + 1) == 1)
    return False

if __name__ == "__main__":
    l = [1, 2, 3, 0, 0, 7]
    l1 = [3, 2, 3, 7, 0, 0]
    l2 = [1, 2, 3, 4, 9, 8]

    print(has_007(l))
    print(has_007(l1))
    print(has_007(l2))