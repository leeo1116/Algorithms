from common_data_structure.ListNode import ListNode


class Solution(object):
    def reverse_k_group(self, head, k):
        """
        Reverse linked list in each group which contains k nodes
        :param head: head of the linked list
        :type head: ListNode
        :param k: number of nodes in a group
        :type k: int
        :return: head of reversed linked list
        :rtype: ListNode
        """
        # Find the head of second group
        h, count = head, 0
        while h and count < k:
            h = h.next
            count += 1
        if count == k:  # if second group exists
            next_head = self.reverse_k_group(h, k)
            while count > 0:
                r = head.next
                head.next = next_head
                next_head = head
                head = r
                count -= 1
            head = next_head
        return head

s = Solution()
h = ListNode(1)
s.reverse_k_group(h, 1)