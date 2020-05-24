# Definition for a binary tree node.
from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def contain(self, root: TreeNode):
        if not root:
            return False
        left = self.contain(root.left)
        right = self.contain(root.right)
        if not left:
            root.left = None
        if not right:
            root.right = None
        return root.val == 1 or left or right

    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.contain(root)
        return root


def create_root(
    arr: List[int], root: Union[TreeNode, None], index: int, n: int
) -> TreeNode:
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


def dfs(root: TreeNode):
    nodes = [root]
    ret = []
    while nodes:
        node = nodes.pop(0)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        ret.append(node.val)
    return ret


if __name__ == "__main__":
    test_arr = [1, 1, 0, 1, 1, 0, 1, 0]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.pruneTree(r)
    print(answer)
