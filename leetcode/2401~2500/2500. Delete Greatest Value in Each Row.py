from typing import List


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        while len(grid[0]) > 0:
            max_value = 0
            for row in grid:
                max_in_row = max(row)
                max_value = max(max_value, max(row))
                row.remove(max_in_row)
            answer += max_value
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.deleteGreatestValue([[1, 2, 4], [3, 3, 1]]) == 8
    assert s.deleteGreatestValue([[10]]) == 10
