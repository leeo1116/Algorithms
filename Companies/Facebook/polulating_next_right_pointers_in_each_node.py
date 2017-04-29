class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect_next_node_1(root):
    """
    Assuming it is a perfect binary tree,  all leaves are at the same level, and every parent has two children
    :type root: TreeLinkNode
    """
    if not root:
        return
    if root.left:
        root.left.next = root.right
    if root.right and root.next:
        root.right.next = root.next.left
    connect_next_node_1(root.left)
    connect_next_node_1(root.right)
    return


def connect_next_node_2(root):
    """
    Any binary tree
    :type root: TreeLinkNode 
    """
    if not root:
        return
    queue = [root]
    while queue:
        level_nodes = []
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                level_nodes.append(node.left)
            if node.right:
                level_nodes.append(node.right)
        connect_level_nodes(level_nodes)
        queue = level_nodes
    return


def connect_level_nodes(level_nodes):
    d = TreeLinkNode(0)
    for n in level_nodes:
        d.next = n
        d = d.next


root = TreeLinkNode(1)
root.left = TreeLinkNode(2)
root.right = TreeLinkNode(3)
root.left.left = TreeLinkNode(4)
root.right.right = TreeLinkNode(5)

connect_next_node_2(root)

"""
FB version
            1                                1
           / \                              / 
          2   3           ===>             2 - 3
         /   /  \                         /     
        4   5    6                       4 - 5 - 6
Idea: similar to connect_next_node_2, level order traversal to connect 'next' pointer, and set nodes' left and right
child to None except for the first node at each level
while queue:
    level_nodes = []
    for i in range(len(queue)):
        node = queue.pop(0)
        if node.left: level_nodes.append(node.left)
        if node.right: level_nodes.append(node.right)
        
        # Delete children
        if i != 0: set left child to None
        set right child to None
    connect_level_nodes(level_nodes)
    queue = level_nodes
"""
