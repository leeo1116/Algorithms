class Solution(object):
    def __init__(self):
        pass

    def max_profit(self, nums):
        buy1, sell1, buy2, sell3 = max(nums), 0, 0, 0
        for n in nums:
            buy1 = min(n, buy1)
            sell1 = max(sell1, n - buy1)
            buy2 = min(buy2, )