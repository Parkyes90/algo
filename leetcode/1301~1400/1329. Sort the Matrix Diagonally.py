from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        for row in range(rows):
            temp = []
            i, j = row, 0
            while i < rows and j < cols:
                temp.append(mat[i][j])
                i += 1
                j += 1
            i, j = row, 0
            temp.sort(reverse=True)
            while i < rows and j < cols:
                mat[i][j] = temp.pop()
                i += 1
                j += 1

        for col in range(1, cols):
            temp = []
            i, j = 0, col
            while i < rows and j < cols:
                temp.append(mat[i][j])
                i += 1
                j += 1
            i, j = 0, col
            temp.sort(reverse=True)
            while i < rows and j < cols:
                mat[i][j] = temp.pop()
                i += 1
                j += 1
        return mat


if __name__ == "__main__":
    s = Solution()
    answer = s.diagonalSort([[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
    print(answer)
