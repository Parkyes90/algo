# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, to_delete, ret):
        if not node:
            return None
        node.left = self.dfs(node.left, to_delete, ret)
        node.right = self.dfs(node.right, to_delete, ret)
        if node.val in to_delete:
            if node.left:
                ret.append(node.left)
            if node.right:
                ret.append(node.right)
            return None
        return node

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ret = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            ret.append(root)
        self.dfs(root, to_delete, ret)
        return ret


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [1, 2, 4, None, 3]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = Solution()
    ans = s.delNodes(r, [3])
    print(ans)
