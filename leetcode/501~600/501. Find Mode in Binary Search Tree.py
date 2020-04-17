# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        values = []
        values_map = {}
        nodes = [root]
        ret = []
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if isinstance(node.val, int):
                values.append(node.val)
        if not values:
            return []
        for value in values:
            values_map[value] = values_map.get(value, 0) + 1
        maximum = max(values_map.values())
        for key, value in values_map.items():
            if maximum == value:
                ret.append(key)
        return ret


if __name__ == "__main__":
    r = TreeNode(0)
    s = Solution()
    answer = s.findMode(r)
    print(answer)
