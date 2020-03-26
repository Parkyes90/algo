from typing import List


class Solution:
    """https://leetcode.com/problems/lucky-numbers-in-a-matrix/"""

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        max_cols = [0] * cols
        for col in range(cols):
            maximum = 0
            for row in range(rows):
                if maximum < matrix[row][col]:
                    maximum = matrix[row][col]
            max_cols[col] = maximum
        ret = []
        for row in range(rows):
            min_row = min(matrix[row])
            for col in range(cols):
                current_value = matrix[row][col]
                if current_value == min_row and current_value == max_cols[col]:
                    ret.append(current_value)
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.luckyNumbers([[7, 8], [1, 2]])
    print(answer)
