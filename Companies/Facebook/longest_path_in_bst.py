from collections import deque


def longest_path_in_BST(root):
    max_path = 0

    def longest_path_in_BST_helper(root):
        """Return the maximum depth of a BST"""
        nonlocal max_path
        if not root:
            return 0
        left_depth = longest_path_in_BST_helper(root.left)
        right_depth = longest_path_in_BST_helper(root.right)
        max_path = max(max_path, left_depth + right_depth + 1)
        return max(left_depth, right_depth) + 1

    longest_path_in_BST_helper(root)
    return max_path


def print_longest_path_in_BST(root):
    path = deque()
    longest_path = []
    print_longest_path_in_BST_helper(root, path, longest_path)
    return longest_path


def print_longest_path_in_BST_helper(root, path, longest_path):
    if not root:
        return []
    if not root.left and not root.right:
        return path.appendleft(root.val)

    path.appendleft(root.val)
    left_path = print_longest_path_in_BST_helper(root.left, path, longest_path)
    right_path = print_longest_path_in_BST_helper(root.right, path, longest_path)

    for l in left_path:
        for r in right_path:
            if len(l) + len(r) + 1 > len(longest_path):
                longest_path = [l + [root.val] + r]
            elif len(l) + len(r) + 1 == len(longest_path):
                longest_path.append(l + [root.val] + r)

    if left_path > right_path:
        return left_path
    elif left_path < right_path:
        return right_path
    else:
        return left_path + right_path


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(longest_path_in_BST(root))
print(print_longest_path_in_BST(root))