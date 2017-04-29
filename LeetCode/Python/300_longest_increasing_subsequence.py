class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        for num in nums:
            pos = self.binary_search(temp, 0, len(temp), num)
            if pos >= len(temp):
                temp.append(num)
            else:
                temp[pos] = num
        return len(temp)

    def binary_search(self, nums, left, right, target):
        if left == right:
            return left
        mid = left + (right - left) // 2
        if nums[mid] < target:
            return self.binary_search(nums, mid + 1, right, target)
        else:
            return self.binary_search(nums, left, mid, target)


s = Solution()
print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
