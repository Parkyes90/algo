from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        base = coordinates[0]
        base2 = coordinates[1]
        try:
            inclination = (base[1] - base2[1]) / (base[0] - base2[0])
        except ZeroDivisionError:
            return False
        for i in range(2, len(coordinates)):
            other_base = coordinates[i]
            try:
                other_inclination = (base[1] - other_base[1]) / (
                    base[0] - other_base[0]
                )
            except ZeroDivisionError:
                return False
            if other_inclination != inclination:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    answer = s.checkStraightLine(
        [
            [-7, -3],
            [-7, -1],
            [-2, -2],
            [0, -8],
            [2, -2],
            [5, -6],
            [5, -5],
            [1, 7],
        ]
    )
    print(answer)
