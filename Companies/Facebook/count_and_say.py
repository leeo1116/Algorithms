def count(n):
    current = 1
    while n - 1 > 0:
        next_num = count_helper(current)
        current = next_num
        n -= 1
    return current


def count_helper(n):
    if n == 1:
        return '11'
    num = str(n)
    next_num = ""
    i = 0
    while i < len(num):
        if i == len(num) - 1 or num[i] != num[i + 1]:
            next_num += ('1' + num[i])
            i += 1
        else:
            j = i
            while j < len(num) - 1 and num[j] == num[j + 1]:
                j += 1
            next_num += (str(j - i + 1) + num[i])
            i = j + 1
    return next_num


print(count(5))
