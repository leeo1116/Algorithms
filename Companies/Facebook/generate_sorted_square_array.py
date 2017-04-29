"""Given a sorted array of integers: [-3, -1, 0, 1, 2], generate a sorted array of their squares: [0, 1, 1, 4, 9]
Idea: 1) Find index of 0, or to be more accurate, find the index of number that is closest to 0
      2) Use two pointers left, right to compare the square of nums[left] and nums[right]
      3) Append whichever is smaller to result and move it to the next element
      4) If left < 0, append right 

"""


def generate_sorted_square_array(nums):
    nums_len = len(nums)
    if nums_len == 0:
        return nums
    if nums[nums_len - 1] < 0:
        square_nums = list(map(lambda x: x ** 2, nums))
        square_nums.reverse()
        return square_nums
    if nums[0] >= 0:
        return list(map(lambda x: x**2, nums))

    left, right = -1, nums_len
    square_nums = []
    for i in range(1, len(nums)):
        if nums[i - 1] < 0 <= nums[i]:
            left = i - 1
            right = i
            break
    while left > -1 and right < nums_len:
        if abs(nums[left]) < nums[right]:
            square_nums.append(nums[left] ** 2)
            left -= 1
        else:
            square_nums.append(nums[right] ** 2)
            right += 1
    if left <= -1:
        square_nums += list(map(lambda x: x ** 2, nums[right]))
    if right >= nums_len:
        square_nums_tmp = list(map(lambda x: x ** 2, nums[:left + 1]))
        square_nums_tmp.reverse()
        square_nums += square_nums_tmp
    return square_nums


print(generate_sorted_square_array([-5]))