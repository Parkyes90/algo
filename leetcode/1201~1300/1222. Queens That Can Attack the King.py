from typing import List


class Solution:
    def add_can_attack_queen(
        self, row, rows, col, cols, answer, chess, direction
    ):
        while 0 <= row < rows and 0 <= col < cols:
            if chess[row][col] == 1:
                answer.append([row, col])
                break
            if direction == "up":
                row -= 1
            elif direction == "down":
                row += 1
            elif direction == "left":
                col -= 1
            elif direction == "right":
                col += 1
            elif direction == "up_left_diagnal":
                row -= 1
                col -= 1
            elif direction == "down_left_diagnal":
                row += 1
                col -= 1
            elif direction == "up_right_diagnal":
                row -= 1
                col += 1
            elif direction == "down_right_diagnal":
                row += 1
                col += 1

    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        answer = []
        directions = (
            "up",
            "down",
            "left",
            "right",
            "up_left_diagnal",
            "down_left_diagnal",
            "up_right_diagnal",
            "down_right_diagnal",
        )
        rows = 8
        cols = 8
        chess = [[0 for _ in range(cols)] for _ in range(rows)]
        chess[king[0]][king[1]] = 2
        for queen in queens:
            row, col = queen
            chess[row][col] = 1

        row, col = king
        for direction in directions:
            self.add_can_attack_queen(
                row, rows, col, cols, answer, chess, direction
            )
        return answer


if __name__ == "__main__":
    s = Solution()
    ans = s.queensAttacktheKing(
        [
            [5, 6],
            [7, 7],
            [2, 1],
            [0, 7],
            [1, 6],
            [5, 1],
            [3, 7],
            [0, 3],
            [4, 0],
            [1, 2],
            [6, 3],
            [5, 0],
            [0, 4],
            [2, 2],
            [1, 1],
            [6, 4],
            [5, 4],
            [0, 0],
            [2, 6],
            [4, 5],
            [5, 2],
            [1, 4],
            [7, 5],
            [2, 3],
            [0, 5],
            [4, 2],
            [1, 0],
            [2, 7],
            [0, 1],
            [4, 6],
            [6, 1],
            [0, 6],
            [4, 3],
            [1, 7],
        ],
        [3, 4],
    )
