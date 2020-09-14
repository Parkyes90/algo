from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 1:
                    is_special = True
                    for r in range(rows):
                        if (r, col) == (row, col):
                            continue

                        if mat[r][col] != 0:
                            is_special = False
                            break
                    for c in range(cols):
                        if (row, col) == (row, c):
                            continue
                        if mat[row][c] != 0:
                            is_special = False
                            break
                    if is_special:
                        count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numSpecial(
        [
            [0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
    )
    print(answer)
