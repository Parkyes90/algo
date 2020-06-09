from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        rows = len(board)
        cols = len(board[0])
        store = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X":
                    store.add((row, col))
                    # 상
                    is_up = (row - 1, col) in store
                    # 좌
                    is_left = (row, col - 1) in store
                    if not is_up and not is_left:
                        count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.countBattleships(
        [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    )
    print(answer)
