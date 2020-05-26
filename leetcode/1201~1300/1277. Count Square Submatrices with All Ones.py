from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])

        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        count += 1
                    else:
                        cell_val = (
                            min(
                                matrix[i - 1][j - 1],
                                matrix[i][j - 1],
                                matrix[i - 1][j],
                            )
                            + matrix[i][j]
                        )
                        count += cell_val
                        matrix[i][j] = cell_val
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.countSquares([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]])
    print(answer)
