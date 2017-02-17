class Solution(object):
    def find_median_sorted_arrays_merge_1(self, nums1, nums2):
        """
        Find median of two sorted arrays
        :param nums1: array one
        :param nums2: array two
        :rtype: float
        :return: median
        """
        # Handle corner case
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 and n2 > 0:
            return (nums2[n2 // 2 - 1] + nums2[n2 // 2]) / 2.0 if n2 % 2 == 0 else nums2[n2 // 2]
        elif n2 == 0 and n1 > 0:
            return (nums1[n1 // 2 - 1] + nums1[n1 // 2]) / 2.0 if n1 % 2 == 0 else nums1[n1 // 2]
        elif n1 == n2 == 0:
            return 0
        # n1 + n2 is Even or Odd
        is_odd = True if (n1 + n2) % 2 == 1 else False
        i, j, median1, median2 = 0, 0, 0, 0
        mid = (n1 + n2) // 2 + 1 if is_odd else (n1 + n2) // 2
        # Merge sort, similar to merging two sorted linked list
        for k in range(mid):
            if j == n2 or (i < n1 and nums1[i] <= nums2[j]):
                median1 = nums1[i]
                i += 1
            elif i == n1 or (j < n2 and nums2[j] < nums1[i]):
                median1 = nums2[j]
                j += 1
        if j == n2:
            median2 = nums1[i]
        elif i == n1:
            median2 = nums2[j]
        else:
            median2 = min(nums1[i], nums2[j])
        return median1 if is_odd else (median1 + median2) / 2.0

    def find_median_sorted_arrays_merge_2(self, nums1, nums2):
        """
        Find median of two sorted arrays
        :param nums1: array one
        :param nums2: array two
        :rtype: float
        :return: median
        """
        # Handle corner case
        n1, n2 = len(nums1), len(nums2)
        if n1 == 0 and n2 > 0:
            return (nums2[n2 // 2 - 1] + nums2[n2 // 2]) / 2.0 if n2 % 2 == 0 else nums2[n2 // 2]
        elif n2 == 0 and n1 > 0:
            return (nums1[n1 // 2 - 1] + nums1[n1 // 2]) / 2.0 if n1 % 2 == 0 else nums1[n1 // 2]
        elif n1 == n2 == 0:
            return 0

        i, j, median1, median2 = 0, 0, 0, 0
        mid = (n1 + n2) // 2 + 1
        # Merge sort, similar to merging two sorted linked list
        for k in range(mid):
            if j == n2 or (i < n1 and nums1[i] <= nums2[j]):
                median2 = median1
                median1 = nums1[i]
                i += 1
            elif i == n1 or (j < n2 and nums2[j] < nums1[i]):
                median2 = median1
                median1 = nums2[j]
                j += 1
        return median1 if (n1 + n2) % 2 == 1 else (median1 + median2) / 2.0

    def find_median_sorted_arrays_find_kth_smallest(self, nums1, nums2):
        """
        Find median of two sorted arrays using find Kth smallest element in two sorted arrays
        Median of two sorted arrays is the same as ((n1 + n2) // 2 + 1)th smallest element in
        two sorted arrays (when n1 + n2 is odd)
        The idea of finding kth smallest element is by comparing the k//2th element in nums1
        with (k - k//2)th element in nums2. If element in nums1 is greater than the element in
        nums2. Then it is sure that all elements before (k - k//2) in nums2 is smaller than the
        kth smallest number. So these elements can be discarded in the next finding. And the kth
        smallest number problem is becoming the (k - (k - k//2))th smallest problem for the remaining
        elements: nums1 and nums2[(k - (k - k//2)):]; Similarly, if element in nums2 is greater
        than the element in nums1. The smallest kth element problem can be scaled down.
        During this process, either the size of nums1 is decreasing or the size of nums2 is decreasing.
        And the k is also decreasing. So it is natural to set the stop criteria as:
        1) len(nums1) == 0, return nums2[k - 1]
        2) k == 1, return min(nums1[0], nums2[0])
        :param nums1: sorted array one
        :param nums2: sorted array two
        :rtype: int
        :return: median
        """
        n1, n2 = len(nums1), len(nums2)
        if (n1 + n2) % 2 == 1:
            return self.find_kth_smallest_element(nums1, n1, nums2, n2, (n1 + n2) // 2 + 1)
        else:
            return (self.find_kth_smallest_element(nums1, n1, nums2, n2, (n1 + n2) // 2)\
                    + self.find_kth_smallest_element(nums1, n1, nums2, n2, (n1 + n2) // 2 + 1)) / 2.0

    def find_kth_smallest_element(self, nums1, n1, nums2, n2, k):
        if n2 < n1:
            return self.find_kth_smallest_element(nums2, n2, nums1, n1, k)
        if n1 == 0:
            return nums2[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        i = min(k // 2, n1)
        j = k - i
        if nums1[i - 1] > nums2[j - 1]:
            return self.find_kth_smallest_element(nums1, n1, nums2[j:], n2 - j, k - j)
        elif nums2[j - 1] > nums1[i - 1]:
            return self.find_kth_smallest_element(nums1[i:], n1 - i, nums2, n2, k - i)
        else:
            return nums1[i - 1]

def main():
    s = Solution()
    print(s.find_median_sorted_arrays_merge([1, 2], [1, 1]))


if __name__ == "__main__":
    main()
