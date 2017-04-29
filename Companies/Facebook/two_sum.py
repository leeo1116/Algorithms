def two_sum(nums, target):
    num_index_dict = {}
    for i, n in enumerate(nums):
        if num_index_dict.get(target - n, -1) != -1:
            return num_index_dict[target - n], i
        num_index_dict[n] = i
    return ()
