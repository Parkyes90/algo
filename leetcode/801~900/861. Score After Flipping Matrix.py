from typing import List


class Solution:
    def bin_to_dec(self, binary: List[int]):
        binary.reverse()
        length = len(binary) - 1
        value = 0
        while binary:
            value += binary.pop() * 2 ** length
            length -= 1
        return value

    def matrixScore(self, A: List[List[int]]) -> int:
        ret = 0
        rows = len(A)
        cols = len(A[0])
        for row in A:
            first = row[0]
            if first == 0:
                for col in range(cols):
                    row[col] = 1 if row[col] == 0 else 0

        for col in range(cols):
            temp = []
            coords = []
            for row in range(rows):
                temp.append((A[row][col]))
                coords.append((row, col))

            if temp.count(0) > temp.count(1):
                for r, c in coords:
                    A[r][c] = 1 if A[r][c] == 0 else 0

        while A:
            ret += self.bin_to_dec(A.pop())
        return ret


if __name__ == "__main__":
    s = Solution()
    answer = s.matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    print(answer)
