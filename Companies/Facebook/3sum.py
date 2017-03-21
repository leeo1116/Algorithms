"""Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in
the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


def three_sum(nums):
    """
    Return the index of 3 elements that sum up to 0, no duplicates
    :param nums: a list of integers
    :type nums: list
    :return: a list of valid index
    """
    # Corner case handling
    indices = []
    nums_len = len(nums)
    if nums_len < 3:
        return indices

    # Sort the numbers
    nums.sort()
    for i in range(nums_len - 2):
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):  # Good practice
            j, k = i + 1, nums_len - 1
            two_sum = 0 - nums[i]
            while j < k:
                # Compare two_sum and sum of elements at j, k
                jk_sum = nums[j] + nums[k]
                if jk_sum == two_sum:
                    indices.append([nums[i], nums[j], nums[k]])
                    # Skipping duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif jk_sum < two_sum:
                    j += 1
                else:
                    k -= 1
    return indices


print(three_sum([-1, 0, 1, 2, -1, -4]))

# Time complexity: sort O(n) average for quick sort
# O(n^2) for comparing 0 with elements' sum

# Other solution - DFS
# 0 = nums[i] + DFS(nums[i + 1:], -nums[i])
