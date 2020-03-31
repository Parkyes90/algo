# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_mirror(self, root1: TreeNode, root2: TreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (
            root1.val == root2.val
            and self.is_mirror(root1.right, root2.left)
            and self.is_mirror(root1.left, root2.right)
        )

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.left = TreeNode(4)
    s = Solution()
    answer = s.isSymmetric(root)
    print(answer)
