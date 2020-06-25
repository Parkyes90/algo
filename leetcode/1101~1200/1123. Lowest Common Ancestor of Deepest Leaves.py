# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, level):
        if not node:
            return None, level
        left = right = node
        l_depth = r_depth = level
        if node.left:
            left, l_depth = self.dfs(node.left, level + 1)
        if node.right:
            right, r_depth = self.dfs(node.right, level + 1)

        if l_depth == r_depth:
            return node, l_depth
        if l_depth > r_depth:
            return left, l_depth

        return right, r_depth

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        node = self.dfs(root, 0)

        return node[0]


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [1, 2, 3, 4, 5]
    s = Solution()
    r = create_root(test_arr, None, 0, len(test_arr))
    answer = s.lcaDeepestLeaves(r)
