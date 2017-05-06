def top_2_max(nums):
    top2max = []
    if not nums:
        return top2max
    max1 = max2 = nums[0]
    for n in nums:
        if n > max1:
            max2 = max1  # delay by one step. Note: it's not necessarily the second maximum
            max1 = n  # Always update maximum (max1)
        elif n > max2:
            max2 = n  # Update to the second maximum which is less than max1
    return [max1, max2]
