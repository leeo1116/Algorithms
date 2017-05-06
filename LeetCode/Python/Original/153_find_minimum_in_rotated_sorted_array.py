def find_minimum(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] >= nums[left]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


def find_minimum_II(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = left + (right - left) // 2
        if nums[mid] > nums[left]:
            left = mid + 1
        elif nums[mid] < nums[left]:
            right = mid
        else:
            left += 1
    return nums[left]


print(find_minimum_II([4, 5, 6, 6, 7, 8, 0, 1, 1, 2]))
