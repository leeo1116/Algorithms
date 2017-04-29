from heapq import heappush, heappop, heapify


def find_median(nums_list):
    """
    Find median of a list of sorted arrays
    :param nums_list: 
    :return: 
    """
    index = [0] * len(nums_list)
    total_nums = sum(list(map(lambda x: len(x), nums_list)))
    heap = []
    for i, nums in enumerate(nums_list):
        heappush(heap, (nums[0], i))

    n = total_nums // 2 + 1
    median1 = median2 = 0
    while n > 0:
        median2 = median1
        median1, j = heappop(heap)
        index[j] += 1
        if index[j] < len(nums_list[j]):
            heappush(heap, (nums_list[j][index[j]], j))
        n -= 1
    return median1 if total_nums % 2 else (median1 + median2) / 2


print(find_median([[1, 2, 3], [5]]))
