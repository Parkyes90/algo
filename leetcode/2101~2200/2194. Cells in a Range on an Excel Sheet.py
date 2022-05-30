from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []

        cols = [chr(code) for code in range(ord("A"), ord("Z") + 1)]
        rows = [str(row) for row in range(1, 10)]

        start, end = s.split(":")

        start_col_index = cols.index(start[0])
        start_row_index = rows.index(start[1])

        end_col_index = cols.index(end[0])
        end_row_index = rows.index(end[1])

        for col_index in range(start_col_index, end_col_index + 1):
            for row_index in range(start_row_index, end_row_index + 1):
                result.append(f"{cols[col_index]}{rows[row_index]}")

        return result


if __name__ == "__main__":
    s = Solution()
    assert ["K1", "K2", "L1", "L2"] == s.cellsInRange("K1:L2")
