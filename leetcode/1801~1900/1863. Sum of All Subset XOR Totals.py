from itertools import combinations
from operator import xor
from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        _sum = 0
        for i in range(1, len(nums) + 1):
            for comb in combinations(nums, i):
                initial = comb[0]
                for item in comb[1:]:
                    initial ^= item
                _sum += initial

        return _sum


if __name__ == "__main__":
    s = Solution()
    answer = s.subsetXORSum([1, 3])
    assert answer == 6

    answer = s.subsetXORSum([5, 1, 6])
    assert answer == 28
