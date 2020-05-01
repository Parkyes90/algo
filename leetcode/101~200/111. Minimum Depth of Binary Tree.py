# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        nodes = [(root, 1, False)]
        leafs = []
        while nodes:
            node, depth, is_leaf = nodes.pop(0)
            if node.left:
                is_leaf_left = not node.left.left and not node.left.right
                nodes.append((node.left, depth + 1, is_leaf_left))
            if node.right:
                is_leaf_right = not node.right.left and not node.right.right
                nodes.append((node.right, depth + 1, is_leaf_right))
            if is_leaf:
                leafs.append(depth)
        return min(leafs)


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)

    return root


if __name__ == "__main__":
    test_arr = [3, 9, 20, None, None, 15, 7]
    s = Solution()
    r = create_root(test_arr, None, 0, len(test_arr))
    answer = s.minDepth(r)
    print(answer)
