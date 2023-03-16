from collections import defaultdict
from typing import List


class Solution:
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:
        ret = []
        items_map = defaultdict(int)

        for item in items2:
            items_map[item[0]] = item[1]

        for item in items1:
            items_map[item[0]] += item[1]

        for value, weight_sum in items_map.items():
            ret.append([value, weight_sum])
        return sorted(ret, key=lambda x: x[0])


if __name__ == "__main__":
    s = Solution()
    assert s.mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]) == [
        [1, 6],
        [3, 9],
        [4, 5],
    ]

    assert s.mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]) == [
        [1, 4],
        [2, 4],
        [3, 4],
    ]

    assert s.mergeSimilarItems([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]) == [
        [1, 7],
        [2, 4],
        [7, 1],
    ]
