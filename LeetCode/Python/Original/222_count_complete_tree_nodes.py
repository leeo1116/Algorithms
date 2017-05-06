from common_data_structure.TreeNode import TreeNode


class Solution(object):
    def count_nodes(self, root):
        """
        Return total number of nodes in a complete binary tree
        :param root: root of binary tree
        :type root: TreeNode
        :return: total number of nodes
        :rtype: int
        """
        # For a complete binary tree with height = h, the total number of tree nodes is 2^h - 1
        h = self.get_complete_tree_height(root)
        if h == 0:
            return 0
        else:
            if self.get_complete_tree_height(root.right) == h - 1:
                return (1 << (h - 1)) + self.count_nodes(root.right)
            else:
                return (1 << (h - 2)) + self.count_nodes(root.left)

    def get_complete_tree_height(self, root):
        if not root:
            return 0
        else:
            return 1 + self.get_complete_tree_height(root.left)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.count_nodes(root))
