from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        ans = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                res = 0
                if i > 0:
                    res += ans[i - 1][j]
                if j > 0:
                    res += ans[i][j - 1]
                if i > 0 and j > 0:
                    res -= ans[i - 1][j - 1]

                res += mat[i][j]
                ans[i][j] = res

        for i in range(rows):
            for j in range(cols):
                x1, y1, x2, y2 = (
                    max(i - K, 0),
                    max(j - K, 0),
                    min(i + K, rows - 1),
                    min(j + K, cols - 1),
                )

                res = ans[x2][y2]
                if x1 > 0:
                    res -= ans[x1 - 1][y2]
                if y1 > 0:
                    res -= ans[x2][y1 - 1]
                if x1 > 0 and y1 > 0:
                    res += ans[x1 - 1][y1 - 1]

                mat[i][j] = res

        return mat


if __name__ == "__main__":
    s = Solution()
    answer = s.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    print(answer)
