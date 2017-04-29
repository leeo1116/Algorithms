from collections import deque


def sliding_window_maximum(nums, k):
    queue = deque()  # save index in queue
    sliding_max = []
    for i in range(len(nums)):
        if queue and i - k == queue[0]:
            queue.popleft()
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)
        if i >= k - 1:
            sliding_max.append(nums[queue[0]])
    return sliding_max

