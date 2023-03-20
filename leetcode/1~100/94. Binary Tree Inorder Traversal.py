from typing import Optional, List
from leetcode.helpers import TreeNode, make_tree_node


class Solution:
    def __init__(self):
        self.output = []

    def recursive_traversal(self, node: TreeNode):
        if not node:
            return

        if node.left:
            self.recursive_traversal(node.left)

        self.output.append(node.val)

        if node.right:
            self.recursive_traversal(node.right)

    def iteratively_traversal(self, node: TreeNode):
        cur = node
        nodes = []

        while cur or nodes:
            while cur:
                nodes.append(cur)
                cur = cur.left
            cur = nodes.pop()
            self.output.append(cur.val)
            cur = cur.right

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.iteratively_traversal(root)
        return self.output


if __name__ == "__main__":
    assert Solution().inorderTraversal(make_tree_node([1, None, 2, 3])) == [1, 3, 2]
    assert Solution().inorderTraversal(make_tree_node([])) == []
    assert Solution().inorderTraversal(make_tree_node([1])) == [1]
