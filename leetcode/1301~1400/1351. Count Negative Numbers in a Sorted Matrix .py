from typing import List


class Solution:
    """https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/"""

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            cols = len(row)
            for col in range(cols):
                if row[col] < 0:
                    count += cols - col
                    break
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.countNegatives([[-1]]))
