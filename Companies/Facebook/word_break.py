"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not
contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code
definition to get the latest changes.
"""


def word_break_dfs(s, words):
    """
    Check if s can be split into a list of words that are contained in word_dict
    :param s: a string
    :type s: str
    :param words: word dictionary
    :type words: list
    :return: s can be split into words
    """
    word_count_dict = dict()
    # Construct a dictionary with {word: count} pair
    for w in words:
        word_count_dict[w] = word_count_dict.get(w, 0) + 1
    return word_break_dfs_helper(s, word_count_dict)


def word_break_dfs_helper(s, word_count_dict):
    # Simplest case
    if word_count_dict.get(s, None):
        return True
    for i in range(len(s)):
        if word_count_dict.get(s[:i + 1], None) and word_break_dfs_helper(s[i + 1:], word_count_dict):
            return True
    return False


print(word_break_dfs("lianglianghili", ["liang", "li", "hi"]))  # TLE for test case s = "aaaa...", words = "a", "aa", ..


# Naive idea: traverse s and determine if the left part of s - word can be broken into words, iteratively
def word_break_dp(s, words):
    can_break = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            if w == s[i - len(w) + 1:i + 1] and (can_break[i - len(w)] or i - len(w) == -1):
                can_break[i] = True
    return can_break[len(s) - 1]


print(word_break_dp("liangli", ["liang", "li"]))




