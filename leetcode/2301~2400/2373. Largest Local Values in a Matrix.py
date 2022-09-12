from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        ans = []
        for i in range(1, rows - 1):
            row = []
            for j in range(1, rows - 1):
                max_num = 1
                for row_k in range(-1, 2):
                    for col_k in range(-1, 2):
                        if grid[i + row_k][j + col_k] > max_num:
                            max_num = grid[i + row_k][j + col_k]
                row.append(max_num)
            ans.append(row)
        return ans


if __name__ == "__main__":
    s = Solution()
    answer = s.largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])
    assert answer == [[9, 9], [8, 6]]
    answer = s.largestLocal(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )
    assert answer == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
