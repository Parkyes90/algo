# Definition for a binary tree node.
from typing import List, Any, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_tree_node(data: List[Any]) -> Optional[TreeNode]:
    if not data:
        return None

    root = TreeNode(data[0])
    nodes = [root]
    for i, v in enumerate(data[1:]):
        if v is None:
            continue
        parent_node = nodes[i // 2]
        node = TreeNode(val=v)
        if i % 2 == 0:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root
