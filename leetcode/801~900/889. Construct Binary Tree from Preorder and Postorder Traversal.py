# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, pre: List[int], post: List[int]
    ) -> TreeNode:
        pass


if __name__ == "__main__":
    s = Solution()
    answer = s.constructFromPrePost(
        [1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]
    )
    print(answer)
