# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        pass


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)

    return root


if __name__ == "__main__":
    test_arr = [2, 3, 1, 3, 1, None, 1]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.pseudoPalindromicPaths(r)
    print(answer)
