# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total_count = 0

    def dfs(self, root: TreeNode):
        if root is None:
            return
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    self.total_count += root.left.left.val
                if root.left.right:
                    self.total_count += root.left.right.val
            if root.right:
                if root.right.left:
                    self.total_count += root.right.left.val
                if root.right.right:
                    self.total_count += root.right.right.val
        if root.left:
            self.dfs(root.left)
        if root.right:
            self.dfs(root.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.total_count


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.sumEvenGrandparent(r)
    print(answer)
