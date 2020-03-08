from typing import List


class Solution:
    """https://leetcode.com/problems/minimum-time-visiting-all-points/"""

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        current = points[0]
        for i in range(1, len(points)):
            next_point = points[i]
            diagonal_move = min(
                (
                    abs(next_point[0] - current[0],),
                    abs(next_point[1] - current[1]),
                )
            )
            is_left = current[0] >= next_point[0]
            is_down = current[1] >= next_point[1]

            if is_left and is_down:
                point_after_diagonal_move = (
                    current[0] - diagonal_move,
                    current[1] - diagonal_move,
                )
            elif is_left and not is_down:
                point_after_diagonal_move = (
                    current[0] - diagonal_move,
                    current[1] + diagonal_move,
                )
            elif not is_left and is_down:
                point_after_diagonal_move = (
                    current[0] + diagonal_move,
                    current[1] - diagonal_move,
                )
            else:
                point_after_diagonal_move = (
                    current[0] + diagonal_move,
                    current[1] + diagonal_move,
                )

            remain_move = max(
                (
                    abs(point_after_diagonal_move[0] - next_point[0]),
                    abs(point_after_diagonal_move[1] - next_point[1]),
                )
            )
            count += remain_move + diagonal_move
            current = next_point
        return count


if __name__ == "__main__":
    s = Solution()
    print(
        s.minTimeToVisitAllPoints(
            [[559, 511], [932, 618], [-623, -443], [431, 91], [838, -127],]
        )
    )
