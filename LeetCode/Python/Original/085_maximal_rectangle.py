class Solution(object):
    def __init__(self):
        pass


    def maximal_rectangle(self, matrix):
        """ Find the maximum rectangle formed by all 1's
        Example matrix
        0 0 0 1 0 0 0
        0 0 1 1 1 0 0
        0 1 1 1 1 1 0
        
        Idea: keeping track of left/right boundary and height
        Row 0:  0 0 0 1 0 0 0
        left:   0 0 0 3
        right:  6 6 2 
        height: 0 0 0 1 0 0 0
        
        Row 1:  0 1 1 1 1 1 0
        left:   0 1
        right:  6
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])

        left = [0] * col  # left boundary
        right = [col - 1] * col  # right boundary
        height = [0] * col  # number of continuous 1's in each column
        max_area = 0
        for i in range(row):
            cur_left, cur_right = 0, col - 1
            # Calculate height
            for j in range(col):
                if matrix[i][j] == 1:
                    height[j] = height[j] + 1
                else:
                    height[j] = 0

            # Calculate left
            for j in range(col):
                if matrix[i][j] == 1:
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            # Calculate right
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == 1:
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = col - 1
                    cur_right = j

            # Calculate area of rectangle for this row i
            for j in range(col):
                max_area = max(max_area, (right[j] - left[j]) * height[j])
        return max_area


s = Solution()
print(s.maximal_rectangle([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0]]))
