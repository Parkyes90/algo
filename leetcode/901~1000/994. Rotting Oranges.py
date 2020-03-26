from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        stage = 0
        total_oranges_count = 0
        total_rottens_count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                if grid[row][col] == 2:
                    total_rottens_count += 1
                total_oranges_count += 1
        while total_rottens_count != total_oranges_count:
            stage += 1
            rottens = []
            after_rottens_count = 0
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 2:
                        rottens.append((row, col))
            for rotten in rottens:
                row, col = rotten
                if row > 0 and grid[row - 1][col] == 1:
                    grid[row - 1][col] = 2
                if row + 1 < rows and grid[row + 1][col] == 1:
                    grid[row + 1][col] = 2
                if col > 0 and grid[row][col - 1] == 1:
                    grid[row][col - 1] = 2
                if col + 1 < cols and grid[row][col + 1] == 1:
                    grid[row][col + 1] = 2
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col] == 2:
                        after_rottens_count += 1
            if total_rottens_count == after_rottens_count:
                return -1
            total_rottens_count = after_rottens_count
        return stage


if __name__ == "__main__":
    s = Solution()
    answer = s.orangesRotting([[1, 2]])
    print(answer)
