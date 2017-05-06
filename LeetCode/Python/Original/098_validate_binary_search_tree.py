from common_data_structure.TreeNode import TreeNode


class Solution(object):
    def validate_BST(self, root):
        """
        Validate if a tree is Binary Search Tree
        :param root: root of the tree
        :type root: TreeNode
        :return: is valid BST
        """
        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None:
            if root.right.val < root.val:
                return False
            else:
                return self.validate_BST(root.right)
        elif root.right is None:
            if root.left.val > root.val:
                return False
            else:
                return self.validate_BST(root.left)
        else:
            return root.left.val < root.val < root.right.val and self.validate_BST(root.right) and self.validate_BST(root.left)


s = Solution()
head = TreeNode(5)
head.left = TreeNode(5)
# head.left.left = TreeNode(2)
# head.left.right = TreeNode(4)
# head.right = TreeNode(8)
print(s.validate_BST(head))
