from typing import List


class Solution:

    numbers = {i for i in range(1, 10)}

    def is_magic_square(self, grid: List[List[int]]) -> bool:
        exists = set()
        check_sum = grid[0][0] + grid[1][1] + grid[2][2]

        # check numbers
        for i in range(3):
            col_sum = 0
            row_sum = 0
            for j in range(3):
                row_num = grid[i][j]
                col_num = grid[j][i]
                row_sum += row_num
                col_sum += col_num
                if row_num not in self.numbers:
                    return False
                if row_num in exists:
                    return False
                exists.add(row_num)
            if col_sum != check_sum or row_sum != check_sum:
                return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        count = 0
        for i in range(rows - 2):
            target_rows = grid[i : i + 3]
            for col in range(cols - 2):
                temp = []
                for t_i in range(3):
                    temp.append(target_rows[t_i][col : col + 3])
                if self.is_magic_square(temp):
                    count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numMagicSquaresInside([[4, 2, 3], [9, 2, 3], [2, 3, 3]])
    print(answer)
