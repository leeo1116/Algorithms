def maximum_product(nums):
    max_product, min_product, global_max = nums[0], nums[0], nums[0]
    for n in range(1, len(nums)):
        if n >= 0:
            max_product = max(n, max_product * n)
            min_product = min(n, min_product * n)
        else:
            max_product = max(n, min_product * n)
            min_product = min(n, max_product * n)
        global_max = max(global_max, max_product)
    return global_max
