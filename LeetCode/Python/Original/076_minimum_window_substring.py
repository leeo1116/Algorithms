class Solution(object):
    def min_window(self, s, t):
        """
        Find the minimum length substring in s that contains t
        :param s: string s
        :type s: str
        :param t: target string t
        :type t: str
        :return: substring with minimum length in s that contains t
        :rtype: str
        """
        char_count_dict = dict()
        for c in t:
            char_count_dict[c] = char_count_dict.get(c, 0) + 1
        begin = end = head = 0
        counter = len(t)
        min_window = len(s) + 1
        while end < len(s):
            if char_count_dict.get(s[end], None) is not None:
                if char_count_dict[s[end]] > 0:
                    counter -= 1
                char_count_dict[s[end]] -= 1
            end += 1
            while counter == 0:  # s[0:end + 1] contains t, i.e. a valid substring
                if end - begin < min_window:
                    min_window = end - begin
                    head = begin
                if char_count_dict.get(s[begin], None) is not None:  # Be careful with dict.get(a, None), dict[a] = 0
                    if char_count_dict[s[begin]] == 0:
                        counter += 1
                    char_count_dict[s[begin]] += 1
                begin += 1
        return "" if min_window == len(s) + 1 else s[head:head + min_window]


s = Solution()
print(s.min_window("bba", "ab"))
