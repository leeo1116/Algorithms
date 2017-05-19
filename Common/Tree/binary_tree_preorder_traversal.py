def preorder_traversal(root, output):
    """ Traverse binary tree iteratively in preorder manner 
    :param root: Binary tree root
    :param output: Traversal output
    :type output: List
    """
    node, stack = root, []
    while node:
        output.append(node)
        if node.right:
            stack.append(node.right)
        node = node.left
        if (not node) and stack:
            node = stack.pop()
    return output
