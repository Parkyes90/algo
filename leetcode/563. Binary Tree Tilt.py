# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """https://leetcode.com/problems/binary-tree-tilt/submissions/"""

    tilt = 0

    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        self.tilt += abs(left - right)
        return left + right + node.val

    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.tilt


if __name__ == "__main__":
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.right = TreeNode(3)
    r.left.left = TreeNode(4)
    r.right.left = TreeNode(5)
    s = Solution()
    answer = s.findTilt(r)
    print(answer)
