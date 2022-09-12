from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    s = Solution()
    answer = s.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
    assert answer == [[9, 9], [8, 6]]
