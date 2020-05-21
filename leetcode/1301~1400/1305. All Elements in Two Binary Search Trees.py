# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nodes = []
        ret = []
        if root1:
            nodes.append(root1)
        if root2:
            nodes.append(root2)
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            ret.append(node.val)
        return sorted(ret)


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = []
    test_arr2 = [5, 1, 7, 0, 2]
    s = Solution()
    r1 = create_root(test_arr, None, 0, len(test_arr))
    r2 = create_root(test_arr2, None, 0, len(test_arr2))
    answer = s.getAllElements(r1, r2)
    print(answer)
