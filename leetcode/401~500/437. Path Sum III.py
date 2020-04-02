# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count_map = {0: 1}
        path = 0

        def dfs(node: TreeNode, target: int, current_sum: int, table: dict):
            if not node:
                return None
            current_sum += node.val

            candidate_sum = current_sum - target

            nonlocal path
            path += table.get(candidate_sum, 0)
            table[current_sum] = table.get(current_sum, 0) + 1

            dfs(node.left, target, current_sum, table)
            dfs(node.right, target, current_sum, table)
            table[current_sum] -= 1

        dfs(root, sum, 0, count_map)
        return path


def insert_level_order(arr, r, i, n):
    # Base case for recursion
    if i < n:
        temp = TreeNode(arr[i])
        r = temp

        # insert left child
        r.left = insert_level_order(arr, r.left, 2 * i + 1, n)

        # insert right child
        r.right = insert_level_order(arr, r.right, 2 * i + 2, n)
    return r


if __name__ == "__main__":
    ar = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    s = Solution()
    root = insert_level_order(ar, None, 0, len(ar))
    answer = s.pathSum(root, 8)
    print(answer)
