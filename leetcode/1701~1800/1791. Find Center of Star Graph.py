from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        return edges[0][1]


if __name__ == "__main__":
    s = Solution()
    assert s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
