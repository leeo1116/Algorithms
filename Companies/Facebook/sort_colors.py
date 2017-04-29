def sort_colors(nums):
    j, k = 0, len(nums) - 1
    for i in range(len(nums)):
        if nums[i] == 0:
            while nums[j] == 0 and j < i:
                j += 1
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(len(nums)):
        if nums[i] == 2 and i < k:
            while nums[k] == 2 and k > i:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]


sort_colors([1, 2, 0])
