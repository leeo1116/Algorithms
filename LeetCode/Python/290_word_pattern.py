class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_word_dict = dict()
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if pattern_word_dict.get(pattern[i], None):
                if pattern_word_dict[pattern[i]] != words[i]:
                    return False
            else:
                pattern_word_dict[pattern[i]] = words[i]
        return True


s = Solution()
print(s.wordPattern("abba", "cat dog dog cat"))