class Solution(object):
    def two_sum(self, nums, target):
        """
        Find the indices of two nums such that they add up to target
        :param nums: a list of nums
        :param target: target sum
        :return: indices of two valid nums
        """
        num_index_dict = dict()
        indices = []
        for i, n in enumerate(nums):
            if num_index_dict.get(target - n, None) is not None:
                return [num_index_dict[target - n], i]
            num_index_dict[n] = i
        return []

