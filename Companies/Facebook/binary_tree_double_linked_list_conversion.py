class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None  # pre
        self.right = None  # next


def binary_tree_to_doubly_linked_list_1(root):
    """
    Time complexity = O(n), Space complexity = O(n)
    :param root: 
    :return: 
    """
    if not root:
        return []
    else:
        left_list = []
        right_list = []
        if root.left:
            left_list = binary_tree_to_doubly_linked_list_1(root.left)
            if len(left_list):
                root.left = left_list[-1]
                left_list[-1].right = root
        if root.right:
            right_list = binary_tree_to_doubly_linked_list_1(root.right)
            if len(right_list):
                root.right = right_list[0]
                right_list[0].left = root
        return left_list + [root] + right_list  # in outer method, return head = list[0]


"""
Idea: the linked list is arranged by in-order traversal
Step 1: if left sub tree exists, convert it to doubly linked list
Step 2: find the predecessor of root from in-order traversal, root.pre = predecessor and predecessor.next = root
Step 3: if right sub tree exists, convert it to doubly linked list
Step 4: find the successor of root from in-order traversal, root.next = successor and successor.pre = root

In previous method, each predecessor is the last element of a list that contains all nodes from in-order traversal of 
left sub tree. And the successor of root is the first element of a list that contains all nodes from in-order traversal 
of right sub tree. This results in O(n) time complexity. 
"""


def binary_tree_to_doubly_linked_list_2(root):
    if not root:
        return root
    h = binary_tree_to_doubly_linked_list_helper(root)
    while h.left:
        h = h.left
    return h


def binary_tree_to_doubly_linked_list_helper(root):
    if not root:
        return root
    if root.left:
        left_child = binary_tree_to_doubly_linked_list_helper(root.left)
        while left_child.right:
            left_child = left_child.right
        left_child.right = root
        root.left = left_child
    if root.right:
        right_child = binary_tree_to_doubly_linked_list_helper(root.right)
        while right_child.left:
            right_child = right_child.left
        root.right = right_child
        right_child.left = root
    return root


def sorted_list_to_binary_search_tree(head):
    if not head or not head.next:
        return TreeNode(head.val) if head else None
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    mid_node = slow.next
    slow.next = None  # cut the linked list
    root = TreeNode(mid_node.val)
    root.left = sorted_list_to_binary_search_tree(head)
    root.right = sorted_list_to_binary_search_tree(mid_node.next)
    return root
