# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorder(self, node: TreeNode, current: int, sum: int) -> bool:
        if node:
            current += node.val
            if not node.left and not node.right:
                if current == sum:
                    return True
                return False
            return self.preorder(node.left, current, sum) or self.preorder(
                node.right, current, sum
            )
        return False

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.preorder(root, 0, sum)


def create_tree(arr: List[int], root, index, n):
    if index < n:
        temp = TreeNode(arr[index])
        root = temp
        root.left = create_tree(arr, root.left, 2 * index + 1, n)
        root.right = create_tree(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    r = create_tree(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.hasPathSum(r, 22)
    print(answer)
