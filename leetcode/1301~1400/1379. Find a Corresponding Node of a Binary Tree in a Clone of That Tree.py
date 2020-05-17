# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        nodes = [cloned]
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if target.val == node.val:
                return node


def create_tree(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_tree(arr, root.left, 2 * index + 1, n)
        root.right = create_tree(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [7, 4, 3, None, None, 6, 19]
    r = create_tree(test_arr, None, 0, len(test_arr))
    r_clone = create_tree(test_arr, None, 0, len(test_arr))
    s = Solution()
    answer = s.getTargetCopy(r, r_clone, r.right)
    print(answer)
