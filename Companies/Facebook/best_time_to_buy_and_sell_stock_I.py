def max_profix_I(nums):
    profit = 0
    if len(nums) < 2:
        return profit
    # min_price, max_price = nums[0], nums[0]
    min_price, max_profit = nums[0], 0
    for n in nums:
        min_price = min(min_price, n)
        # max_price = max(max_price, n)  # wrong solution: [8, 1]
        max_profit = max(max_profit, n - min_price)
    return max_profit


def max_profit_II(nums):
    profit = 0
    if len(nums) < 2:
        return profit
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > 0:
            profit += nums[i] - nums[i - 1]
    return profit
