# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root: TreeNode, maximum):
            nonlocal ans
            if not root:
                return
            if maximum <= root.val:
                ans += 1
                maximum = root.val
            dfs(root.left, maximum)
            dfs(root.right, maximum)

        dfs(root, float("-inf"))
        return ans


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [2, None, 4, None, None, 10, 8]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.goodNodes(r)
    print(answer)
