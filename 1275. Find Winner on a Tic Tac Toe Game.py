from typing import List, Union


class Solution:
    def who_win(self, tic_tac_toe: List[List[Union[None, str]]], play):
        play_count = 0
        # column
        for col in range(3):
            for row in range(3):
                if tic_tac_toe[row][col] == play:
                    play_count += 1
            if play_count == 3:
                return True
            else:
                play_count = 0
        # row
        for row in range(3):
            for col in range(3):
                if tic_tac_toe[row][col] == play:
                    play_count += 1
            if play_count == 3:
                return True
            else:
                play_count = 0

        # diagonal
        for i in range(3):
            if tic_tac_toe[i][i] == play:
                play_count += 1
        if play_count == 3:
            return True
        play_count = 0

        # reverse diagonal
        for i in range(2, -1, -1):
            if tic_tac_toe[i][2 - i] == play:
                play_count += 1
        if play_count == 3:
            return True
        return False

    def tictactoe(self, moves: List[List[int]]) -> str:
        tic_tac_toe = [[None for _ in range(3)] for _ in range(3)]

        for index, move in enumerate(moves):
            row, col = move
            play = "X" if index % 2 == 0 else "O"
            tic_tac_toe[row][col] = play

            if self.who_win(tic_tac_toe, play):
                return "A" if play == "X" else "B"

        for row in range(3):
            for col in range(3):
                if tic_tac_toe[row][col] is None:
                    return "Pending"
        return "Draw"


if __name__ == "__main__":
    s = Solution()
    answer = s.tictactoe([[0, 0], [1, 1]])
    print(answer)
