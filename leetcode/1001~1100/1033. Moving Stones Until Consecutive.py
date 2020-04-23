from typing import List


class Solution:
    def get_diffs(self, stones):
        diffs = []
        for i in range(1, len(stones)):
            diff = abs(stones[i] - abs(stones[i - 1]))
            if diff > 1:
                diffs.append(diff)
        return diffs

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = [a, b, c]
        stones.sort()
        diffs = self.get_diffs(stones)
        maximum = 0
        if not diffs:
            return [0, 0]

        for diff in diffs:
            maximum += diff - 1

        if len(diffs) < 2:
            return [1, maximum]

        is_exist_between = any(diff for diff in diffs if diff < 3)

        if is_exist_between:
            return [1, maximum]
        return [2, maximum]


if __name__ == "__main__":
    s = Solution()
    answer = s.numMovesStones(1, 2, 5)
    print(answer)
