from typing import List, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode):
        self.new_root = self.restore(root)
        self.nodes = set()
        self.all_find()

    def recursive(self, root):
        if not root:
            return

        if root.left:
            root.left.val = root.val * 2 + 1
            self.recursive(root.left)
        if root.right:
            root.right.val = root.val * 2 + 2
            self.recursive(root.right)

    def restore(self, root: TreeNode) -> TreeNode:
        root.val = 0
        self.recursive(root)
        return root

    def all_find(self):
        nodes = [self.new_root]
        while nodes:
            node = nodes.pop(0)

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            self.nodes.add(node.val)

    def find(self, target: int) -> bool:
        return target in self.nodes


def create_root(
    arr: List[int], root: Union[TreeNode, None], index: int, n: int
) -> TreeNode:

    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [-1, -1, -1, -1, -1]
    r = create_root(test_arr, None, 0, len(test_arr))
    s = FindElements(r)
    print(s.find(2))
