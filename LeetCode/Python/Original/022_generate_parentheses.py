class Solution(object):
    def generate_parentheses(self, n):
        p = []
        self.gen_parentheses_helper(p, "", n, 0)
        return p

    def gen_parentheses(self, p, s, left, right):
        """
        Generate parentheses recursively
        :param p: parentheses list that will be updated
        :type p: list
        :param s: current parentheses combination
        :param left: left remaining parentheses
        :param right: right remaining parentheses
        :return: None
        """
        if left == right == 0:
            p.append(s)
            return
        if left > 0:
            self.gen_parentheses(p, s + '(', left - 1, right + 1)
        if right > 0:
            self.gen_parentheses(p, s + ')', left, right - 1)
