from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret = [[1]]
        for row_idx in range(2, rowIndex + 2):
            row = [1] * row_idx
            before_row = ret[row_idx - 2]
            for col in range(1, row_idx - 1):
                row[col] = before_row[col - 1] + before_row[col]
            ret.append(row)
        return ret[rowIndex]


if __name__ == "__main__":
    s = Solution()
    answer = s.getRow(3)
    print(answer)
