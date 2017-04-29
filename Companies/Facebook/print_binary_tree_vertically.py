"""Print a binary tree in vertical order, column by column 
                     2
                  /    \
                3       4      ==>    1, 3, 5, 2, 4
              /  \
            1     5
"""


def print_binary_tree_vertically(root):
    offset_nodes_dict = {}
    construct_offset_nodes_map(root, 0, offset_nodes_dict)
    for k, v in sorted(offset_nodes_dict):
        for node in v:
            print(node.val)


def construct_offset_nodes_map(root, offset, offset_nodes_map):
    if not root:
        return
    if offset_nodes_map.get(offset, None):
        offset_nodes_map[offset].append(root)
    else:
        offset_nodes_map[offset] = [root]
    construct_offset_nodes_map(root.left, offset - 1, offset_nodes_map)
    construct_offset_nodes_map(root.right, offset + 1, offset_nodes_map)
