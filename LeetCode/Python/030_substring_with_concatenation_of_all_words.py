class Solution(object):
    def find_sub_string(self, s, words):
        indices, num_words = [], len(words)
        if num_words == 0:
            return indices
        str_len, word_len = len(s), len(words[0])
        word_count_dict = dict()
        # Get frequency of each word. Words may contain duplicates
        for w in words:
            word_count_dict[w] = word_count_dict.get(w, 0) + 1
        # Traverse from
        for i in range(str_len - num_words * word_len + 1):
            j, str_count_dict = 0, dict()
            while j < num_words:
                sub_str = s[i + word_len * j: i + word_len * (j + 1)]
                if word_count_dict.get(sub_str, None):
                    str_count_dict[sub_str] = str_count_dict.get(sub_str, 0) + 1
                    if str_count_dict[sub_str] > word_count_dict[sub_str]:
                        break
                else:
                    break
                j += 1
            if j == num_words:
                indices.append(i)
        return indices


s = Solution()
print(s.find_sub_string("barfoofoo", ["foo", "bar"]))