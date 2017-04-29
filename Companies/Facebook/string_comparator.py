def compare_str(s1, s2):
    """
    Compare two strings. Char > digit
    :type s1: str 
    :type s2: str 
    :return: True if s1 is smaller than s2
    """
    s1_len, s2_len = len(s1), len(s2)
    i = j = 0
    while i < s1_len and j < s2_len:
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif s1[i].isalpha() and s2[j].isalpha():
            return s1[i] < s2[j]
        elif s1[i].isdigit() and s2[j].isdigit():
            return s1[i] < s2[j]
        elif s1[i].isalpha():
            return False
        else:
            return


print(compare_str("abc1a", "abc8"))