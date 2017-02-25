class Solution(object):
    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # candidates.sort()
        # return self.search(candidates, target)

    # def search(self, candidates, target):
        if target == 0:
            return [[]]
        res = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                continue
            for r in self.combination_sum(candidates[i:], target-candidates[i]):
                res.append([candidates[i]]+r)
        return res


s = Solution()
print(s.combination_sum([8, 7, 4, 3], 11))
