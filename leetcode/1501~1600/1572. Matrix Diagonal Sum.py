from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        coords = set()
        rows = len(mat)
        total = 0
        for i in range(rows):
            total += mat[i][i]
            coords.add((i, i))
            secondary = rows - 1 - i
            if (i, secondary) not in coords:
                total += mat[i][secondary]
        return total


if __name__ == "__main__":
    s = Solution()
    answer = s.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(answer)
    assert answer == 25
