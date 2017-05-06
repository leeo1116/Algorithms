class Solution(object):
    def is_number(self, s):
        s_len = len(s)

        # Remove leading and trailing white spaces
        i, j = 0, s_len - 1
        while i <= j and s[i] == ' ':
            i += 1
        if i == j + 1:
            return False
        while i <= j and s[j] == ' ':
            j -= 1

        # Skip leading '+' or '-'
        if s[i] == '+' or s[i] == '-':
            i += 1

        # Check numeric char
        seen_digit = seen_dot = seen_exp = False
        while i <= j:
            if s[i].isnumeric():
                seen_digit = True
            elif s[i] == '.':
                if seen_dot or seen_exp:
                    return False
                else:
                    seen_dot = True
            elif s[i] == 'e':
                if seen_exp or not seen_digit:
                    return False
                else:
                    seen_exp = True
                    seen_digit = False
            elif s[i] == '+' or s[i] == '-':
                if s[i-1] != 'e':
                    return False
            else:
                return False
            i += 1
        return seen_digit


s = Solution()
print(s.is_number('-1.'))