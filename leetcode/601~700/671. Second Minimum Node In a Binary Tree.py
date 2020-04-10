# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bfs(self, root):
        nodes = [root]
        nodes_val_set = set()
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            if isinstance(node.val, int):
                nodes_val_set.add(node.val)
        return list(nodes_val_set)

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        answer = self.bfs(root)
        if len(answer) < 2:
            return -1
        answer.sort()
        return answer[1]


def create_root(arr, r, index, n):
    if index < n:
        temp = TreeNode(arr[index])
        r = temp
        r.left = create_root(arr, r.left, 2 * index + 1, n)
        r.right = create_root(arr, r.right, 2 * index + 2, n)
    return r


if __name__ == "__main__":
    arr = [2, 2, 2]
    root = create_root(arr, None, 0, len(arr))
    s = Solution()
    answer = s.findSecondMinimumValue(root)
    print(answer)
