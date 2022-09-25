from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, items: List[Optional[int]]) -> "TreeNode":
        root = cls(val=items.pop(0))
        nodes = [root]
        for index, item in enumerate(items):
            if item is None:
                continue
            parent_node = nodes[index // 2]
            is_left = index % 2 == 0
            node = cls(val=item)
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node
            nodes.append(node)
        return root

    @classmethod
    def recursive_print(cls, tree: "TreeNode", level=0, prefix="root"):
        print(f"{level * '  '}{prefix:5s}: val={tree.val}")
        if tree.left:
            cls.recursive_print(tree.left, level + 1, "left")
        if tree.right:
            cls.recursive_print(tree.right, level + 1, "right")


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        left = None
        right = None

        if root.left:
            left = self.evaluateTree(root.left)
        if root.right:
            right = self.evaluateTree(root.right)

        if root.val == 0:
            return False
        if root.val == 1:
            return True

        if root.val == 2:
            return left or right
        return left and right


if __name__ == "__main__":
    s = Solution()
    tree_node = TreeNode.from_list([2, 1, 3, None, None, 0, 1])
    TreeNode.recursive_print(tree_node)
    answer = s.evaluateTree(tree_node)
    assert answer is True

    tree_node = TreeNode.from_list([0])
    TreeNode.recursive_print(tree_node)
    answer = s.evaluateTree(tree_node)
    assert answer is False
