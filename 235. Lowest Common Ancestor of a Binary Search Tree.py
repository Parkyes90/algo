# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/"""

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_val = p.val
        q_val = q.val
        node = root

        while node:
            parent = node.val

            if p_val > parent and q_val > parent:
                node = node.right
            elif p_val < parent and q_val < parent:
                node = node.left
            else:
                return node


if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    s = Solution()
    answer = s.lowestCommonAncestor(
        root, root.left.right.left, root.left.right.right
    )
    print(answer.val)
