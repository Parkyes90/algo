# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0

    def recursive(self, node):
        if not node:
            return 0

        left = self.recursive(node.left)
        right = self.recursive(node.right)
        self.count += abs(left) + abs(right)
        return node.val + left + right - 1

    def distributeCoins(self, root: TreeNode) -> int:
        self.recursive(root)
        return self.count


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    s = Solution()
    t_arr = [1, 0, 0, None, 3]
    r = create_root(t_arr, None, 0, len(t_arr))
    answer = s.distributeCoins(r)
    print(answer)
