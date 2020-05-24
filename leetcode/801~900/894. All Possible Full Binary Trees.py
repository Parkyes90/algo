# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    cache = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in self.cache:
            ret = []
            for i in range(N):
                j = N - 1 - i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(j):
                        r = TreeNode(0)
                        r.left = left
                        r.right = right
                        ret.append(r)
                self.cache[N] = ret
        return self.cache[N]


if __name__ == "__main__":
    s = Solution()
    answer = s.allPossibleFBT(7)
    print(answer)
