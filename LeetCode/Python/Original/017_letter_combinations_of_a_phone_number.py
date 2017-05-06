class Solution(object):
    def letter_combination(self, digits):
        if not digits:
            return []
        num_str_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = [""]
        for d in digits:
            temp_combinations = []
            for c in num_str_dict[d]:
                for s in combinations:
                    temp_combinations.append(s + c)
            combinations = temp_combinations
        return combinations