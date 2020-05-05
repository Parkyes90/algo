# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.maximum = 0

    def get_length(self, node: TreeNode):
        if not node:
            return 0
        left_length = self.get_length(node.left)
        right_length = self.get_length(node.right)
        left = right = 0
        if node.left and node.left.val == node.val:
            left = left_length + 1
        if node.right and node.right.val == node.val:
            right = right_length + 1
        self.maximum = max(self.maximum, left + right)
        return max(left, right)

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.get_length(root)
        return self.maximum


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)

    return root


if __name__ == "__main__":
    test_arr = [5, 4, 5, 1, 1, None, 5]
    s = Solution()
    r = create_root(test_arr, None, 0, len(test_arr))
    answer = s.longestUnivaluePath(r)
    print(answer)
