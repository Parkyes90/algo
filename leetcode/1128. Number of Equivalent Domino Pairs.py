from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        rows = len(dominoes)
        domino_map = {}
        for row in range(rows):
            a, b = dominoes[row]
            if (a, b) in domino_map:
                domino_map[(a, b)].append(row)
            elif (b, a) in domino_map:
                domino_map[(b, a)].append(row)
            else:
                domino_map[(a, b)] = [row]
        count = 0
        for _, value in domino_map.items():
            value_length = len(value)
            if value_length > 1:
                count += value_length * (value_length - 1) // 2
        return count


if __name__ == "__main__":
    s = Solution()
    answer = s.numEquivDominoPairs(
        [[2, 1], [1, 2], [1, 2], [1, 2], [2, 1], [1, 1], [1, 2], [2, 2]]
    )
    assert answer == 15
