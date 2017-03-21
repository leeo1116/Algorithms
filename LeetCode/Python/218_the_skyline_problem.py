class Solution(object):
    def get_skyline(self, buildings):
        """
        Get the contour of given buildings
        :param buildings: buildings in which each building is represented by [L, R, H]
        :type buildings: list[list[int]]
        :return: key points (turning points)
        :rtype: list
        """
        key_points = []
        if not buildings:
            return key_points

        # Get the x range of all buildings
        x_low, x_high = buildings[0][0], 0
        for b in buildings:
            x_high = max(x_high, b[1])
        x_range = range(x_low, x_high + 1)

        # Construct a height map for each build. Get the maximum height for each unit interval [i, i+1]
        heights = [0] * len(x_range)
        for b in buildings:
            for x in range(b[0], b[1]):
                i = x - x_range[0]  # considering x offset
                heights[i] = max(heights[i], b[2])

        # Obtain key points
        for i in range(len(heights)):
            if i == 0 or heights[i] != heights[i-1]:
                key_points.append([x_range[i], heights[i]])

        return key_points


s = Solution()
print(s.get_skyline([[0,2147483647,2147483647]]))
