# Definition for a binary tree node.
from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree_to_arr(self, root: TreeNode) -> List[int]:
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

    def balanceBST(self, root: TreeNode) -> TreeNode:
        arr = self.tree_to_arr(root)
        arr.sort()
        return self.create_bst(arr)

    def create_bst(self, arr: List[int]) -> Union[TreeNode, None]:
        if not arr:
            return None

        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        root.left = self.create_bst(arr[:mid])
        root.right = self.create_bst(arr[mid + 1 :])
        return root

    def create_root(
        self, arr: List[int], root: Union[TreeNode, None], index: int, n: int
    ):
        if index < n and arr[index] is not None:
            root = TreeNode(arr[index])
            root.left = self.create_root(arr, root.left, 2 * index + 1, n)
            root.right = self.create_root(arr, root.right, 2 * index + 2, n)
        return root


if __name__ == "__main__":
    test_arr = [
        1,
        None,
        2,
        None,
        None,
        None,
        3,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        4,
        None,
        None,
    ]
    s = Solution()
    r = s.create_root(test_arr, None, 0, len(test_arr))
    answer = s.balanceBST(r)
    print(answer)
