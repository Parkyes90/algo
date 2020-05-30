# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    removed_nodes = []

    def recursive(
        self, node: TreeNode, target: int, parent: TreeNode, is_left
    ):
        if not node:
            return
        self.recursive(node.left, target, node, True)
        self.recursive(node.right, target, node, False)
        if not node.left and not node.right and node.val == target:
            self.removed_nodes.append(node.val)
            if is_left:
                parent.left = None
            else:
                parent.right = None

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        start_length = len(self.removed_nodes)

        while True:
            self.recursive(root.left, target, root, True)
            self.recursive(root.right, target, root, False)
            current_length = len(self.removed_nodes)
            if current_length != start_length:
                start_length = current_length
            else:
                break

        if not root.right and not root.left and root.val == target:
            return None
        return root


def bfs(root):
    nodes = [root]
    ret = []
    while nodes:
        node = nodes.pop(0)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        ret.append(node.val)
    print(ret)


def create_root(arr, root, i, n):
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = create_root(arr, root.left, 2 * i + 1, n)
        root.right = create_root(arr, root.right, 2 * i + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [1, 1, 1]
    s = Solution()
    r = create_root(test_arr, None, 0, len(test_arr))
    answer = s.removeLeafNodes(r, 1)
    print(answer)
