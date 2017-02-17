from common_data_structure.ListNode import ListNode


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        Add two numbers represented by two inverse linked list
        :param l1: linked list one
        :param l2: linked list two
        :rtype: ListNode
        :return: linked list representing the sum
        """
        h = l = ListNode(0)
        carry_in, digit_sum = 0, 0
        while l1 and l2 or carry_in:
            d1 = l1.val if l1 else 0
            d2 = l2.val if l2 else 0

            digit_sum = carry_in + d1 + d2
            l.next = ListNode(digit_sum % 10)
            carry_in = digit_sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            l = l.next

        if (not l1) and l2:
            l.next = l2
        elif (not l2) and l1:
            l.next = l1
        return h.next
