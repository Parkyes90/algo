# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    deepest_level = 0
    deepest_nodes = set()

    def calculate_deepest_level(self, node, current_level):
        if not node:
            return
        new_level = current_level + 1
        self.deepest_level = max(new_level, self.deepest_level)
        self.calculate_deepest_level(node.left, new_level)
        self.calculate_deepest_level(node.right, new_level)

    def register_deepest_nodes(self, node, level):
        if not node:
            return
        if level == self.deepest_level:
            self.deepest_nodes.add(node.val)
        self.register_deepest_nodes(node.left, level + 1)
        self.register_deepest_nodes(node.right, level + 1)

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.calculate_deepest_level(root.left, 0)
        self.calculate_deepest_level(root.right, 0)
        self.register_deepest_nodes(root, 0)
        print(self.deepest_nodes)


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
