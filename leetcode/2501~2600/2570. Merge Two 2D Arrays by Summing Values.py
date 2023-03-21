from typing import List
from collections import defaultdict


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        counter = defaultdict(int)

        for num in nums1 + nums2:
            _id, val = num
            counter[_id] += val

        answer = [[key, val] for key, val in counter.items()]
        answer.sort(key=lambda x: x[0])
        return answer


if __name__ == "__main__":
    s = Solution()
    assert s.mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]) == [
        [1, 6],
        [2, 3],
        [3, 2],
        [4, 6],
    ]

    assert s.mergeArrays([[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]) == [
        [1, 3],
        [2, 4],
        [3, 6],
        [4, 3],
        [5, 5],
    ]
