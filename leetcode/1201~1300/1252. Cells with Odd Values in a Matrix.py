from typing import List


class Solution:
    """https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/"""

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0] * m for _ in range(n)]
        count = 0
        for ind in indices:
            row, col = ind
            for c in range(m):
                mat[row][c] += 1
            for r in range(n):
                mat[r][col] += 1

        for row in range(n):
            for col in range(m):
                if mat[row][col] % 2 == 1:
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.oddCells(2, 3, [[0, 1], [1, 1]])
    print(answer)
