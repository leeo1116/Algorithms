def intersection_naive(nums1, nums2):
    """
    Find the intersection of two arrays. 
    Note: this only solves the case when all elements in the array are distinct
    :param nums1: array 1 
    :param nums2: array 2
    :return: intersection of the input arrays
    """
    nums = []
    nums1_set = set(nums1)
    for n2 in nums2:
        if n2 in nums1_set:
            nums.append(n2)
    return nums


def intersection(nums1, nums2):
    nums = []
    num_count_dict = {}
    for n1 in nums1:
        num_count_dict[n1] = num_count_dict.get(n1, 0) + 1

    for n2 in nums2:
        if num_count_dict.get(n2, -1) > 0:
            nums.append(n2)
            num_count_dict[n2] -= 1

    return nums


print(intersection_naive([1, 2, 3, 4, 5], [1, 1, 1, 3, 4]))
print(intersection([2, 1, 3, 4, 1, 5], [1, 1, 1, 3, 4]))
