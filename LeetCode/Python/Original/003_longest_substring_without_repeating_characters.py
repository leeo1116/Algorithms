class Solution(object):
    def length_of_longest_substring(self, s):
        """
        Find the length of longest substring without repeating characters
        :param s: input string
        :rtype: int
        :return: length of longest valid string
        """
        char_index_dict = dict()
        max_len, start = 0, 0
        for i, char in enumerate(s):
            if char_index_dict.get(char, None) is not None:
                start = max(char_index_dict[char] + 1, start)
            max_len = max(max_len, i - start + 1)
            char_index_dict[char] = i
        return max_len


def main():
    s = Solution()
    max_len = s.length_of_longest_substring("abba")
    print(max_len)


if __name__ == '__main__':
    main()
