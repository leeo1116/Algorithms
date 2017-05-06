class Solution(object):
    def subsets(self, nums):
        """
        Return all subsets of nums
        :param nums: input number list
        :type nums: list
        :return: all subsets
        :rtype: list
        """
        subsets = [[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(subsets)
            for j in range(len(subsets) - l, len(subsets)):
                subsets.append(subsets[j] + nums[i])
        return subsets

