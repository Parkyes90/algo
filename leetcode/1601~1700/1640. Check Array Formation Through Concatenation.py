from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            start = piece[0]
            length = len(piece)
            try:
                index = arr.index(start)
                arr_piece = arr[index : index + length]
                if arr_piece != piece:
                    return False
            except ValueError:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]])

    assert answer
