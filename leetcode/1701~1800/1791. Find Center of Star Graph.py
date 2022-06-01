from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        result = set(edges[0])
        for edge in edges:
            result &= set(edge)
        return result.pop()


if __name__ == "__main__":
    s = Solution()
    assert s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
