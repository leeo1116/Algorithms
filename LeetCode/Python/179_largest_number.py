from functools import cmp_to_key


class Solution(object):
    def largest_number(self, nums):
        """
        Find largest number formed by elements in nums
        :param nums: a list of nums
        :type nums: list
        :return: the largest number represented by string
        :rtype: str
        """
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(lambda s1, s2: int(s1 + s2) - int(s2 + s1)), reverse=True)
        return ''.join(nums)


s = Solution()
print(s.largest_number([1, 4, 32, 2]))