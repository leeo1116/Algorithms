def min_subarray_sum(n, s):
    """
    Find the minimum size of sub array which has sum greater than or equal to s
    :param n: array with positive integers
    :param s: target sum
    :return: minimum size of sub array
    """
    n_len = len(n)
    min_size = n_len + 1
    if n_len == 0:
        return 0

    sum_ij = 0
    j = 0
    for i in range(n_len):
        # Move left cursor
        if i != 0:
            sum_ij -= n[i - 1]
            if sum_ij >= s:
                min_size = min(min_size, j - i + 1)
                continue
            else:
                j += 1
        # Move right cursor
        while j < n_len:
            sum_ij += n[j]
            if sum_ij >= s:
                min_size = min(min_size, j - i + 1)
                break
            j += 1
    return min_size if min_size != n_len + 1 else 0


def min_size_subarray_sum_concise(n, s):
    sub_sum = i = 0
    min_len = len(n) + 1
    for j in range(len(n)):
        sub_sum += n[j]
        while sub_sum >= s:
            min_len = min(min_len, j - i + 1)
            sub_sum -= n[i]
            i += 1
    return min_len if min_len < len(n) + 1 else 0


def subarray_sum_2d_brute_force(nums, target):
    row = len(nums)
    if row == 0:
        return False
    col = len(nums[0])
    if col == 0:
        return False

    # Calculate accumulative sum and overwrite nums
    for i in range(1, row):  # first column
        nums[i][0] += nums[i - 1][0]

    for j in range(1, col):  # first row
        nums[0][j] += nums[0][j - 1]

    for i in range(1, row):
        for j in range(1, col):
            nums[i][j] = nums[i - 1][j] + nums[i][j - 1] - nums[i - 1][j - 1] + nums[i][j]

    for n in nums:
        n.insert(0, 0)
    nums.insert(0, [0] * (col + 1))

    # Search rectangle inside which the elements sum up to target
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            sub_sum = nums[i][j]
            if sub_sum >= target:
                for m in range(i + 1):
                    for n in range(j + 1):
                        if sub_sum == target:
                            return True
                        sub_sum = nums[i][j] - nums[m][j] - nums[i][n] + nums[m][n]
    return False


def subarray_sum_2d_concise(nums, target):
    # Corner cases: nums = None, nums = []
    if not nums:
        return False
    row = len(nums)
    col = len(nums[0])
    # Corner case: nums = [[]]
    if col == 0:
        return False

    for left in range(col):
        row_sum = [0] * col
        for right in range(left, col):
            # Get sum of elements at the same row
            for r in range(row):
                row_sum[r] += nums[r][right]
            # Leveraging 1D case
            if check_rectangle_sum(row_sum, target):
                return True
    return False


def check_rectangle_sum(array, target):
    s = i = 0
    for j in range(len(array)):
        s += array[j]
        while s >= target:
            if s == target:
                return True
            s -= array[i]
            i += 1
    return False


print(min_subarray_sum([3, 1], 10))
print(subarray_sum_2d_brute_force([[2, 3, 6], [4, 1, 5], [7, 8, 9]], 20))
print(subarray_sum_2d_concise([[2, 3, 6], [4, 1, 5], [7, 8, 9]], 20))
