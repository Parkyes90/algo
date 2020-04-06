# Definition for a binary tree node.
from typing import List, Union


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def equals(self, s: TreeNode, t: TreeNode):
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        return (
            s.val == t.val
            and self.equals(s.left, t.left)
            and self.equals(s.right, t.right)
        )

    def traverse(self, s: TreeNode, t: TreeNode):
        return s is not None and (
            self.equals(s, t)
            or self.traverse(s.left, t)
            or self.traverse(s.right, t)
        )

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.traverse(s, t)


def create_tree(
    arr: List[int], r: Union[TreeNode, None], index, n
) -> Union[TreeNode, None]:
    if n > index:
        temp = TreeNode(arr[index])
        r = temp
        r.left = create_tree(arr, r.left, 2 * index + 1, n)
        r.right = create_tree(arr, r.right, 2 * index + 2, n)
    return r


def dfs(r: Union[TreeNode, None]):
    ret = []
    if not r:
        return ret
    ret.append(r.val)
    ret += dfs(r.left)
    ret += dfs(r.right)
    return ret


def bfs(r: Union[TreeNode, None]):
    if not r:
        return []
    nodes = [r]
    ret = []
    while nodes:
        node = nodes.pop(0)
        if node.left:
            nodes.append(node.left)
        if node.right:
            nodes.append(node.right)
        ret.append(node.val)
    return ret


if __name__ == "__main__":
    s = Solution()
    tree1_arr = [3, 4, 5, 1, 2]
    tree2_arr = [4, 1, 2]
    tree1 = create_tree(tree1_arr, None, 0, len(tree1_arr))
    tree2 = create_tree(tree2_arr, None, 0, len(tree2_arr))
    answer = s.isSubtree(tree1, tree2)
    print(answer)
