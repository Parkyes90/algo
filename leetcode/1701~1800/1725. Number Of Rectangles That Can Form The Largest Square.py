from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squares = []
        for r in rectangles:
            squares.append(min(r))
        max_len = max(squares)
        return squares.count(max_len)


if __name__ == "__main__":
    s = Solution()
    answer = s.countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]])
    assert answer == 3
