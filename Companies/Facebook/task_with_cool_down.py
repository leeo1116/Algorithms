from heapq import heappush, heappop


def execution_time(tasks, cool_down):
    """
    Calculate the total execution time of a given task with cool down
    :param tasks: a string denoting tasks
    :param cool_down: cool down time for the same task
    :return: total execution time
    """
    task_index_dict = {}  # {task: index in execution list + 1 = exe_time}
    exe_time = 0
    for t in tasks:
        if t in task_index_dict and exe_time - (task_index_dict[t] - 1) <= cool_down:
            exe_time += (cool_down - (exe_time - task_index_dict[t]))
        exe_time += 1
        task_index_dict[t] = exe_time
    return exe_time


print(execution_time("AABA", 3))


# Follow up: rearrange the order of tasks to minimize the total execution time
def min_task_sequence(tasks, cool_down):
    task_freq_dict, freq_heap = {}, []
    # Step 1: go through tasks and calculate their frequency
    for t in tasks:
        task_freq_dict[t] = task_freq_dict.get(t, 0) + 1

    # Step 2: Maintain a max heap to get task by frequency
    for t, f in task_freq_dict.items():
        heappush(freq_heap, [-f, t])  # min heap by default

    # Step 3: Rearrange sequences. e.g. AAAAABBBBCCCDDEF -> ABAB... if cool_down = 1
    # ABCABC... if cool_down = 2; ABCDABCD... if cool_down = 3
    # In general, put the most frequent task first, and then the less frequent task, and so on. window len = cool_down
    min_sequence = ""
    while freq_heap:
        group = []
        # Put the most frequent task first, and then the less frequent task, inside a widow with len = cool_down
        for i in range(cool_down + 1):
            if freq_heap:  # length of freq_heap may be < cool_down
                task = heappop(freq_heap)
                min_sequence += task[1]  # Get the task occurring most frequently
                group.append(task)
            else:
                break

        # Make as many groups as possible
        group_len = len(group)
        while group:
            task = group.pop()
            task[0] += 1  # Subtract the frequency by 1, Notice '-' in [-f, t]
            if -task[0] > 0:
                heappush(min_sequence, task)  # Get task out and subtract by 1 and then push it back

        # Fill sequence with '-' when the group_len is less than cool_down. i.e. groups * N + remainder
        if freq_heap:
            min_sequence += '_' * (cool_down + 1 - group_len)
    return min_sequence
