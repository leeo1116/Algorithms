def search(nums, target):
    # Step 1: search for pivot
    low, high = 0, len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:  # Note: nums[mid] is compared with nums[high]
            low = mid + 1
        else:
            high = mid

    # Step 2: binary search accounting for rotation
    pivot = low
    low, high = 0, len(nums) - 1
    while low <= high:
        mid_tmp = low + (high - low) // 2
        mid = (pivot + mid_tmp) % len(nums)
        if nums[mid] < target:
            low = mid_tmp + 1
        elif nums[mid] > target:
            high = mid_tmp - 1
        else:
            return mid
    return -1


def binary_search_unique(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[low]:  # left part, note >= sign, fluent thinking
            if nums[mid] > target >= nums[low]:  # note >= sign, of course target can be equal to nums[low]
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[high]: # note <= sign, of course target can be equal to nums[high]
                low = mid + 1
            else:
                high = mid - 1
    return -1


def binary_search_duplicates(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        # nums[mid] >= nums[low] no longer guarantees that mid is in left part due to duplicates. e.g. 2 3 2 2 2
        if nums[mid] > nums[low]:
            if nums[mid] > target >= nums[low]:  # note >= sign, of course target can be equal to nums[low]
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < nums[low]:
            if nums[mid] < target <= nums[high]: # note <= sign, of course target can be equal to nums[high]
                low = mid + 1
            else:
                high = mid - 1
        else:
            low += 1
    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 6))

