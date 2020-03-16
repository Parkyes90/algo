from typing import List


class Solution:
    """https://leetcode.com/problems/shift-2d-grid/"""

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ret = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                add_row, col = divmod(c + k, cols)
                row = add_row + r
                if row >= rows:
                    row = (add_row + r) % rows
                ret[row][col] = grid[r][c]
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
    print(answer)
