# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodes = [(root, 0)]
        deepest_level = 0
        ret = []
        while nodes:
            node, level = nodes.pop(0)
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))
            if level > deepest_level:
                deepest_level += 1
            ret.append((node.val, level))
        ans = 0
        for val, level in ret:
            if level == deepest_level:
                ans += val
        return ans


def create_root(arr, root, index, n):
    if index < n and arr[index] is not None:
        root = TreeNode(arr[index])
        root.left = create_root(arr, root.left, 2 * index + 1, n)
        root.right = create_root(arr, root.right, 2 * index + 2, n)
    return root


if __name__ == "__main__":
    test_arr = [
        1,
        2,
        3,
        4,
        5,
        None,
        6,
        7,
        None,
        None,
        None,
        None,
        None,
        None,
        8,
    ]
    s = Solution()
    r = create_root(test_arr, None, 0, len(test_arr))
    answer = s.deepestLeavesSum(r)
    print(answer)
