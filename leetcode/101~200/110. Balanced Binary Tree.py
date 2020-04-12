# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_height(self, root):
        if not root:
            return 0

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return max(left_height, right_height) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        left_balance = self.isBalanced(root.left)
        right_balance = self.isBalanced(root.right)

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        is_gap = abs(left_height - right_height) < 2
        return left_balance and right_balance and is_gap


def create_tree(arr, r, index, n):
    if index < n:
        temp = TreeNode(arr[index])
        r = temp
        r.left = create_tree(arr, r.left, 2 * index + 1, n)
        r.right = create_tree(arr, r.right, 2 * index + 2, n)
    return r


if __name__ == "__main__":
    arr1 = [3, 9, 20, None, None, 15, 7]
    arr2 = [1, 2, 2, 3, 3, None, None, 4, 4]
    arr3 = [1, 2, 2, 3, None, None, 3, 4, None, None, 4]

    rt1 = create_tree(arr1, None, 0, len(arr1))
    rt2 = create_tree(arr2, None, 0, len(arr2))
    rt3 = create_tree(arr2, None, 0, len(arr2))
    s = Solution()
    ans1 = s.isBalanced(rt1)
    ans2 = s.isBalanced(rt2)
    ans3 = s.isBalanced(rt3)
    print(ans1)
    print(ans2)
    print(ans3)
